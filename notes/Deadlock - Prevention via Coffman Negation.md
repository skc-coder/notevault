> [!theorem] Systematic Invalidation of the Four Conditions
> 
> ### 1. Attacking Mutual Exclusion
> * **Mechanism**: Make all resources fully shareable so multiple processes can read/access concurrently without waiting[cite: 1].
> * **Feasibility**: **Generally impossible**[cite: 1]. Intrinsically non-shareable hardware resources (printers, tape drives, audio speakers) cannot be accessed concurrently without corrupting output[cite: 1]. Spooling can decouple direct access for printers, but cannot be applied universally to all system devices[cite: 1].
> 
> ### 2. Attacking Hold and Wait
> Can be eliminated using two distinct operational protocols[cite: 1]:
> * **Protocol A (Hold but Never Wait)**: A process must request and be allocated all its required resources at once before starting execution[cite: 1]. If all resources cannot be allocated simultaneously, it waits without holding any resource[cite: 1].
>   * *Drawback*: Requires knowing all future resource requirements in advance; leads to extremely low resource utilization[cite: 1].
> * **Protocol B (Wait but Never Hold)**: A process can request resources only when it holds none[cite: 1]. If it holds resources and needs more, it must release all its currently held resources before making a new batch request[cite: 1].
>   * *Drawback*: Starvation is possible; highly inefficient[cite: 1].
> 
> ### 3. Attacking No Preemption
> * **Mechanism**: If a process holding resources requests another resource that cannot be immediately allocated, all resources currently held by this process are preempted forcibly[cite: 1].
> * **Feasibility**: **Not viable for arbitrary resources**[cite: 1]. Viable only for resources whose states can be saved and easily restored (such as CPU registers and memory pages)[cite: 1]. Preempting a printer midway through a print job renders output unusable[cite: 1].
> 
> ### 4. Attacking Circular Wait (Resource Ordering Protocol)
> * **Mechanism**: Impose a global total ordering on all resource types[cite: 1]. Define a one-to-one indexing function:
>   $$F: R \to \mathbb{N}$$[cite: 1]
> * **Rule**: A process can request an instance of resource type $R_j$ if and only if:
>   $$F(R_j) > F(R_i)$$[cite: 1]
>   where $R_i$ is the highest-indexed resource currently held by the process[cite: 1].
> * **Property**: Circular wait is mathematically impossible because a cycle would require an increasing sequence of integers to wrap around ($k_1 < k_2 < \dots < k_n < k_1$), a contradiction[cite: 1].
> * **Practicality**: Highly practical, easy to enforce, and widely implemented in system software[cite: 1].
