---
title: Bitwise Operations & Standard Idioms
tags:
  - clang
  - c-language
  - bitwise
  - study
---

# Bitwise Operations & Standard Idioms

Bitwise operators perform direct binary bit manipulation on integer operands.

---

## Shift Operations

- **Left Shift (`<<`):** $x \ll n$ is mathematically equivalent to $x \cdot 2^n$.
- **Right Shift (`>>`):** $x \gg n$ divides $x$ by $2^n$ with truncation:
  - If $x$ is `unsigned`: **logical right shift** (zero-filled).
  - If $x$ is `signed` and negative: **implementation-defined** (typically arithmetic right shift replicating sign bit).

---

## Bitwise Negation vs Logical NOT

- `!x` produces an integer Boolean result ($1$ if $x = 0$, otherwise $0$).
- `~x` flips every bit in two's complement: $\sim x = -(x + 1)$.

---

## Standard Bit Manipulation Idioms

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

## Related Notes
- [[Operator Precedence & Associativity Hierarchy]]
- [[Assignment & Comma Operators]]
