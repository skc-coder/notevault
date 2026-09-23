> [!definition]
> **Relational Normal Forms** define structural constraints on schemas to eliminate modification anomalies (Insert, Update, Delete) and data redundancy[cite: 2].
> * **1NF:** Every attribute domain contains only atomic (indivisible) values[cite: 2]. No composite or multi-valued attributes allowed[cite: 1, 2].
> * **2NF:** Relation is in 1NF and contains no **partial dependencies**[cite: 2]. Every non-prime attribute must be fully functionally dependent on every candidate key[cite: 1, 2].
>   $$\text{Partial Dependency Violation: } X \rightarrow Y \text{ where } X \subset CK \text{ and } Y \text{ is non-prime}$$[cite: 2]
> * **3NF:** Relation is in 2NF and contains no **transitive dependencies** of non-prime attributes on candidate keys[cite: 2]. For every non-trivial FD $X \rightarrow Y$:
>   $$X \text{ is a Super Key (SK)} \quad \lor \quad Y \text{ is a Prime Attribute}$$[cite: 2]
> * **BCNF (Boyce-Codd Normal Form):** For every non-trivial FD $X \rightarrow Y$:
>   $$X \text{ is a Super Key (SK)}$$[cite: 2]

| Normal Form | Allowed LHS ($X$) | Allowed RHS ($Y$) | Redundancy Over FDs |
| :--- | :--- | :--- | :--- |
| **1NF** | Any attribute set[cite: 2] | Any attribute set[cite: 2] | Highest[cite: 2] |
| **2NF** | Full Candidate Key / Super Key (for non-primes)[cite: 2] | Prime or Non-prime[cite: 2] | High[cite: 2] |
| **3NF** | Super Key OR Non-SK if RHS is prime[cite: 2] | Prime (if $X$ not SK) or Any (if $X$ is SK)[cite: 2] | Low (allows $X \subset CK \rightarrow Y \subset CK$)[cite: 2] |
| **BCNF** | Must be Super Key (strictly)[cite: 2] | Any attribute set[cite: 2] | $0\%$ redundancy over FDs[cite: 2] |

> [!theorem]
> **Key Structural Invariants for Rapid CBT Testing:**
> 1. Any binary relation $R(A, B)$ is **always in BCNF**[cite: 1].
> 2. If every candidate key of relation $R$ consists of a single attribute (simple candidate keys), then $R$ is **always in 2NF** (no proper subset of a key can exist)[cite: 1, 2].
> 3. If a relation has **only prime attributes**, it is **always in 3NF**[cite: 2].
> 4. If a relation contains no non-trivial functional dependencies, it is **always in BCNF**[cite: 2].
> 5. Decomposition into 3NF can **always** achieve both **Lossless Join** and **Dependency Preservation**[cite: 2].
> 6. Decomposition into BCNF is **always Lossless**, but **may not preserve dependencies**[cite: 2].

> [!trap]
> **The 3NF vs BCNF Trap Condition:**
> A schema $R$ is in 3NF but fails BCNF if and only if there exists an FD $X \rightarrow Y$ where $X$ is not a super key, but $Y$ is a prime attribute[cite: 2]. This strictly occurs when candidate keys overlap and:
> $$(\text{Proper subset of a CK}) \rightarrow (\text{Proper subset of another CK})$$[cite: 2]

> [!question]
> **PSU CBT Practice Drill:**
> Consider the schema $R(A, B, C, D)$ with functional dependency set:
> $$F = \{AB \rightarrow C, AB \rightarrow D, C \rightarrow A, D \rightarrow B\}$$[cite: 1]
> Find the highest normal form of $R$[cite: 1].
>
> **Step-by-Step Resolution:**
> 1. Compute candidate keys:
>    * $(AB)^+ = \{A, B, C, D\} \implies AB$ is a CK[cite: 1].
>    * Since $C \rightarrow A$, replace $A$ in $AB$ with $C \implies (CB)^+ = \{C, B, A, D\} \implies BC$ is a CK[cite: 1].
>    * Since $D \rightarrow B$, replace $B$ in $AB$ with $D \implies (AD)^+ = \{A, D, B, C\} \implies AD$ is a CK[cite: 1].
>    * Replace $B$ in $BC$ with $D \implies (CD)^+ = \{C, D, A, B\} \implies CD$ is a CK[cite: 1].
> 2. Candidate Keys: $\{AB, BC, AD, CD\}$[cite: 1].
> 3. Prime attributes: $\{A, B, C, D\}$[cite: 1].
> 4. Check Normal Form conditions:
>    * Non-prime attributes: None ($\emptyset$)[cite: 1, 2].
>    * Since all attributes in $R$ are prime attributes, the relation is **guaranteed to be in 3NF**[cite: 1, 2].
>    * Check BCNF: In $C \rightarrow A$, $C^+ = \{C, A\} \neq R$, so $C$ is not a super key[cite: 1]. Thus, BCNF is violated[cite: 2].
>
> **Highest Normal Form:** Third Normal Form (3NF)[cite: 1]

Bill Kent famously summarized Edgar Codd’s rules for 3NF with the courtroom oath:


> _"Every non-key attribute must provide a fact about the key, the whole key, and nothing but the key, so help me Codd."_
> 
>   

Here is the upgraded, foolproof version that actually fixes its flaws, includes BCNF, and makes the logical ladder stick instantly:

  

### The Boss Oath

Think of the **Candidate Key (CK)** as the **Only Boss** in the room.

  

```
1NF: "No clown cars."
     One seat = one person (Atomic values only).

2NF: "Respect the WHOLE Boss."
     You can't take orders from half a boss. 
     (No proper subset of a CK determining non-primes).

3NF: "No middle management."
     You take orders ONLY from the Boss, not from another employee.
     (No non-prime determining non-primes).

BCNF: "If you give orders, YOU MUST BE A BOSS."
      Zero exceptions. If you determine anything, you MUST be a full key.
```

### How to Picture the Filter

Every step simply eliminates who is allowed to boss around other columns:

  

1. **1NF:** Eliminates **groups/lists** in a single cell.
    
      
    
2. **2NF:** Eliminates **half-key bosses** (fixes composite keys).
    
      
    
3. **3NF:** Eliminates **coworker bosses** (fixes transitive middlemen).
    
      
    
4. **BCNF:** Eliminates **pretender bosses** (anyone giving orders who isn't a certified candidate key).
    
      
    

### The 2-Second Test on Any Arrow ($X \rightarrow Y$)

When checking a functional dependency $X \rightarrow Y$ in an exam:

```
Is X a Super Key?
  ├── YES ──> Passed ALL (1NF, 2NF, 3NF, BCNF)
  └── NO  ──> Look at Y:
               ├── Is Y a Prime Attribute (part of a key)?
               │    ├── YES ──> Passed 3NF (Fails BCNF)
               │    └── NO  ──> Fails 3NF!
               │                 │
               │                 └── Is X part of a composite key?
               │                      ├── YES ──> Fails 2NF (Partial)
               │                      └── NO  ──> Fails 3NF (Transitive)
```

You have hit on the exact mechanical reality of normalization. When stripped of formal textbook jargon, the normal forms are nothing more than a severity scale of **how unrelated data is being forced into the same table**.

  

Here is your exact intuition aligned with relational theory, broken down by how each bad arrow matches real-world database rot.

  

### The Baseline: $SK \rightarrow \text{Anything}$ (The Clean State)

- **What you said:** If $X$ is a Candidate Key / Super Key, $X$ is unique per row, so $Y$ doesn't repeat for that key.
    
      
    
- **Theory:** If **every** non-trivial dependency in a table is of the form $SK \rightarrow \text{Anything}$, the schema is in **BCNF**.
    
      
    
- **Redundancy:** **0% redundancy** over functional dependencies. Every row is a distinct fact about the primary identifier.
    
      
    

### Level 1 (Catastrophic Mess): $\text{Proper Subset of CK} \rightarrow \text{Non-Prime}$ (Fails 2NF)

- **Notation:** $PA_{\text{subset}} \rightarrow NPA$
    
      
    
      
    
- **Your Intuition:** _"Big mess... unrelated data together. E.g., salary of a teacher and address of a student."_
    
      
    
- **Why it's a disaster:** You have a composite key representing two completely separate entities meeting together (like `StudentID + TeacherID`). Putting the teacher’s salary or student's address here forces an attribute to bind to only **half** of the identity. Every time that student takes a class with that teacher, the salary or address gets copy-pasted over and over.
    
      
    
- **The Normal Form Fix:** **2NF** specifically targets and eliminates this exact severity level.
    
      
    

### Level 2 (Intermediate Mess): $\text{Non-Prime} \rightarrow \text{Non-Prime}$ (Fails 3NF)

- **Notation:** $NPA \rightarrow NPA$
    
      
    
      
    
- **Your Intuition:** _"Related, but still not so related... info about a teacher, but in what room a subject is taught is slightly unrelated."_
    
      
    
- **Why it's sloppy:** The primary key is clean and intact (maybe a single key like `CourseID`), but inside the non-key columns, one non-key attribute acts as a "puppet master" over another non-key attribute.
    
      
    - E.g., `CourseID` determines `Teacher`, but `Teacher` determines `RoomNumber`.
        
          
        
    - The teacher and room are connected to the course, but `RoomNumber` belongs to the `Teacher`, not the `Course`.
        
          
        
- **The Normal Form Fix:** **3NF** forbids this entirely. In 3NF, a non-prime is **never** allowed to dictate another non-prime.
    
      
    

### Level 3 (The Tolerable Edge Case): $\text{Proper Subset of CK} \rightarrow \text{Proper Subset of CK}$ (Passes 3NF, Fails BCNF)

- **Notation:** $PA_{\text{subset}} \rightarrow PA_{\text{subset}}$
    
      
    
      
    
- **Your Intuition:** _"Least troubling... highly related data, still some redundancy. Tutor depends on subject and student... solving this may be possible or not, but it's enough."_
    
      
    
- **Why this is profound:** You captured the exact reason Edgar Codd created 3NF before BCNF was even discovered:
    
      
    - In this scenario, all the columns are **prime** (they are all pieces of candidate keys). The data is inherently tightly coupled.
        
          
        
    - There is still minor duplication (e.g., repeating that a Tutor teaches a specific Subject across multiple student assignments).
        
          
        
    - **The Tradeoff:** As you pointed out, _"solving this may be possible or not"_—if you force this into BCNF by splitting it, you often **destroy dependency preservation**! You can't verify the combined rule without doing an expensive multi-table join.
        
          
        
- **The Normal Form Fix:** **3NF intentionally forgives this edge case** because preserving the business constraint without joins is worth tolerating that small slice of redundancy. Only **BCNF** is stubborn enough to break it apart anyway.
    
      
    

### Summary: Your Mental Map vs. Academic Terminology

|**Your Intuition**|**Formal Dependency Type**|**Failed Level**|**Permitted By**|
|---|---|---|---|
|**Clean / Unique Data**|$SK \rightarrow \text{All}$|None (Optimal)|1NF, 2NF, 3NF, BCNF|
|**Big Mess (Unrelated entities smashed together)**|$PA_{\text{proper subset}} \rightarrow NPA$|**Fails 2NF** (Partial Dependency)|1NF only|
|**Second Mess (Coworker dictating coworker)**|$NPA \rightarrow NPA$|**Fails 3NF** (Transitive Dependency)|2NF|
|**Minor Overlap (Tightly coupled keys, slight leak)**|$PA_{\text{subset}} \rightarrow PA_{\text{subset}}$|**Fails BCNF** (Overlapping CK Loophole)|**Allowed in 3NF**|

This mental model cuts straight to the real engineering reason tables are decomposed: you are simply filtering out looser and looser relationships until every single column answers only to the unique identity of that table.