import os

VAULT = '/home/skc/Documents/notevault'
SUBJECT_DIR = os.path.join(VAULT, 'subject-dashboards')

c_prog = {
    'id': 'c-programming',
    'section': 'Section 4: Programming and Data Structures',
    'name': 'C Programming',
    'moc': 'notes/moc clang.md',
    'keywords': ['c programming', 'c-programming', 'programming', 'clang'],
    'syllabus_topics': [
        'Data Types, Variables & Constants',
        'Operators, Expressions & Precedence',
        'Control Flow (if-else, switch, loops)',
        'Functions, Parameter Passing & Scope',
        'Recursion & Call Stack Mechanics',
        'Pointers, Pointer Arithmetic & Memory Addresses',
        'Arrays, Multi-dimensional Arrays & String Handling',
        'Structures, Unions & Bit-fields',
        'Dynamic Memory Allocation (malloc, calloc, realloc, free)',
        'File Handling & Preprocessor Directives (#define, #include)'
    ]
}

fname = f"{c_prog['id']}.md"
fpath = os.path.join(SUBJECT_DIR, fname)

kw_conditions = " OR ".join([f'lower(subject) = "{k}"' for k in c_prog['keywords']])

chapter_rows = ""
for ch in c_prog['syllabus_topics']:
    chapter_rows += f"| {ch} | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |\n"
    
content = f"""---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - c-programming
---

# 💻 C Programming — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `{c_prog['section']}`

- **Core Concept Note Hub**: [[{c_prog['moc'][:-3]}|C Programming MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 GATE 2027 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{chapter_rows}

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
WHERE {kw_conditions}
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
WHERE ({kw_conditions}) AND (contains(category, "quiz") OR contains(category, "Quiz"))
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
WHERE ({kw_conditions}) AND (contains(category, "Series") OR contains(category, "2027"))
SORT file.name ASC
```
"""

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Created c-programming.md subject dashboard!")
