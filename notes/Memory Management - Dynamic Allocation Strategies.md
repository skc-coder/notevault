> [!definition] Heap Dynamic Storage Allocation
> During runtime, memory requests (`malloc()` / `free()`) allocate and deallocate variable-sized memory segments dynamically in heap memory, creating alternating allocated regions and free holes[cite: 7].
> * These placement strategies are equally applicable to variable-sized physical partitioning and pure segmentation[cite: 7].

> [!theorem] Comparison of Placement Strategies
> 1. **First-Fit**: Search the free list from the beginning; allocate the **first available hole** that is large enough[cite: 7].
>    * Fast and simple[cite: 7].
> 2. **Next-Fit**: Same as First-Fit, but searches the free list starting from the location of the **last allocation pointer/hole**, wrapping around[cite: 7].
> 3. **Best-Fit**: Searches the entire free list to find the **smallest hole that is large enough** to satisfy the request[cite: 7].
>    * Minimizes leftover residue per allocation, but creates tiny, unusable residual holes[cite: 7, 8].
>    * Can stop search early if an exact size match is discovered[cite: 7].
> 4. **Worst-Fit**: Searches the entire free list to find the **largest available hole**[cite: 7].
>    * Leaves the largest possible remaining hole, preventing small unusable fragments[cite: 7].

> [!theorem] Relative Performance and Fragmentation Properties
> * **Empirical Performance**: First-fit and Best-fit consistently outperform Worst-fit in terms of both execution speed and storage utilization[cite: 7]. First-fit is typically faster than Best-fit[cite: 8].
> * **Internal Fragmentation**: Best-fit minimizes internal fragmentation within partitions, but cannot completely avoid it[cite: 8].
> * **External Fragmentation**: Both First-fit and Best-fit suffer from external fragmentation over continuous runtime[cite: 8].

> [!question] GATE CSE 2015: Best-Fit Memory Placement Trace
> Given memory partitions in order:
> $$200\text{ KB},\; 400\text{ KB},\; 600\text{ KB},\; 500\text{ KB},\; 300\text{ KB},\; 250\text{ KB}$$[cite: 7]
> Four process requests arrive in order:
> $$357\text{ KB},\; 210\text{ KB},\; 468\text{ KB},\; 491\text{ KB}$$[cite: 7]
> Using **Best-Fit**, determine which partitions remain unused[cite: 7].
> 
> **Trace**:
> 1. Request $357\text{ KB}$:
>    * Candidate holes: $400, 600, 500$[cite: 7].
>    * Smallest sufficient hole $= 400\text{ KB}$ $\implies$ Allocated to $400\text{ KB}$[cite: 7].
> 2. Request $210\text{ KB}$:
>    * Candidate holes: $250, 300, 500, 600$[cite: 7].
>    * Smallest sufficient hole $= 250\text{ KB}$ $\implies$ Allocated to $250\text{ KB}$[cite: 7].
> 3. Request $468\text{ KB}$:
>    * Candidate holes: $500, 600$[cite: 7].
>    * Smallest sufficient hole $= 500\text{ KB}$ $\implies$ Allocated to $500\text{ KB}$[cite: 7].
> 4. Request $491\text{ KB}$:
>    * Candidate holes: $600$[cite: 7].
>    * Smallest sufficient hole $= 600\text{ KB}$ $\implies$ Allocated to $600\text{ KB}$[cite: 7].
> 
> Unused Partitions: $\mathbf{200\text{ KB}}$ and $\mathbf{300\text{ KB}}$[cite: 7].
