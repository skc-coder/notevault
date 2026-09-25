---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - c-programming
---

# 💻 C Programming — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 4: Programming and Data Structures`

- **Core Concept Note Hub**: [[notes/moc clang|C Programming MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Data Types, Variables & Constants | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Operators, Expressions & Precedence | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Control Flow (if-else, switch, loops) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Functions, Parameter Passing & Scope | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Recursion & Call Stack Mechanics | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Pointers, Pointer Arithmetic & Memory Addresses | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Arrays, Multi-dimensional Arrays & String Handling | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Structures, Unions & Bit-fields | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Dynamic Memory Allocation (malloc, calloc, realloc, free) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| File Handling & Preprocessor Directives (#define, #include) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


---

## 🧠 2. Weekly Quizzes

```dataview
TABLE WITHOUT ID
  choice(done, "✅", "❌") AS Status,
  file.link AS "Test Note",
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests"
WHERE (lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "programming" OR lower(subject) = "clang") AND (contains(category, "quiz") OR contains(category, "Quiz"))
SORT file.name ASC
```

---

## 🏛️ 3. Test Series (GO Overflow & GO Classes)

```dataview
TABLE WITHOUT ID
  choice(done, "✅", "❌") AS Status,
  file.link AS "Test Note",
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests"
WHERE (lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "programming" OR lower(subject) = "clang") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
