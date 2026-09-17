---
tags:
  - clang
  - c-language
  - two-complement
  - bit-manipulation
  - study
---


## 1. The Identity Formula 📐

When an $n$-bit binary integer has its Most Significant Bit set to $1$ ($\text{MSB} = 1 \implies U \ge 2^{n-1}$):

$$U - S = 2^n$$

Equivalently:
$$S = U - 2^n$$
$$U = S + 2^n$$

Where:
* $n$ = bit-width of the integer container ($8$ for `char`, $16$ for `short`, $32$ for `int`)
* $U$ = Unsigned interpretation of the $n$-bit pattern ($\text{val} \pmod{2^n}$)
* $S$ = Signed two's complement interpretation ($S < 0$)

---

## 2. Mathematical Proof & Intuition 🧮

In an $n$-bit positional binary system:
- **Unsigned Weight of MSB (bit $n-1$):** $+2^{n-1}$
- **Two's Complement Weight of MSB (bit $n-1$):** $-2^{n-1}$

The positional weights for all remaining lower bits ($b_0$ to $b_{n-2}$) are identical in both systems:
$$U = 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$
$$S = -2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$

Subtracting $S$ from $U$:
$$U - S = \left(2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i\right) - \left(-2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i\right)$$
$$U - S = 2^{n-1} - (-2^{n-1}) = 2^{n-1} + 2^{n-1} = 2^n$$

$$\therefore U - S = 2^n$$

---

## 3. Practical Applications & Worked Examples 💡

### Example 1: 8-Bit Container ($n = 8 \implies 2^8 = 256$)
Given an unsigned bit pattern $U = 251_{10}$ (`11111011_2`):
- Since $251 \ge 128$, $\text{MSB} = 1$.
- Applying the Shift Identity:
  $$S = U - 2^8 = 251 - 256 = -5$$

### Example 2: Finding Unsigned Bit Pattern from Negative Value
Given $S = -6_{10}$ in an $8$-bit container ($n = 8$):
- Applying the Shift Identity:
  $$U = S + 2^8 = -6 + 256 = 250_{10} \quad (\text{0xFA})$$

