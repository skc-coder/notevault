**Hamming Code** is a linear error-correcting block code invented by Richard Hamming. It is primarily designed to **detect up to 2-bit errors** and **correct single-bit errors**.

  

### 1. Fundamental Principle: Parity Bits and Redundancy

A standard dataword of $m$ bits is transmitted by appending $r$ parity (redundant) bits, creating an $n$-bit codeword ($n = m + r$).

  

To correct a single-bit error, the number of parity bits $r$ must satisfy the **Hamming Rule**:

  

$$m + r + 1 \le 2^r$$

  

- **Why?**
    
      
    - There are $m + r$ possible bit positions where a single error can occur.
        
          
        
    - There is $1$ additional case where no error occurs at all.
        
          
        
    - Hence, the parity bits must be capable of representing at least $(m + r + 1)$ distinct states.
        
          
        
    - Since $r$ bits can produce $2^r$ states, $2^r \ge m + r + 1$.
        
          
        

### 2. Bit Positioning Architecture

Hamming codes strategically place the redundant parity bits in **powers-of-2 bit positions** (indexed 1-based from left to right or right to left; commonly left to right):

  

- **Parity Bit Positions:** $1, 2, 4, 8, 16, \dots, 2^{i}$
    
      
    
- **Data Bit Positions:** All remaining non-power-of-2 positions ($3, 5, 6, 7, 9, 10, 11, \dots$)
    
      
    

#### Bit Coverage Map (Parity Bit Sets)

Each parity bit $P_k$ checks every bit position whose binary representation has a `1` in the $k$-th power-of-2 position:

  

- **$P_1$ (checks bit positions with LSB $= 1$):** Checks positions $1, 3, 5, 7, 9, 11, \dots$
    
      
    
- **$P_2$ (checks bit positions with 2nd bit $= 1$):** Checks positions $2, 3, 6, 7, 10, 11, \dots$
    
      
    
- **$P_4$ (checks bit positions with 3rd bit $= 1$):** Checks positions $4, 5, 6, 7, 12, 13, 14, 15, \dots$
    
      
    
- **$P_8$ (checks bit positions with 4th bit $= 1$):** Checks positions $8, 9, 10, 11, 12, 13, 14, 15, \dots$
    
      
    

Each parity bit is chosen (typically using even parity) so that the modulo-2 sum (XOR) of its monitored bit set is `0`.

  

### 3. Worked Example: Generating a Hamming(7, 4) Code

Suppose we want to encode $4$ data bits ($m = 4$): `1 0 1 1`.

  

#### Step A: Determine Redundancy Bits ($r$)

$$4 + r + 1 \le 2^r \implies 5 + r \le 2^r$$

  

- For $r = 3$: $5 + 3 = 8 \le 2^3 = 8$ (Holds true!)
    
      
    
- Total codeword length $n = 4 + 3 = 7$ bits (known as the classic **Hamming(7, 4)** code).
    
      
    

#### Step B: Map Bits into Positions (1 to 7)

|**Position**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Bit Type**|$P_1$|$P_2$|$D_1$|$P_4$|$D_2$|$D_3$|$D_4$|
|**Value**|$?$|$?$|**1**|$?$|**0**|**1**|**1**|

#### Step C: Compute Even Parity for Each $P_k$

- **$P_1$ (Positions 1, 3, 5, 7):**
    
      
    
    $$P_1 \oplus D_1 \oplus D_2 \oplus D_4 = 0 \implies P_1 \oplus 1 \oplus 0 \oplus 1 = 0 \implies P_1 = 0$$
    
- **$P_2$ (Positions 2, 3, 6, 7):**
    
      
    
    $$P_2 \oplus D_1 \oplus D_3 \oplus D_4 = 0 \implies P_2 \oplus 1 \oplus 1 \oplus 1 = 0 \implies P_2 = 1$$
    
- **$P_4$ (Positions 4, 5, 6, 7):**
    
      
    
    $$P_4 \oplus D_2 \oplus D_3 \oplus D_4 = 0 \implies P_4 \oplus 0 \oplus 1 \oplus 1 = 0 \implies P_4 = 0$$
    

**Final Transmitted Codeword:**

  

`0 1 1 0 0 1 1`

  

### 4. How Error Detection and Correction Works (The Syndrome)

When the receiver gets the codeword, it recalculates parity checks across the same subsets. The result forms a binary number called the **Syndrome Vector** ($S = S_4 S_2 S_1$):

  

- $S_1 = \text{Bit}_1 \oplus \text{Bit}_3 \oplus \text{Bit}_5 \oplus \text{Bit}_7$
    
      
    
- $S_2 = \text{Bit}_2 \oplus \text{Bit}_3 \oplus \text{Bit}_6 \oplus \text{Bit}_7$
    
      
    
- $S_4 = \text{Bit}_4 \oplus \text{Bit}_5 \oplus \text{Bit}_6 \oplus \text{Bit}_7$
    
      
    

#### Interpreting the Syndrome

- **If $S = 000_2$ ($0_{10}$):** No bit error detected.
    
      
    
- **If $S \ne 000_2$:** The decimal value of the binary syndrome gives the **exact bit position** that was inverted!
    
      
    - _Example:_ If bit position 5 flips during transit, $S_1 = 1, S_2 = 0, S_4 = 1 \implies S = 101_2 = 5_{10}$.
        
          
        
    - The receiver simply inverts the bit at index $5$ to correct the error back to its original state.
        
          
        

### 5. Capabilities and Error Bounds

- **Minimum Hamming Distance ($d_{\min}$):** Standard Hamming code has $d_{\min} = 3$.
    
      
    - **Detection:** $d_{\min} \ge d + 1 \implies d = 3 - 1 = 2$ bits detected.
        
          
        
    - **Correction:** $d_{\min} \ge 2t + 1 \implies 2t \le 2 \implies t = 1$ bit corrected.
        
          
        
- **SECDED (Single Error Correction, Double Error Detection):**
    
      
    
    By appending one extra overall parity bit to the entire codeword (increasing $d_{\min}$ to $4$), the system can simultaneously correct any 1-bit error and reliably detect 2-bit errors without falsely miscorrecting them. This variation is standard in ECC (Error-Correcting Code) computer RAM.