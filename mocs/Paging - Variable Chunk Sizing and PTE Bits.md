> [!question] GATE CSE 2008 Variant: Frame Bits with Variable Chunk Sizes
> System Parameters:
> * $\text{VAS} = 32\text{ bits}$, $\text{PAS} = 36\text{ bits}$, $\text{Page Size} = 4\text{ KB} = 2^{12}\text{ B}$
> * $\text{PTE} = 4\text{ B} = 2^2\text{ B}$
> * A $3$-level page table hierarchy is used with the virtual address split: $[2 \mid 9 \mid 9 \mid 12]$
> * Question: What are the number of bits required to address the next level chunk/frame from Level 2, Level 1, and Level 0 respectively?
> 
> Detailed Mathematical Derivation:
> 1. **Chunk Sizes at each level**:
>    * Innermost Level (Data Pages): $\text{Size} = 2^{12}\text{ B}$
>    * Level 1 Page Table Chunk: Contains $2^9\text{ entries}$ of size $2^2\text{ B}$ each $\implies \text{Chunk Size} = 2^9 \times 2^2 = 2^{11}\text{ B}$
>    * Level 2 Page Table Chunk: Contains $2^9\text{ entries}$ of size $2^2\text{ B}$ each $\implies \text{Chunk Size} = 2^9 \times 2^2 = 2^{11}\text{ B}$
> 2. **Frame Bits Calculation**:
>    * **Level 2 Entries (Points to Level 1 chunk)**:
>      Level 1 chunks are of size $2^{11}\text{ B}$.
>      $$\text{Number of chunks/frames in physical memory} = \frac{\text{PAS}}{\text{Chunk Size}} = \frac{2^{36}\text{ B}}{2^{11}\text{ B}} = 2^{25}$$
>      $$\implies \mathbf{25\text{ bits}}$$
>    * **Level 1 Entries (Points to Level 0 chunk)**:
>      Level 0 chunks are of size $2^{11}\text{ B}$.
>      $$\text{Number of chunks/frames in physical memory} = \frac{\text{PAS}}{\text{Chunk Size}} = \frac{2^{36}\text{ B}}{2^{11}\text{ B}} = 2^{25}$$
>      $$\implies \mathbf{25\text{ bits}}$$
>    * **Level 0 Entries (Points to Target Data Frame)**:
>      Data pages are of size $2^{12}\text{ B}$.
>      $$\text{Number of data frames in physical memory} = \frac{\text{PAS}}{\text{Page Size}} = \frac{2^{36}\text{ B}}{2^{12}\text{ B}} = 2^{24}$$
>      $$\implies \mathbf{24\text{ bits}}$$
> 
> $$\text{Result: } (25,\; 25,\; 24)\text{ bits}$$

> [!trap] Why Store Frame Numbers Instead of Byte Addresses in PTE?
> Page table entries store physical **frame numbers** rather than complete physical **byte addresses**. 
> * Storing frame numbers allows the hardware MMU to replace the virtual page number with the physical frame number and directly append the unmodified page offset.
> * If raw byte addresses were stored, the MMU would need an addition operation $(\text{Base} + \text{Offset})$ rather than a concatenation, increasing hardware latency and complexity.
