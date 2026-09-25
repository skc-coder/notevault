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
TABLE subject, questions, marks, duration, status, url
FROM "Tests/CSE Quizzes"
SORT file.name ASC
```

---

## 📊 DA Weekly Quizzes (62 Quizzes)

```dataview
TABLE subject, questions, marks, duration, status, url
FROM "Tests/DA Quizzes"
SORT file.name ASC
```
