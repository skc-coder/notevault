---
title: Two's Complement Fundamentals & Weight Method
tags:
  - clang
  - c-language
  - integer-representation
  - study
---

# Two's Complement Fundamentals & Weight Method

In C, signed integer types are standardly represented using **two's complement notation**.

> [!definition] Two's Complement
> The two's complement of an $n$-bit binary integer is formed by inverting all bits (1's complement) and adding $1$ to the least significant bit (LSB):
> $$\text{Two's Complement}(A) = \sim A + 1$$

> [!important] Key Representation Invariant
> In two's complement systems, positive numbers have standard binary representation with `0` in the MSB, while negative numbers store the 2's complement of their absolute value. 
> 
> Redundant sign bits can be added or eliminated without altering the numeric value:
> - **Positive numbers:** `0001` $\equiv$ `01`
> - **Negative numbers:** `11101` $\equiv$ `101`

---

## Direct Evaluation via Negative MSB Weight

An $n$-bit signed binary number $b_{n-1}b_{n-2}\dots b_1b_0$ can be directly converted to its decimal equivalent by assigning a **negative positional weight** to the Most Significant Bit (MSB):

> [!formula] Direct Two's Complement Formula
> $$V = -b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$

### Evaluation Examples
- **Evaluating `1011` ($4$-bit signed):**
  $$V = -1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = -8 + 0 + 2 + 1 = -5$$
- **Evaluating `0101` ($4$-bit signed):**
  $$V = -0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 0 + 4 + 0 + 1 = 5$$

---

## Alternative Evaluation Algorithm

1. **If $\text{MSB} = 0$:** The number is positive; perform standard binary-to-decimal conversion.
2. **If $\text{MSB} = 1$:** The number is negative; compute two's complement ($\sim A + 1$), convert to decimal, and prepend a minus sign ($-$).

---

## Related Notes
- [[Integer Value Ranges & Signed vs Unsigned Systems]]
- [[Integer Promotion Rules in C]]
- [[Bit-Width Conversions & Extensions]]
- [[Overflow Definition & Detection Rules]]
