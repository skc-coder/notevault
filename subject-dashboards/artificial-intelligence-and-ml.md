---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - artificial-intelligence-and-ml
---

# 📚 Artificial Intelligence & Machine Learning (DA) — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `DA Section: AI & ML`

- **Core Concept Note Hub**: [[notes/moc python|Artificial Intelligence & Machine Learning (DA) MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Python Syntax & Data Structures | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Search Algorithms (Informed & Uninformed) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Supervised Learning (Regression & Classification) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Unsupervised Learning (Clustering & Dimensionality Reduction) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Neural Networks & Model Evaluation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "artificial intelligence" OR lower(subject) = "machine learning" OR lower(subject) = "python" OR lower(subject) = "python programming"
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
WHERE (lower(subject) = "artificial intelligence" OR lower(subject) = "machine learning" OR lower(subject) = "python" OR lower(subject) = "python programming") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "artificial intelligence" OR lower(subject) = "machine learning" OR lower(subject) = "python" OR lower(subject) = "python programming") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
