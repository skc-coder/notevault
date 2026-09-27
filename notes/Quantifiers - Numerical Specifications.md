Standard quantifiers can be combined with the identity relation ($=$ and $\neq$) to express exact, lower-bound, and upper-bound counts of domain elements satisfying a property $P$[cite: 1].

### Exact and Bounded Numerical Quantifications

* **At least 1 element satisfies $P$**:
  $$\exists x \, P(x)$$[cite: 1]
* **At least 2 distinct elements satisfy $P$**:
  $$\exists x \, \exists y \, [P(x) \wedge P(y) \wedge (x \neq y)]$$[cite: 1]
* **At least 3 distinct elements satisfy $P$**:
  $$\exists x \, \exists y \, \exists z \, [P(x) \wedge P(y) \wedge P(z) \wedge (x \neq y) \wedge (y \neq z) \wedge (x \neq z)]$$[cite: 1]
* **At most 1 element satisfies $P$** (meaning either zero or one element has $P$):
  $$\forall x \, \forall y \, [(P(x) \wedge P(y)) \to (x = y)]$$[cite: 1]

### Uniqueness Quantifier: Exactly One ($\exists!$)

The statement *"There exists exactly one $x$ such that $P(x)$"* (written as $\exists! x \, P(x)$ or $\exists^{=1} x \, P(x)$) asserts that at least one exists and at most one exists[cite: 1]:

> [!formula] Uniqueness Formulations
> 1. **Expanded Standard Form (Existence + Uniqueness)**:
>    $$\exists x [P(x) \wedge \forall y (P(y) \to x = y)]$$[cite: 1]
> 2. **Equivalent Two-Variable Form**:
>    $$\exists x \, \forall y [P(x) \wedge (P(y) \to x = y)]$$[cite: 1]
> 3. **Compact Equivalence Form**:
>    $$\exists x \, \forall y [P(y) \leftrightarrow x = y]$$[cite: 1]
>    *(Asserts that an object $y$ satisfies predicate $P$ if and only if $y$ is the specific object $x$)*[cite: 1].

### Generalization to Exactly $n$ Elements ($\exists^{=n}$)

To express that exactly $n$ distinct elements satisfy predicate $P(x)$[cite: 1]:
$$\exists x_1 \exists x_2 \dots \exists x_n \left[ \bigwedge_{1 \le i < j \le n} (x_i \neq x_j) \wedge \bigwedge_{i=1}^n P(x_i) \wedge \forall y \left( P(y) \to \bigvee_{i=1}^n (y = x_i) \right) \right]$$[cite: 1]
Or in compact equivalence notation[cite: 1]:
$$\exists x_1 \exists x_2 \dots \exists x_n \left[ \bigwedge_{1 \le i < j \le n} (x_i \neq x_j) \wedge \forall y \left( P(y) \leftrightarrow \bigvee_{i=1}^n (y = x_i) \right) \right]$$[cite: 1]

> [!theorem] Negation of Uniqueness
> Negating that exactly one element satisfies $P(x)$ means either no elements satisfy $P(x)$ or at least two distinct elements satisfy $P(x)$[cite: 1]:
> $$\neg \exists! x \, P(x) \equiv \forall x \, \neg P(x) \vee \exists x \, \exists y \, [P(x) \wedge P(y) \wedge (x \neq y)]$$[cite: 1]
