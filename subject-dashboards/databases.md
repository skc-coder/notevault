---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - databases
---

# 📚 Databases — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 9: Databases`

- **Core Concept Note Hub**: [[notes/moc dbms|Databases MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ER-Model | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Relational Model: Relational Algebra, Tuple Calculus, SQL | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Integrity Constraints & Normal Forms | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| File Organization & Indexing (e.g. B and B+ trees) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Transactions and Concurrency Control | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "databases" OR lower(subject) = "dbms" OR lower(subject) = "database management and warehousing" OR lower(subject) = "databases management and warehousing"
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
WHERE (lower(subject) = "databases" OR lower(subject) = "dbms" OR lower(subject) = "database management and warehousing" OR lower(subject) = "databases management and warehousing") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "databases" OR lower(subject) = "dbms" OR lower(subject) = "database management and warehousing" OR lower(subject) = "databases management and warehousing") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
