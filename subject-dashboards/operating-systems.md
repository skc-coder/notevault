---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - operating-systems
---

# 📚 Operating Systems — Tracker & Materials

- **Core Note Hub**: [[notes/moc os|Operating Systems MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| System Calls, Processes & Threads | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| CPU Scheduling Algorithms | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Process Synchronization & Semaphores | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Deadlocks (Prevention, Avoidance, Banker's) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Memory Management & Paging (TLB, Virtual Memory) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| File Systems & Disk Scheduling | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "operating system" OR lower(subject) = "operating systems"
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
