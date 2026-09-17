---
title: Integer Representation & Encoding
tags:
  - clang
  - c-language
  - moc
  - study
---

# Integer Representation & Encoding

> [!abstract] Overview
> Logical hub note for binary integer encoding formats, two's complement arithmetic, positional weighting, and value range bounds in C.

---

## Logical Sequence & Atomic Notes

1. **[[Two's Complement Fundamentals & Weight Method]]**
   - Direct positional evaluation via negative MSB weight ($V = -b_{n-1}\cdot 2^{n-1} + \dots$).
   - Bit inversion algorithm ($\sim A + 1$) and sign extension invariants.

2. **[[Integer Value Ranges & Signed vs Unsigned Systems]]**
   - Unsigned vs Signed ($1$'s complement, sign-magnitude, $2$'s complement) ranges.
   - Why two's complement is standard (unique zero, full $2^n$ code utilization).

3. **[[Overflow Definition & Detection Rules]]**
   - Detection rules for sign-magnitude and two's complement ($0+0 \to 1$ or $1+1 \to 0$).

---

## Next Sequence
- [[Type Conversions, Integer Promotion & Arithmetic Hierarchy]]
- [[Bit-Width Conversions & Extensions]]
