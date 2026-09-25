Dynamically two types of memory are allocated; stack and heap.
But heap is tricky.

###### Heap Dynamic Storage Allocation
During runtime, memory requests (`malloc()` / `free()`) allocate and deallocate variable-sized memory segments dynamically in heap memory, creating alternating allocated regions and free holes[cite: 7].
* These placement strategies are equally applicable to variable-sized physical partitioning and pure segmentation[cite: 7].

###### Comparison of Placement Strategies
1. **First-Fit**: Search the free list from the beginning; allocate the **first available hole** that is large enough[cite: 7].
   * Fast and simple[cite: 7].
2. **Next-Fit**: Same as First-Fit, but searches the free list starting from the location of the **last allocation pointer/hole**, wrapping around[cite: 7].
3. **Best-Fit**: Searches the entire free list to find the **smallest hole that is large enough** to satisfy the request[cite: 7].
   * Minimizes leftover residue per allocation, but creates tiny, unusable residual holes[cite: 7, 8].
   * Can stop search early if an exact size match is discovered[cite: 7].
4. **Worst-Fit**: Searches the entire free list to find the **largest available hole**[cite: 7].
   * Leaves the largest possible remaining hole, preventing small unusable fragments[cite: 7].

###### Relative Performance and Fragmentation Properties
* **Empirical Performance**: First-fit and Best-fit consistently outperform Worst-fit in terms of both execution speed and storage utilization[cite: 7]. First-fit is typically faster than Best-fit[cite: 8].
* **Internal Fragmentation**: Best-fit minimizes internal fragmentation within partitions, but cannot completely avoid it[cite: 8].
* **External Fragmentation**: Both First-fit and Best-fit suffer from external fragmentation over continuous runtime[cite: 8].
