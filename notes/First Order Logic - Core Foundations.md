First-Order Logic ($\text{FOL}$), also known as Predicate Calculus, Predicate Logic, or Quantificational Logic, is a formal logic system that extends Propositional Logic ($\text{PL}$) by decomposing propositions into individual objects, domains of discourse, and the properties or relations that hold between them[cite: 1].

> [!definition] Category and Predicate Components
> In First-Order Logic:
> * **Domain / Universe of Discourse ($U$)**: A non-empty set of concrete or abstract entities/objects being reasoned about[cite: 1].
> * **Object / Constant**: An individual entity in the domain (e.g., $2$, John, Alice)[cite: 1].
> * **Variable**: A placeholder symbol (e.g., $x, y, z$) that can take values from the domain[cite: 1].
> * **Property**: A unary predicate asserting an attribute of a single object (e.g., $\text{Even}(x)$, $\text{Odd}(y)$)[cite: 1].
> * **Predicate (Relation)**: An $n$-ary relation over objects, acting as a truth-valued function from $U^n \to \{\text{True}, \text{False}\}$ (e.g., $P(x, y): x > y$)[cite: 1].
> * **Quantification**: A logical construct specifying the extent or quantity of elements in the domain for which a predicate holds (e.g., all, some, or a specific count)[cite: 1].

### Expressive Leap: Propositional Logic vs. First-Order Logic

In Propositional Logic, the atomic proposition is an indivisible black box assigned a single truth value ($\text{True}$ or $\text{False}$)[cite: 1]. $\text{PL}$ cannot inspect the internal constituents of a sentence[cite: 1]. 

$\text{FOL}$ overcomes this limitation by modeling sub-propositional parts: variables represent domain objects, and predicates evaluate their relationships[cite: 1].

| Feature | Propositional Logic ($\text{PL}$) | First-Order Logic ($\text{FOL}$) |
| :--- | :--- | :--- |
| **Elementary Unit** | Indivisible Proposition ($P, Q$)[cite: 1] | Objects, Variables, and Predicates ($P(x), R(x, y)$)[cite: 1] |
| **Variable Domain** | Truth values only ($\{\text{T}, \text{F}\}$)[cite: 1] | Concrete domain elements ($U$)[cite: 1] |
| **Expressive Power** | Finite boolean evaluations[cite: 1] | Generalized statements across infinite/finite domains[cite: 1] |
| **Quantification** | Absent[cite: 1] | Universal ($\forall$) and Existential ($\exists$)[cite: 1] |

### Converting an Open Predicate into a Proposition

A predicate containing unbound variables has no fixed truth value and is therefore not a proposition[cite: 1]. There are two distinct methods to convert an open predicate into a valid proposition[cite: 1]:
1. **Direct Substitution**: Replace every free variable with a specific constant from the domain (e.g., $\text{Even}(x) \xrightarrow{x=2} \text{Even}(2) \equiv \text{True}$)[cite: 1].
2. **Quantification**: Bind every free variable using a quantifier (e.g., $\forall x \, \text{Even}(x)$ or $\exists x \, \text{Even}(x)$)[cite: 1].

> [!trap] Non-Empty Domain Axiom
> In standard First-Order Logic, the domain of discourse $U$ is **strictly non-empty by default** ($U \neq \emptyset$)[cite: 1]. 
> * If an empty domain were permitted, the universal statement $\forall x \, P(x)$ would be vacuously True, while the existential statement $\exists x \, P(x)$ would be False, causing the standard deduction rule $\forall x \, P(x) \implies \exists x \, P(x)$ to fail[cite: 1].
