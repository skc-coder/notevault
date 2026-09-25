---
cssclasses:
  - dashboard
  - cols-2
tags:
  - quizzes
  - weekly-quizzes
  - dashboard
---

# 🧠 Quiz Dashboard

Tracking for **CSE Weekly Quizzes** and **DA Weekly Quizzes**.

---

## 💻 CSE Weekly Quizzes (109 Quizzes)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests/cse quizzes"
SORT file.name ASC
```

---

## 📊 DA Weekly Quizzes (62 Quizzes)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests/da quizzes"
SORT file.name ASC
```
