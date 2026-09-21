> [!definition]
> - **$LR(0)$ Item**: A production with a marker dot ($\cdot$) indicating how much of the RHS has been scanned:
>   $$A \to \alpha \cdot \beta$$
>   - *Shift item*: Dot precedes a terminal ($A \to \alpha \cdot a \beta$).
>   - *Non-terminal transition*: Dot precedes a non-terminal ($A \to \alpha \cdot B \beta$).
>   - *Reduce item*: Dot is at the extreme right ($A \to \alpha \beta \cdot$).
> - **$LR(1)$ Item**: An $LR(0)$ item paired with a 1-terminal lookahead: $[A \to \alpha \cdot \beta, \; a]$.

> [!formula]
> **Closure Operations**:
> - **$LR(0)$ Closure**: If $A \to \alpha \cdot B \beta \in I$, then add $B \to \cdot \gamma$ to $I$ for all $B \to \gamma \in G$.
> - **$LR(1)$ Closure**: If $[A \to \alpha \cdot B \beta, \; a] \in I$, then add $[B \to \cdot \gamma, \; b]$ to $I$ for all $B \to \gamma \in G$ and for all $b \in \text{FIRST}(\beta a)$.

> [!theorem]
> **Table Entry Rules for Reductions across LR Families**:
> 1. **$LR(0)$**: If $A \to \alpha \cdot$ is in state $I_k$ (production #$i$), place $R_i$ in **ALL action columns** for row $k$.
> 2. **$SLR(1)$**: If $A \to \alpha \cdot$ is in state $I_k$, place $R_i$ **ONLY in columns corresponding to $a \in \text{FOLLOW}(A)$**.
> 3. **$CLR(1) / LALR(1)$**: If $[A \to \alpha \cdot, \; a]$ is in state $I_k$, place $R_i$ **ONLY in column $a$**.
> 4. **Accept Entry**: If augmented production $[S' \to S \cdot, \; \$]$ is in state $I_k$, place $\text{accept}$ in cell $M[k, \$]$.

> [!trap]
> - A state containing $[A \to \alpha \cdot a \beta]$ and $[B \to \gamma \cdot]$ causes an **SR conflict** in $LR(0)$.
> - In $SLR(1)$, this is an SR conflict if and only if $a \in \text{FOLLOW}(B)$.
> - In $CLR(1)$, this is an SR conflict if and only if $a$ matches the exact lookahead of the reduction item.

> [!question]
> For the grammar augmented with $S' \to \cdot S$ and $S \to a A b$, what does the closure of $I_0 = \{[S' \to \cdot S]\}$ contain in an $LR(0)$ automaton?
> - (A) $\{S' \to \cdot S, \; S \to a \cdot A b\}$
> - (B) $\{S' \to \cdot S, \; S \to \cdot a A b\}$
> - (C) $\{S' \to \cdot S, \; S \to \cdot a A b, \; A \to \cdot \text{id}\}$
> - (D) $\{S' \to S \cdot\}$
>
> **Correct Option**: **(B)**
> **Explanation**: The dot precedes variable $S$ in $S' \to \cdot S$. Closure brings in all productions of $S$ with the dot at the beginning: $S \to \cdot a A b$. Since the symbol after the dot is terminal $a$, closure terminates.
