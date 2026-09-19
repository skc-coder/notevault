> [!definition] Virtual Address Split
> In multilevel paging, the CPU-generated Virtual Address ($\text{VA}$) / Logical Address ($\text{LA}$) is partitioned into multiple index fields followed by a single within-page offset:
> $$\text{VA} = [p_k \mid p_{k-1} \mid \dots \mid p_1 \mid d]$$
> where each $p_i$ is an index into a page table chunk at level $i$, and $d$ is the page offset.

> [!formula] Virtual Address Partitioning
> For an address split across levels $k, k-1, \dots, 1$ and offset $d$:
> * $\text{Offset bits } d = \log_2(\text{Page Size})$
> * $\text{Entries per chunk at level } i = 2^{p_i}$
> * $\text{Number of chunks at level } i = \prod_{j=i+1}^{k} 2^{p_j} = 2^{\sum_{j=i+1}^k p_j}$
> * $\text{Total entries at level } i = (\text{Number of chunks}) \times (\text{Entries per chunk}) = 2^{\sum_{j=i}^k p_j}$

> [!question] Worked Walkthrough: 32-bit Logical Address Decomposition
> Consider a $32$-bit Virtual Address Space split as:
> 
> | Level 3 (Outer) | Level 2 | Level 1 | Level 0 (Offset / Inner) |
> | :--- | :--- | :--- | :--- |
> | $6\text{ bits}$ | $8\text{ bits}$ | $8\text{ bits}$ | $10\text{ bits}$ |
> 
> Detailed hierarchical derivation:
> * **Level 3 (Outermost)**:
>   * Number of entries per chunk: $2^6 = 64\text{ entries}$
>   * Total chunks: $1$
>   * Total entries: $2^6 = 64$
> * **Level 2**:
>   * Number of entries per chunk: $2^8 = 256\text{ entries}$
>   * Number of chunks: $2^6 = 64\text{ chunks}$
>   * Total entries: $2^6 \times 2^8 = 2^{14}\text{ entries}$
> * **Level 1**:
>   * Number of entries per chunk: $2^8 = 256\text{ entries}$
>   * Number of chunks: $2^{14} / 2^8 = 2^6 \times 2^8 = 2^{14} = 16384\text{ chunks}$
>   * Total entries: $2^{14} \times 2^8 = 2^{22}\text{ entries}$
> * **Level 0 (Data Pages)**:
>   * Page size (chunk size): $2^{10}\text{ B} = 1\text{ KB}$
>   * Total data pages: $2^{22}$
>   * Total addressable space: $2^{22} \times 2^{10}\text{ B} = 2^{32}\text{ B} = 4\text{ GB}$
