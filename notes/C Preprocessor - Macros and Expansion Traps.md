> [!definition] Preprocessor Directives
> Lines starting with `#` are processed by the C preprocessor before compilation[cite: 1].
> Directives like `#define` perform purely textual substitution—they **do not perform mathematical computation** or adhere to C operator precedence at definition time[cite: 1].

### Preprocessor Pitfalls and Textual Substitution Traps

> [!trap] Macro Text Expansion Trap 1
> ```c
> #define plusone(x) x + 1
> 
> int result = 3 * plusone(2);
> ```
> * **Intuition:** Expects $3 \times (2 + 1) = 9$.
> * **Actual Replacement:** `3 * 2 + 1`[cite: 1].
> * **Calculation:** $(3 \times 2) + 1 = 6 + 1 = \mathbf{7}$[cite: 1].
> * **Resolution:** Always wrap macro expressions in parentheses:
>   ```c
>   #define plusone(x) ((x) + 1)
>   ```

> [!trap] Macro Text Expansion Trap 2
> ```c
> #define mul(a, b) a * b
> 
> int result = mul(2 + 3, 3 + 5);
> ```
> * **Intuition:** Expects $(2 + 3) \times (3 + 5) = 5 \times 8 = 40$.
> * **Actual Replacement:** `2 + 3 * 3 + 5`[cite: 1].
> * **Calculation:** $2 + (3 \times 3) + 5 = 2 + 9 + 5 = \mathbf{16}$[cite: 1].
> * **Resolution:** Always wrap individual arguments and the whole expression in parentheses:
>   ```c
>   #define mul(a, b) ((a) * (b))
>   /* Expands to: ((2 + 3) * (3 + 5)) = (5 * 8) = 40 */
>   ```

> [!theorem] GATE CSE Scope Note
> **Call by Reference** (in native C, achieved only via pointers / call by address) and **Dynamic Scoping** (where identifier bindings depend on the runtime call stack rather than static lexical blocks) are **not part of the standard GATE syllabus**[cite: 1]. C strictly utilizes **Lexical / Static Scoping** and **Call by Value**[cite: 1].
