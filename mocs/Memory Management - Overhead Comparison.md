> [!question] GATE IT 2006: Memory Overhead Comparison
> System Specifications:
> * Process workload profiles:
>   * $P_1$: Size $= 195\text{ KB}$, Number of segments $= 4$
>   * $P_2$: Size $= 254\text{ KB}$, Number of segments $= 5$
>   * $P_3$: Size $= 45\text{ KB}$, Number of segments $= 3$
>   * $P_4$: Size $= 364\text{ KB}$, Number of segments $= 8$
> * $\text{Page Size} = 1\text{ KB} = 2^{10}\text{ B}$
> * $\text{PTE Size} = 4\text{ B} = 2^2\text{ B}$
> * $\text{STE Size (Segment Table Entry)} = 8\text{ B} = 2^3\text{ B}$
> * $\text{Maximum Segment Size} = 256\text{ KB} = 2^{18}\text{ B}$
> 
> Let:
> * $P$ = Total storage overhead for **2-Level Paging**
> * $S$ = Total storage overhead for **Pure Segmentation**
> * $T$ = Total storage overhead for **Paged Segmentation** (Segmentation with Paging)
> 
> Find the relation between $P$, $S$, and $T$.

> [!theorem] Mathematical Derivation of Overheads
> **1. Calculation of $S$ (Pure Segmentation)**:
> * Total segments across all processes $= 4 + 5 + 3 + 8 = 20\text{ segments}$.
> * Segment Table Size $= \sum (\text{Number of Segments} \times \text{STE Size})$:
>   $$S = (4 \times 8) + (5 \times 8) + (3 \times 8) + (8 \times 8) = 32 + 40 + 24 + 64 = \mathbf{160\text{ Bytes}}$$
> 
> **2. Calculation of $P$ (2-Level Paging)**:
> * Assume chunk size for page table equals page size ($1\text{ KB}$).
> * Page capacity $= 1\text{ KB} / 4\text{ B} = 256\text{ PTEs/chunk}$.
> * Number of pages required per process:
>   * $P_1$ ($195\text{ KB}$): $195\text{ pages} \implies 1\text{ Level 1 chunk}$.
>   * $P_2$ ($254\text{ KB}$): $254\text{ pages} \implies 1\text{ Level 1 chunk}$.
>   * $P_3$ ($45\text{ KB}$): $45\text{ pages} \implies 1\text{ Level 1 chunk}$.
>   * $P_4$ ($364\text{ KB}$): $364\text{ pages} \implies 2\text{ Level 1 chunks}$ (since $364 > 256$).
> * Outer Level (Level 2) table: Requires $1$ chunk per process ($4 \times 1 = 4\text{ chunks}$).
> * Total chunks for $P_1 = 1 + 1 = 2$; $P_2 = 1 + 1 = 2$; $P_3 = 1 + 1 = 2$; $P_4 = 2 + 1 = 3$.
> * Total chunks $= 2 + 2 + 2 + 3 = 9\text{ chunks}$.
> * Each chunk is $1\text{ KB}$.
>   $$P = 9 \times 1\text{ KB} = \mathbf{9\text{ KB}} = 9216\text{ Bytes}$$
> 
> **3. Calculation of $T$ (Paged Segmentation)**:
> * Overhead includes: (Segment Tables) $+$ (Page Tables for each segment).
> * Segment Tables overhead $= S = 160\text{ Bytes}$.
> * Maximum segment size is $256\text{ KB}$. With $1\text{ KB}$ pages, each segment requires a page table capable of mapping up to $256\text{ pages}$ ($256 \times 4\text{ B} = 1024\text{ B} = 1\text{ KB}$).
> * Each active segment allocates its page table ($1\text{ KB}$ per segment):
>   * $P_1$: $4\text{ segments} \implies 4 \times 1\text{ KB} = 4\text{ KB}$
>   * $P_2$: $5\text{ segments} \implies 5 \times 1\text{ KB} = 5\text{ KB}$
>   * $P_3$: $3\text{ segments} \implies 3 \times 1\text{ KB} = 3\text{ KB}$
>   * $P_4$: $8\text{ segments} \implies 8 \times 1\text{ KB} = 8\text{ KB}$
> * Page Table overhead $= 4 + 5 + 3 + 8 = 20\text{ KB}$.
> * Total Overhead $T = 20\text{ KB} + 160\text{ B} = \mathbf{20640\text{ Bytes}}$.

> [!theorem] Final Order of Overhead
> Comparing values:
> $$S = 160\text{ B} \quad < \quad P = 9216\text{ B} \quad < \quad T = 20640\text{ B}$$
> $$\mathbf{S < P < T}$$
