When multiple quantifiers govern an expression, their left-to-right syntactic ordering determines the dependency structure of the variables[cite: 1].

### Nested Quantifier Permutations over $P(x, y)$

Let $P(x, y)$ denote the relation *"x loves y"*[cite: 1]:

| Quantified Formula | Natural Language Meaning | Semantic Interpretation |
| :--- | :--- | :--- |
| $\forall x \, \forall y \, P(x, y)$[cite: 1] | Everybody loves everybody[cite: 1]. | Holds for all Cartesian pairs $(x, y) \in U \times U$[cite: 1]. |
| $\forall x \, \exists y \, P(x, y)$[cite: 1] | Everybody loves someone[cite: 1]. | For every person $x$, there is a (possibly different) person $y$ they love[cite: 1]. |
| $\exists x \, \forall y \, P(x, y)$[cite: 1] | Someone loves everybody[cite: 1]. | There exists a single universal lover $x$ who loves every person $y$[cite: 1]. |
| $\exists x \, \exists y \, P(x, y)$[cite: 1] | Someone loves someone[cite: 1]. | There exists at least one pair $(x, y)$ satisfying the relation[cite: 1]. |

> [!theorem] Quantifier Commutativity and Non-Commutativity
> Identical consecutive quantifiers commute freely without changing semantic truth[cite: 1]:
> $$\forall x \, \forall y \, P(x, y) \equiv \forall y \, \forall x \, P(x, y)$$
> $$\exists x \, \exists y \, P(x, y) \equiv \exists y \, \exists x \, P(x, y)$$
> Mixed quantifiers **do not commute**[cite: 1]:
> $$\exists x \, \forall y \, P(x, y) \implies \forall y \, \exists x \, P(x, y)$$
> The converse does not hold ($\forall y \, \exists x \, P(x, y) \centernot\implies \exists x \, \forall y \, P(x, y)$)[cite: 1]. Finding a single entity that works for all implies that for each element someone exists, but the reverse does not guarantee a single uniform choice[cite: 1].
