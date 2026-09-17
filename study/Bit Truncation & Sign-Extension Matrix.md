---
tags:
  - clang
  - c-language
  - type-conversion
  - bit-manipulation
  - study
---


## 1. Overview & Setup 🗺️

When a value is truncated into an $n$-bit container, the hardware retains only the lower $n$ bits:
$$U = \text{val} \pmod{2^n}$$

Where:
* $n$ = bit-width of the narrow/source variable (e.g., $8$ for `char`, $16$ for `short`)
* $N$ = bit-width of the promoted/destination container (e.g., $32$ for `int` / `printf`)
* The **MSB** (Most Significant Bit, bit $n-1$) and the type of variable containg `U` determines the extension bit.

---

## 2. The Master Conversion Table 📊

| Specifier / Interpretation | $\text{MSB} = 0$ (Positive) | $\text{MSB} = 1$ (Negative)                                |
| :------------------------- | :-------------------------- | :--------------------------------------------------------- |
| **`signed` / `%d`**        | $\text{val} \pmod{2^n}$     | $-2^n + \left(\text{val} \pmod{2^n}\right)$                |
| **`unsigned` / `%u`**      | $\text{val} \pmod{2^n}$     | $2^N - 2^n + \left(\text{val} \pmod{2^n}\right) = 2^N + S$ |

---

## 3. Mathematical Derivations 🧮

### Row 1: Signed Interpretation (`%d`)
* **When $\text{MSB} = 0$:**
  The sign bit carries no negative weight.
  $$\text{Value} = U = \text{val} \pmod{2^n}$$

* **When $\text{MSB} = 1$:**
  In two's complement, bit $n-1$ has a weight of $-2^{n-1}$, whereas in unsigned it had $+2^{n-1}$. The difference is $-2^n$ (see [[Two's Complement Unsigned-Signed Shift Identity (U - S = 2^n)]]):
  $$S = U - 2^n \implies U - S = 2^n$$
  $$S = -2^n + \left(\text{val} \pmod{2^n}\right)$$

---

### Row 2: Unsigned Interpretation (`%u`) with Sign Extension
When an $n$-bit signed variable with $\text{MSB} = 1$ is widened to an $N$-bit container (such as during `printf` promotion to $32$ bits), the CPU replicates $1$s across all upper bits from position $n$ to $N-1$:

1. **Weight of the added $1$s:**
   $$\sum_{i=n}^{N-1} 2^i = 2^N - 2^n$$

2. **Total unsigned value in the $N$-bit register:**
   $$\text{Register Value} = \underbrace{(2^N - 2^n)}_{\text{Upper extended 1s}} + \underbrace{\left(\text{val} \pmod{2^n}\right)}_{\text{Lower } n \text{ bits } (U)}$$

3. **Simplification via Signed Value $S$:**
   Since $S = -2^n + U$:
   $$\text{Register Value} = 2^N + \left(-2^n + U\right) = 2^N + S = 2^N - |S|$$

---

## 4. Worked Examples 🔍

### Example 1: `signed char c = -5;` printed with `%u`
* Narrow size: $n = 8$ ($2^8 = 256$)
* Promoted size: $N = 32$ ($2^{32}$)
* Lower 8 bits:
  $$U = -5 \pmod{2^8} = 256 - 5 = 251$$
* Because $251 \ge 128$, $\text{MSB} = 1$.
* Applying the table formula:
  $$\text{Printed Value} = 2^{32} - 2^8 + (2^8 - 5) = 2^{32} - 5 = 4294967291$$

### Example 2: `signed char c = 250;` printed with `%d`
* $n = 8$
* Truncation: $250 \pmod{256} = 250$
* Since $250 \ge 128$, $\text{MSB} = 1$.
* Row 1 formula:
  $$S = -2^8 + 250 = -256 + 250 = -6$$

### Example 3: `short s = 0xABCD;` ($43981_{10}$)
* $n = 16$ ($2^{16} = 65536$)
* Since $43981 \ge 32768$, $\text{MSB} = 1$.
* Row 1 formula:
  $$S = 43981 - 2^{16} = 43981 - 65536 = -21555$$

---

## Related Notes
- [[Bit-Width Conversions & Extensions]]
- [[Bit-Width Extensions & Sign vs Zero Extension]]
- [[Narrowing & Truncation Mechanics]]
- [[C Integer Conversion & Printf Formatting Case Studies]]
