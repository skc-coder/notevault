---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - computer-organization-and-architecture
---

# 📚 Computer Organization & Architecture — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 3: Computer Organization and Architecture`

- **Core Concept Note Hub**: [[notes/moc coa|Computer Organization & Architecture MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Instruction Set Architecture and Addressing Modes | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Design of Arithmetic and Logic Unit (ALU) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Design of Control Unit (Hardwired and Microprogrammed) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Memory Interfacing & Hierarchy: Performance, Cache Mapping | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| I/O Interface (Interrupt and DMA) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Instruction Pipelining and Pipeline Hazards | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "co & architecture" OR lower(subject) = "co and architecture" OR lower(subject) = "computer organization & architecture"
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
