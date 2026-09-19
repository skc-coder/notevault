A Page Table is indexed by the Page Number ($p$). Each entry is called a **Page Table Entry (PTE)**.

| Frame Number ($f$) | Valid / Invalid Bit | Protection Bits | Reference Bit | Dirty Bit |
| :---: | :---: | :---: | :---: | :---: |
| $(m - k)$ bits | Present Bit ($1/0$) | Access ($R/W/X$) | Accessed Bit | Modified Bit |

* **Frame Number ($f$):** The base address bits of physical memory where the page resides. The minimum size of this field is $\lceil \log_2(\text{Number of Frames}) \rceil = (m - k)\text{ bits}$.
* **Valid / Invalid Bit (Present Bit):** Indicates whether the page is currently loaded in Main Memory ($1$) or still on secondary storage / unallocated ($0$).
* **Protection Bits:** Enforce access control ($R, W, X$).
* **Reference Bit (Accessed Bit):** Set by hardware whenever the page is read or written (used by page replacement algorithms like Clock/LRU).
* **Dirty Bit (Modified Bit):** Set by hardware whenever a write access modifies the page contents in memory (indicates the page must be written back to disk on eviction).

> [!trap] Minimum PTE Size vs. Real-World Alignment
> While the theoretical minimum bits required for a PTE is the number of bits needed to index all frames ($m - k$), in actual operating systems:
> $$\text{PTE Size} \ge (m - k) + \text{Control Bits}$$
> Furthermore, memory controllers require PTE sizes to be rounded up to byte-aligned or power-of-two boundaries (e.g., $2\text{ Bytes}$, $4\text{ Bytes}$, or $8\text{ Bytes}$).
> 
> $$\text{Page Table Size} = (\text{Number of Pages}) \times (\text{PTE Size}) = 2^{n-k} \times \text{PTE Size}$$
