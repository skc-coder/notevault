# Foolproof Memory Blueprint: Full Adder Equations & Gate Counts

---

## 1. Why $C_{out} = AB + (A \oplus B)C_{in}$ Makes Total Intuitive Sense

Do not memorize this like a formula; understand the **two conditions that can ever generate a carry** when adding three bits ($A, B, C_{in}$):

1. **Direct Generation:** If both $A$ and $B$ are $1$, they immediately create a carry regardless of what $C_{in}$ is.
   $$\text{Term } 1 = AB$$
2. **Passed-Through Carry:** If exactly one of $A$ or $B$ is $1$ (which is $A \oplus B$), and an incoming carry arrives ($C_{in} = 1$), their sum becomes $1 + 1 = 2$, which pushes a new carry forward.
   $$\text{Term } 2 = (A \oplus B)C_{in}$$

Either scenario creates a carry:
$$C_{out} = AB + (A \oplus B)C_{in}$$

### 10-Second Algebraic Proof (If you ever doubt it in an exam):
Expand the XOR term:
$$(A \oplus B)C_{in} = (A'B + AB')C_{in} = A'B C_{in} + AB' C_{in}$$
Add $AB$:
$$C_{out} = AB + A'BC_{in} + AB'C_{in}$$
Using Boolean absorption ($AB = AB + ABC_{in}$):
$$C_{out} = AB + BC_{in}(A' + A) = AB + BC_{in} + AC_{in}$$

---

## 2. The "2 HA + 1 OR" Architecture

A **Half Adder (HA)** can only add **2 inputs** and produces:
- $\text{Sum} = X \oplus Y$
- $\text{Carry} = X \cdot Y$

A **Full Adder (FA)** needs to add **3 inputs** ($A, B, C_{in}$):

1. **First Half Adder (HA 1):** Adds $A$ and $B$.
   - Outputs: $S_1 = A \oplus B$ and $C_1 = AB$
2. **Second Half Adder (HA 2):** Adds the intermediate sum $S_1$ with the third bit $C_{in}$.
   - Final Sum output: $S = S_1 \oplus C_{in} = (A \oplus B) \oplus C_{in}$
   - Second Carry output: $C_2 = S_1 \cdot C_{in} = (A \oplus B)C_{in}$
3. **The Final OR Gate:** Merges both carries.
   - $C_{out} = C_1 + C_2 = AB + (A \oplus B)C_{in}$

<Image src="image_agent_tag_175577372590200249" alt="Full Adder implementation using two Half Adders and one OR gate" caption="Full Adder from 2 HAs and 1 OR Gate" />

---

> **Why an OR gate instead of an XOR gate for combining carries?**
> $C_1$ ($AB$) and $C_2$ ($(A \oplus B)C_{in}$) are **mutually exclusive**. They can never be 1 at the same time because $A \oplus B = 1$ requires $A \neq B$, while $AB = 1$ requires $A = B = 1$. In digital logic, when two terms can never both be 1 ($X \cdot Y = 0$), **OR and XOR are identical**:
> $$C_1 + C_2 \equiv C_1 \oplus C_2$$

---

## 3. The "5 and 9" Universal Gate Number Trick

Exam questions repeatedly ask for the minimum number of NAND or NOR gates for Half and Full Adders. Remember this single ascending sequence:

$$\mathbf{5 \to 9}$$

| Component | Minimum 2-input NAND gates | Minimum 2-input NOR gates |
| :--- | :---: | :---: |
| **Half Adder (HA)** | **5** | **5** |
| **Half Subtractor (HS)** | **5** | **5** |
| **Full Adder (FA)** | **9** | **9** |
| **Full Subtractor (FS)** | **9** | **9** |

### Why is it 9 and NOT 11? ($5 + 5 + 1 \neq 11$)

Many students make the mistake of calculating:
$$\text{HA}_1 (5) + \text{HA}_2 (5) + \text{OR Gate} (3) = 13 \text{ gates}$$
This is unoptimized. Here is where the savings happen:

1. A 2-input XOR gate built from NAND gates uses **4 NAND gates**.
2. Crucially, the internal NAND gate inside the XOR architecture generates the sub-expression $\overline{AB}$.
3. That means the carry term ($AB$) is already computed inside the XOR block—you get it **for free** without adding extra gates for the AND operation.
4. When cascading two such optimized XOR blocks:
   - HA 1 = 4 NANDs (producing $A \oplus B$ and internal $\overline{AB}$)
   - HA 2 = 4 NANDs (producing final Sum and internal $\overline{(A \oplus B)C_{in}}$)
   - Final stage to combine the carries into $C_{out}$ = **1 single NAND gate** (by De Morgan's: $\overline{\overline{AB} \cdot \overline{(A \oplus B)C_{in}}} = AB + (A \oplus B)C_{in}$)

$$4 + 4 + 1 = \mathbf{9 \text{ NAND Gates}}$$

By circuit duality, NOR gate synthesis follows the exact same symmetrical optimization:
$$\mathbf{9 \text{ NOR Gates}}$$

---

## The 3-Second Exam Recall Anchor

- **Carry Equation:** "Either both make a carry ($AB$), or one makes a carry that catches $C_{in}$ ($(A \oplus B)C_{in}$)."
- **Components:** $1 \text{ FA} = \mathbf{2} \text{ HA} + \mathbf{1} \text{ OR}$.
- **Gate Counts (NAND / NOR):**
  - **Half** = **5**
  - **Full** = **9**
  *(Adders and Subtractors have identical gate counts: 5 for Half, 9 for Full).*