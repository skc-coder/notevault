> [!question] Comparative File Sizing Under Varied Schemes
> Assume a uniform block size of $4\text{ KB}$ ($2^{12}\text{ B}$) and pointer size of $4\text{ B}$ ($2^2\text{ B}$):
> 1. **Simple Direct Inode**: The inode has $10$ direct pointers and no indirect pointers.
> 2. **Extent-Based System**: The inode stores $1$ extent pointer with an $8$-bit length field specifying the run length in blocks.
> 3. **Indirection System**: The inode contains exactly $1$ direct, $1$ single indirect, and $1$ double indirect pointer.
> 
> Compute the maximum file size supported under each scheme.

1. **Simple Direct**:
   $$\text{Max Size} = 10 \times 4\text{ KB} = 40\text{ KB}$$

2. **Extent-Based**:
   An $8$-bit unsigned field represents a maximum length of $2^8 - 1 = 255$ blocks:
   $$\text{Max Size} = 255 \times 4\text{ KB} = 1020\text{ KB}$$

3. **Indirection System**:
   Pointers per block $K = \frac{4\text{ KB}}{4\text{ B}} = 1024 = 2^{10}$.
   $$\text{Max Blocks} = 1 + 2^{10} + 2^{20}$$

   $$\text{Max Size} = (1 \times 4\text{ KB}) + (1024 \times 4\text{ KB}) + (1024^2 \times 4\text{ KB})$$

   $$\text{Max Size} = 4\text{ KB} + 4\text{ MB} + 4\text{ GB} \approx 4.004\text{ GB}$$


> [!theorem] Factors Dictating Maximum File Size (GATE CS 2002)
> In an indexed allocation scheme, the maximum supported file size depends strictly on:
> 4. Size of a disk block
> 5. Number of block pointers per index block (governed by block size and pointer size)
> 6. Size and type of block pointers (direct vs. multilevel indirect)
