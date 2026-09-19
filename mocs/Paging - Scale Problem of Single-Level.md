## The Scale Problem of Single-Level Paging

In modern 32-bit and 64-bit architectures, single-level paging tables become prohibitively large to store in contiguous physical memory:

Consider a 32-bit logical address space ($LA = 32\text{ bits}$), with standard $4\text{ KB}$ pages ($2^{12}\text{ B}$):
$$\text{Number of Pages} = \frac{2^{32}}{2^{12}} = 2^{20}\text{ pages}$$
Assuming each $\text{PTE} = 4\text{ Bytes}$:
$$\text{Page Table Size} = 2^{20} \times 4\text{ Bytes} = 4\text{ MB per process}$$

If an OS runs hundreds of active processes, hundreds of megabytes of physical RAM are wasted purely storing page tables. Moreover, because compilers separate code, stack, and heap across a vast sparse logical address range, most of those $2^{20}$ entries are marked invalid/empty.

> [!theorem] The Need for Multi-Level Paging
> Single-level page tables must be allocated contiguously in physical memory. When the table grows to multiple megabytes per process, allocating contiguous physical space for the table itself reintroduces the very contiguous-allocation problems paging was designed to solve. 
> 
> This necessitates **Multi-Level Paging**, where the page table itself is split into pages and dynamically allocated on demand.
