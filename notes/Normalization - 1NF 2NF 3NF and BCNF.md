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
