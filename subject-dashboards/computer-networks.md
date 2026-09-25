---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - computer-networks
---

# 📚 Computer Networks — Tracker & Materials

- **Core Note Hub**: [[notes/moc cn|Computer Networks MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Concept of Layering & OSI/TCP-IP | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Data Link Control (Framing, Error Control, Sliding Window) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| MAC Protocols (ALOHA, CSMA/CD, Ethernet) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Network Layer (IPv4, CIDR Subnetting, Routing Algorithms) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Transport Layer (TCP Mechanics, Flow Control, Congestion) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Application Layer Protocols (DNS, HTTP, SMTP, FTP) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "computer networks" OR lower(subject) = "cn"
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
