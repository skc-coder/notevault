---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - probability-and-statistics
---

# 📚 Probability and Statistics — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 1: Engineering Mathematics`

- **Core Concept Note Hub**: [[notes/moc probablity|Probability and Statistics MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Random Variables | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Uniform, Normal, Exponential, Poisson and Binomial Distributions | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Mean, Median, Mode and Standard Deviation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Conditional Probability and Bayes Theorem | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "probability" OR lower(subject) = "conditional probability" OR lower(subject) = "probability distributions" OR lower(subject) = "probability and statistics"
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
WHERE (lower(subject) = "probability" OR lower(subject) = "conditional probability" OR lower(subject) = "probability distributions" OR lower(subject) = "probability and statistics") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "probability" OR lower(subject) = "conditional probability" OR lower(subject) = "probability distributions" OR lower(subject) = "probability and statistics") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
