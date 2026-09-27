When direct translation into First-Order Logic is difficult, negating the English statement can simplify translation before applying De Morgan's laws to recover the original statement[cite: 1].

> [!question] Translation Walkthrough 1: Strict Upper Extremum
> *Statement*: *"There is a number that is larger than every other number."*[cite: 1]
> 
> *Analysis*:
> * The phrase *"every other number"* means every number $y$ distinct from $x$ ($y \neq x$)[cite: 1].
> * It does not say another number exists; it states that **if** another number exists, $x$ is larger[cite: 1].
> * Direct translation:
>   $$\exists x \, \forall y \, [(x \neq y) \to x > y]$$[cite: 1]
> * Alternate derivation via negation:
>   * Negation: *"For every number, there is a distinct number that is greater than or equal to it."*[cite: 1]
>   * Negated logic: $\forall x \, \exists y \, [(x \neq y) \wedge y \ge x]$[cite: 1]
>   * Negating back: $\neg \forall x \, \exists y \, [(x \neq y) \wedge y \ge x] \equiv \exists x \, \forall y \, [\neg (x \neq y) \vee \neg (y \ge x)] \equiv \exists x \, \forall y \, [(x \neq y) \to x > y]$[cite: 1].

> [!question] Translation Walkthrough 2: Infinitude of Primes
> *Statement*: *"There are infinitely many primes."*[cite: 1]
> 
> *Analysis*:
> * Expressed in predicate logic: For every natural number $n$, there exists a prime number $p$ strictly greater than $n$[cite: 1]:
>   $$\forall n \, \exists p \, [p > n \wedge \text{Prime}(p)]$$[cite: 1]
