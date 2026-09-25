---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - general-aptitude
---

# 📚 General Aptitude — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `General Aptitude`

- **Core Concept Note Hub**: [[notes/moc aptitude|General Aptitude MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Verbal Ability & Grammar | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Quantitative Aptitude & Numerical Reasoning | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Analytical & Spatial Reasoning | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |


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
WHERE lower(subject) = "general aptitude" OR lower(subject) = "aptitude" OR lower(subject) = "analytical & spatial aptitude" OR lower(subject) = "quantitative aptitude" OR lower(subject) = "verbal aptitude"
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
WHERE (lower(subject) = "general aptitude" OR lower(subject) = "aptitude" OR lower(subject) = "analytical & spatial aptitude" OR lower(subject) = "quantitative aptitude" OR lower(subject) = "verbal aptitude") AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE (lower(subject) = "general aptitude" OR lower(subject) = "aptitude" OR lower(subject) = "analytical & spatial aptitude" OR lower(subject) = "quantitative aptitude" OR lower(subject) = "verbal aptitude") AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
