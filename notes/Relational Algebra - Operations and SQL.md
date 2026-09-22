> [!definition]
> * **Relational Algebra:** A procedural query language operating on relation instances that returns a relation without duplicate tuples[cite: 2].
> * **Relational Calculus:** A non-procedural (declarative) query language describing what information is retrieved rather than how[cite: 2].

> [!formula]
> **Cardinality Boundaries for Joins and Set Operations:**
> Given relation $R$ with $n$ tuples and relation $S$ with $m$ tuples:
> * Cartesian Product ($R \times S$): Exactly $n \cdot m$ tuples[cite: 2].
> * Natural Join ($R \bowtie S$): $0 \le \vert{}R \bowtie S\vert{} \le n \cdot m$[cite: 2].
>   * If common attribute is a foreign key in $R$ referencing candidate key in $S$: $\vert{}R \bowtie S\vert{} \le n$[cite: 1, 2].
> * Left Outer Join ($R = \bowtie S$): $\max(n, \vert{}R \bowtie S\vert{}) \implies n \le \vert{}R = \bowtie S\vert{} \le n \cdot m$[cite: 2].
> * Full Outer Join ($R = \bowtie= S$): $\max(n, m) \le \vert{}R = \bowtie= S\vert{} \le n \cdot m$[cite: 2].
> * Union ($R \cup S$): $\max(n, m) \le \vert{}R \cup S\vert{} \le n + m$[cite: 2].
> * Intersection ($R \cap S$): $0 \le \vert{}R \cap S\vert{} \le \min(n, m)$[cite: 2].
> * Division ($R / S$ where $S$ has degree $k$ and $R$ has degree $> k$): $0 \le \vert{}R / S\vert{} \le \lfloor n / m \rfloor$[cite: 2].

> [!trap]
> **Relational Division Operator Definition:**
> Relational division $\pi_{AB}(R) / \pi_B(S)$ retrieves values of $A$ that are paired with **every** value of $B$ in $S$[cite: 2].
> Expressed via fundamental operators:
> $$R / S = \pi_A(R) - \pi_A((\pi_A(R) \times S) - R)$$[cite: 2]

> [!question]
> **GATE / PSU Practice Drill:**
> Functional dependencies $B \rightarrow A$ and $A \rightarrow C$ hold for relations $R(A, B, C)$ and $S(B, D, E)$[cite: 1]. Relation $R$ contains $200\text{ tuples}$ and relation $S$ contains $100\text{ tuples}$[cite: 1]. Compute the maximum number of tuples possible in the natural join $R \bowtie S$[cite: 1].
>
> **Step-by-Step Resolution:**
> 1. The natural join $R \bowtie S$ joins over common attribute $\{B\}$[cite: 1, 2].
> 2. Check the candidate key status of $B$ in $R$:
>    * Given $B \rightarrow A$ and $A \rightarrow C \implies B^+ = \{A, B, C\} = R$[cite: 1].
>    * Hence, $B$ is a candidate key of $R$[cite: 1, 2].
> 3. Cardinality analysis:
>    * Since $B$ is unique in $R$, each tuple of $S$ can match at most one tuple of $R$[cite: 1, 2].
>    * Relation $S$ contains $100\text{ tuples}$[cite: 1].
>    * Even if every tuple in $S$ finds a matching $B$ in $R$, it matches exactly one tuple[cite: 1, 2].
> 4. Therefore, the maximum number of joined tuples is $\min(\vert{}S\vert{}, \vert{}R\vert{}) = 100$[cite: 1].
>
> **Maximum Tuples:** $100$[cite: 1]
