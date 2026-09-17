---
title: Overflow Definition & Detection Rules
tags:
  - clang
  - c-language
  - overflow
  - study
---

# Overflow Definition & Detection Rules

Integer overflow occurs when an arithmetic calculation produces a numeric result that falls outside the representable range of the target type.

---

## Overflow Detection Rules by Number System

### Sign-Magnitude System
Overflow occurs if there is a carry out from the magnitude's Most Significant Bit (MSB), **ignoring the sign bit**. (This is only possible when adding numbers of identical sign).

### 1's and 2's Complement Systems
- Overflow occurs **only when adding two numbers of the same sign**.
- **Sign Invariant Detection Rule:**
  - If both inputs have $\text{MSB} = 1$ and result has $\text{MSB} = 0$ $\longrightarrow$ **Overflow**.
  - If both inputs have $\text{MSB} = 0$ and result has $\text{MSB} = 1$ $\longrightarrow$ **Overflow**.
  - Adding numbers with different sign MSBs $\longrightarrow$ **Overflow is mathematically impossible**.

---

## Related Notes
- [[Two's Complement Fundamentals & Weight Method]]
- [[Integer Value Ranges & Signed vs Unsigned Systems]]
- [[Narrowing & Truncation Mechanics]]
