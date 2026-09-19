> [!theorem] Chunk Sizing Independence
> It is **not mandatory** that every chunk of a multilevel page table have a size equal to the physical page size. 
> * Chunks at different levels can have different sizes.
> * While standard system implementations set chunk size equal to physical page size for simplicity (so every chunk fits precisely into one page frame), this is an architectural choice, not a theoretical requirement.

> [!trap] Hard Partition Fallacy of Physical RAM
> Physical RAM does not have hardwired physical frame boundaries that permanently freeze chunk dimensions. If chunk size differs from the physical page size, physical memory is partitioned conceptually into frames conforming to the chunk size of that level. Consequently:
> * The number of bits required to specify a frame number depends on the chunk size at that particular level.
> * The number of bits for frame index is given by:
>   $$\text{Bits} = \log_2\left(\frac{\text{PAS}}{\text{Chunk Size}}\right)$$

### Analysis: 2-Level Paging with Equal Indexing Bits
System Parameters:
* $\text{VAS} = 32\text{ bits}$, $\text{PAS} = 32\text{ bits}$
* $\text{Page Size} = 4\text{ KB} = 2^{12}\text{ B}$
* $\text{Levels} = 2$
* $\text{Equal indexing bits used for Level 1 and Level 2}$
* $\text{PTE} = 4\text{ B}$

Calculations:
1. **Address Split**:
   $$\text{Offset } d = \log_2(4\text{ KB}) = 12\text{ bits}$$
   $$\text{Remaining bits} = 32 - 12 = 20\text{ bits}$$
   $$\text{Bits per level} = \frac{20}{2} = 10\text{ bits each}$$
   $$\text{Address Split: } [10 \mid 10 \mid 12]$$
2. **PTEs per page**:
   $$\text{Number of PTEs per page} = \frac{\text{Page Size}}{\text{PTE Size}} = \frac{2^{12}\text{ B}}{4\text{ B}} = 2^{10}\text{ entries}$$
3. **Extra bits available in PTE**:
   $$\text{Number of physical frames} = \frac{\text{PAS}}{\text{Page Size}} = \frac{2^{32}\text{ B}}{2^{12}\text{ B}} = 2^{20}\text{ frames}$$
   $$\text{Frame bits required} = 20\text{ bits}$$
   $$\text{PTE Size} = 4\text{ B} = 32\text{ bits}$$
   $$\text{Extra / Unused bits} = 32 - 20 = 12\text{ bits}$$
