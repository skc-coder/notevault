---
title: Relational Chaining Pitfall
tags:
  - clang
  - c-language
  - operators
  - study
---


Continuous mathematical inequality chaining does **not** hold in C due to strict left-to-right relational evaluation.

---

## Code Example & Parsing

```c
int a = 10, b = 20, c = 30;

// Evaluation: a < b < c -> (10 < 20) -> 1 < 30 -> 1 (true)
int res1 = (a < b < c); // Evaluates to 1 (true)

// Evaluation: c > b > a -> (30 > 20) -> 1 > 10 -> 0 (false)
int res2 = (c > b > a); // Evaluates to 0 (false)
```

---

## Correct C Formulation

To check if $b$ lies between $a$ and $c$, use logical AND (`&&`):

```c
if (a < b && b < c) {
    /* Valid range check */
}
```

---

## Related Notes
- [[Operator Precedence & Associativity Hierarchy]]
- [[Sequence Points & Short-Circuit Evaluation]]
