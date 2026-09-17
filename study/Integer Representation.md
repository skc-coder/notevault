---
tags:
  - clang
  - c-language
  - moc
  - study
---


---

## Logical Sequence & Atomic Notes

1. **[[Twos Complement Fundamentals]]**
   - Direct positional evaluation via negative MSB weight ($V = -b_{n-1}\cdot 2^{n-1} + \dots$).
   - Bit inversion algorithm ($\sim A + 1$) and sign extension invariants.

2. **[[Twos Complement Shift Identity]]**
   - Direct mathematical identity $U - S = 2^n$ translating between unsigned $U$ and signed two's complement $S$ when $\text{MSB} = 1$.

3. **[[Integer Value Ranges]]**
   - Unsigned vs Signed ($1$'s complement, sign-magnitude, $2$'s complement) ranges.
   - Why two's complement is standard (unique zero, full $2^n$ code utilization).

4. **[[Overflow Detection Rules]]**
   - Detection rules for sign-magnitude and two's complement ($0+0 \to 1$ or $1+1 \to 0$).

---

## Next Sequence
- [[Type Conversions Hierarchy]]
- [[Bit Width Conversions]]
