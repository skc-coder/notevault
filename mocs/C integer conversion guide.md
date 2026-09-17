## 1. Core Principles

Integer conversions occur when assigning values across differing bit-widths or passing narrower integers to functions such as `printf`.

```mermaid
flowchart LR
    A["RHS (Source Value)"] --> B{"LHS vs RHS Width?"}
    B -- "Narrower LHS (W_dest < W_src)" --> C["Phase 1: Truncation ✂️<br>(Chop upper bits)"]
    B -- "Wider LHS (W_dest > W_src)" --> D["Phase 1: Extension 🏹<br>(Pad upper bits)"]
    C --> E["Memory Storage 📦<br>(N-bit representation)"]
    D --> E
    E --> F["Phase 2: Integer Promotion ⬆️<br>(to int / unsigned int)"]
    F --> G["Phase 3: printf Specifier 🖨️<br>(%d vs %u viewing lens)"]
````

## 2. Narrowing (Truncation) ✂️

### Hardware Invariant

- Truncation occurs when $W_{\text{dest}} < W_{\text{source}}$.
    
      
    
- Hardware mechanically preserves only the lowest $N$ bits ($N = W_{\text{dest}}$) and discards the upper bits.
    
      
    
- **Signedness of LHS and RHS has zero effect on the bit-slicing process.**
    
      
    

### The Math: Why Modulo $2^N$ Works

Any integer value can be expressed in terms of its power-of-2 components:

$$\text{value} = \sum_{k=0}^{M-1} b_k 2^k = \underbrace{\sum_{k=N}^{M-1} b_k 2^k}_{\text{Bits } \ge N \text{ (Multiples of } 2^N\text{)}} + \underbrace{\sum_{i=0}^{N-1} b_i 2^i}_{\text{Lower } N \text{ bits}}$$

Factoring out $2^N$:

  

$$\text{value} = 2^N \cdot D + L$$

Where:
- $D = \sum_{k=N}^{M-1} b_k 2^{k-N}$ (discarded upper bits)
- $L = \sum_{i=0}^{N-1} b_i 2^i$ (the retained lower $N$ bits)

Since hardware drops all bits at and above position $N$, the remaining value is:

$$L = \text{value} \pmod{2^N}$$

### Formulas: Evaluating the Truncated Pattern

For an $N$-bit destination container:

  

- **Unsigned Destination:**
        
    
    $$\text{Stored Value} = U = \text{value} \pmod{2^N}$$
    
- **Signed Destination (Two's Complement):**
    
    Check the MSB ($b_{N-1}$, which holds weight $2^{N-1}$):
    
      
    - If $U < 2^{N-1}$ (MSB $= 0$):
        
          
        
        $$\text{Stored Value} = +U$$
        
    - If $U \ge 2^{N-1}$ (MSB $= 1$):
        
          
        
        $$\text{Stored Value} = U - 2^N$$
        

#### Why $U - 2^N$?

In Two's Complement, the MSB carries a negative positional weight:

  

$$S = -b_{N-1}2^{N-1} + \sum_{i=0}^{N-2} b_i 2^i$$

The unsigned interpretation of those same bits is:

  

$$U = +b_{N-1}2^{N-1} + \sum_{i=0}^{N-2} b_i 2^i$$

Subtracting the two:

  

$$U - S = 2(b_{N-1}2^{N-1}) = b_{N-1}2^N$$

If $\text{MSB} = 1$, then $U - S = 2^N \implies S = U - 2^N$.

  

## 3. Widening (Extension) 🏹

### Hardware Invariant

- Extension occurs when $W_{\text{dest}} > W_{\text{source}}$.
    
      
    
- **Golden Rule:** Extension depends **strictly on the source type (RHS)**, never on the destination type (LHS).
    
      
    

|**Source Type (RHS)**|**Extension Method**|**Action**|**Value Impact**|
|---|---|---|---|
|**Signed**|Sign-Extension 🏹|Replicate source MSB into all upper bits|Preserves original signed numeric value|
|**Unsigned**|Zero-Extension 0️⃣|Pad all upper bit positions with `0`|Preserves original unsigned magnitude|

### The Extension Trap Table

|**Source**|**Assignment**|**Upper Bits Filled With**|**Resulting Bit Logic**|
|---|---|---|---|
|`signed char sc = -5;`|`unsigned int ui = sc;`|`1`s (Sign-extended)|Source is signed; sign-extends first, producing `0xFFFFFFFB` ($2^{32} - 5$).|
|`unsigned char uc = 251;`|`int si = uc;`|`0`s (Zero-extended)|Source is unsigned; zero-extends first, producing `0x000000FB` ($+251$).|

## 4. Variadic Promotion & Format Specifiers 🖨️

### Default Argument Promotion

When passing arguments narrower than `int` to `printf`:

  

- `signed char` / `short` $\xrightarrow{\text{Sign-extends}}$ `int` (32 bits)
    
      
    
- `unsigned char` / `unsigned short` $\xrightarrow{\text{Zero-extends}}$ `int` (32 bits)
    
      
    

### Specifier Interpretation

The format specifier does **not** convert bit representations; it merely reads the resulting 32-bit register pattern through a specific viewing lens:

  

- **`%d` Lens:** Evaluates the 32 bits as a **Two's Complement signed int**:
    
      
    
    $$\text{Printed} = \begin{cases} \text{Bits}_{32}, & \text{if bit 31} = 0 \\ \text{Bits}_{32} - 2^{32}, & \text{if bit 31} = 1 \end{cases}$$
    
- **`%u` Lens:** Evaluates the 32 bits as a **pure unsigned integer**:
    
      
    
    $$\text{Printed} = \text{Bits}_{32} \in [0,\; 2^{32} - 1]$$
    
- **`%x` Lens:** Displays raw hexadecimal representation without sign interpretation.
    
      
    

## 5. Summary Mental Algorithm

1. **Assignment (RHS $\to$ LHS):**
    
      
    - _Narrowing?_ Compute $U = \text{RHS} \pmod{2^{N_{\text{dest}}}}$. If LHS is signed and $U \ge 2^{N-1}$, value is $U - 2^N$.
        
          
        
    - _Widening?_ If RHS is signed $\to$ sign-extend. If RHS is unsigned $\to$ zero-extend.
        
          
        
2. **Promotion to `printf`:**
    
      
    - Is the variable type signed? $\to$ Sign-extend to 32 bits.
        
          
        
    - Is the variable type unsigned? $\to$ Zero-extend to 32 bits.
        
          
        
3. **Specifier (`%d` vs `%u`):**
    
      
    - Read the final 32-bit pattern as signed (`%d`) or unsigned (`%u`).
        
          
        

````

---

Now that you have this in your vault, let's test how this algorithm works under exam pressure:

Suppose we execute:
```c
short s = -1;
unsigned int u = (unsigned short)s;
printf("%u\n", u);
````

Using the step-by-step rules from the note, what decimal value will `%u` display?

# The Fundamental Two's Complement Identity: $U - S = 2^n$

## 1. Definitions 🏷️
For an $n$-bit binary pattern $b_{n-1} b_{n-2} \dots b_1 b_0$:

* **$U$ (Unsigned Value):** Every bit has a standard positive binary weight:
  $$U = \sum_{i=0}^{n-1} b_i 2^i = b_{n-1}2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i$$
* **$S$ (Signed Two's Complement Value):** The Most Significant Bit (MSB, $b_{n-1}$) serves as the sign bit with negative weight:
  $$S = -b_{n-1}2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i$$

---

## 2. Algebraic Derivation 🧮

Subtract the signed value $S$ from the unsigned value $U$:

$$
\begin{aligned}
U - S &= \left( b_{n-1}2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i \right) - \left( -b_{n-1}2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i \right) \\
&= b_{n-1}2^{n-1} - \left(-b_{n-1}2^{n-1}\right) \\
&= 2 \cdot \left(b_{n-1}2^{n-1}\right) \\
&= b_{n-1}2^n
\end{aligned}
$$

### The Two States:
* **Case 1: Positive Number ($\text{MSB } b_{n-1} = 0$)**
  $$U - S = 0 \implies U = S$$
  The bit pattern represents the exact same positive value in both systems.

* **Case 2: Negative Number ($\text{MSB } b_{n-1} = 1$)**
  $$U - S = 2^n \implies \begin{cases} S = U - 2^n \\ U = S + 2^n = 2^n - |S| \end{cases}$$

---

## 3. Modular Arithmetic & Hardware Intuition ⚙️

An $n$-bit register forms a finite cyclic ring modulo $2^n$:

$$2^n \equiv 0 \pmod{2^n}$$

Because overflowing past $2^n$ resets the counter to $0$:
1. A negative number $S$ is defined by the property: $S + |S| \equiv 0 \pmod{2^n}$.
2. Replacing $0$ with $2^n$:
   $$S + |S| = 2^n \implies U = 2^n - |S| = 2^n + S$$
3. Thus, hardware stores the unsigned pattern $U = 2^n + S$ directly in the register. Addition and subtraction hardware remain identical for both signed and unsigned values.

---

## 4. Practical Cheat Sheet 🚀

| Goal | Given | Formula | Condition |
| :--- | :--- | :--- | :--- |
| **Decode raw bits to signed** | Unsigned pattern $U$ | $S = U - 2^n$ | When $U \ge 2^{n-1}$ (MSB $= 1$) |
| **Encode negative integer to bits** | Signed value $S$ ($S < 0$) | $U = 2^n - \|S\|$ | Always |
| **Predict `%u` output for `%d` negative** | 32-bit signed value $S$ | Prints $2^{32} - \|S\|$ | Variable promoted/cast to unsigned |

---

## 5. Worked Examples 🔍

### Example A: 8-bit System ($n = 8$, $2^8 = 256$)
* Stored raw byte: `0xFB` $= 251_{10}$ (so $U = 251$).
* Since $251 \ge 128$, the MSB is $1$.
* Signed value:
  $$S = U - 2^8 = 251 - 256 = -5$$

### Example B: Truncating Negative Constants
* Truncate $-130$ into an 8-bit signed container:
  $$U = (-130) \pmod{256} = 256 - 130 = 126$$
* Since $126 < 128$, MSB is $0$:
  $$S = U = +126$$