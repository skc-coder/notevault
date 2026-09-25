# Module 3: Combinational Circuits (PSU & Competitive Exam Reference)

---

## 1. Compact Truth Tables

Standard truth tables list all $2^n$ combinations explicitly. For higher-variable optimization and Multiplexer/Decoder routing, **Compact Truth Tables** collapse outputs into algebraic functions of a single input variable or treat subsets of inputs as selectors.

### Construction Rule
1. Choose $k$ variables as primary select/index lines (usually the most significant variables).
2. The remaining variable(s) serve as data expressions ($0, 1, X, X'$).
3. Each row of the compact table maps directly to a multiplexer data input line $I_k$ or a decoder sub-function.

**Example:** Expressing $F(A, B, C) = \sum m(1, 2, 4, 7)$ using $A, B$ as select lines and $C$ as data:

| $A$ | $B$ | Minterms Evaluated | $C=0$ | $C=1$ | Compact Output $I_k$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | $m_0, m_1$ | 0 | 1 | $I_0 = C$ |
| 0 | 1 | $m_2, m_3$ | 1 | 0 | $I_1 = C'$ |
| 1 | 0 | $m_4, m_5$ | 1 | 0 | $I_2 = C'$ |
| 1 | 1 | $m_6, m_7$ | 0 | 1 | $I_3 = C$ |

---

## 2. Multiplexers (MUX)

A Multiplexer is a **Data Selector** / **Many-to-One** combinational circuit. It routes one of $2^n$ data inputs to a single output line based on $n$ select lines.

### Fundamental Equation
For a $2^n \times 1$ MUX with select lines $S_{n-1}, \dots, S_0$:
$$Y = \sum_{k=0}^{2^n-1} m_k(S) \cdot I_k$$

For a $4 \times 1$ MUX:
$$Y = S_1' S_0' I_0 + S_1' S_0 I_1 + S_1 S_0' I_2 + S_1 S_0 I_3$$

### Logic Function Realization Using MUX

#### Rule 1: Realizing an $n$-variable function using a $2^n \times 1$ MUX
- Connect all $n$ function variables to the $n$ select lines.
- For each minterm present in the function, tie the corresponding data input $I_k$ to logic `1`.
- For absent minterms, tie $I_k$ to logic `0`.

#### Rule 2: Realizing an $n$-variable function using a $2^{n-1} \times 1$ MUX
- Connect $(n-1)$ variables to select lines.
- The remaining variable maps to data inputs as $0$, $1$, $V$, or $V'$:
  - If minterms for $(V=0, V=1)$ are $(0, 0) \implies I_k = 0$
  - If minterms are $(0, 1) \implies I_k = V$
  - If minterms are $(1, 0) \implies I_k = V'$
  - If minterms are $(1, 1) \implies I_k = 1$

#### Rule 3: Tree Expansion Formula
To build an $N \times 1$ MUX using lower-order $m \times 1$ multiplexers:
$$\text{Total MUXes required} = \frac{N}{m} + \frac{N}{m^2} + \frac{N}{m^3} + \dots + 1$$
*Example:* Implementing a $64 \times 1$ MUX using $4 \times 1$ MUXes:
$$\frac{64}{4} + \frac{16}{4} + \frac{4}{4} = 16 + 4 + 1 = \mathbf{21 \text{ MUXes}}$$

---

## 3. Demultiplexers (DEMUX)

A Demultiplexer is a **Data Distributor** / **One-to-Many** circuit. It directs a single input signal to one of $2^n$ outputs based on $n$ select inputs.

- **Relationship:** A $1 \times 2^n$ DEMUX is structurally identical to an $n \times 2^n$ Decoder with an active Enable ($E$) line acting as the data input.
- **For a $1 \times 4$ DEMUX with Data Input $D$ and Selects $S_1, S_0$:**
  - $Y_0 = S_1' S_0' D$
  - $Y_1 = S_1' S_0 D$
  - $Y_2 = S_1 S_0' D$
  - $Y_3 = S_1 S_0 D$

---

## 4. Encoders & Priority Encoders

An Encoder performs the inverse operation of a decoder, converting $2^n$ (or fewer) input lines into an $n$-bit coded output.

### Standard Binary Encoder ($2^n \to n$)
- Limitation: Only one input line must be asserted high at any instant. If multiple lines go high simultaneously, the output code is invalid/corrupted.

### Priority Encoder ($4 \to 2$)
Assigns operational priority to inputs. If two or more inputs are active simultaneously, the output corresponds to the input with the highest priority index (commonly $D_3 > D_2 > D_1 > D_0$).

A valid output flag ($V$) is added to differentiate between "Input $D_0$ is active" and "No inputs are active".

| $D_3$ | $D_2$ | $D_1$ | $D_0$ | $Y_1$ | $Y_0$ | $V$ (Valid Bit) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | X | X | 0 |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | X | 0 | 1 | 1 |
| 0 | 1 | X | X | 1 | 0 | 1 |
| 1 | X | X | X | 1 | 1 | 1 |

- **Simplified Boolean Equations:**
  $$Y_1 = D_3 + D_2$$
  $$Y_0 = D_3 + D_2' D_1$$
  $$V = D_3 + D_2 + D_1 + D_0$$

---

## 5. Decoders & Function Realization

A Decoder converts an $n$-bit binary input code into a maximum of $2^n$ distinct output lines.

### Characteristics
- **Active-HIGH Decoder:** Selected output line goes to logic `1`; produces standard **Minterms** ($m_i$).
  - A Boolean function in SOP form is realized by feeding minterm outputs into an **OR gate**.
- **Active-LOW Decoder:** Selected output line goes to logic `0`; produces standard **Maxterms** ($M_i$).
  - A Boolean function in SOP form is realized by feeding active-low outputs into a **NAND gate**.

### Higher-Order Decoder Implementation
To construct an $M$-output decoder using smaller $k$-output decoders:
$$\text{Number of required ICs} = \frac{\text{Outputs needed}}{\text{Outputs per available IC}}$$
*Example:* Constructing a $4 \times 16$ Decoder ($16$ outputs) using $2 \times 4$ Decoders ($4$ outputs):
- First stage: $\frac{16}{4} = 4$ decoders (to generate individual outputs).
- Enable routing: $\frac{4}{4} = 1$ decoder (drives the enable inputs of the first stage).
- Total required: $4 + 1 = \mathbf{5 \text{ decoders}}$.

---

## 6. Adders: Architectures & Analysis

### A. Half Adder (HA)
Adds two 1-bit binary inputs ($A, B$).
- **Sum:** $S = A \oplus B = A'B + AB'$
- **Carry:** $C = A \cdot B$
- **NAND Implementation:** Requires **5 two-input NAND gates**.
- **NOR Implementation:** Requires **5 two-input NOR gates**.

### B. Full Adder (FA)
Adds three 1-bit binary inputs ($A, B, C_{in}$).
- **Sum:** $S = A \oplus B \oplus C_{in}$
- **Carry Out:** 
  $$C_{out} = AB + BC_{in} + AC_{in} = AB + (A \oplus B)C_{in}$$
- **Gate Counts & Minimum Implementations:**
  - $1 \text{ Full Adder} = \mathbf{2 \text{ Half Adders}} + \mathbf{1 \text{ OR Gate}}$
  - Implementation with NAND only: **9 two-input NAND gates**
  - Implementation with NOR only: **9 two-input NOR gates**
[[ adder trick]]
---

### C. Ripple Carry Adder (RCA)

Constructed by cascading $n$ Full Adders in series, where the carry output of each stage ($C_i$) feeds as the carry input to the subsequent stage ($C_{i+1}$).

- **Delay Formulation:**
  - Let $t_{carry}$ be the carry propagation delay per FA.
  - Let $t_{sum}$ be the delay to compute Sum in a FA.
  - Worst-case path occurs when a carry ripples from LSB to MSB:
    $$T_{worst} = (n - 1) \cdot t_{carry} + \max(t_{sum}, t_{carry})$$
    *(Often approximated in competitive exams as $T_{total} = n \cdot t_{carry}$)*
- **Bottleneck:** Operating speed drops linearly ($O(n)$) as the bit-width expands.

---

### D. Carry Look-Ahead Adder (CLA)

Eliminates the linear carry ripple delay by computing carry bits ahead of time using parallel combinational logic.

#### Generation and Propagation Variables
For stage $i$ with inputs $A_i$ and $B_i$:
- **Carry Generate ($G_i$):** Creates an immediate carry independent of previous carry.
  $$G_i = A_i \cdot B_i$$
- **Carry Propagate ($P_i$):** Propagates an incoming carry to the next stage.
  $$P_i = A_i \oplus B_i \quad (\text{or } A_i + B_i)$$

#### Look-Ahead Carry Expansion
$$C_1 = G_0 + P_0 C_0$$
$$C_2 = G_1 + P_1 C_1 = G_1 + P_1 G_0 + P_1 P_0 C_0$$
$$C_3 = G_2 + P_2 C_2 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
$$C_4 = G_3 + P_3 C_3 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$

#### Delay Analysis (Assuming 2-input/multi-input equivalent gate delays $\tau$):
1. Generation of all $P_i, G_i$: $1\tau$ (or $1 \text{ XOR delay}$ for $P_i$).
2. Carry Generator Logic (AND-OR two-level network): $2\tau$ (one AND layer + one OR layer).
3. Final Sum computation ($S_i = P_i \oplus C_i$): $1 \text{ XOR delay}$.
- **Result:** Carry computation occurs in constant time ($O(1)$ delay), independent of bit-width $n$.
- **Practical Limit:** High fan-in requirements on AND/OR gates restrict standalone CLA blocks to 4 bits.

---

## 7. Functional Completeness & Post's Theorem

### Functional Completeness
A set of logic gates/operations is **functionally complete** (or **universal**) if every possible switching function can be synthesized using only elements from that set, without requiring external constants other than input variables (or with available constants $0, 1$).

#### Universal Gate Sets:
- $\{\text{NAND}\}$ alone
- $\{\text{NOR}\}$ alone
- $\{\text{AND}, \text{NOT}\}$
- $\{\text{OR}, \text{NOT}\}$
- $\{\text{MUX}\}$ (given logic constants $0$ and $1$)
- $\{\text{XOR}, \text{AND}, 1\}$

#### Incomplete Sets (Common Negative Questions):
- $\{\text{AND}, \text{OR}\}$ (cannot invert a signal; monotonic only)
- $\{\text{XOR}, \text{XNOR}\}$ (linear functions only; cannot produce AND/OR operations)

---

### Post's Functional Completeness Theorem

A mathematical formulation establishing the necessary and sufficient conditions for a set of Boolean operators $F$ to be functionally complete. 

According to Post's Theorem, **a set of Boolean functions $F$ is functionally complete if and only if it is not entirely contained within any of the following 5 closed functional classes:**

1. **$T_0$ (0-Preserving / Zero-Preserving):**
   - A function $f$ preserves zero if $f(0, 0, \dots, 0) = 0$.
   - *Example:* AND, OR preserve 0. NOT, NAND, NOR do **not** preserve 0.
   - *Criterion:* $F \not\subseteq T_0$ (The set must contain at least one function where $f(0, 0, \dots, 0) = 1$).

2. **$T_1$ (1-Preserving / One-Preserving):**
   - A function $f$ preserves one if $f(1, 1, \dots, 1) = 1$.
   - *Example:* AND, OR preserve 1. NOT, NAND, NOR do **not** preserve 1.
   - *Criterion:* $F \not\subseteq T_1$ (The set must contain at least one function where $f(1, 1, \dots, 1) = 0$).

3. **$S$ (Self-Dual Functions):**
   - A function is self-dual if negating all inputs negates the output:
     $$f(x_1', x_2', \dots, x_n') = f'(x_1, x_2, \dots, x_n)$$
   - *Example:* NOT is self-dual ($0' = 1, 1' = 0$). NAND and NOR are **not** self-dual.
   - *Criterion:* $F \not\subseteq S$ (The set must contain at least one non-self-dual function).

4. **$M$ (Monotonic Functions):**
   - A function is monotonic if increasing any input from $0 \to 1$ never causes the output to decrease from $1 \to 0$:
     $$X \le Y \implies f(X) \le f(Y)$$
   - *Example:* AND, OR are monotonic. NOT, NAND, NOR are **not** monotonic.
   - *Criterion:* $F \not\subseteq M$ (The set must contain at least one non-monotonic function).

5. **$L$ (Linear / Affine Functions):**
   - A function is linear if it can be represented as:
     $$f(x_1, x_2, \dots, x_n) = c_0 \oplus c_1 x_1 \oplus c_2 x_2 \oplus \dots \oplus c_n x_n \quad (c_i \in \{0, 1\})$$
   - *Example:* XOR, XNOR, NOT, BUFFER are linear. AND, OR, NAND, NOR are non-linear.
   - *Criterion:* $F \not\subseteq L$ (The set must contain at least one non-linear function).

> **Post's Decision Rule:**
> A set $F$ is functionally complete **if and only if**:
> $$F \not\subseteq T_0 \quad\land\quad F \not\subseteq T_1 \quad\land\quad F \not\subseteq S \quad\land\quad F \not\subseteq M \quad\land\quad F \not\subseteq L$$

---

## Quick Revision Summary (High-Yield Formulae)

1. **Multiplexer & Decoder Sizing:**
   - $2^n \times 1$ MUX: $n$ select lines, 1 output.
   - $n \times 2^n$ Decoder: $n$ input lines, $2^n$ output lines.
   - Decoders with active-LOW outputs implement SOP via **NAND** gates.
   - Decoders with active-HIGH outputs implement SOP via **OR** gates.

2. **Full Adder Implementation Limits:**
   - $1 \text{ FA} = 2 \text{ HA} + 1 \text{ OR gate}$
   - Min NAND gates for Half Adder = **5**
   - Min NAND gates for Full Adder = **9**
   - Min NOR gates for Half Adder = **5**
   - Min NOR gates for Full Adder = **9**

3. **Adder Delay Comparison:**
   - **Ripple Carry Adder (RCA):** Delay $\propto n$ ($O(n)$ time complexity).
   - **Carry Look-Ahead Adder (CLA):** Delay $\propto 1$ ($O(1)$ constant time complexity), limited practically by gate fan-in constraints.
   - Generate: $G_i = A_i B_i$; Propagate: $P_i = A_i \oplus B_i$.

4. **Priority Encoder Identity ($4 \to 2$):**
   - $Y_1 = D_3 + D_2$
   - $Y_0 = D_3 + D_2' D_1$

5. **Post's Functional Completeness Classes Checklist:**
   - Non-$T_0$ (does not map $0 \to 0$)
   - Non-$T_1$ (does not map $1 \to 1$)
   - Non-Self-Dual ($f(X') \neq f'(X)$)
   - Non-Monotonic (must allow $0 \to 1$ input transition to yield $1 \to 0$ output)
   - Non-Linear (cannot be factored strictly with XOR/XNOR)

# Half Subtractor & Full Subtractor (Complete PSU Reference)

---

## 1. Half Subtractor (HS)

Computes the difference between two single bits ($A - B$).

### Truth Table

| $A$ (Minuend) | $B$ (Subtrahend) | Difference ($D$) | Borrow ($B_{out}$) |
| :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

### Boolean Expressions
- **Difference ($D$):** 
  $$D = A'B + AB' = A \oplus B$$
  *(Identical to the Sum expression of a Half Adder)*
- **Borrow ($B_{out}$):**
  $$B_{out} = A'B$$
  *(Requires a borrow only when trying to subtract $1$ from $0$)*

---

## 2. Full Subtractor (FS)

Computes the subtraction of three bits: $A - B - B_{in}$ ($A$ is minuend, $B$ is subtrahend, $B_{in}$ is incoming borrow).

### Truth Table

| $A$ | $B$ | $B_{in}$ | Difference ($D$) | Borrow ($B_{out}$) | Minterms ($m$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | - |
| 0 | 0 | 1 | 1 | 1 | $m_1$ |
| 0 | 1 | 0 | 1 | 1 | $m_2$ |
| 0 | 1 | 1 | 0 | 1 | $m_3$ |
| 1 | 0 | 0 | 1 | 0 | $m_4$ |
| 1 | 0 | 1 | 0 | 0 | - |
| 1 | 1 | 0 | 0 | 0 | - |
| 1 | 1 | 1 | 1 | 1 | $m_7$ |

### Boolean Expressions
- **Difference ($D$):**
  $$D = \sum m(1, 2, 4, 7) = A \oplus B \oplus B_{in}$$
  *(Notice: The Difference expression of FS is **100% identical** to the Sum of FA)*

- **Borrow Out ($B_{out}$):**
  $$B_{out} = \sum m(1, 2, 3, 7) = A'B + A'B_{in} + B B_{in}$$

- **Factored / Half-Subtractor Form:**
  $$B_{out} = A'B + (A \oplus B)' B_{in}$$
  *(Can also be written as $A'B + (A \odot B) B_{in}$)*

---

## 3. Implementation Using Two Half Subtractors

Just like a Full Adder requires $2\text{ HA} + 1\text{ OR}$, a Full Subtractor requires:
$$\mathbf{1 \text{ Full Subtractor}} = \mathbf{2 \text{ Half Subtractors}} + \mathbf{1 \text{ OR Gate}}$$

<Image src="image_agent_tag_685658861065099330" alt="Full Subtractor logic circuit using two half subtractors and an OR gate" caption="Full Subtractor from 2 HS and 1 OR Gate" />

### Signal Flow:
1. **First Half Subtractor ($\text{HS}_1$):**
   - Inputs: $A, B$
   - Intermediate Difference: $D_1 = A \oplus B$
   - Intermediate Borrow: $B_1 = A'B$
2. **Second Half Subtractor ($\text{HS}_2$):**
   - Inputs: $D_1$ and $B_{in}$
   - Final Difference: $D = D_1 \oplus B_{in} = A \oplus B \oplus B_{in}$
   - Second Borrow: $B_2 = D_1' \cdot B_{in} = (A \oplus B)' B_{in}$
3. **Combining Borrows:**
   - $B_{out} = B_1 + B_2 = A'B + (A \oplus B)' B_{in}$
   - Since $B_1$ and $B_2$ are mutually exclusive ($B_1 \cdot B_2 = 0$), the OR gate can also be replaced by an XOR gate without changing functionality.

---

## 4. Adder vs. Subtractor: The Master Comparison

The only difference between an adder and a subtractor in algebraic form is the **inversion of input $A$** on the borrow logic.

| Parameter | Full Adder (FA) | Full Subtractor (FS) |
| :--- | :--- | :--- |
| **Sum / Difference** | $S = A \oplus B \oplus C_{in}$ | $D = A \oplus B \oplus B_{in}$ |
| **Minterms of $S$ / $D$** | $\sum m(1, 2, 4, 7)$ | $\sum m(1, 2, 4, 7)$ |
| **Carry / Borrow Out** | $C_{out} = AB + (A \oplus B)C_{in}$ | $B_{out} = A'B + (A \oplus B)' B_{in}$ |
| **Minterms of $C_{out}$ / $B_{out}$** | $\sum m(3, 5, 6, 7)$ | $\sum m(1, 2, 3, 7)$ |
| **Basic Components** | $2 \text{ HA} + 1 \text{ OR}$ | $2 \text{ HS} + 1 \text{ OR}$ |
| **Min 2-input NAND Gates** | **9** | **9** |
| **Min 2-input NOR Gates** | **9** | **9** |

---

## 5. Universal Gate Memory Anchor (The "5 and 9" Rule)

Every basic adder and subtractor follows the exact same pattern:

```
          ┌───────────────┬────────────────┐
          │  Half (HA/HS) │  Full (FA/FS)  │
┌─────────┼───────────────┼────────────────┤
│  NAND   │       5       │       9        │
│  NOR    │       5       │       9        │
└─────────┴───────────────┴────────────────┘
```

- **Half Anything (HA or HS):** Always **5** gates.
- **Full Anything (FA or FS):** Always **9** gates.
- **Why borrow has $(A \oplus B)'$ instead of $(A \oplus B)$:** The second half subtractor negates its minuend, which is $D_1 = (A \oplus B)$, producing $(A \oplus B)' B_{in} = (A \odot B) B_{in}$.