---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - databases
---

# 📚 Databases (DBMS) — Tracker & Materials

- **Core Note Hub**: [[notes/moc dbms|Databases (DBMS) MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ER-Model & Relational Algebra | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| SQL Queries & Aggregations | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Functional Dependencies & Normalization (1NF to BCNF) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Transactions & Concurrency Control (Serializability, 2PL) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| File Structures, B-Trees & B+ Trees Indexing | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


---

## 📑 1. GATE PYQs

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

## 🧠 2. Weekly Quizzes (CSE & DA)

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
