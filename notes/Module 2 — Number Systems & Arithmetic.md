## 1. Octal and Hexadecimal Number Systems

Radix conversion relies on power-of-two groupings because $8 = 2^3$ and $16 = 2^4$.

### Base Conversion Rules
- **Binary $\leftrightarrow$ Octal:** Group binary bits into clusters of **3 bits** starting from the binary point (left for integer parts, right for fractional parts). Pad with leading/trailing zeros as needed.
- **Binary $\leftrightarrow$ Hexadecimal:** Group binary bits into clusters of **4 bits** starting from the binary point. Pad with zeros if necessary. Hex digits span $0\text{--}9$ and $\text{A}\text{--}\text{F}$ ($\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$).
- **Octal $\leftrightarrow$ Hexadecimal:** Always route through Binary as the intermediate step ($\text{Octal} \to \text{Binary} \to \text{Hexadecimal}$), which avoids tedious multi-digit decimal division.

**Example:** Convert $(11010110.101)_2$
- **To Octal:** $(011)(010)(110).(101)_2 \implies (326.5)_8$
- **To Hex:** $(1101)(0110).(1010)_2 \implies (\text{D}6.\text{A})_{16}$

---

## 2. Binary Addition

Binary bit-level rules govern all digital ALU addition:
- $0 + 0 = 0 \quad (\text{Carry } 0)$
- $0 + 1 = 1 \quad (\text{Carry } 0)$
- $1 + 0 = 1 \quad (\text{Carry } 0)$
- $1 + 1 = 0 \quad (\text{Carry } 1)$
- $1 + 1 + 1 = 1 \quad (\text{Carry } 1)$

---

## 3. Radix & Diminished Radix Complements

For a number $N$ with base (radix) $r$ having an integer length of $n$ digits and a fractional length of $m$ digits:

### Radix Complement ($r$'s Complement)
$$r\text{'s Complement} = r^n - N$$

### Diminished Radix Complement ($(r-1)$'s Complement)
$$(r-1)\text{'s Complement} = (r^n - r^{-m}) - N$$
For integers ($m = 0$):
$$(r-1)\text{'s Complement} = (r^n - 1) - N$$

### Relation Between Complements
$$r\text{'s Complement} = [(r-1)\text{'s Complement}] + r^{-m}$$
For pure integers:
$$r\text{'s Complement} = [(r-1)\text{'s Complement}] + 1$$

---

## 4. Subtraction Using Complements ($M - N$)

Assume both numbers are represented in $n$ digits.

### A. Using $r$'s Complement (e.g., 2's or 10's complement)
1. Add the $r$'s complement of the subtrahend $N$ to the minuend $M$:
   $$\text{Sum} = M + (r^n - N) = r^n + (M - N)$$
2. **Case 1: If an end-carry is generated** (carry out of MSB = 1):
   - Discard the end-carry ($r^n$).
   - The result is **positive** and equals $(M - N)$.
3. **Case 2: If no end-carry is generated** (carry out of MSB = 0):
   - The result is **negative**.
   - Take the $r$'s complement of the resulting sum and attach a negative sign:
     $$\text{Result} = -[r\text{'s complement of Sum}]$$

### B. Using $(r-1)$'s Complement (e.g., 1's or 9's complement)
1. Add the $(r-1)$'s complement of $N$ to $M$:
   $$\text{Sum} = M + (r^n - 1 - N) = r^n - 1 + (M - N)$$
2. **Case 1: If an end-carry occurs**:
   - The result is **positive**.
   - Perform an **End-Around Carry**: Add $1$ to the LSB of the result.
3. **Case 2: If no end-carry occurs**:
   - The result is **negative**.
   - Take the $(r-1)$'s complement of the resulting sum and attach a negative sign.

---

## 5. Signed Number Systems & Ranges (for $n$ bits)

| System | MSB Interpretation | Positive Representation | Negative Representation | Zero Representation | Range ($n$ bits) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Unsigned** | Magnitude bit | Binary | N/A | Unique (`00...0`) | $0 \text{ to } 2^n - 1$ |
| **Sign-Magnitude** | Sign ($0=+, 1=-$) | Normal binary | Invert MSB only | Dual ($+0$ and $-0$) | $-(2^{n-1} - 1) \text{ to } +(2^{n-1} - 1)$ |
| **1's Complement** | Sign ($0=+, 1=-$) | Normal binary | Bitwise NOT all bits | Dual ($+0$ and $-0$) | $-(2^{n-1} - 1) \text{ to } +(2^{n-1} - 1)$ |
| **2's Complement** | Sign ($0=+, 1=-$) | Normal binary | 1's comp $+ 1$ | Unique (`00...0`) | $\mathbf{-2^{n-1} \text{ to } +(2^{n-1} - 1)}$ |

### High-Yield 2's Complement Properties:
- Extra negative value: In an $n$-bit 2's complement system, the minimum number is $-2^{n-1}$, represented as `100...00`. Negating this value in the same bit-width produces an overflow because $+2^{n-1}$ cannot be represented.
- **Sign Extension Rule:** To expand an $n$-bit signed number into $k$ bits ($k > n$), duplicate the MSB (sign bit) to fill the newly added upper positions on the left.
- **Weight of 2's complement bits:**
  $$\text{Value}(b_{n-1} \dots b_0) = -b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$

---

## 6. Arithmetic with Signed Numbers & Overflow Detection

### Signed Addition Rules
In a 2's complement hardware adder:
1. Carry generated out of the sign bit (MSB) does **not** indicate overflow. It is simply ignored.
2. An overflow occurs if and only if the calculated result falls outside the representable range $[-2^{n-1}, +2^{n-1} - 1]$.

### Conditions When Overflow CAN and CANNOT Occur:
- $(\text{Positive}) + (\text{Negative}) \to$ **Never causes overflow**.
- $(\text{Positive}) - (\text{Positive}) \to$ **Never causes overflow**.
- $(\text{Positive}) + (\text{Positive}) = \text{Negative result} \to$ **Overflow occurs**.
- $(\text{Negative}) + (\text{Negative}) = \text{Positive result} \to$ **Overflow occurs**.

### Hardware Detection Formulae
Let $C_{in}$ be the carry into the sign bit position, and $C_{out}$ be the carry out of the sign bit position:

$$\mathbf{V = C_{in} \oplus C_{out}}$$

- If $V = 0 \implies \text{No Overflow}$ (result valid).
- If $V = 1 \implies \text{Overflow occurred}$ (result corrupted).

Alternatively, using operand sign bits $A_{n-1}, B_{n-1}$ and result sign bit $S_{n-1}$:
$$V = A_{n-1} B_{n-1} S_{n-1}' + A_{n-1}' B_{n-1}' S_{n-1}$$

---

## 7. Binary Codes

| Code Type | Weighted? | Self-Complementing? | Cyclic / Unit-Distance? | Primary Applications |
| :--- | :---: | :---: | :---: | :--- |
| **8421 (BCD)** | Yes | No | No | Decimal displays, digital clocks, simple meters |
| **Excess-3 (XS-3)** | No | **Yes** | No | Decimal arithmetic (simplifies 9's complement hardware) |
| **2421 (Aiken)** | Yes | **Yes** | No | Self-complementing weighted calculations |
| **Gray Code** | No | No | **Yes** | Shaft encoders, K-maps, clock-domain crossing FIFOs |

### Self-Complementing Rule
A code is self-complementing if the 1's complement of its code word yields the 9's complement of the decimal digit it represents.
- For a weighted code with weights $w_3, w_2, w_1, w_0$ to be self-complementing:
  $$\sum w_i = 9$$
- Examples: **Excess-3**, **2421**, **5211**, **3321**, **4311**.
- **8421 BCD is NOT self-complementing** because $8+4+2+1 = 15 \neq 9$.

---

## 8. Gray Code (Reflected Binary Code)

Gray code is an unweighted, non-arithmetic, **unit-distance code** where successive values differ by exactly **one bit**. This eliminates spurious glitches and intermediate race states in mechanical encoders and asynchronous logic boundaries.

### Binary to Gray Conversion
Given binary number $B = B_{n-1} B_{n-2} \dots B_1 B_0$:
$$G_{n-1} = B_{n-1} \quad (\text{MSB remains identical})$$
$$G_i = B_{i+1} \oplus B_i \quad \text{for } i = n-2, \dots, 0$$

### Gray to Binary Conversion
Given Gray code $G = G_{n-1} G_{n-2} \dots G_1 G_0$:
$$B_{n-1} = G_{n-1} \quad (\text{MSB remains identical})$$
$$B_i = B_{i+1} \oplus G_i \quad \text{for } i = n-2, \dots, 0$$

```
B ───⊕───> B ───⊕───> B ───⊕───> B (Horizontal / Side-by-side) │ │ │ │ ▼ ▼ ▼ ▼ G G G G
```
```
G G G G │ ↗ │ ↗ │ ↗ │ ▼ ⊕ ▼ ⊕ ▼ ⊕ ▼ (Bounce / Zigzag) B ─────┘ B ─────┘ B ─────┘ B
```
### Summary Anchor

- Going to **G**ray? $\to$ **G**round / **G**ate between neighbors (horizontal XOR).
    
- Going to **B**inary? $\to$ **B**ounce / **B**ounce-up diagonally (zigzag XOR).
## Quick Revision Summary (High-Yield Formulae)

1. **Range of $n$-bit integers:**
   - Unsigned: $[0, 2^n - 1]$
   - Sign-Magnitude: $[-(2^{n-1} - 1), +(2^{n-1} - 1)]$
   - 1's Complement: $[-(2^{n-1} - 1), +(2^{n-1} - 1)]$
   - 2's Complement: $[-2^{n-1}, +(2^{n-1} - 1)]$

2. **Zero Representations:**
   - 1's Comp & Sign-Mag have **two zeros**: $+0$ and $-0$.
   - 2's Comp has a **unique zero** (`00...0`).

3. **Complement Relations:**
   - $r\text{'s Complement} = (r-1)\text{'s Complement} + 1$
   - 1's Complement of $N$: Bitwise NOT all bits.
   - 2's Complement of $N$: Leave all trailing zeros and the first '1' untouched; flip all bits to the left of it.

4. **Overflow Flag:**
   $$V = C_{in} \oplus C_{out} = A_{n-1} B_{n-1} S_{n-1}' + A_{n-1}' B_{n-1}' S_{n-1}$$

5. **Self-Complementing Codes:**
   - Sum of weights must equal 9.
   - Excess-3 = $\text{BCD} + 0011_2$.
   - 8421 BCD is **not** self-complementing.