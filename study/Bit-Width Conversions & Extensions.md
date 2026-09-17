---
title: Bit-Width Conversions & Extensions
tags:
  - clang
  - c-language
  - moc
  - study
---

# Bit-Width Conversions & Extensions

> [!abstract] Overview
> Hub note for literal typing, bit extension invariants (zero vs sign extension), narrowing truncation, usual arithmetic conversions, and printf formatting behavior.

---

## Logical Sequence & Atomic Notes

1. **[[Integer Literal Typing & Parsing Rules]]**
   - Suffixes (`u`, `l`, `ll`, `ull`) and literal typing defaults.
   - Lexical parsing trap of unary minus on literals.

2. **[[Bit-Width Extensions & Sign vs Zero Extension]]**
   - Extension invariant: source operand (RHS) signedness dictates extension, never destination (LHS).
   - Zero-extension (`unsigned`) vs sign-extension (`signed`).

3. **[[Narrowing & Truncation Mechanics]]**
   - Discarding upper bits during bit slicing.
   - Sign flipping and magnitude alteration on narrowing.

4. **[[Bit Truncation & Sign-Extension Matrix]]**
   - Modulo arithmetic setup ($U = \text{val} \pmod{2^n}$), Master conversion matrix, mathematical derivations, and worked numerical examples.

5. **[[Usual Arithmetic Conversions & Hierarchy]]**
   - Integer conversion rank hierarchy.
   - Phase 1 (Promotion) and Phase 2 (Unification) rules.

6. **[[C Integer Conversion & Printf Formatting Case Studies]]**
   - Detailed trace of `signed char c = 130` and `unsigned char c = 130` passed to `%d` and `%u`.

---

## Related Sequence
- [[Integer Representation & Promotion]]
- [[Type Conversions & Arithmetic Hierarchy]]
