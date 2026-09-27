Variables appearing in predicate expressions are categorized by whether they fall within the operational scope of a quantifier[cite: 1].

> [!definition] Bound, Dummy, and Free Variables
> * **Bound Variable (Quantified / Dummy Variable)**: A variable $x$ occurring within the syntactical scope of $\forall x$ or $\exists x$[cite: 1]. It acts as a placeholder taking values across the domain[cite: 1].
> * **Free Variable (Real Variable / Non-Quantified)**: A variable that is not governed by any quantifier scope[cite: 1]. Its interpretation depends on an external assignment[cite: 1].
> * **Sentence (Closed Formula)**: A First-Order Logic formula containing **no free variables**[cite: 1]. Sentences have an unambiguous truth value under a given interpretation and represent complete propositions[cite: 1].

### Variable Renaming and Scope Independence

The scope of a quantifier is the structural subformula to which the quantifier applies[cite: 1].

* In an expression such as $G(x) \equiv H(x) \wedge F(x)$, both occurrences of $x$ designate the identical variable entity (analogous to the equation $f(x) = x^2 + x + 2$)[cite: 1].
* When quantifiers operate over non-overlapping or disjoint subformulas, identical variable names are semantically distinct dummy variables and can be renamed without altering meaning (alpha-conversion)[cite: 1]:
  $$\forall x \, H(x) \wedge \forall x \, P(x) \equiv \forall x \, H(x) \wedge \forall y \, P(y)$$[cite: 1]
