---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - operating-system
---

# 📚 Operating System — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 8: Operating System`

- **Core Concept Note Hub**: [[notes/moc os|Operating System MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| System Calls, Processes, Threads & IPC | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Concurrency and Synchronization & Deadlock | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| CPU and I/O Scheduling | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Memory Management and Virtual Memory | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| File Systems | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "operating system" OR lower(subject) = "operating systems"
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
WHERE (lower(subject) = "operating system" OR lower(subject) = "operating systems") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "operating system" OR lower(subject) = "operating systems") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
