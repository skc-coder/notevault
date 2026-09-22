> [!definition]
> **Error Control** encompasses mechanisms to detect and correct bit errors introduced by channel noise during frame transmission[cite: 2]. The number of corrupted bits is directly proportional to transmission speed and disturbance interval[cite: 2]:
> $$\text{Corrupted Bits} = \text{Data Rate (bps)} \times \text{Noise Duration (s)}$$

> [!revision] Revision
> > Let $d_{\min}$ denote the minimum Hamming distance across all valid codewords in a code system:
> 1. **Detection Invariant:** To detect up to $d$ bit errors, the minimum Hamming distance must satisfy[cite: 2]:
>    $$d_{\min} \ge d + 1$$
> 2. **Correction Invariant:** To correct up to $t$ bit errors, the minimum Hamming distance must satisfy[cite: 2]:
>    $$d_{\min} \ge 2t + 1$$

| Technique              | Detection Capability                                                           | Correction Capability                                                         | Overhead                                                |
| :--------------------- | :----------------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :------------------------------------------------------ |
| **Simple Parity (1D)** | Detects all single-bit & odd-numbered bit errors[cite: 1, 2]                   | None (cannot localize error)[cite: 1, 2]                                      | 1 extra bit per word [cite: 2]                          |
| **2D Parity**          | Detects all 1-bit, 2-bit, and 3-bit errors; some $\ge 4$-bit patterns[cite: 2] | Corrects all single-bit errors (row $\cap$ column intersection)[cite: 2]      | $R + C + 1$ bits per $R \times C$ data block[cite: 2]   |
| **Checksum**           | Detects single & odd-bit errors, most burst patterns[cite: 1]                  | None[cite: 1, 2]                                                              | 16 bits standard (1's complement sum)[cite: 2]          |
| **CRC**                | Detects all single, double, odd errors, and bursts $\le k-1$ bits[cite: 1, 2]  | Capable (computationally expensive, generally used for detection)[cite: 1, 2] | $k-1$ bits for degree-$k$ generator[cite: 2]            |
| **[[Hamming Code]]**   | Detects up to 2-bit errors ($d_{\min} \ge 3$)[cite: 2]                         | Corrects single-bit error ($t=1$)[cite: 1, 2]                                 | $r$ parity bits satisfying $m + r + 1 \le 2^r$[cite: 2] |

> [!revision] Revision
> **Hamming Code Redundancy Equation:**  
> For $m$ data bits and $r$ redundancy/parity bits[cite: 2]:
> $$m + r + 1 \le 2^r$$
> Total codeword length $n = m + r$[cite: 2].

> [!trap]
> A simple parity check detects **only** an odd number of bit inversions[cite: 1, 2]. If an even number of bits (e.g., 2 bits, 4 bits) are simultaneously inverted, the parity bit remains identical, creating an undetected transmission error[cite: 1, 2].

> [!question]
> **Q:** If a communication system transmits 7 data bits, what is the minimum number of parity bits required to correct a single-bit error using standard Hamming code?  
> (A) 3  
> (B) 4  
> (C) 5  
> (D) 8  
>
> **Answer:** **(B)**  
> **Explanation:**  
> Substitute $m = 7$ into the bound $m + r + 1 \le 2^r$[cite: 2]:  
> - For $r = 3$: $7 + 3 + 1 = 11 \le 2^3 = 8$ (False)  
> - For $r = 4$: $7 + 4 + 1 = 12 \le 2^4 = 16$ (True)  
> Thus, $r_{\min} = 4$ check bits[cite: 2].
