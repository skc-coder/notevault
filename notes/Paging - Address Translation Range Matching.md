### Common Page Table Entry Sharing
Given a $2$-level page table system:
* $\text{VAS} = 42\text{ bits}$, $\text{PAS} = 40\text{ bits}$
* $\text{PTE} = 2^3\text{ B} = 8\text{ B}$, $\text{Page Size} = 2^{16}\text{ B} = 64\text{ KB}$, $\text{Chunk Size} = 2^{16}\text{ B}$
* Find the range of Logical Addresses that share the same first-level (outer) page table entry as $\mathtt{0x00123456789}$.

Derivations:
1. **Address Split**:
   * $\text{Offset } d = 16\text{ bits}$
   * $\text{Entries per page} = \frac{2^{16}\text{ B}}{2^3\text{ B}} = 2^{13}\text{ entries} \implies p_1 = 13\text{ bits}$
   * Outer level bits $p_2 = 42 - (13 + 16) = 13\text{ bits}$
   $$\text{Address Split: } [p_2: 13\text{ bits} \mid p_1: 13\text{ bits} \mid d: 16\text{ bits}]$$

2. **Outer Table Match Condition**:
   * Any address that shares the same first-level entry must have the identical upper $13$ bits ($p_2$).
   * The remaining lower $13 + 16 = 29\text{ bits}$ can range from all $0\text{s}$ to all $1\text{s}$.
   * Inspecting the $42$-bit address $\mathtt{0x00123456789}$:
     $$\text{Hex representation of upper bits: } \mathtt{0x0012\dots} \text{ to } \mathtt{0x0013\dots}$$
     The lower $29$ bits vary across $[0,\; 2^{29}-1]$, spanning from $\mathtt{0x00120000000}$ to $\mathtt{0x0013FFFFFFF}$.

3. **Second-Level (Inner Table) Match Condition**:
   * Sharing both Level 2 and Level 1 entries requires the upper $13 + 13 = 26\text{ bits}$ to be identical.
   * Only the lower $16$ offset bits vary:
     $$\text{Range: } \mathtt{0x00123450000} \text{ to } \mathtt{0x0012345FFFF}$$
