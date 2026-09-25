---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - data-structures-and-algorithms
---

# 📚 Data Structures & Algorithms — Tracker & Materials

- **Core Note Hub**: [[notes/moc dsa|Data Structures & Algorithms MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | GO Overflow | GO Classes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Arrays, Stacks, Queues & Linked Lists | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Trees, Binary Search Trees & Heaps | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Graph Traversals (BFS, DFS, Minimum Spanning Trees) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Asymptotic Analysis & Recurrences | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Sorting & Searching Algorithms | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Divide & Conquer, Greedy & Dynamic Programming | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "algorithms" OR lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms"
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
WHERE (lower(subject) = "algorithms" OR lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "algorithms" OR lower(subject) = "programming and ds" OR lower(subject) = "data structures" OR lower(subject) = "c programming" OR lower(subject) = "c-programming" OR lower(subject) = "ds" OR lower(subject) = "data structure and algorithms" OR lower(subject) = "data structures & algorithms" OR lower(subject) = "data structures and algorithms") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
