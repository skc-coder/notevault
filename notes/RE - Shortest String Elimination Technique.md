> [!definition]
> **Regular Expressions (RE)** represent regular sets declaratively using basic constants and four primary operations: Union ($+$), Concatenation ($\cdot$), Kleene Star ($*$), and Positive Closure ($+$)[cite: 1].
> - **Identity Laws:** $\phi + R = R$; $R \cdot \epsilon = \epsilon \cdot R = R$; $\phi^* = \epsilon$; $\epsilon^* = \epsilon$[cite: 1].
> - **Annihilators:** $R \cdot \phi = \phi \cdot R = \phi$[cite: 1].

> [!theorem]
> ### The Candidate Elimination Strategy for PSU CBT Exams
> In high-speed recruitment exams, deriving an RE algebraically or drawing full state diagrams consumes too much time[cite: 1]. Solve RE multiple-choice questions by **generating small characteristic strings and pruning non-conforming choices**[cite: 1]:
> 1. **Step 1 (Length-0 Test):** Check if the empty string $\epsilon$ is in the target language[cite: 1]. Eliminate all options whose minimum generated string has length $\ge 1$[cite: 1].
> 2. **Step 2 (Length-1 Test):** Check valid / invalid single symbols (e.g., $0$ or $1$)[cite: 1].
> 3. **Step 3 (Over-generation Test):** Check if an option generates an invalid string (e.g., producing an odd number of $1$'s when even is required)[cite: 1].

> [!question]
> **Worked Practice Drill (Even Number of 1's):**
> Which regular expression represents all strings over $\Sigma = \{0, 1\}$ having an **even number of 1's**?[cite: 1]
> - (A) $(0^* 1 0^* 1)^*$
> - (B) $0^* (1 0^* 1 0^*)^*$
> - (C) $0^* (1 0^* 1^* 0^*)$
> - (D) $1 1 (0 + 1)^* 1 1$
>
> **Option-by-Option Elimination Execution:**
> 1. **Target Language Properties:**
>    - Valid strings: $\epsilon$ (zero 1's, even), $0$ (zero 1's, even), $00$, $11$, $01010$, $1001$, etc[cite: 1].
>    - Invalid strings: $1$ (one 1, odd), $111$, $010$[cite: 1].
> 2. **Filter via $\epsilon$ (Minimum Length):**
>    - (D) Minimum string is $1111$ (length 4) $\implies$ Cannot generate $\epsilon$ or $0 \implies$ **Eliminate (D)**[cite: 1].
> 3. **Filter via Single Zero '$0$':**
>    - (A) Setting outer star to $1$ requires at least two $1$'s ($0^* 1 0^* 1$)[cite: 1]. Setting outer star to $0$ yields $\epsilon$[cite: 1]. Single '$0$' can never be generated $\implies$ **Eliminate (A)**[cite: 1].
> 4. **Filter via Over-generation (Illegal Single '$1$'):**
>    - (C) Expression contains $1^*$ inside: $0^* (1 0^* 1^* 0^*)$[cite: 1]. Setting initial $0^* \to \epsilon$, middle $0^* \to \epsilon$, inner $1^* \to \epsilon$, trailing $0^* \to \epsilon$ leaves a single isolated symbol **'1'**[cite: 1]. An odd count of $1$'s is accepted $\implies$ **Eliminate (C)**[cite: 1].
> 5. **Confirmation:**
>    - (B) $0^*(10^* 10^*)^*$ generates $\epsilon$ (all stars 0), generates $0$ ($0^*$), generates $11$ ($0^*(10^*10^*)$), and strictly couples every $1$ in matched pairs separated by arbitrary zero runs $\implies$ **(B) is Correct**[cite: 1].
