> [!definition]
> - **Left Recursion:** A production is directly left recursive if it has the form $A \to A\alpha$[cite: 1]. It causes top-down parsers (e.g., LL(1)) to enter an infinite loop[cite: 1].
> - **Indirect Left Recursion:** Cycles through multiple production steps (e.g., $S \to Aa \dots$ and $A \to Sd$)[cite: 1].

> [!formula]
> ### Direct Left Recursion Elimination Formula
> Given productions with left recursion and non-left-recursive base cases:
> $$A \to A\alpha_1 \mid A\alpha_2 \mid \dots \mid A\alpha_m \mid \beta_1 \mid \beta_2 \mid \dots \mid \beta_n$$
> where no $\beta_i$ begins with variable $A$.
>
> Replace these productions with right-recursive rules using a new non-terminal $A'$:
> $$A \to \beta_1 A' \mid \beta_2 A' \mid \dots \mid \beta_n A'$$
> $$A' \to \alpha_1 A' \mid \alpha_2 A' \mid \dots \mid \alpha_m A' \mid \epsilon$$
>
> *(Every generated string retains the identical prefix $\beta_i$ followed by arbitrary repetitions of trailing segments $\alpha_j$.)*

> [!trap]
> **The Two-Step Indirect Recursion Elimination Rule:**
> If a grammar has indirect left recursion, you cannot apply the formula directly[cite: 1]. You must first substitute the calling variable's productions into the body to expose direct recursion[cite: 1].
>
> **Example Process:**
> Given grammar:
> $$S \to Aa \mid b$$
> $$A \to Ac \mid Sd \mid \epsilon$$
>
> 1. **Step 1: Eliminate Indirect Reference in $A$:**
>    Substitute $S \to Aa \mid b$ into $A \to Sd$:
>    $$A \to Ac \mid (Aa \mid b)d \mid \epsilon \implies A \to Ac \mid Aad \mid bd \mid \epsilon$$[cite: 1]
> 2. **Step 2: Partition into $\alpha$ and $\beta$ sets:**
>    - Recursive terms: $A \to A(c)$ and $A \to A(ad) \implies \alpha_1 = c, \alpha_2 = ad$[cite: 1].
>    - Base terms: $A \to bd$ and $A \to \epsilon \implies \beta_1 = bd, \beta_2 = \epsilon$[cite: 1].
> 3. **Step 3: Generate the Final Non-Recursive Rules:**
>    $$S \to Aa \mid b$$
>    $$A \to bd A' \mid \epsilon A' \implies A \to bd A' \mid A'$$[cite: 1]
>    $$A' \to c A' \mid ad A' \mid \epsilon$$[cite: 1]

> [!question]
> **IOCL CBT Practice Question:**
> What is the transformed, non-left-recursive equivalent of the production $E \to E + T \mid T$?
> (A) $E \to T E', \; E' \to + T E' \mid \epsilon$
> (B) $E \to + T E' \mid \epsilon, \; E' \to T E'$
> (C) $E \to T E', \; E' \to E + T \mid \epsilon$
> (D) $E \to + T E', \; E' \to \epsilon$
>
> **Answer:** (A)
> **Step-by-Step Explanation:**
> 1. Match against standard pattern: $E \to E\alpha \mid \beta$, where $\alpha = + T$ and $\beta = T$.
> 2. Apply formula:
>    $$E \to \beta E' \implies E \to T E'$$
>    $$E' \to \alpha E' \mid \epsilon \implies E' \to + T E' \mid \epsilon$$
> 3. Matches option (A) identically.
