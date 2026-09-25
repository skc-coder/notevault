---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - compiler-design
---

# 📚 Compiler Design — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 7: Compiler Design`

- **Core Concept Note Hub**: [[notes/moc cd|Compiler Design MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Lexical Analysis | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Parsing (Top-Down & Bottom-Up Parsing) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Syntax-Directed Translation & Intermediate Code Generation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Runtime Environments | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Local Optimisation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Data Flow Analyses: Constant Propagation, Liveness Analysis, Common Sub-expression Elimination | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "compiler design" OR lower(subject) = "cd"
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
WHERE (lower(subject) = "compiler design" OR lower(subject) = "cd") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "compiler design" OR lower(subject) = "cd") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
