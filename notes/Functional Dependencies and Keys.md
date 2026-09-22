> [!definition]
> Let $R$ be a relational schema and $X, Y \subseteq R$[cite: 2]. A **Functional Dependency (FD)** $X \rightarrow Y$ holds on $R$ if for any legal relation instance $r(R)$, for all pairs of tuples $t_1, t_2 \in r$:
> $$t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$[cite: 2]
> * **Trivial FD:** $X \rightarrow Y$ where $Y \subseteq X$[cite: 2].
> * **Non-Trivial FD:** $X \rightarrow Y$ where $X \cap Y = \emptyset$[cite: 2].
> * **Semi-Non-Trivial FD:** $X \rightarrow Y$ where $X \cap Y \neq \emptyset$ and $Y \not\subseteq X$[cite: 2].
> * **Super Key (SK):** A set of attributes $K \subseteq R$ such that $K^+ = R$[cite: 2].
> * **Candidate Key (CK):** A minimal super key; $K^+ = R$ and $\forall A \in K, (K \setminus \{A\})^+ \neq R$[cite: 2].
> * **Prime Attribute:** An attribute that is a member of at least one candidate key[cite: 2].
> * **Non-Prime Attribute:** An attribute that does not belong to any candidate key[cite: 2].

> [!formula]
> **Counting Super Keys for Schema $R(A_1, A_2, \dots, A_n)$:**
> * Single attribute candidate key $\{A_1\}$:
>   $$\text{Total Super Keys} = 2^{n-1}$$[cite: 2]
> * Two candidate keys of single attributes $\{A_1\}$ and $\{A_2\}$:
>   $$\vert{}S_{A_1} \cup S_{A_2}\vert{} = 2^{n-1} + 2^{n-1} - 2^{n-2} = 3 \cdot 2^{n-2}$$[cite: 2]
> * Two composite candidate keys $\{A_1 A_2\}$ and $\{A_3 A_4\}$:
>   $$\vert{}S_{A_1 A_2} \cup S_{A_3 A_4}\vert{} = 2^{n-2} + 2^{n-2} - 2^{n-4} = 2^{n-1} - 2^{n-4}$$[cite: 2]
> * Candidate key containing all $n$ attributes $\{A_1 A_2 \dots A_n\}$:
>   $$\text{Total Super Keys} = 1$$[cite: 2]

> [!theorem]
> **Armstrong's Axioms (Inference Rules):**
> * **Reflexivity:** If $Y \subseteq X$, then $X \rightarrow Y$[cite: 2].
> * **Augmentation:** If $X \rightarrow Y$, then $XZ \rightarrow YZ$[cite: 2].
> * **Transitivity:** If $X \rightarrow Y$ and $Y \rightarrow Z$, then $X \rightarrow Z$[cite: 2].
> * **Union (Additive):** If $X \rightarrow Y$ and $X \rightarrow Z$, then $X \rightarrow YZ$[cite: 2].
> * **Decomposition (Projective):** If $X \rightarrow YZ$, then $X \rightarrow Y$ and $X \rightarrow Z$[cite: 2].
> * **Pseudotransitivity:** If $X \rightarrow Y$ and $YW \rightarrow Z$, then $XW \rightarrow Z$[cite: 2].

> [!trap]
> **RHS Decomposition vs. LHS Decomposition:**
> * $X \rightarrow YZ \implies X \rightarrow Y \text{ and } X \rightarrow Z$ is valid (Decomposition)[cite: 2].
> * $XY \rightarrow Z \not\implies X \rightarrow Z \text{ or } Y \rightarrow Z$ (LHS decomposition is invalid; forms partial dependencies)[cite: 2].

> [!question]
> **PSU CBT Practice Drill:**
> Given a relation schema $R(A, B, C, D, E, H)$ with the functional dependency set:
> $$F = \{A \rightarrow B, BC \rightarrow D, E \rightarrow C, D \rightarrow A\}$$[cite: 1]
> Determine all candidate keys of $R$[cite: 1].
>
> **Step-by-Step Resolution:**
> 1. Identify attributes not appearing on any RHS of $F$:
>    * $A$ appears on LHS and RHS ($D \rightarrow A$)[cite: 1].
>    * $B$ appears on RHS ($A \rightarrow B$)[cite: 1].
>    * $C$ appears on RHS ($E \rightarrow C$)[cite: 1].
>    * $D$ appears on RHS ($BC \rightarrow D$)[cite: 1].
>    * $E$ and $H$ never appear on any RHS[cite: 1].
> 2. Essential attributes: $\{E, H\}$ must be present in every candidate key[cite: 1].
> 3. Compute attribute closures with essential attributes:
>    * $\{E, H\}^+ = \{E, H, C\} \neq R$[cite: 1]
> 4. Test 3-attribute combinations adding each remaining attribute:
>    * $\{A, E, H\}^+$:
>      $$\{A, E, H\}^+ = \{A, E, H, B, C, D\} = R \implies AEH \text{ is a CK}$$[cite: 1]
>    * $\{B, E, H\}^+$:
>      $$\{B, E, H\}^+ = \{B, E, H, C, D, A\} = R \implies BEH \text{ is a CK}$$[cite: 1]
>    * $\{D, E, H\}^+$:
>      $$\{D, E, H\}^+ = \{D, E, H, A, B, C\} = R \implies DEH \text{ is a CK}$$[cite: 1]
>    * $\{C, E, H\}^+$:
>      $$\{C, E, H\}^+ = \{C, E, H\} \neq R$$[cite: 1]
>
> **Candidate Keys:** $\{AEH, BEH, DEH\}$[cite: 1]
