> [!definition]
> - **Immediate Left Recursion**: A production of the form $A \to A\alpha \mid \beta$, where $\beta$ does not begin with $A$.
> - **Left Factoring**: Transformation of productions $A \to \alpha\beta_1 \mid \alpha\beta_2$ with common prefix $\alpha$ to defer decisions until lookahead reveals subsequent tokens.

> [!formula]
> **Elimination of Immediate Left Recursion**:
> Replace:
> $$A \to A\alpha_1 \mid A\alpha_2 \mid \dots \mid A\alpha_m \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n$$
> with:
> $$A \to \beta_1 A' \mid \beta_2 A' \mid \dots \mid \beta_n A'$$
> $$A' \to \alpha_1 A' \mid \alpha_2 A' \mid \dots \mid \alpha_m A' \mid \epsilon$$

> [!formula]
> **Left Factoring Transformation**:
> Replace:
> $$A \to \alpha\beta_1 \mid \alpha\beta_2 \mid \dots \mid \alpha\beta_k \mid \gamma$$
> with:
> $$A \to \alpha A' \mid \gamma$$
> $$A' \to \beta_1 \mid \beta_2 \mid \dots \mid \beta_k$$

> [!trap]
> Eliminating left recursion converts a left-recursive grammar into a right-recursive grammar. While this permits $LL(1)$ parsing, right-recursive structures distort the natural left-associativity of arithmetic operators (like subtraction and division) into right-associativity unless corrected in semantic evaluation.

> [!question]
> Eliminate immediate left recursion from the arithmetic expression grammar:
> $$E \to E + T \mid T, \quad T \to T * F \mid F, \quad F \to (E) \mid \text{id}$$
> What are the resulting productions for $E$ and $E'$?
> - (A) $E \to E + T \mid \epsilon, \quad E' \to T E'$
> - (B) $E \to T E', \quad E' \to + T E' \mid \epsilon$
> - (C) $E \to + T E', \quad E' \to T \mid \epsilon$
> - (D) $E \to T, \quad E' \to + E \mid \epsilon$
>
> **Correct Option**: **(B)**
> **Explanation**: Applying $A \to \beta A'$ and $A' \to \alpha A' \mid \epsilon$ with $A = E$, $\alpha = + T$, and $\beta = T$ yields $E \to T E'$ and $E' \to + T E' \mid \epsilon$.
