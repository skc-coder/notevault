---
title: Type Conversions, Integer Promotion & Arithmetic Hierarchy
tags:
  - clang
  - c-language
  - moc
  - study
---


> [!abstract] Overview
> Unified hub note for type conversions, integer promotion rules, conversion rank hierarchy, and usual arithmetic conversions in C.

---

## Logical Sequence & Atomic Notes

1. **[[Integer Promotion Rules in C]]**
   - Automatic promotion of narrow integer types (`_Bool`, `char`, `short`) to `int` or `unsigned int` prior to expression evaluation or variadic function calls.
   - Character literal typing discrepancy (`'a'` as `int` in C vs `char` in C++).

2. **[[Usual Arithmetic Conversions & Hierarchy]]**
   - Two-phase expression evaluation pipeline:
     $$\text{Operands} \longrightarrow \text{Phase 1: Integer Promotion} \longrightarrow \text{Phase 2: Arithmetic Conversion} \longrightarrow \text{Common Type}$$
   - Integer conversion rank ordering rules.
   - Signed vs Unsigned operand unification rules.

3. **[[Bit-Width Extensions & Sign vs Zero Extension]]**
   - Extension invariant: RHS source type signedness dictates extension, never LHS destination.
   - Zero-extension (`unsigned`) vs sign-extension (`signed`).

4. **[[C Integer Conversion & Printf Formatting Case Studies]]**
   - Trace of promotion and format specifier decoding for `signed char` and `unsigned char`.

---

## Related Sequence
- [[Integer Representation & Encoding]]
- [[Bit-Width Conversions & Extensions]]
