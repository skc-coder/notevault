### Reducing Page Table Levels by Increasing Page Size
Given a system with:
* Virtual Address Space ($\text{VAS}$) = $48\text{ bits}$
* Physical Address Space ($\text{PAS}$) = $52\text{ bits}$
* Page Table Entry ($\text{PTE}$) size = $2^3\text{ B} = 8\text{ B}$
* Chunk Size at every level = Page Size (i.e., at every level, a page table chunk must fit exactly into a single page)
* Currently, a $4$-level page table scheme is used.

If the page size is increased, the number of levels can be reduced. Determine the page size required if we want to reduce the translation hierarchy to exactly **$2$ levels**.

> [!formula] Level Constraints for $k$-Level Paging
> Let the page size be $2^p\text{ B}$ (where offset $d = p\text{ bits}$).
> * Number of entries fitting into one page-sized chunk:
>   $$\text{Entries per chunk} = \frac{\text{Page Size}}{\text{PTE Size}} = \frac{2^p\text{ B}}{2^3\text{ B}} = 2^{p - 3}\text{ entries}$$
> * Bits allocated to index any intermediate/inner level chunk:
>   $$\text{Index bits per level} = \log_2(2^{p - 3}) = (p - 3)\text{ bits}$$
> * For a $2$-level page table hierarchy, the Virtual Address comprises:
>   * Level 2 (Outer) index bits: at most $(p - 3)$ bits (to fit into one page frame)
>   * Level 1 (Inner) index bits: $(p - 3)$ bits
>   * Page offset: $p$ bits

> [!theorem] Algebraic Derivation of Required Page Size
> Setting the sum of the components equal to the total Virtual Address width:
> $$(p - 3) + (p - 3) + p = 48$$
> $$3p - 6 = 48$$
> $$3p = 54 \implies p = 18$$
> 
> Therefore:
> * $\text{Page Size} = 2^{18}\text{ B} = 256\text{ KB}$
> * Resulting Address Split: $[15 \mid 15 \mid 18]$ bits.
> * Outermost level contains $2^{15}\text{ entries} \le 2^{15}\text{ capacity}$, thus fitting completely within a single page frame.
