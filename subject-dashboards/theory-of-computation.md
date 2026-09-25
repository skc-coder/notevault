---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - theory-of-computation
---

# 📚 Theory of Computation — Tracker & Materials

- **Core Note Hub**: [[notes/moc toc|Theory of Computation MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | GO Overflow | GO Classes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Regular Languages & Finite Automata (DFA, NFA, Minimization) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Context-Free Languages & Pushdown Automata (PDA) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Turing Machines & Undecidability | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "theory of computation" OR lower(subject) = "toc"
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
WHERE (lower(subject) = "theory of computation" OR lower(subject) = "toc") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "theory of computation" OR lower(subject) = "toc") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
