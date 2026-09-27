Null quantification applies when a quantified formula contains a subformula that does not contain the quantified bound variable[cite: 1].

> [!definition] Null Quantification
> If $A$ is a formula that contains **no free occurrence of variable $x$**, the quantification over $A$ is null (has no operational effect)[cite: 1]:
> $$\forall x \, A \equiv A \quad \text{and} \quad \exists x \, A \equiv A$$[cite: 1]

### Null Quantification Shift Equivalences

Let $A$ be a formula independent of variable $x$[cite: 1]:

> [!theorem] Conjunction and Disjunction Null Shifts
> 1. $\forall x [P(x) \wedge A] \equiv \forall x \, P(x) \wedge A$[cite: 1]
> 2. $\forall x [P(x) \vee A] \equiv \forall x \, P(x) \vee A$[cite: 1]
> 3. $\exists x [P(x) \wedge A] \equiv \exists x \, P(x) \wedge A$[cite: 1]
> 4. $\exists x [P(x) \vee A] \equiv \exists x \, P(x) \vee A$[cite: 1]

> [!theorem] Implication Null Shifts (Quantifier Inversion Rules)
> When pulling an independent subformula $A$ out of an implication, the quantifier flips if and only if $A$ was in the antecedent position[cite: 1]:
> 
> * **$A$ in Antecedent (Position 1 — Quantifier Flips)**:
>   * $\forall x [A \to P(x)] \equiv A \to \forall x \, P(x)$[cite: 1]
>   * $\exists x [A \to P(x)] \equiv A \to \exists x \, P(x)$[cite: 1]
>   * $\forall x [P(x) \to A] \equiv \exists x \, P(x) \to A$[cite: 1] *(Antecedent $P(x)$ shifts $\forall \to \exists$)*[cite: 1]
>   * $\exists x [P(x) \to A] \equiv \forall x \, P(x) \to A$[cite: 1] *(Antecedent $P(x)$ shifts $\exists \to \forall$)*[cite: 1]

> [!formula] Proof of Antecedent Inversion Rule
> Expanding the implication using material implication:
> $$\forall x [P(x) \to A] \equiv \forall x [\neg P(x) \vee A]$$[cite: 1]
> Since $A$ is independent of $x$, apply disjunction shift[cite: 1]:
> $$\forall x [\neg P(x) \vee A] \equiv \forall x [\neg P(x)] \vee A$$[cite: 1]
> Applying De Morgan's quantifier law[cite: 1]:
> $$\forall x [\neg P(x)] \vee A \equiv \neg \exists x \, P(x) \vee A$$[cite: 1]
> Recombining via material implication[cite: 1]:
> $$\neg (\exists x \, P(x)) \vee A \equiv \exists x \, P(x) \to A$$[cite: 1]
