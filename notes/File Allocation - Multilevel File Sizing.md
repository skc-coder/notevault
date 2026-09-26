## Multilevel Inode File Sizing Derivations

> [!formula] General File Capacity Formula
> For a block size $B$ and disk pointer size $P$, the number of pointers per index block is:
> $$K = \frac{B}{P}$$[cite: 1]
> If an inode contains $D$ direct pointers, $S$ single indirect pointers, $DI$ double indirect pointers, and $TI$ triple indirect pointers, the maximum addressable file size is:
> $$\text{Max File Size} = \left( D + S \cdot K + DI \cdot K^2 + TI \cdot K^3 \right) \times B$$[cite: 1]

> [!question] Comprehensive Multilevel Inode Capacity
> Consider a file system with a block size of $2048\text{ B}$ ($2\text{ KB}$) and $32$-bit disk block addresses[cite: 1]. An inode contains:
> * $12$ direct pointers[cite: 1]
> * $1$ single indirect pointer[cite: 1]
> * $1$ double indirect pointer[cite: 1]
> * $1$ triple indirect pointer[cite: 1]
> 
> 1. What is the maximum disk partition size the file system can address[cite: 1]?
> 2. What is the maximum possible file size[cite: 1]?

### 1. Maximum Addressable Disk Partition Size

With $32$-bit disk block pointers, the system can address $2^{32}$ unique disk blocks[cite: 1]:

$$\text{Max Disk Size} = 2^{32} \times 2048\text{ B} = 2^{32} \times 2^{11}\text{ B} = 2^{43}\text{ B} = 8\text{ TB}$$
[cite: 1]

### 2. Maximum File Size Calculation

* Block size $B = 2048\text{ B} = 2^{11}\text{ B}$[cite: 1]
* Pointer size $P = 32\text{ bits} = 4\text{ B} = 2^2\text{ B}$[cite: 1]
* Number of pointers per index block:
  $$K = \frac{2048\text{ B}}{4\text{ B}} = 512 = 2^9\text{ pointers/block}$$
[cite: 1]

Capacity contribution by pointer level:
* **Direct Pointers ($12$)**:
  $$\text{Cap}_{\text{direct}} = 12 \times 2048\text{ B} = 24\text{ KB}$$
[cite: 1]
* **Single Indirect Pointer ($1$)**:
  $$\text{Cap}_{\text{single}} = 1 \times 512 \times 2048\text{ B} = 2^9 \times 2^{11}\text{ B} = 2^{20}\text{ B} = 1\text{ MB}$$
[cite: 1]
* **Double Indirect Pointer ($1$)**:
  $$\text{Cap}_{\text{double}} = 1 \times 512^2 \times 2048\text{ B} = 2^{18} \times 2^{11}\text{ B} = 2^{29}\text{ B} = 512\text{ MB}$$
[cite: 1]
* **Triple Indirect Pointer ($1$)**:
  $$\text{Cap}_{\text{triple}} = 1 \times 512^3 \times 2048\text{ B} = 2^{27} \times 2^{11}\text{ B} = 2^{38}\text{ B} = 256\text{ GB}$$
[cite: 1]

Summing the capacities:

$$\text{Max File Size} = 24\text{ KB} + 1\text{ MB} + 512\text{ MB} + 256\text{ GB} \approx 256.5\text{ GB}$$
[cite: 1]

> [!question] Algebraic Parameterized File Sizing
> Consider a file system with $512\text{ B}$ blocks[cite: 1]. The inode holds $N$ direct block pointers and $1$ single indirect pointer[cite: 1]. The single indirect block holds up to $M$ data block pointers[cite: 1]. Express the maximum file size[cite: 1].

$$\text{Total Data Blocks} = N + M$$
[cite: 1]
$$\text{Max File Size} = (N + M) \times 512\text{ Bytes}$$
[cite: 1]

> [!question] Comparative File Sizing Under Varied Schemes
> Assume a uniform block size of $4\text{ KB}$ ($2^{12}\text{ B}$) and pointer size of $4\text{ B}$ ($2^2\text{ B}$)[cite: 1]:
> 1. **Simple Direct Inode**: The inode has $10$ direct pointers and no indirect pointers[cite: 1].
> 2. **Extent-Based System**: The inode stores $1$ extent pointer with an $8$-bit length field specifying the run length in blocks[cite: 1].
> 3. **Indirection System**: The inode contains exactly $1$ direct, $1$ single indirect, and $1$ double indirect pointer[cite: 1].
> 
> Compute the maximum file size supported under each scheme[cite: 1].

1. **Simple Direct**:
   $$\text{Max Size} = 10 \times 4\text{ KB} = 40\text{ KB}$$
[cite: 1]
2. **Extent-Based**:
   An $8$-bit unsigned field represents a maximum length of $2^8 - 1 = 255$ blocks[cite: 1]:
   $$\text{Max Size} = 255 \times 4\text{ KB} = 1020\text{ KB}$$
[cite: 1]
3. **Indirection System**:
   Pointers per block $K = \frac{4\text{ KB}}{4\text{ B}} = 1024 = 2^{10}$[cite: 1].
   $$\text{Max Blocks} = 1 + 2^{10} + 2^{20}$$
[cite: 1]
   $$\text{Max Size} = (1 \times 4\text{ KB}) + (1024 \times 4\text{ KB}) + (1024^2 \times 4\text{ KB})$$
[cite: 1]
   $$\text{Max Size} = 4\text{ KB} + 4\text{ MB} + 4\text{ GB} \approx 4.004\text{ GB}$$
[cite: 1]

> [!theorem] Factors Dictating Maximum File Size (GATE CS 2002)
> In an indexed allocation scheme, the maximum supported file size depends strictly on:
> 1. Size of a disk block[cite: 1]
> 2. Number of block pointers per index block (governed by block size and pointer size)[cite: 1]
> 3. Size and type of block pointers (direct vs. multilevel indirect)[cite: 1]
