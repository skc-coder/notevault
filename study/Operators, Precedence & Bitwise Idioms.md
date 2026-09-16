## 1. Loop Control Flow: `break` and `continue`

> [!property] Target Scope of Jump Statements
> Both `break` and `continue` statements apply strictly to the innermost enclosing loop construct (`for`, `while`, `do-while`) in which they appear. They do not terminate or skip iterations of outer parent loops.
>
> *(Note: `break` also exits an enclosing `switch` block, but `continue` does not; a `continue` inside a `switch` located within a loop continues the enclosing loop).*

---

## 2. Operator Precedence and Associativity Hierarchy

In C, operator precedence and associativity resolve syntactic grouping of expressions, **not** runtime order of evaluation.

| Priority / Rank | Category | Operators | Associativity |
| :---: | :--- | :--- | :---: |
| **1** | Primary / Postfix | `()`, `[]`, `.`, `->`, `postfix ++`, `postfix --` | $\text{Left-to-Right } (\to)$ |
| **2** | Unary / Prefix | `!`, `~`, `prefix ++`, `prefix --`, unary `+`, unary `-`, `*` (deref), `&` (addr), `sizeof` | $\text{Right-to-Left } (\leftarrow)$ |
| **3** | Multiplicative Arithmetic | `*`, `/`, `%` | $\text{Left-to-Right } (\to)$ |
| **4** | Additive Arithmetic | `+`, `-` | $\text{Left-to-Right } (\to)$ |
| **5** | Bitwise Shift | `<<`, `>>` | $\text{Left-to-Right } (\to)$ |
| **6** | Relational | `<`, `<=`, `>`, `>=` | $\text{Left-to-Right } (\to)$ |
| **7** | Equality | `==`, `!=` | $\text{Left-to-Right } (\to)$ |
| **8** | Bitwise AND | `&` | $\text{Left-to-Right } (\to)$ |
| **9** | Bitwise XOR | `^` | $\text{Left-to-Right } (\to)$ |
| **10** | Bitwise OR | `\|` | $\text{Left-to-Right } (\to)$ |
| **11** | Logical AND | `&&` | $\text{Left-to-Right } (\to)$ |
| **12** | Logical OR | `\|\|` | $\text{Left-to-Right } (\to)$ |
| **13** | Conditional (Ternary) | `? :` | $\text{Right-to-Left } (\leftarrow)$ |
| **14** | Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `\|=` | $\text{Right-to-Left } (\leftarrow)$ |
| **15** | Comma | `,` | $\text{Left-to-Right } (\to)$ |

> [!property] Right-to-Left Associativity of Unary Not
> Both logical NOT (`!`) and bitwise NOT (`~`) occupy Unary Priority (Rank 2) with right-to-left associativity:
> $$!\,!\,a \equiv !(!a)$$

### Relational Chaining Pitfall
Mathematical continuous chaining does not hold in C due to left-to-right evaluation:

```c
int a = 10, b = 20, c = 30;

// Evaluation: a < b < c -> (10 < 20) -> 1 < 30 -> 1 (true)
int res1 = (a < b < c); // Evaluates to 1 (true)

// Evaluation: c > b > a -> (30 > 20) -> 1 > 10 -> 0 (false)
int res2 = (c > b > a); // Evaluates to 0 (false)
```

---

## 3. Bitwise Operators and Standard Idioms

### Shift Operations
* **Left Shift (`<<`):** $x \ll n$ is mathematically equivalent to $x \cdot 2^n$.
* **Right Shift (`>>`):** $x \gg n$ divides $x$ by $2^n$ with truncation towards zero or $-\infty$:
  * If $x$ is `unsigned`: **logical right shift** (zero filled).
  * If $x$ is `signed` and negative: **implementation-defined** (typically arithmetic right shift).

### Bitwise Negation vs. Logical NOT
* `!x` produces integer Boolean result ($1$ if $x = 0$, otherwise $0$).
* `~x` flips every bit in two's complement: $\sim x = -(x + 1)$.

### Standard Bit Manipulation Idioms
```c
// Setting the n-th bit
x |= (1U << n);

// Clearing the n-th bit
x &= ~(1U << n);

// Toggling the n-th bit
x ^= (1U << n);

// Testing parity (Even / Odd)
if (x & 1) { /* Odd number */ } else { /* Even number */ }

// XOR In-Place Swap Idiom (valid when &a != &b)
a ^= b; b ^= a; a ^= b;
```

---

## 4. Assignment and Comma Operators

* **Compound Assignment:** $V \text{ op}= E \implies V = V \text{ op } (E)$.
* **Comma Operator (`,`):** Evaluates operands left to right, yielding the value and type of the rightmost operand.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->
