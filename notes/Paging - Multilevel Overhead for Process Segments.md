### Process with Dispersed Segments Across Memory
System Specifications:
* $\text{PTE} = 2\text{ B} = 2^1\text{ B}$
* Address Split: $[p_3: 10\text{ bits} \mid p_2: 8\text{ bits} \mid p_1: 6\text{ bits} \mid d: 8\text{ bits}]$
* $\text{Page Size} = 2^8\text{ B} = 256\text{ B}$

Calculate the page table memory overhead for a process comprising three distinct, non-contiguous segments:
1. **Code Segment**: Size $= 48\text{ KB}$, starting at address $\mathtt{0x10000000}$.
2. **Data Segment**: Size $= 600\text{ KB}$, starting at address $\mathtt{0x80000000}$.
3. **Stack Segment**: Size $= 64\text{ KB}$, growing upward starting at address $\mathtt{0xF0000000}$.
*(Assume all segments are sufficiently far apart that they do not share any lower or intermediate level chunks)*.

> [!formula] Chunk Capacities Across Levels
> * **Innermost Level (Level 1)**: Index has $6\text{ bits} \implies 2^6 = 64\text{ entries/chunk}$.
> * **Intermediate Level (Level 2)**: Index has $8\text{ bits} \implies 2^8 = 256\text{ entries/chunk}$.
> * **Outermost Level (Level 3)**: Index has $10\text{ bits} \implies 2^{10} = 1024\text{ entries}$ ($1$ chunk).


> [!theorem] Step-by-Step Chunk Allocation Derivation
> **1. Code Segment ($48\text{ KB}$)**:
> * $\text{Useful pages} = \frac{48 \times 2^{10}\text{ B}}{2^8\text{ B}} = 48 \times 4 = 192\text{ pages}$ ($192\text{ entries needed}$).
> * Chunks needed at Level 1: $\lceil \frac{192}{64} \rceil = 3\text{ chunks}$.
> * Chunks needed at Level 2: These $3$ entries require $\lceil \frac{3}{256} \rceil = 1\text{ chunk}$.
> 
> **2. Data Segment ($600\text{ KB}$)**:
> * $\text{Useful pages} = \frac{600 \times 2^{10}\text{ B}}{2^8\text{ B}} = 600 \times 4 = 2400\text{ pages}$.
> * Chunks needed at Level 1: $\lceil \frac{2400}{64} \rceil = 37.5 \implies 38\text{ chunks}$.
> * Chunks needed at Level 2: These $38$ entries require $\lceil \frac{38}{256} \rceil = 1\text{ chunk}$.
> 
> **3. Stack Segment ($64\text{ KB}$)**:
> * $\text{Useful pages} = \frac{64 \times 2^{10}\text{ B}}{2^8\text{ B}} = 64 \times 4 = 256\text{ pages}$.
> * Chunks needed at Level 1: $\lceil \frac{256}{64} \rceil = 4\text{ chunks}$.
> * Chunks needed at Level 2: These $4$ entries require $\lceil \frac{4}{256} \rceil = 1\text{ chunk}$.
> 
> **4. Level 3 (Root Page Table)**:
> * Requires exactly $1\text{ chunk}$ permanently in RAM.
> 
> **Total Entries & Memory Footprint**:
> * Level 1 total entries: $(3 + 38 + 4) \times 64 = 45 \times 64 = 2880\text{ entries}$
> * Level 2 total entries: $(1 + 1 + 1) \times 256 = 3 \times 256 = 768\text{ entries}$
> * Level 3 total entries: $1 \times 1024 = 1024\text{ entries}$
> * Total Entries $= 2880 + 768 + 1024 = 4672\text{ entries}$
> * $\text{Total Size} = 4672 \times \text{PTE Size} = 4672 \times 2\text{ B} = \mathbf{9344\text{ Bytes}}$.
