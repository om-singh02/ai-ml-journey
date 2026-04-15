# Python Quick Reference — Phase 0

A working reference for Python fundamentals, with every example grounded in inventory and procurement work: SKUs, suppliers, POs, stock levels, reorder points, lead times.

---

## 1. Lists — the ordered, mutable workhorse

Lists hold sequences where order matters and duplicates are allowed. In procurement: line items on a PO, SKUs in a shipment, daily stock counts.

```python
skus = ["SKU-001", "SKU-002", "SKU-003"]
stock = [42, 17, 0, 88, 5]
```

### Core methods

```python
skus.append("SKU-004")          # add to end
skus.extend(["SKU-005", "SKU-006"])  # add many (NOT append — that nests)
skus.insert(0, "SKU-000")       # insert at index
skus.remove("SKU-002")          # remove first match by VALUE (raises if missing)
last = skus.pop()               # remove + return last; pop(0) for first
del skus[2]                     # delete by index, no return
skus.index("SKU-003")           # find position (raises if missing)
skus.count("SKU-001")           # how many times it appears
skus.sort()                     # in-place; sort(reverse=True) for desc
skus.reverse()                  # in-place reverse
skus.clear()                    # empty it
```

### `pop` vs `remove` vs `del` — the confusion killer

| | takes | returns | use when |
|---|---|---|---|
| `pop(i)` | index (default -1) | the item | you need the value back (e.g. process the popped PO) |
| `remove(x)` | value | nothing | you know the SKU but not where it is |
| `del lst[i]` | index | nothing | you just want it gone |

### Slicing

```python
stock[1:4]        # items 1,2,3
stock[:3]         # first 3
stock[-2:]        # last 2 — great for "most recent receipts"
stock[::2]        # every other
stock[::-1]       # reversed copy
stock[1:4] = [0]  # replace a slice with new contents
```

### The copy trap

```python
a = [1, 2, 3]
b = a              # NOT a copy — both names point to the same list
b.append(99)       # a is now [1, 2, 3, 99] too

b = a.copy()       # actual copy (also: a[:] or list(a))
```

For nested lists (e.g. PO with line-item lists), `copy()` is shallow — inner lists are still shared. Use `copy.deepcopy()` when you have nesting.

### List comprehensions — simple to complex

```python
# simple: bump every stock level by safety buffer
buffered = [s + 10 for s in stock]

# with filter: only SKUs that are out of stock
out_of_stock = [sku for sku, qty in zip(skus, stock) if qty == 0]

# with transform + filter: uppercase SKUs needing reorder (qty < 20)
reorder = [sku.upper() for sku, qty in zip(skus, stock) if qty < 20]

# nested: flatten a list of POs (each PO is a list of SKUs)
pos = [["SKU-001", "SKU-002"], ["SKU-003"], ["SKU-004", "SKU-005"]]
all_lines = [sku for po in pos for sku in po]

# conditional expression inside: tag each SKU
tagged = ["LOW" if q < 20 else "OK" for q in stock]
```

Rule of thumb: if the comprehension needs more than two `for`/`if` clauses, write a regular loop — readability beats cleverness.

---

## 2. Dicts — keyed lookups, the procurement lookup table

Dicts map keys to values. In procurement: SKU → stock level, supplier_id → lead time, PO number → status.

```python
stock = {"SKU-001": 42, "SKU-002": 17, "SKU-003": 0}
lead_times = {"ACME": 14, "Globex": 7, "Initech": 30}
```

### Safe access — `get` and `setdefault`

```python
stock["SKU-999"]              # KeyError if missing
stock.get("SKU-999")          # None if missing
stock.get("SKU-999", 0)       # 0 if missing — perfect for stock counts

# setdefault: get the value, but insert a default if absent
orders_by_supplier = {}
orders_by_supplier.setdefault("ACME", []).append("PO-1001")
orders_by_supplier.setdefault("ACME", []).append("PO-1002")
# {"ACME": ["PO-1001", "PO-1002"]}
```

### Views: keys, values, items

```python
for sku in stock.keys():           # .keys() optional — default iteration
    ...
for qty in stock.values():
    ...
for sku, qty in stock.items():     # the workhorse
    print(f"{sku}: {qty} units")
```

Views are *live* — they reflect changes to the dict. Wrap in `list(...)` if you need a snapshot.

### Update and merge

```python
stock.update({"SKU-001": 50, "SKU-004": 25})  # adds new, overwrites existing

# merge (Python 3.9+)
combined = stock | lead_times          # new dict
stock |= {"SKU-005": 10}               # update in place

# older syntax
combined = {**stock, **lead_times}
```

### Dict comprehensions

```python
# build SKU → reorder-needed bool
needs_reorder = {sku: qty < 20 for sku, qty in stock.items()}

# invert a dict (supplier_id → name becomes name → supplier_id)
suppliers = {1: "ACME", 2: "Globex"}
by_name = {name: sid for sid, name in suppliers.items()}

# filter: only suppliers with lead time under 14 days
fast = {s: lt for s, lt in lead_times.items() if lt < 14}
```

---

## 3. Sets — uniqueness and membership, fast

A set is an unordered collection of unique items. Reach for sets when you need: deduplication, fast `in` checks, or comparing two groups.

```python
skus_in_warehouse = {"SKU-001", "SKU-002", "SKU-003"}
skus_on_order = {"SKU-003", "SKU-004", "SKU-005"}
```

`{}` alone is an empty *dict* — use `set()` for an empty set.

### When to use a set

- You're calling `if x in collection:` repeatedly on a large list → convert to a set first (O(1) vs O(n)).
- You need to dedupe: `unique_skus = set(messy_sku_list)`.
- You're answering "what's in A but not B?" type questions.

### Methods

```python
s.add("SKU-006")
s.discard("SKU-001")   # no error if missing
s.remove("SKU-001")    # KeyError if missing
s.update({"SKU-007", "SKU-008"})
```

### Set math — the procurement sweet spot

```python
# union: everything we have OR have ordered
all_skus = skus_in_warehouse | skus_on_order

# intersection: what we have AND have re-ordered (overstock risk?)
both = skus_in_warehouse & skus_on_order

# difference: in warehouse but NOT on order (these we own outright right now)
only_warehouse = skus_in_warehouse - skus_on_order

# symmetric difference: in one but not the other
mismatched = skus_in_warehouse ^ skus_on_order

# subset / superset
{"SKU-001"} <= skus_in_warehouse   # True
```

### Set comprehensions

```python
unique_suppliers = {po["supplier"] for po in purchase_orders}
```

---

## 4. Strings — formatting and cleanup

```python
sku = "sku-001"
supplier = "ACME"
qty = 1250
unit_cost = 3.4567
```

### f-strings with formatting

```python
f"{qty:,} units"              # 1,250 units
f"${unit_cost:.2f}"           # $3.46
f"${qty * unit_cost:,.2f}"    # $4,320.88
f"{supplier:<10}|{qty:>6}"    # ACME      |  1250  (left/right pad)
f"{0.873:.1%}"                # 87.3%
f"{sku=}"                     # sku='sku-001'  (debug form)
```

### Split / join / strip / replace

```python
"SKU-001,SKU-002,SKU-003".split(",")   # ['SKU-001', 'SKU-002', 'SKU-003']
",".join(["SKU-001", "SKU-002"])       # 'SKU-001,SKU-002'
"  PO-1001  \n".strip()                # 'PO-1001'  (also lstrip/rstrip)
"sku-001".replace("sku", "SKU")        # 'SKU-001'
"SKU-001-A".split("-", 1)              # ['SKU', '001-A']  (max splits)
```

### Case and inspection

```python
sku.upper()         # 'SKU-001'
"ACME Corp".lower()
"acme corp".title() # 'Acme Corp'
sku.startswith("sku")
"PO-1001".endswith("01")
"123".isdigit()
"  ".isspace()
```

---

## 5. General-purpose built-ins

```python
stock = [42, 17, 0, 88, 5]
skus  = ["SKU-001", "SKU-002", "SKU-003", "SKU-004", "SKU-005"]
costs = [3.45, 12.10, 0.99, 7.50, 22.00]
```

```python
len(stock)              # 5
min(stock), max(stock)  # 0, 88
sum(stock)              # 152

list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 10, 2))   # [2, 4, 6, 8]
```

### enumerate — index + value

```python
for i, sku in enumerate(skus, start=1):
    print(f"Line {i}: {sku}")
```

### zip — walk multiple sequences together

```python
for sku, qty, cost in zip(skus, stock, costs):
    print(f"{sku}: {qty} @ ${cost}")

# build a dict from two lists
stock_map = dict(zip(skus, stock))
```

`zip` stops at the shortest input. Use `itertools.zip_longest` if that's a problem.

### map / filter — usually a comprehension is clearer

```python
totals = list(map(lambda q, c: q * c, stock, costs))
# almost always better as:
totals = [q * c for q, c in zip(stock, costs)]

low = list(filter(lambda q: q < 20, stock))
# better:
low = [q for q in stock if q < 20]
```

### any / all — quick boolean checks across a sequence

```python
any(q == 0 for q in stock)        # any stockouts?
all(q > 0 for q in stock)         # everything in stock?
any(sku.startswith("SKU-") for sku in skus)
```

### sorted with `key=`

```python
sorted(stock)                                  # ascending copy
sorted(stock, reverse=True)                    # descending

# sort SKUs by their stock level
sorted(skus, key=lambda s: stock_map[s])

# sort POs (list of dicts) by total value desc
pos = [{"id": "PO-1", "total": 1200}, {"id": "PO-2", "total": 800}]
sorted(pos, key=lambda p: p["total"], reverse=True)

# multi-key: by supplier asc, then total desc
sorted(pos, key=lambda p: (p["supplier"], -p["total"]))
```

`sorted()` returns a new list. `list.sort()` mutates in place and returns `None`.

---

## 6. Functions reference

### Positional vs keyword arguments

```python
def reorder(sku, qty, supplier):
    ...

reorder("SKU-001", 100, "ACME")                            # positional
reorder(sku="SKU-001", qty=100, supplier="ACME")           # keyword
reorder("SKU-001", supplier="ACME", qty=100)               # mixed (positional first)
```

### Defaults — and the mutable default trap

```python
def add_to_po(sku, po=None):
    if po is None:        # the correct pattern
        po = []
    po.append(sku)
    return po

# DO NOT do this:
def broken(sku, po=[]):   # the list is created ONCE, at function definition
    po.append(sku)
    return po
broken("A")  # ['A']
broken("B")  # ['A', 'B']  — surprise! the same list persists
```

Rule: never use a mutable object (`[]`, `{}`, `set()`) as a default. Use `None` and create inside.

### `*args` and `**kwargs` — the sticky mental model

The `*` says "collect the rest of the positional arguments into a tuple." The `**` says "collect the rest of the keyword arguments into a dict." The names `args` and `kwargs` are convention — the `*` and `**` do the work.

```python
def total_cost(*line_items, **shipping_options):
    # line_items is a tuple of (qty, price) pairs
    # shipping_options is a dict like {"express": True, "insured": False}
    subtotal = sum(qty * price for qty, price in line_items)
    if shipping_options.get("express"):
        subtotal += 25
    return subtotal

total_cost((10, 3.45), (5, 12.10), express=True, insured=False)
```

Unpacking in the other direction:

```python
parts = ("SKU-001", 100, "ACME")
reorder(*parts)            # spreads tuple into positional args

opts = {"sku": "SKU-001", "qty": 100, "supplier": "ACME"}
reorder(**opts)            # spreads dict into keyword args
```

### Return values

A function with no `return` returns `None`. You can return multiple values as a tuple:

```python
def stock_summary(levels):
    return min(levels), max(levels), sum(levels) / len(levels)

lo, hi, avg = stock_summary([42, 17, 88, 5])   # tuple unpacking
```

### Lambdas — single-expression anonymous functions

Best used inline as `key=` or simple callbacks. If it needs a name or a second line, write `def`.

```python
sorted(pos, key=lambda p: p["total"])
discount = lambda price: price * 0.9
```

---

## 7. Control flow

### if / elif / else

```python
if qty == 0:
    status = "STOCKOUT"
elif qty < 20:
    status = "REORDER"
elif qty < 100:
    status = "OK"
else:
    status = "OVERSTOCK"
```

### Boolean operators

`and`, `or`, `not` — not `&&`, `||`, `!`. They short-circuit (stop evaluating once the answer is known) and return one of the operands, not a strict `True`/`False`:

```python
supplier = preferred_supplier or "DEFAULT"   # fallback pattern
qty > 0 and qty < 20                         # in-stock but low
```

Chained comparisons work like math:

```python
if 0 < qty < 20:    # cleaner than qty > 0 and qty < 20
    flag_low(sku)
```

### Ternary (conditional expression)

```python
status = "LOW" if qty < 20 else "OK"
```

### break, continue

```python
for sku, qty in stock.items():
    if qty < 0:
        break              # bail out of the loop entirely
    if qty == 0:
        continue           # skip to next iteration
    process(sku, qty)
```

### loop-else (rarely used, often misunderstood)

The `else` on a loop runs **only if the loop completed without hitting `break`**. Useful for search patterns:

```python
for po in purchase_orders:
    if po["sku"] == "SKU-001":
        print("Already on order")
        break
else:
    print("Need to create new PO")
```

---

## 8. "I always forget"

### Truthy / falsy

These all evaluate as `False` in a boolean context:

```
False, None, 0, 0.0, "", [], {}, set(), ()
```

Everything else is truthy. So:

```python
if stock:           # True if list/dict has any items
    process(stock)

if qty:             # CAREFUL — False when qty == 0
    ...
if qty is not None: # safer when 0 is a valid value
    ...
```

### Mutable vs immutable

| Mutable (can change in place) | Immutable (can't) |
|---|---|
| list, dict, set | int, float, str, tuple, frozenset, bool |

Consequences:
- Immutable types are safe as dict keys and set members. Lists and dicts are not.
- Passing a list into a function and mutating it changes the caller's list. Passing an int doesn't (you can't mutate an int).
- Tuples of immutables are hashable; tuples containing a list are not.

### `is` vs `==`

- `==` asks "do these have equal values?"
- `is` asks "are these the exact same object in memory?"

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b      # True  — same contents
a is b      # False — different objects

a is None   # the only place you should use `is` regularly
            # (also: is True / is False — but usually unnecessary)
```

Don't use `is` to compare strings or numbers. It sometimes works due to interning, which makes the bug intermittent and worse.

### Common errors and what they mean

| Error | Usually means |
|---|---|
| `KeyError: 'SKU-999'` | Dict key missing — use `.get()` or check first |
| `IndexError: list index out of range` | Index past the end — check `len()` first |
| `TypeError: 'NoneType' object is not iterable` | A function returned `None` and you tried to loop it |
| `TypeError: unhashable type: 'list'` | Tried to use a list as a dict key or set member |
| `AttributeError: 'NoneType' object has no attribute 'X'` | You called `.X` on something that's `None` |
| `ValueError: ... not in list` | `.remove()` or `.index()` on a missing value |
| `UnboundLocalError` | Assigned to a variable inside a function without `global`/`nonlocal`, but read it before assigning |
| `IndentationError` | Mixed tabs and spaces, or wrong indent level |

### Other small things that bite

- `range(10)` gives 0–9, not 0–10.
- `dict.keys()` is a view, not a list — wrap in `list()` if you need to index it.
- Modifying a list while iterating it skips items. Iterate a copy: `for x in lst[:]:`.
- `"3" + 3` is a `TypeError`. Cast explicitly: `int("3") + 3` or `"3" + str(3)`.
- Integer division is `//`, regular division is `/` (always returns float).
- `not x in y` works but `x not in y` is the idiom.
