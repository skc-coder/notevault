---
cssclasses:
  - dashboard
  - cols-2
tags:
  - gate
  - progress-tracker
  - dashboard
---

# 🎯 GATE Progress Tracker (Subject-Wise & Dataview Dashboards)

---

## 📌 Column Legend Explained

* **PYQ 1 & PYQ 2**: First complete solving of PYQs, followed by second timed/error-review pass.
* **Rev 1, Rev 2, Rev 3**: 3 spaced revision cycles for core concept notes & formulas.
* **Var 1 & Var 2**: Solving modified, tricky, or twisted GATE-level variation questions.
* **Test Series 1 & 2**: GATE Overflow & GO Classes test series.

---

## 📊 Subject Progress Matrix

| Subject / MOC | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | Test Series 1 (GO Overflow) | Test Series 2 (GO Classes) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 🔌 [[notes/moc dl|Digital Logic]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🏛️ [[notes/moc coa|Computer Organization & Arch]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| ⚙️ [[notes/moc os|Operating Systems]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🔣 [[notes/moc toc|Theory of Computation]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🛠️ [[notes/moc cd|Compiler Design]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🗄️ [[notes/moc dbms|Databases (DBMS)]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 📡 [[notes/moc cn|Computer Networks]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| ⚡ [[notes/moc algo|Algorithms]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🏗️ [[notes/moc dsa|Data Structures]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🧮 [[notes/moc maths|Engineering Mathematics]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 📐 [[notes/moc calculus|Calculus & Optimization]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🔢 [[notes/moc la|Linear Algebra]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 🎲 [[notes/moc probablity|Probability & Statistics]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| 💡 [[notes/moc aptitude|General Aptitude]] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 🚀 Quick Navigation Dashboards

- 📂 [[test-series-dashboard|GO Test Series & Overflow Dashboards]]
- 🧠 [[quiz-dashboard|CSE & DA Weekly Quizzes Dashboard]]

---

## 📑 GATE CSE PYQs (Sorted by Subject & Test Name)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration
FROM "tests/gate cse pyqs"
SORT subject ASC, file.name ASC
```
