---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - probability-and-statistics
---

# 📚 Probability & Statistics — Tracker & Materials

- **Core Note Hub**: [[notes/moc probablity|Probability & Statistics MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | GO Overflow | GO Classes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Counting, Permutations & Combinations | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Axioms of Probability & Bayes Theorem | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Random Variables (Discrete & Continuous) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Distributions (Binomial, Poisson, Normal, Exponential) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Mean, Median, Mode & Standard Deviation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "probability" OR lower(subject) = "conditional probability" OR lower(subject) = "probability distributions" OR lower(subject) = "probability and statistics"
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
