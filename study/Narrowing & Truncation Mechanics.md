---
tags:
  - clang
  - c-language
  - type-conversion
  - study
---


Converting a wider integer type to a narrower integer type (narrowing conversion) causes excess bits to be discarded.

> [!definition] Truncation Rule
> When narrowing an integer from width $W_{\text{source}}$ to $W_{\text{dest}}$:
> - The upper $(W_{\text{source}} - W_{\text{dest}})$ bytes/bits are discarded (**truncated**).
> - Truncation operates purely via bit slicing; neither the signedness of the RHS nor LHS affects bit chopping.
> - Discarding upper bits can abruptly alter numeric magnitude or flip the sign bit (changing a positive value into negative or vice versa).

---

## Direct Example: Overflowing Container Width

```c
signed char x = 258;
```
1. Constant representation ($32$-bit `int`):
   $$258_{10} = 00000000\;00000000\;00000001\;00000010_2$$
2. **Truncation to 8 bits (`signed char`):** Discards upper 24 bits, retaining lower 8 bits:
   $$00000010_2 = 2_{10}$$
3. Resulting value in `x` is `2`.

