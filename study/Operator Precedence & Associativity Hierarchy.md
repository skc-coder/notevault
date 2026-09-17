---
title: Operator Precedence & Associativity Hierarchy
tags:
  - clang
  - c-language
  - operators
  - study
---


In C, operator precedence and associativity resolve syntactic grouping of expressions, **not** runtime order of evaluation.

---

## Precedence and Associativity Table

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
> Unary NOT (`!`) and bitwise NOT (`~`) occupy Unary Priority (Rank 2) with right-to-left associativity:
> $$!\,!\,a \equiv !(!a)$$

---

## The 4 Mental Shortcuts for Instant Parsing

1. **"Calculate $\to$ Compare $\to$ Connect $\to$ Assign"**
   - **Calculate:** Math (`*`, `+`, `<<`)
   - **Compare:** Checks (`<`, `==`)
   - **Connect:** Logic (`&`, `|`, `&&`, `||`)
   - **Assign:** Side-effects (`=`)
2. **Bitwise beats Logical; AND beats OR:**
   $$\& \quad > \quad \mid \quad > \quad \&\& \quad > \quad \parallel$$
3. **Shift vs. Comparison Trap:** Shifts bind tighter than relational checks (`a << 2 < b` $\equiv$ `(a << 2) < b`).
4. **Historical Bug Trap:** Equality operators (`==`, `!=`) rank **higher** than bitwise AND/OR (`&`, `^`, `|`).
   - `if (x & 1 == 0)` parses as `x & (1 == 0)`.

---

## Right-to-Left Associativity Exception

Only three operator classes walk backwards (right-to-left):
- **Prefix Unary Operators**
- **Assignment Operators:** `a = b = c` $\to$ `a = (b = c)`
- **Ternary Operator:** `a ? b : c ? d : e` $\to$ `a ? b : (c ? d : e)`

---

## Related Notes
- [[Relational Chaining Pitfall]]
- [[Bitwise Operations & Standard Idioms]]
- [[Assignment & Comma Operators]]
