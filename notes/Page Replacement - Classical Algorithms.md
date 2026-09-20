> [!definition] Page Replacement Algorithm
> When physical memory is saturated and a page fault occurs, a page replacement algorithm decides which existing physical frame (the victim page) must be evicted to secondary storage to make room for the newly requested page[cite: 3].
> * **Objective**: Minimize the total number of page faults across the life of the process[cite: 3].

> [!theorem] Optimal Page Replacement (OPT / Belady's Optimal)
> Evict the page that will **not be used for the longest period of time in the future**[cite: 3].
> * Provides the absolute theoretical minimum page faults[cite: 3].
> * **Practical Limitation**: Impossible to implement in general-purpose operating systems because it requires perfect future knowledge of memory references; used as a benchmark for comparison[cite: 3].

> [!question] Optimal Algorithm Walkthrough
> * Frames: $4$ frames[cite: 3]
> * Reference String: $1,\; 2,\; 3,\; 4,\; 1,\; 2,\; 5,\; 1,\; 2,\; 3,\; 4,\; 5$[cite: 3]
> 
> Frame Trace:
> 1. Ref $1 \implies$ $[1, -, -, -]$ $\to$ **PF (1)**[cite: 3]
> 2. Ref $2 \implies$ $[1, 2, -, -]$ $\to$ **PF (2)**[cite: 3]
> 3. Ref $3 \implies$ $[1, 2, 3, -]$ $\to$ **PF (3)**[cite: 3]
> 4. Ref $4 \implies$ $[1, 2, 3, 4]$ $\to$ **PF (4)**[cite: 3]
> 5. Ref $1 \implies$ $[1, 2, 3, 4]$ $\to$ Hit[cite: 3]
> 6. Ref $2 \implies$ $[1, 2, 3, 4]$ $\to$ Hit[cite: 3]
> 7. Ref $5 \implies$ Future accesses: $1$ (at 8), $2$ (at 9), $3$ (at 10), $4$ (at 11). Page $4$ is used furthest in future $\implies$ Evict $4$ $\implies$ $[1, 2, 3, 5]$ $\to$ **PF (5)**[cite: 3]
> 8. Ref $1 \implies$ Hit[cite: 3]
> 9. Ref $2 \implies$ Hit[cite: 3]
> 10. Ref $3 \implies$ Hit[cite: 3]
> 11. Ref $4 \implies$ Future access: $5$. Evict $3$ (or $1$/$2$) $\implies$ $[1, 2, 4, 5]$ $\to$ **PF (6)**[cite: 3]
> 12. Ref $5 \implies$ Hit[cite: 3]
> 
> Total Page Faults $= \mathbf{6}$ (Theoretical Minimum)[cite: 3].

> [!definition] First-In First-Out (FIFO)
> Evicts the page that was brought into physical memory earliest (the oldest loaded page), regardless of how frequently or recently it was accessed[cite: 4].
> * Tracked easily using a FIFO queue[cite: 4].

> [!definition] Least Recently Used (LRU)
> Evicts the page that has not been referenced for the longest period in past time[cite: 4].
> * Implemented via counters or doubly-linked stacks updated on every memory reference[cite: 4].
> * Optimal backward approximation of OPT[cite: 3, 4].

> [!definition] Least Frequently Used (LFU)
> Associates an access counter with each page frame, incremented on every reference[cite: 4].
> * Evicts the page with the smallest reference count[cite: 4].

> [!question] FIFO vs. LRU Comparison Trace
> Reference String: $1,\; 2,\; 3,\; 4,\; 1,\; 2,\; 5,\; 1,\; 2,\; 3,\; 4,\; 5$ ($4$ Frames)[cite: 4]
> 
> **FIFO Trace**:
> 1. Refs $1, 2, 3, 4 \implies [1, 2, 3, 4]$ $\to$ $4$ PFs[cite: 4]
> 2. Refs $1, 2 \implies$ Hits[cite: 4]
> 3. Ref $5 \implies$ Oldest is $1 \implies$ Replace $1 \to [5, 2, 3, 4]$ $\to$ **PF (5)**[cite: 4]
> 4. Ref $1 \implies$ Oldest is $2 \implies$ Replace $2 \to [5, 1, 3, 4]$ $\to$ **PF (6)**[cite: 4]
> 5. Ref $2 \implies$ Oldest is $3 \implies$ Replace $3 \to [5, 1, 2, 4]$ $\to$ **PF (7)**[cite: 4]
> 6. Ref $3 \implies$ Oldest is $4 \implies$ Replace $4 \to [5, 1, 2, 3]$ $\to$ **PF (8)**[cite: 4]
> 7. Ref $4 \implies$ Oldest is $5 \implies$ Replace $5 \to [4, 1, 2, 3]$ $\to$ **PF (9)**[cite: 4]
> 8. Ref $5 \implies$ Oldest is $1 \implies$ Replace $1 \to [4, 5, 2, 3]$ $\to$ **PF (10)**[cite: 4]
> Total FIFO Page Faults with $4$ frames $= \mathbf{10}$[cite: 4].
> 
> **LRU Trace**:
> 1. Refs $1, 2, 3, 4 \implies [1, 2, 3, 4]$ $\to$ $4$ PFs[cite: 4]
> 2. Refs $1, 2 \implies$ Hits (Updates recent order: $3, 4, 1, 2$)[cite: 4]
> 3. Ref $5 \implies$ LRU page is $3 \implies$ Replace $3 \to [1, 2, 5, 4]$ $\to$ **PF (5)**[cite: 4]
> 4. Refs $1, 2 \implies$ Hits (Recent order: $4, 5, 1, 2$)[cite: 4]
> 5. Ref $3 \implies$ LRU page is $4 \implies$ Replace $4 \to [1, 2, 5, 3]$ $\to$ **PF (6)**[cite: 4]
> 6. Ref $4 \implies$ LRU page is $5 \implies$ Replace $5 \to [1, 2, 4, 3]$ $\to$ **PF (7)**[cite: 4]
> 7. Ref $5 \implies$ LRU page is $1 \implies$ Replace $1 \to [5, 2, 4, 3]$ $\to$ **PF (8)**[cite: 4]
> Total LRU Page Faults with $4$ frames $= \mathbf{8}$[cite: 4].
