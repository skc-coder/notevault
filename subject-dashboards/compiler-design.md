---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - compiler-design
---

# 📚 Compiler Design — Tracker & Materials

- **Core Note Hub**: [[notes/moc cd|Compiler Design MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Lexical Analysis & Tokenization | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Parsing (LL(1), LR(0), SLR, LALR, CLR) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Syntax-Directed Translation & Intermediate Code (3AC) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Code Optimization & Runtime Environments | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "compiler design" OR lower(subject) = "cd"
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
