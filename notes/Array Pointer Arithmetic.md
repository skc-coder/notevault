---
tags:
  - clang
  - c-language
  - arrays
  - pointers
  - study
---
The array subscript operator `[]` in C is defined strictly by pointer arithmetic.

> [!property] Commutative Equivalence of Array Subscripting
> $$\text{arr}[i] \equiv *( \text{arr} + i ) \equiv *( i + \text{arr} ) \equiv i[\text{arr}]$$

---

## The One-Past-The-End Rule & Pointer Distance

> [!definition] One-Past-The-End Rule
> Pointer arithmetic and comparisons are valid across index $0$ to $N-1$, plus the **one-past-the-end** index $N$. Dereferencing index $N$ or calculating addresses beyond $N$ is **Undefined Behavior (UB)**.

$$\text{end} - \text{start} = N \quad (\text{for pointers to index } N \text{ and } 0)$$

