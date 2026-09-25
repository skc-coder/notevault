---
cssclasses:
  - dashboard
  - cols-2
tags:
  - gate
  - progress-tracker
  - dashboard
---

# 🎯 GATE Progress Tracker

Track your syllabus coverage across subjects and chapters: **PYQs (2 passes)**, **Revision (3 rounds)**, **Variations (2 sets)**, and **Test Series (GO Overflow & GO Classes)**.

---

## 📊 Subject Progress Matrix

| Subject / MOC             |             PYQ 1              | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | Test Series 1 (GO Overflow) | Test Series 2 (GO Classes) |     |
| :------------------------ | :----------------------------: | :---: | :---: | :---: | :---: | :---: | :---: | :-------------------------: | :------------------------: | --- |
| 🔌 [[notes/moc dl         |        Digital Logic]]         |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🏛️ [[notes/moc coa       | Computer Organization & Arch]] |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| ⚙️ [[notes/moc os         |      Operating Systems]]       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🔣 [[notes/moc toc        |    Theory of Computation]]     |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🛠️ [[notes/moc cd        |       Compiler Design]]        |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🗄️ [[notes/moc dbms      |       Databases (DBMS)]]       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 📡 [[notes/moc cn         |      Computer Networks]]       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| ⚡ [[notes/moc algo        |          Algorithms]]          |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🏗️ [[notes/moc dsa       |       Data Structures]]        |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🧮 [[notes/moc maths      |   Engineering Mathematics]]    |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 📐 [[notes/moc calculus   |   Calculus & Optimization]]    |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🔢 [[notes/moc la         |        Linear Algebra]]        |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 🎲 [[notes/moc probablity |   Probability & Statistics]]   |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |
| 💡 [[notes/moc aptitude   |       General Aptitude]]       |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |  [ ]  |             [ ]             |            [ ]             | [ ] |

---

## 📑 PYQ Test Progress Overview (Dataview)

```dataview
TABLE questions, marks, duration, status
FROM "Tests/GATE CSE PYQs"
SORT file.name ASC
LIMIT 15
```
> View complete test series breakdown in [[Test Series Dashboard]] and quizzes in [[Quiz Dashboard]].
