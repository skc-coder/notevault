---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - discrete-mathematics
---

# 📚 Discrete Mathematics — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 1: Engineering Mathematics`

- **Core Concept Note Hub**: [[notes/moc dm|Discrete Mathematics MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Propositional and First Order Logic | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Sets, Relations & Functions | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Partial Orders and Lattices | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Monoids & Groups | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Graphs: Connectivity, Matching, Colouring | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Combinatorics: Counting, Recurrence Relations & Generating Functions | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "discrete mathematics" OR lower(subject) = "combinatorics" OR lower(subject) = "counting" OR lower(subject) = "graph theory" OR lower(subject) = "mathematical logic" OR lower(subject) = "relations" OR lower(subject) = "set theory and algebra"
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
WHERE (lower(subject) = "discrete mathematics" OR lower(subject) = "combinatorics" OR lower(subject) = "counting" OR lower(subject) = "graph theory" OR lower(subject) = "mathematical logic" OR lower(subject) = "relations" OR lower(subject) = "set theory and algebra") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "discrete mathematics" OR lower(subject) = "combinatorics" OR lower(subject) = "counting" OR lower(subject) = "graph theory" OR lower(subject) = "mathematical logic" OR lower(subject) = "relations" OR lower(subject) = "set theory and algebra") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
