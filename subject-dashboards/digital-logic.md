---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - digital-logic
---

# 📚 Digital Logic — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 2: Digital Logic`

- **Core Concept Note Hub**: [[notes/moc dl|Digital Logic MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Boolean Algebra and Minimization (Algebraic Technique, K-Map, Tabular Method) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Design of Combinational Circuits | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Design of Sequential Circuits | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Number Representation and Arithmetic (Fixed and Floating Point) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "digital logic" OR lower(subject) = "dl"
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
WHERE (lower(subject) = "digital logic" OR lower(subject) = "dl") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "digital logic" OR lower(subject) = "dl") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
