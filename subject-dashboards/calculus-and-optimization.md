---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - calculus-and-optimization
---

# 📚 Calculus & Optimization — Tracker & Materials

- **Core Note Hub**: [[notes/moc calculus|Calculus & Optimization MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | GO Overflow | GO Classes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Limits, Continuity & Differentiability | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Mean Value Theorems | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Evaluation of Definite & Improper Integrals | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Partial Derivatives, Maxima & Minima | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Optimization Techniques | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "calculus" OR lower(subject) = "calculus and optimisation" OR lower(subject) = "calculus and optimization"
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
WHERE (lower(subject) = "calculus" OR lower(subject) = "calculus and optimisation" OR lower(subject) = "calculus and optimization") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "calculus" OR lower(subject) = "calculus and optimisation" OR lower(subject) = "calculus and optimization") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
