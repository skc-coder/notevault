Quantifiers specify how a predicate behaves across the entire universe of discourse $U = \{x_1, x_2, x_3, \dots\}$[cite: 1].

> [!definition] Universal Quantifier ($\forall$)
> The notation $\forall x \, P(x)$ denotes *"for all $x$, $P(x)$ holds"*[cite: 1]. It evaluates to $\text{True}$ if and only if $P(c)$ is true for every element $c \in U$[cite: 1].
> * It behaves as an infinite or finite conjunction ($\wedge$) over the domain[cite: 1]:
>   $$\forall x \, P(x) \equiv P(x_1) \wedge P(x_2) \wedge P(x_3) \wedge \dots$$[cite: 1]
> * **Falsification Condition**: $\forall x \, P(x)$ is $\text{False}$ if and only if there exists at least one **counterexample** $c \in U$ such that $P(c) \equiv \text{False}$[cite: 1].

> [!definition] Existential Quantifier ($\exists$)
> The notation $\exists x \, P(x)$ denotes *"there exists an $x$ such that $P(x)$ holds"*[cite: 1]. It evaluates to $\text{True}$ if and only if $P(c)$ is true for at least one element $c \in U$[cite: 1].
> * It behaves as an infinite or finite disjunction ($\vee$) over the domain[cite: 1]:
>   $$\exists x \, P(x) \equiv P(x_1) \vee P(x_2) \vee P(x_3) \vee \dots$$[cite: 1]
> * **Verification Condition**: $\exists x \, P(x)$ is $\text{True}$ if and only if there exists at least one **witness** $w \in U$ such that $P(w) \equiv \text{True}$[cite: 1].

> [!theorem] Quantifier Duality (De Morgan's Laws for Quantifiers)
> Negating a quantifier flips its type and negates the inner predicate formula[cite: 1]:
> 1. $\neg \forall x \, P(x) \equiv \exists x \, \neg P(x)$[cite: 1]
> 2. $\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$[cite: 1]
