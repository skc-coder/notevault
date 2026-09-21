> [!definition]
> - **Lexeme**: The concrete syntactic sequence of characters in the source code matching a pattern.
> - **Token**: The abstract internal unit `(token-name, attribute-value)` passed to the syntax analyzer.
> - **Pattern**: The formal rule (regular expression) describing what form a lexeme may take.

> [!theorem]
> **Maximal Munch Rule (Longest Match / Longest Prefix Matching)**:
> If multiple lexical rules match the current character stream, the lexical analyzer selects the rule that matches the **longest possible sequence of input characters** before breaking into a token. If two patterns match identical lengths, rule priority in the lex specification resolves the tie (e.g., keywords prioritized over identifiers).

> [!formula]
> Given an input stream $S$, the scanner advances lookahead pointer $P_R$ from start pointer $P_L$:
> $$\text{Token Lexeme} = S[P_L \dots P_R - 1] \quad \text{such that } P_R = \max \{k \mid S[P_L \dots k-1] \in \mathcal{L}(R_i)\}$$

> [!trap]
> In token counting drills, string constants (`"text"`) constitute a **single token**. Preprocessor directives, block comments `/* ... */`, and unescaped whitespace produce **0 tokens**. Unclosed string literals or malformed identifiers (e.g., `int 1x23;`) trigger **Lexical Errors**, terminating token generation.

> [!question]
> Determine the exact number of tokens generated for the following C statement:
> ```c
> int x, *p; x = 10; p = &x; x++;
> ```
> - (A) 14
> - (B) 16
> - (C) 18
> - (D) 20
>
> **Correct Option**: **(C)**
> **Step-by-Step Breakdown**:
> 1. `int` (keyword)
> 2. `x` (identifier)
> 3. `,` (punctuation)
> 4. `*` (operator)
> 5. `p` (identifier)
> 6. `;` (punctuation)
> 7. `x` (identifier)
> 8. `=` (operator)
> 9. `10` (constant)
> 10. `;` (punctuation)
> 11. `p` (identifier)
> 12. `=` (operator)
> 13. `&` (operator)
> 14. `x` (identifier)
> 15. `;` (punctuation)
> 16. `x` (identifier)
> 17. `++` (operator via maximal munch)
> 18. `;` (punctuation)
> Total = **18 tokens**.
