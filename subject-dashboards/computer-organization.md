---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - computer-organization
---

# 📚 Computer Organization & Architecture — Tracker & Materials

- **Core Note Hub**: [[notes/moc coa|Computer Organization & Architecture MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Machine Instructions & Addressing Modes | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| ALU, Data Path & Control Unit (Hardwired & Microprogrammed) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Instruction Pipelining & Hazard Mitigation | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Memory Hierarchy, Cache Mapping & AMAT | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| I/O Interface (Interrupts & DMA) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "co & architecture" OR lower(subject) = "co and architecture" OR lower(subject) = "computer organization & architecture"
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
WHERE (lower(subject) = "co & architecture" OR lower(subject) = "co and architecture" OR lower(subject) = "computer organization & architecture") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "co & architecture" OR lower(subject) = "co and architecture" OR lower(subject) = "computer organization & architecture") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
