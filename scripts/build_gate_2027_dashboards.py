import os

VAULT = '/home/skc/Documents/notevault'
SUBJECT_DIR = os.path.join(VAULT, 'subject-dashboards')
os.makedirs(SUBJECT_DIR, exist_ok=True)

# Exact GATE 2027 CSE Syllabus Structure (10 Sections)
gate_sections = [
    {
        'id': 'discrete-mathematics',
        'section': 'Section 1: Engineering Mathematics',
        'name': 'Discrete Mathematics',
        'moc': 'notes/moc dm.md',
        'keywords': ['discrete mathematics', 'combinatorics', 'counting', 'graph theory', 'mathematical logic', 'relations', 'set theory and algebra'],
        'syllabus_topics': [
            'Propositional and First Order Logic',
            'Sets, Relations & Functions',
            'Partial Orders and Lattices',
            'Monoids & Groups',
            'Graphs: Connectivity, Matching, Colouring',
            'Combinatorics: Counting, Recurrence Relations & Generating Functions'
        ]
    },
    {
        'id': 'linear-algebra',
        'section': 'Section 1: Engineering Mathematics',
        'name': 'Linear Algebra',
        'moc': 'notes/moc la.md',
        'keywords': ['linear algebra', 'orthogonal projections and projection matrix', 'singular value decomposition (svd)'],
        'syllabus_topics': [
            'Matrices & Determinants',
            'System of Linear Equations',
            'Eigenvalues and Eigenvectors',
            'LU Decomposition'
        ]
    },
    {
        'id': 'calculus',
        'section': 'Section 1: Engineering Mathematics',
        'name': 'Calculus',
        'moc': 'notes/moc calculus.md',
        'keywords': ['calculus', 'calculus and optimisation', 'calculus and optimization'],
        'syllabus_topics': [
            'Limits, Continuity and Differentiability',
            'Maxima and Minima',
            'Mean Value Theorem',
            'Integration'
        ]
    },
    {
        'id': 'probability-and-statistics',
        'section': 'Section 1: Engineering Mathematics',
        'name': 'Probability and Statistics',
        'moc': 'notes/moc probablity.md',
        'keywords': ['probability', 'conditional probability', 'probability distributions', 'probability and statistics'],
        'syllabus_topics': [
            'Random Variables',
            'Uniform, Normal, Exponential, Poisson and Binomial Distributions',
            'Mean, Median, Mode and Standard Deviation',
            'Conditional Probability and Bayes Theorem'
        ]
    },
    {
        'id': 'digital-logic',
        'section': 'Section 2: Digital Logic',
        'name': 'Digital Logic',
        'moc': 'notes/moc dl.md',
        'keywords': ['digital logic', 'dl'],
        'syllabus_topics': [
            'Boolean Algebra and Minimization (Algebraic Technique, K-Map, Tabular Method)',
            'Design of Combinational Circuits',
            'Design of Sequential Circuits',
            'Number Representation and Arithmetic (Fixed and Floating Point)'
        ]
    },
    {
        'id': 'computer-organization-and-architecture',
        'section': 'Section 3: Computer Organization and Architecture',
        'name': 'Computer Organization & Architecture',
        'moc': 'notes/moc coa.md',
        'keywords': ['co & architecture', 'co and architecture', 'computer organization & architecture'],
        'syllabus_topics': [
            'Instruction Set Architecture and Addressing Modes',
            'Design of Arithmetic and Logic Unit (ALU)',
            'Design of Control Unit (Hardwired and Microprogrammed)',
            'Memory Interfacing & Hierarchy: Performance, Cache Mapping',
            'I/O Interface (Interrupt and DMA)',
            'Instruction Pipelining and Pipeline Hazards'
        ]
    },
    {
        'id': 'programming-and-data-structures',
        'section': 'Section 4: Programming and Data Structures',
        'name': 'Programming & Data Structures',
        'moc': 'notes/moc dsa.md',
        'keywords': ['programming and ds', 'data structures', 'c programming', 'c-programming', 'ds', 'data structure and algorithms', 'data structures & algorithms', 'data structures and algorithms'],
        'syllabus_topics': [
            'Programming in C & Recursion',
            'Arrays, Stacks, Queues and Linked Lists',
            'Trees & Binary Search Trees',
            'Binary Heaps',
            'Graphs (Representations & Basics)'
        ]
    },
    {
        'id': 'algorithms',
        'section': 'Section 5: Algorithms',
        'name': 'Algorithms',
        'moc': 'notes/moc algo.md',
        'keywords': ['algorithms'],
        'syllabus_topics': [
            'Searching, Sorting and Hashing',
            'Asymptotic Worst Case Time and Space Complexity',
            'Algorithm Design Techniques: Greedy, Dynamic Programming & Divide-and-Conquer',
            'Graph Traversals, Minimum Spanning Trees & Shortest Paths'
        ]
    },
    {
        'id': 'theory-of-computation',
        'section': 'Section 6: Theory of Computation',
        'name': 'Theory of Computation',
        'moc': 'notes/moc toc.md',
        'keywords': ['theory of computation', 'toc'],
        'syllabus_topics': [
            'Regular Expressions and Finite Automata',
            'Context-Free Grammars and Push-Down Automata',
            'Regular and Context-Free Languages & Pumping Lemma',
            'Turing Machines and Undecidability'
        ]
    },
    {
        'id': 'compiler-design',
        'section': 'Section 7: Compiler Design',
        'name': 'Compiler Design',
        'moc': 'notes/moc cd.md',
        'keywords': ['compiler design', 'cd'],
        'syllabus_topics': [
            'Lexical Analysis',
            'Parsing (Top-Down & Bottom-Up Parsing)',
            'Syntax-Directed Translation & Intermediate Code Generation',
            'Runtime Environments',
            'Local Optimisation',
            'Data Flow Analyses: Constant Propagation, Liveness Analysis, Common Sub-expression Elimination'
        ]
    },
    {
        'id': 'operating-system',
        'section': 'Section 8: Operating System',
        'name': 'Operating System',
        'moc': 'notes/moc os.md',
        'keywords': ['operating system', 'operating systems'],
        'syllabus_topics': [
            'System Calls, Processes, Threads & IPC',
            'Concurrency and Synchronization & Deadlock',
            'CPU and I/O Scheduling',
            'Memory Management and Virtual Memory',
            'File Systems'
        ]
    },
    {
        'id': 'databases',
        'section': 'Section 9: Databases',
        'name': 'Databases',
        'moc': 'notes/moc dbms.md',
        'keywords': ['databases', 'dbms', 'database management and warehousing', 'databases management and warehousing'],
        'syllabus_topics': [
            'ER-Model',
            'Relational Model: Relational Algebra, Tuple Calculus, SQL',
            'Integrity Constraints & Normal Forms',
            'File Organization & Indexing (e.g. B and B+ trees)',
            'Transactions and Concurrency Control'
        ]
    },
    {
        'id': 'computer-networks',
        'section': 'Section 10: Computer Networks',
        'name': 'Computer Networks',
        'moc': 'notes/moc cn.md',
        'keywords': ['computer networks', 'cn'],
        'syllabus_topics': [
            'Principles of Layering',
            'Basics of Switching (Circuit, Packet, Virtual Circuit) & Performance Metrics',
            'Data Link Layer: Error Detection, Medium Access Control, Ethernet',
            'Distance Vector and Link State Routing',
            'IPv4: Fragmentation, CIDR Notation, Network Address Translation (NAT)',
            'TCP: Flow Control, Congestion Control, Socket API',
            'Application Protocols: DNS and HTTP'
        ]
    },
    {
        'id': 'general-aptitude',
        'section': 'General Aptitude',
        'name': 'General Aptitude',
        'moc': 'notes/moc aptitude.md',
        'keywords': ['general aptitude', 'aptitude', 'analytical & spatial aptitude', 'quantitative aptitude', 'verbal aptitude'],
        'syllabus_topics': [
            'Verbal Ability & Grammar',
            'Quantitative Aptitude & Numerical Reasoning',
            'Analytical & Spatial Reasoning'
        ]
    },
    {
        'id': 'artificial-intelligence-and-ml',
        'section': 'DA Section: AI & ML',
        'name': 'Artificial Intelligence & Machine Learning (DA)',
        'moc': 'notes/moc python.md',
        'keywords': ['artificial intelligence', 'machine learning', 'python', 'python programming'],
        'syllabus_topics': [
            'Python Syntax & Data Structures',
            'Search Algorithms (Informed & Uninformed)',
            'Supervised Learning (Regression & Classification)',
            'Unsupervised Learning (Clustering & Dimensionality Reduction)',
            'Neural Networks & Model Evaluation'
        ]
    }
]

for s in gate_sections:
    fname = f"{s['id']}.md"
    fpath = os.path.join(SUBJECT_DIR, fname)
    
    kw_conditions = " OR ".join([f'lower(subject) = "{k}"' for k in s['keywords']])
    
    chapter_rows = ""
    for ch in s['syllabus_topics']:
        chapter_rows += f"| {ch} | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |\n"
        
    content = f"""---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - {s['id']}
---

# 📚 {s['name']} — Syllabus Tracker & Materials
> **GATE 2027 Syllabus**: `{s['section']}`

- **Core Concept Note Hub**: [[{s['moc'][:-3]}|{s['name']} MOC]]
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

print(f"Generated {len(gate_sections)} subject dashboards aligned 100% with GATE 2027 syllabus!")
