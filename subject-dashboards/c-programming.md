---
cssclasses:
  - dashboard
  - cols-2
tags:
  - c-programming
  - moc
  - dashboard
---

# 💻 C Programming — Master MOC & Progress Dashboard
> **GATE 2027 Syllabus**: `Section 4: Programming and Data Structures`

- **Master Index**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic                                             | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :---------------------------------------------------------- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Data Types, Variables & Constants                           |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Operators, Expressions & Precedence                         |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Control Flow (if-else, switch, loops)                       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Functions, Parameter Passing & Scope                        |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Recursion & Call Stack Mechanics                            |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Pointers, Pointer Arithmetic & Memory Addresses             |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Arrays, Multi-dimensional Arrays & String Handling          |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Structures, Unions & Bit-fields                             |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| Dynamic Memory Allocation (malloc, calloc, realloc, free)   |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |
| File Handling & Preprocessor Directives (#define, #include) |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |

---

## 📚 Core Concept Notes (MOC)

### 🧠 Module 1: Basics, Integers & Control Structures
- [[notes/static and dynamic|Static and Dynamic Mechanics]]
- [[notes/Integer Representation|Integer Representation]]
- [[notes/Type and Bit Conversions|Type and Bit Conversions]]
- [[notes/Constant Expressions|Constant Expressions]]
- [[notes/Operators|Operators & Precedence]]
- [[notes/Sequence Points|Sequence Points]]

---

### ⚙️ Module 2: Functions, Storage Classes & Memory
- [[notes/Functions|Functions]]
- [[notes/Storage Classes and Memory Layout|Storage Classes and Memory Layout]]
- [[notes/Memory Details|Memory Details]]

---

### 🔁 Module 3: Recursion, Pointers, Arrays & Strings
- [[notes/Recursion|Recursion]]
- [[notes/Pointers and arrays|Pointers and Arrays]]
- [[notes/Multidimensional Arrays|Multidimensional Arrays]]
- [[notes/Memory Mapping - Multidimensional Arrays|Memory Mapping - Multidimensional Arrays]]

---

### 🧱 Module 4: Memory Management & Advanced Declarations
- [[notes/malloc|Dynamic Allocation (malloc, calloc, free)]]
- [[notes/Complex Declarations|Complex Declarations]]
- [[notes/pyq analyses clang|PYQ Analyses & Tricky Scenarios]]

---

## 📑 1. Subject GATE PYQs

```dataview
TABLE WITHOUT ID
  choice(done, "✅", "❌") AS Status,
  file.link AS "Test Note",
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests/gate cse pyqs"
WHERE lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "programming" OR lower(subject) = "clang"
SORT file.name ASC
```

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
