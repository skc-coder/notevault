---
title: Integer Representation & Promotion
tags:
  - clang
  - c-language
  - moc
  - study
---

# Integer Representation & Promotion

> [!abstract] Overview
> This hub note logically chains the core concepts of binary integer encodings, two's complement arithmetic, value ranges, and automatic integer promotion rules in C.

---

## Logical Sequence & Atomic Notes

1. **[[Two's Complement Fundamentals & Weight Method]]**
   - Direct positional evaluation via negative MSB weight ($V = -b_{n-1}\cdot 2^{n-1} + \dots$).
   - Alternative negation algorithm ($\sim A + 1$).

2. **[[Integer Value Ranges & Signed vs Unsigned Systems]]**
   - Unsigned vs Signed ($1$'s complement, sign-magnitude, $2$'s complement) ranges.
   - Why two's complement is standard (unique zero, full $2^n$ utilization).

3. **[[Integer Promotion Rules in C]]**
   - Automatic promotion of narrow types (`char`, `short`) to `int` prior to expression evaluation.
   - Character literal typing discrepancy (`'a'` as `int` in C vs `char` in C++).

4. **[[Overflow Definition & Detection Rules]]**
   - Same-sign addition overflow rule ($0+0 \to 1$ or $1+1 \to 0$).

---

## Next Sequence
- [[Bit-Width Conversions & Extensions]]
- [[Type Conversions & Arithmetic Hierarchy]]
