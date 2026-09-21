> [!definition]
> An **$LL(1)$ Parser** is a top-down, non-recursive predictive parser that scans input from **L**eft to right, constructs a **L**eftmost derivation, using **1** token of lookahead.

> [!theorem]
> **Necessary and Sufficient Conditions for a Grammar to be $LL(1)$**:
> A CFG $G$ is $LL(1)$ if and only if for every non-terminal production $A \to \alpha \mid \beta$:
> 1. $\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$
> 2. At most one of $\alpha$ or $\beta$ can derive $\epsilon$.
> 3. If $\beta \Rightarrow^* \epsilon$, then $\text{FIRST}(\alpha) \cap \text{FOLLOW}(A) = \emptyset$.

> [!formula]
> **Predictive Parsing Table Entry Construction**:
> For every production $A \to \alpha$:
> 1. For every terminal $a \in \text{FIRST}(\alpha)$, add $A \to \alpha$ to $M[A, a]$.
> 2. If $\epsilon \in \text{FIRST}(\alpha)$, add $A \to \alpha$ to $M[A, b]$ for every terminal $b \in \text{FOLLOW}(A)$ (including $\$$).
>
> $$\text{Conflict Metric}: \exists (A, a) \text{ such that } |M[A, a]| > 1 \iff G \notin LL(1)$$

> [!trap]
> **Instant Elimination Shortcuts for $LL(1)$**:
> If a grammar has any of the following, it is **guaranteed NOT to be $LL(1)$**:
> - **Left Recursion** (Immediate: $A \to A\alpha$, or Indirect: $A \Rightarrow^+ A\alpha$)
> - **Left Factoring needed** (Common prefixes: $A \to \alpha\beta_1 \mid \alpha\beta_2$)
> - **Ambiguity** (e.g., dangling-else problem)


