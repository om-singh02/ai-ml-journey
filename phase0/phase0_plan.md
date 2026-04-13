# Phase 0 — Python Consolidation (Locked Plan)

**Dates:** April 13 – May 10, 2026 (4 weeks)
**Goal:** Go from "I know basic Python but freeze on functions and classes" to "I can confidently design and build small multi-file Python tools." Close small recall gaps. Build 4 real inventory sub-projects.
**Exit criteria:** I can build the Phase 1 data pipeline without stopping every 10 minutes to look up syntax or wonder how to structure my code.

---

## 1. Skill level — what we're working with

- Comfortable with: variables, types, strings, lists, dicts, loops, conditionals (reading them, modifying them)
- Shaky on: designing my own functions from scratch
- Wall: classes and OOP — no working mental model yet
- Small recall gaps: `pop` vs `remove` vs `del`, complex list comprehensions, `*args` / `**kwargs`, and similar "I used to know this" moments

Phase 0 is designed around **this exact profile.** Teaching weight goes to functions and classes. The small gaps get a quick reference sheet, not full lessons.

---

## 2. The four sub-projects (one per week)

| Week | Dates | Teaching focus | Sub-project |
|---|---|---|---|
| 1 | Apr 13–19 | Functions, deeply — designing them, not just writing them | Reorder Point Calculator |
| 2 | Apr 20–26 | Classes, slowly and properly — the wall, patiently climbed | Stockout Detector |
| 3 | Apr 27 – May 3 | Modules, imports, file I/O, project structure | Supplier Scorecard |
| 4 | May 4–10 | Error handling, validation, edge cases + closing remaining small gaps | Inventory Data Cleaner |

**Business concepts run alongside** (one per week): inventory vocabulary → ROP/EOQ → working capital → ABC/XYZ.

**Each sub-project is standalone.** Separate folder in the repo, its own README, its own commits. Nothing gets refactored from a previous week — each week is a fresh build using that week's new concept.

---

## 3. Weekly rhythm

| Day | Time | Activity |
|---|---|---|
| Mon | 1.5 hrs evening | Heavy technical — new lesson, core coding |
| Tue | 30–45 min | Light — business reading + 15-min drill + 15 min source reading |
| Wed | 1.5 hrs evening | Heavy technical — continue sub-project |
| Thu | 30–45 min | Light — debugging, journaling, 15-min drill |
| Fri | 1.5 hrs evening | Heavy technical — finish week's task, commit |
| **Sat** | **4 hrs morning** | **Deep work — main sub-project build** |
| **Sun** | **4 hrs + 30 min** | **~3 hrs sub-project + ~1 hr practice layer + Sunday ritual** |
| Work-time sneak | 30 min flex | Business concept reading |

**Total: ~12–13 hrs/week.** Floor 11, ceiling 16.

### The Sunday ritual (30 min, non-negotiable)

1. Update the project journal: what I learned, what I built, what I understand now that I didn't last Sunday
2. Commit and push everything to GitHub
3. Draft the weekly LinkedIn post (even if not published)
4. Look at next week's plan and flag anything I'm nervous about
5. Close the laptop. Rest.

---

## 4. The Practice Layer

The practice layer targets the specific gap: designing code, not solving puzzles. Four components, all living *inside* the existing weekly hours.

### 4.1 The "build it twice" rule (highest value)

Every Sunday, after the main sub-project is done, spend ~30 min rebuilding **part of it** with one constraint changed. Examples:

- Week 1 (Reorder Point Calculator): rebuild one function using `*args` / `**kwargs`
- Week 2 (Stockout Detector): rebuild one class with an extra method you didn't originally plan for
- Week 3 (Supplier Scorecard): split a single file into two modules
- Week 4 (Inventory Data Cleaner): add one more validation rule and handle it properly

Goal: feel the *design decisions*, which is where the real learning lives.

### 4.2 Source code reading (30 min/week, split across Tue + Thu)

15-min blocks on light days. Read small, well-regarded Python code top to bottom. Don't try to use it, just read it and note what I don't understand.

**Reading list for Phase 0:**
- Week 1: `pathlib` module (standard library) — clean class-based API
- Week 2: `requests` library source — readable, well-structured, real classes
- Week 3: `click` library source — beautiful composition
- Week 4: free choice — pick a small library I'm curious about

### 4.3 Exercism.io Python track (30 min on Sunday)

One problem per week, no more. Submit, wait for mentor feedback, read the feedback carefully. The feedback loop is the point — not the problem count.

**Skip LeetCode entirely in Phase 0.** Revisit in Phase 1.5 when algorithms start mattering.

### 4.4 The 15-min daily drill (Tue + Thu)

15 min at the start of each light day, targeted at the week's weak spot:

- Weeks 1–2: rewrite one function from current sub-project as a class method, or vice versa
- Weeks 3–4: take yesterday's code and split it into two modules, or add one edge case

Small, targeted, consistent. The "typing reps" that turn recall gaps into muscle memory.

---

## 5. The Python Quick Reference

A single markdown file (`python_quick_reference.md`) I keep open in a VS Code tab while coding. When I freeze on "is it `pop` or `remove`," I glance, unfreeze, keep building. No shame in it.

**Covers:** Lists, Dicts, Sets, Strings, General-purpose built-ins (`map`, `zip`, `enumerate`, `any`, `all`, etc.), Functions reference, Control flow, "I always forget" section.

All examples use inventory/procurement context so the reference reinforces business vocabulary at the same time.

The reference grows organically: every time a gap comes up while building a sub-project, we add it to the sheet.

---

## 6. What NOT to do in Phase 0

- Don't buy a Udemy course — I have concepts, I need reps
- Don't grind LeetCode
- Don't read Fluent Python yet (comes back in Phase 2)
- Don't start a side project outside the plan — sub-projects ARE the practice
- Don't skip the "build it twice" rule because it feels redundant — it's where the skill compounds

---

## 7. Phase 0 exit checklist

By May 10, I should be able to honestly say yes to all of these:

- [ ] 4 working sub-projects on GitHub, each in its own folder with a README
- [ ] I can design a function from scratch without freezing
- [ ] I have a working mental model of classes — I know when to use one and when a dict is enough
- [ ] I can split a project across multiple files and import between them
- [ ] I can write code that handles bad input without crashing
- [ ] The quick reference has grown to include every small gap I hit during Phase 0
- [ ] My Sunday ritual has held for 4 consecutive weeks
- [ ] I've posted at least 1 LinkedIn update with real code to link to
- [ ] I'm not afraid of Phase 1

---

## 8. Repo structure for Phase 0

```
ai-inventory-platform/
├── README.md
├── journal.md
├── phase0/
│   ├── python_quick_reference.md
│   ├── week1_reorder_point/
│   │   ├── README.md
│   │   └── [code files]
│   ├── week2_stockout_detector/
│   ├── week3_supplier_scorecard/
│   └── week4_data_cleaner/
└── [future phases...]
```
