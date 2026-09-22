> [!definition]
> In the C programming standard, expressions containing multiple unsequenced modifications to the same scalar object produce **Undefined Behavior (UB)**[cite: 12]. A side effect may occur in any order between sequence points, making expressions like `printf("%d %d %d", a, a++, ++a)` completely non-standard and compiler-dependent[cite: 12].

> [!theorem]
> **Operator Precedence and Evaluation Rules:**
> 1. **Postfix vs. Prefix:** Post-increment (`x++`) returns the original value before incrementing; pre-increment (`++x`) increments the value first and yields the updated result[cite: 11, 12].
> 2. **Short-Circuit Evaluation:**
>    * Logical OR (`||`): If the first operand evaluates to non-zero (true), the second operand is never evaluated.
>    * Logical AND (`&&`): If the first operand evaluates to zero (false), the second operand is skipped entirely.
> 3. **The `sizeof` Operator:** Evaluated strictly at compile-time[cite: 11, 12]. Expressions inside `sizeof(...)` are not executed at runtime, so side effects (such as `sizeof(a++)`) are discarded[cite: 12].
> 4. **Bitwise NOT (`~`):** Operates on two's complement integers: $\sim x = -(x + 1)$.

> [!formula]
> **Ternary Operator Associativity & Nested Logic:**
> The ternary conditional operator `?:` associates **Right-to-Left**:
> $$L_1 \ ? \ M_1 \ : \ L_2 \ ? \ M_2 \ : \ R_2 \equiv L_1 \ ? \ M_1 \ : \ (L_2 \ ? \ M_2 \ : \ R_2)$$

> [!trap]
> **PSU CBT Trap - Side Effects in `sizeof`:**
> Consider `int a = 5; printf("%d %d", sizeof(a++), a);`[cite: 12]. 
> Because `sizeof` computes its type size at compile-time (typically 4 bytes for an integer), `a++` is never executed[cite: 11, 12]. The printed output is strictly `4 5`, not `4 6`[cite: 12].

> [!question]
> **IOCL CBT Practice Drill:**
> What is the output of the following C code snippet[cite: 12]?
> ```c
> #include <stdio.h>
> int main() {
>     int a = 5, b = 10;
>     printf("%d ", a+++b);
>     printf("%d %d", a, b);
>     return 0;
> }
> ```
> (A) 15 6 11[cite: 12]  
> (B) 16 6 10[cite: 12]  
> (C) 15 6 10[cite: 12]  
> (D) Undefined behavior[cite: 12]  
>
> **Step-by-Step Resolution:**
> 1. According to the maximal munch (greedy lexer) rule in C, `a+++b` is parsed as `(a++) + b`[cite: 12].
> 2. `a++` returns current value $5$, and schedules `a` to become $6$[cite: 11, 12].
> 3. Addition: $5 + 10 = 15$ is printed first[cite: 12].
> 4. After the full expression, `a` is $6$ while `b` remains unmodified at $10$[cite: 12].
> 5. Second `printf` yields `6 10`[cite: 12].
>
> **Correct Answer:** (C) 15 6 10[cite: 12]
