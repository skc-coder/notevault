---
title: Type Conversions & Arithmetic Hierarchy
tags:
  - clang
  - c-language
  - moc
  - study
---

# Type Conversions & Arithmetic Hierarchy

> [!abstract] Overview
> Hub note for standard arithmetic hierarchy and implicit type conversions in C.

---

## Logical Sequence & Atomic Notes

1. **[[Usual Arithmetic Conversions & Hierarchy]]**
   - Two-phase evaluation pipeline (Promotion $\to$ Arithmetic Conversion).
   - Rules for same signedness vs mixed signedness.

2. **[[Integer Promotion Rules in C]]**
   - Rank lower than `int` promoted to `int` or `unsigned int`.

3. **[[Bit-Width Extensions & Sign vs Zero Extension]]**
   - Sign extension vs Zero extension behavior during promotion.

4. **[[C Integer Conversion & Printf Formatting Case Studies]]**
   - Variadic argument promotion interactions with format specifiers.

---

## Related Sequence
- [[Integer Representation & Promotion]]
- [[Bit-Width Conversions & Extensions]]
