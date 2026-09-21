> [!definition]
> - $\text{FIRST}(\alpha)$: The set of terminals that begin strings derived from $\alpha$. If $\alpha \Rightarrow^* \epsilon$, then $\epsilon \in \text{FIRST}(\alpha)$.
> - $\text{FOLLOW}(A)$: The set of terminals that can appear immediately to the right of non-terminal $A$ in some sentential form:
>   $$\text{FOLLOW}(A) = \{a \in V_T \mid S \Rightarrow^* \alpha A a \beta\} \cup \{\$ \text{ if } S \Rightarrow^* \alpha A\}$$

> [!formula]
> **Algorithmic Rules for $\text{FIRST}(X)$**:
> 1. If $X \in V_T$, $\text{FIRST}(X) = \{X\}$.
> 2. If $X \to \epsilon$, add $\epsilon \in \text{FIRST}(X)$.
> 3. If $X \in V_N$ and $X \to Y_1 Y_2 \dots Y_k$:
>    - Add $(\text{FIRST}(Y_1) \setminus \{\epsilon\}) \subseteq \text{FIRST}(X)$.
>    - If $\epsilon \in \text{FIRST}(Y_1)$, add $(\text{FIRST}(Y_2) \setminus \{\epsilon\}) \subseteq \text{FIRST}(X)$, cascading up to $Y_k$.
>    - If $\epsilon \in \text{FIRST}(Y_i)$ for all $1 \le i \le k$, add $\epsilon \in \text{FIRST}(X)$.
>
> **Algorithmic Rules for $\text{FOLLOW}(A)$**:
> 1. Place $\$$ into $\text{FOLLOW}(S)$, where $S$ is the start symbol.
> 2. If $A \to \alpha B \beta$, then $(\text{FIRST}(\beta) \setminus \{\epsilon\}) \subseteq \text{FOLLOW}(B)$.
> 3. If $A \to \alpha B$ or $A \to \alpha B \beta$ where $\epsilon \in \text{FIRST}(\beta)$, then $\text{FOLLOW}(A) \subseteq \text{FOLLOW}(B)$.
> 4. Right-recursive rules $A \to \alpha A$ contribute nothing to $\text{FOLLOW}(A)$.

> [!trap]
> - $\text{FIRST}$ sets can contain $\epsilon$, but **$\text{FOLLOW}$ sets can NEVER contain $\epsilon$**.
> - In derivations $S \to ABC$, if $\text{FIRST}(A)$ and $\text{FIRST}(B)$ contain $\epsilon$, but $\text{FIRST}(C)$ does **not** contain $\epsilon$, then $\epsilon \notin \text{FIRST}(S)$.

> [!question]
> Given grammar $G$:
> $$S \to ABC, \quad A \to a \mid \epsilon, \quad B \to b \mid \epsilon, \quad C \to c$$
> Find $\text{FIRST}(S)$ and $\text{FOLLOW}(A)$.
> - (A) $\text{FIRST}(S) = \{a, b, c, \epsilon\}; \text{ FOLLOW}(A) = \{b, c\}$
> - (B) $\text{FIRST}(S) = \{a, b, c\}; \text{ FOLLOW}(A) = \{b, c\}$
> - (C) $\text{FIRST}(S) = \{a, b, c\}; \text{ FOLLOW}(A) = \{b, \$\}$
> - (D) $\text{FIRST}(S) = \{a, b\}; \text{ FOLLOW}(A) = \{c\}$
>
> **Correct Option**: **(B)**
> **Step-by-Step Calculation**:
> 1. $\text{FIRST}(A) = \{a, \epsilon\}$, $\text{FIRST}(B) = \{b, \epsilon\}$, $\text{FIRST}(C) = \{c\}$.
> 2. $\text{FIRST}(S) = (\text{FIRST}(A) \setminus \{\epsilon\}) \cup (\text{FIRST}(B) \setminus \{\epsilon\}) \cup \text{FIRST}(C) = \{a, b, c\}$. Since $C$ cannot produce $\epsilon$, $\epsilon \notin \text{FIRST}(S)$.
> 3. For $\text{FOLLOW}(A)$ from $S \to ABC$: $\text{FOLLOW}(A) = \text{FIRST}(BC) = (\text{FIRST}(B) \setminus \{\epsilon\}) \cup \text{FIRST}(C) = \{b, c\}$.
