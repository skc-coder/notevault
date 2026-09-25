---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - computer-networks
---

# 📚 Computer Networks — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `Section 10: Computer Networks`

- **Core Concept Note Hub**: [[notes/moc cn|Computer Networks MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Principles of Layering | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Basics of Switching (Circuit, Packet, Virtual Circuit) & Performance Metrics | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Data Link Layer: Error Detection, Medium Access Control, Ethernet | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Distance Vector and Link State Routing | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| IPv4: Fragmentation, CIDR Notation, Network Address Translation (NAT) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| TCP: Flow Control, Congestion Control, Socket API | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Application Protocols: DNS and HTTP | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "computer networks" OR lower(subject) = "cn"
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
WHERE (lower(subject) = "computer networks" OR lower(subject) = "cn") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "computer networks" OR lower(subject) = "cn") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
