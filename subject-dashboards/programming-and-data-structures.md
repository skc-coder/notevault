---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - programming-and-data-structures
---

# 📚 Programming & Data Structures — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 4: Programming and Data Structures`

- **Core Concept Note Hub**: [[notes/moc dsa|Programming & Data Structures MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Programming in C & Recursion | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Arrays, Stacks, Queues and Linked Lists | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Trees & Binary Search Trees | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Binary Heaps | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Graphs (Representations & Basics) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms"
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
WHERE (lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
