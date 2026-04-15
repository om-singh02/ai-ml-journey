# # Block 1
# name= "Om Singh"
# age = 24
# temperature = 36.6
# is_learning = True

# print(name, age, temperature, is_learning)

# #block 2
# x = 10
# print(type(x))

# x = "hello"
# print(type(x))

# x = 3.14
# print(type(x))

# #block 3
# a = 15
# b = 4

# print(a+b) # Addition
# print(a-b) # Subtraction
# print(a*b)
# print(a/b)
# print(a//b) # Floor division
# print(a%b)
# print(a**b) # Exponentiation

# #block4
# first = "Machine"
# second = "Learning"

# full = first + " " + second
# print(full)

# phase = 0
# week = 1
# print(f"You are in Phase {phase}, Week {week}")

# sentence = " Hello World "
# print(sentence.strip())
# print(sentence.lower())
# print(sentence.upper())
# print(sentence.replace("World", "Python"))

# result = "AI"*3
# print(result)

#block 5 --Lists

# inventory = ["bolts", "nuts", "washers"]

# inventory.append("screws")
# print(inventory)

# inventory.remove("nuts")
# print(inventory)

# inventory[0] = "hex bolts"
# print(inventory)

# inventory.sort()
# print(inventory)

# numbers = [10, 25, 3, 47, 8, 19]

# print(numbers[::2])
# print(numbers[::-1])
# print(numbers[1:5:2])

# numbers.insert(0, 99)  #insert at specific index
# numbers.extend([1,2,3]) #merges another list in
# print(numbers)

# numbers.pop() #removes last item
# numbers.pop(2) #removes by index
# numbers.remove(3) #removes first occurence of value 25
# del numbers[0] #deletes by index
# print(numbers)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(numbers.count(10)) #how many times 10 appears
# print(numbers.index(47)) #prints index of the number

# a = [1,2,3]
# b = a
# b.append(4)
# print(b)
# print(a)

# item = {
#     "item_no": "1001",
#     "description": "Hex Bolt M8",
#     "quantity": 250,
#     "location": "Bin A3"
# }

# print(item.items())
# print(item.keys())
# print(item.values())

# print(item.get("supplier")) #safe access into dictionay without crashing
# print(item.get("supplier", "N/A")) # second argument gives default value

# item.update({"quantity": 300, "unit_cost":40})
# print(item)

# item.pop("location")
# print("location" in item)
# print(item.items())

# for key, value in item.items():
#     print(f"{key}:{value}")

#building dictionary dynamically
# fields = ["item_no", "quantity", "cost"]
# values = ["10001M", 250, 0.45]
# built = dict(zip(fields, values))
# print(built)


#functions

# def check_stocks(item_name, quantity):
#     print(f"checking {item_name} : {quantity} units")

# check_stocks("ITEM1001", 100)

# def get_status(quantity):
#     if quantity == 0:
#         return "OUT OF STOCK"
#     elif quantity < 50:
#         return "LOW STOCK"
#     else:
#         return "AVAILABLE"

# status = get_status(100)
# status1 = get_status(0)
# print(status)
# print(status1)

# inventory = [
#     {"item_no": "1001", "description": "Hex Bolt M8", "quantity": 250},
#     {"item_no": "1002", "description": "Nut M8", "quantity": 30},
#     {"item_no": "1003", "description": "Washer M8", "quantity": 420},
#     {"item_no": "1004", "description": "Screw M6", "quantity": 15},
# ]

# def get_status(quantity, reorder_stock=50):
#     if quantity == 0:
#         return "OUT OF STOCK"
#     elif quantity < reorder_stock:
#         return "LOW STOCK"
#     else:
#         return "AVAILABLE"
    
# def print_inventory_report(inventory):
#     print("="*40)
#     print("Inventory Report")
#     print("="*40)

#     for item in inventory:
#         status = get_status(item["quantity"])
#         print(f"{item['description']: <20} {item['quantity']:>5} - {status}") #> and < here is use to pad. < 20 charcaters to ur left and >5 characters to ur right
#     print("="*40)

# # print_inventory_report(inventory)
# get_status()

# ERROR HANDLING

# inventory = {"item_no": "1001", "description": "Hex Bolt M8"}
# print(inventory["quantity"])

# try:
#     print(inventory["quantity"])
# except KeyError:
#     print("Quanity field is missing from this item")

# def get_quantity(inventory, key):
#     try:
#         quantity = inventory[key]
#         result = 100/quantity
#         return result
#     except KeyError:
#         print(f"{key} is missing from this item")
#     except ZeroDivisionError:
#         print(f"{key} - Quantity can't be zero")
#     except TypeError:
#         print(f"{key} - quanitity has be integer")

# item1 = {"item_no": "1001", "quantity": 100}
# item2 = {"item_no": "1001"}
# item3 = {"item_no": "1001", "quantity": 0}
# item4 = {"item_no": "1001", "quantity": "abc"}

# get_quantity(item1, "quantity")
# get_quantity(item2, "quantity")
# get_quantity(item3, "quantity")
# get_quantity(item4, "quantity")

# def process_item(item):
#     try:
#         quantity = item["quantity"]
#         status = "LOW STOCK" if quantity < 50 else "Ok"
#     except KeyError:
#         print("Quantity filed missing in this item")
#     else:
#         print(f"{item['item_no']}: {quantity} -- {status} ")
#     finally:
#         print(f"The item is processed")

# process_item({"item_no": 1001, "quantity": 250})
# process_item({"item_no": 1002})