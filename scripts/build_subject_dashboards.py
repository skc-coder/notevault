import os
import re

VAULT = '/home/skc/Documents/notevault'
SUBJECT_DIR = os.path.join(VAULT, 'subject-dashboards')
os.makedirs(SUBJECT_DIR, exist_ok=True)

# Standard Subject Mapping for CS & DA
subjects = [
    {
        'id': 'digital-logic',
        'name': 'Digital Logic',
        'moc': 'notes/moc dl.md',
        'keywords': ['digital logic', 'dl'],
        'chapters': [
            'Boolean Algebra Basics & Laws',
            'Standard Forms (SOM / POM) & Minterms',
            'K-Map Minimization & Prime Implicants',
            'Number Systems, Base Conversions & Complements',
            'Combinational Circuits (MUX, DEMUX, Decoders, Encoders)',
            'Adders, Subtractors & Carry Look-Ahead',
            'Sequential Circuits (Latches, Flip-Flops, FSM)',
            'Counters (Ripple, Synchronous, Ring, Johnson)'
        ]
    },
    {
        'id': 'computer-organization',
        'name': 'Computer Organization & Architecture',
        'moc': 'notes/moc coa.md',
        'keywords': ['co & architecture', 'co and architecture', 'computer organization & architecture'],
        'chapters': [
            'Machine Instructions & Addressing Modes',
            'ALU, Data Path & Control Unit (Hardwired & Microprogrammed)',
            'Instruction Pipelining & Hazard Mitigation',
            'Memory Hierarchy, Cache Mapping & AMAT',
            'I/O Interface (Interrupts & DMA)'
        ]
    },
    {
        'id': 'operating-systems',
        'name': 'Operating Systems',
        'moc': 'notes/moc os.md',
        'keywords': ['operating system', 'operating systems'],
        'chapters': [
            'System Calls, Processes & Threads',
            'CPU Scheduling Algorithms',
            'Process Synchronization & Semaphores',
            'Deadlocks (Prevention, Avoidance, Banker\'s)',
            'Memory Management & Paging (TLB, Virtual Memory)',
            'File Systems & Disk Scheduling'
        ]
    },
    {
        'id': 'theory-of-computation',
        'name': 'Theory of Computation',
        'moc': 'notes/moc toc.md',
        'keywords': ['theory of computation', 'toc'],
        'chapters': [
            'Regular Languages & Finite Automata (DFA, NFA, Minimization)',
            'Context-Free Languages & Pushdown Automata (PDA)',
            'Turing Machines & Undecidability'
        ]
    },
    {
        'id': 'compiler-design',
        'name': 'Compiler Design',
        'moc': 'notes/moc cd.md',
        'keywords': ['compiler design', 'cd'],
        'chapters': [
            'Lexical Analysis & Tokenization',
            'Parsing (LL(1), LR(0), SLR, LALR, CLR)',
            'Syntax-Directed Translation & Intermediate Code (3AC)',
            'Code Optimization & Runtime Environments'
        ]
    },
    {
        'id': 'databases',
        'name': 'Databases (DBMS)',
        'moc': 'notes/moc dbms.md',
        'keywords': ['databases', 'dbms', 'database management and warehousing', 'databases management and warehousing'],
        'chapters': [
            'ER-Model & Relational Algebra',
            'SQL Queries & Aggregations',
            'Functional Dependencies & Normalization (1NF to BCNF)',
            'Transactions & Concurrency Control (Serializability, 2PL)',
            'File Structures, B-Trees & B+ Trees Indexing'
        ]
    },
    {
        'id': 'computer-networks',
        'name': 'Computer Networks',
        'moc': 'notes/moc cn.md',
        'keywords': ['computer networks', 'cn'],
        'chapters': [
            'Concept of Layering & OSI/TCP-IP',
            'Data Link Control (Framing, Error Control, Sliding Window)',
            'MAC Protocols (ALOHA, CSMA/CD, Ethernet)',
            'Network Layer (IPv4, CIDR Subnetting, Routing Algorithms)',
            'Transport Layer (TCP Mechanics, Flow Control, Congestion)',
            'Application Layer Protocols (DNS, HTTP, SMTP, FTP)'
        ]
    },
    {
        'id': 'data-structures-and-algorithms',
        'name': 'Data Structures & Algorithms',
        'moc': 'notes/moc dsa.md',
        'keywords': ['algorithms', 'programming and ds', 'data structures', 'c programming', 'c-programming', 'ds', 'data structure and algorithms', 'data structures & algorithms', 'data structures and algorithms'],
        'chapters': [
            'Arrays, Stacks, Queues & Linked Lists',
            'Trees, Binary Search Trees & Heaps',
            'Graph Traversals (BFS, DFS, Minimum Spanning Trees)',
            'Asymptotic Analysis & Recurrences',
            'Sorting & Searching Algorithms',
            'Divide & Conquer, Greedy & Dynamic Programming'
        ]
    },
    {
        'id': 'linear-algebra',
        'name': 'Linear Algebra',
        'moc': 'notes/moc la.md',
        'keywords': ['linear algebra', 'orthogonal projections and projection matrix', 'singular value decomposition (svd)'],
        'chapters': [
            'Matrices & Determinants',
            'Systems of Linear Equations',
            'Eigenvalues, Eigenvectors & LU Decomposition',
            'Vector Spaces & Projections (SVD)'
        ]
    },
    {
        'id': 'calculus-and-optimization',
        'name': 'Calculus & Optimization',
        'moc': 'notes/moc calculus.md',
        'keywords': ['calculus', 'calculus and optimisation', 'calculus and optimization'],
        'chapters': [
            'Limits, Continuity & Differentiability',
            'Mean Value Theorems',
            'Evaluation of Definite & Improper Integrals',
            'Partial Derivatives, Maxima & Minima',
            'Optimization Techniques'
        ]
    },
    {
        'id': 'probability-and-statistics',
        'name': 'Probability & Statistics',
        'moc': 'notes/moc probablity.md',
        'keywords': ['probability', 'conditional probability', 'probability distributions', 'probability and statistics'],
        'chapters': [
            'Counting, Permutations & Combinations',
            'Axioms of Probability & Bayes Theorem',
            'Random Variables (Discrete & Continuous)',
            'Distributions (Binomial, Poisson, Normal, Exponential)',
            'Mean, Median, Mode & Standard Deviation'
        ]
    },
    {
        'id': 'discrete-mathematics',
        'name': 'Discrete Mathematics',
        'moc': 'notes/moc dm.md',
        'keywords': ['discrete mathematics', 'combinatorics', 'counting', 'graph theory', 'mathematical logic', 'relations', 'set theory and algebra'],
        'chapters': [
            'Propositional & First Order Logic',
            'Set Theory, Relations & Functions',
            'Partial Orders, Lattices & Boolean Algebra',
            'Groups & Combinatorics',
            'Graph Connectivity, Coloring & Trees'
        ]
    },
    {
        'id': 'general-aptitude',
        'name': 'General Aptitude',
        'moc': 'notes/moc aptitude.md',
        'keywords': ['general aptitude', 'aptitude', 'analytical & spatial aptitude', 'quantitative aptitude', 'verbal aptitude'],
        'chapters': [
            'Verbal Ability & Grammar',
            'Quantitative Aptitude & Numerical Reasoning',
            'Analytical & Spatial Reasoning'
        ]
    },
    {
        'id': 'artificial-intelligence-and-ml',
        'name': 'Artificial Intelligence & Machine Learning (DA)',
        'moc': 'notes/moc python.md',
        'keywords': ['artificial intelligence', 'machine learning', 'python', 'python programming'],
        'chapters': [
            'Python Syntax & Data Structures',
            'Search Algorithms (Informed & Uninformed)',
            'Supervised Learning (Regression & Classification)',
            'Unsupervised Learning (Clustering & Dimensionality Reduction)',
            'Neural Networks & Model Evaluation'
        ]
    }
]

for s in subjects:
    fname = f"{s['id']}.md"
    fpath = os.path.join(SUBJECT_DIR, fname)
    
    # Build list of matching subject names for Dataview WHERE clause
    kw_conditions = " OR ".join([f'lower(subject) = "{k}"' for k in s['keywords']])
    
    chapter_rows = ""
    for ch in s['chapters']:
        chapter_rows += f"| {ch} | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |\n"
        
    content = f"""---
cssclasses:
  - dashboard
tags:
  - subject-dashboard
  - {s['id']}
---

# 📚 {s['name']} — Tracker & Materials

- **Core Note Hub**: [[{s['moc'][:-3]}|{s['name']} MOC]]
- **Master Progress Tracker**: [[gate-progress-tracker|GATE Progress Tracker]]

---

## 📊 Chapter-Wise Progress Matrix

| Chapter / Topic | PYQ 1 | PYQ 2 | Rev 1 | Rev 2 | Rev 3 | Var 1 | Var 2 | GO Overflow | GO Classes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{chapter_rows}

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
WHERE {kw_conditions}
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

print(f"Generated {len(subjects)} individual subject dashboards in {SUBJECT_DIR}/")
