The distributive behavior of quantifiers over binary propositional connectives depends on whether the quantifier matches the connective type[cite: 1].

### Distributive Laws: Equivalence vs. One-Way Implication

Let $Q$ denote a quantifier ($\forall$ or $\exists$) and $\circ$ denote a logical connective[cite: 1]:

| Formula Pair | Form | Implication / Equivalence Direction | GATE Invariant |
| :--- | :--- | :--- | :--- |
| $\forall x [P(x) \wedge Q(x)]$ | vs. | $\forall x \, P(x) \wedge \forall x \, Q(x)$ | $\forall x [P(x) \wedge Q(x)] \equiv \forall x \, P(x) \wedge \forall x \, Q(x)$[cite: 1] | **Full Equivalence** ($\equiv$)[cite: 1] |
| $\forall x [P(x) \vee Q(x)]$ | vs. | $\forall x \, P(x) \vee \forall x \, Q(x)$ | $\forall x \, P(x) \vee \forall x \, Q(x) \implies \forall x [P(x) \vee Q(x)]$[cite: 1] | **One-way implication** ($\Leftarrow$)[cite: 1] |
| $\exists x [P(x) \vee Q(x)]$ | vs. | $\exists x \, P(x) \vee \exists x \, Q(x)$ | $\exists x [P(x) \vee Q(x)] \equiv \exists x \, P(x) \vee \exists x \, Q(x)$[cite: 1] | **Full Equivalence** ($\equiv$)[cite: 1] |
| $\exists x [P(x) \wedge Q(x)]$ | vs. | $\exists x \, P(x) \wedge \exists x \, Q(x)$ | $\exists x [P(x) \wedge Q(x)] \implies \exists x \, P(x) \wedge \exists x \, Q(x)$[cite: 1] | **One-way implication** ($\Rightarrow$)[cite: 1] |
| $\forall x [P(x) \to Q(x)]$ | vs. | $\forall x \, P(x) \to \forall x \, Q(x)$ | $\forall x [P(x) \to Q(x)] \implies (\forall x \, P(x) \to \forall x \, Q(x))$[cite: 1] | **One-way implication** ($\Rightarrow$)[cite: 1] |
| $\exists x [P(x) \to Q(x)]$ | vs. | $\exists x \, P(x) \to \exists x \, Q(x)$ | $(\exists x \, P(x) \to \exists x \, Q(x)) \implies \exists x [P(x) \to Q(x)]$[cite: 1] | **One-way implication** ($\Leftarrow$)[cite: 1] |

> [!trap] Universal Distribution Over Disjunction Failure
> While $\forall$ distributes over $\wedge$, it **never distributes over $\vee$**[cite: 1]:
> $$\forall x [P(x) \vee Q(x)] \centernot\implies \forall x \, P(x) \vee \forall x \, Q(x)$$
> *Counterexample*: Let domain $U$ be all integers $\mathbb{Z}$. Let $P(x)$ be *"x is even"* and $Q(x)$ be *"x is odd"*.
> * Every integer is either even or odd: $\forall x [P(x) \vee Q(x)] \equiv \text{True}$.
> * But not all integers are even, and not all integers are odd: $\forall x \, P(x) \vee \forall x \, Q(x) \equiv \text{False} \vee \text{False} \equiv \text{False}$.
