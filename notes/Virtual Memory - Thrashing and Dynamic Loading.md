> [!definition] Thrashing
> Thrashing is the pathological state where an operating system spends substantially more time swapping pages into and out of secondary storage (disk) than executing actual process instructions[cite: 8].
> * As the degree of multiprogramming increases beyond system capacity, CPU utilization collapses toward zero[cite: 8].

> [!theorem] Causes and Conditions of Thrashing
> 1. **Insufficient Physical Memory**: The physical RAM is too small to accommodate the active memory workloads of all scheduled processes[cite: 8].
> 2. **Locality Set Overflow**: Thrashing occurs when:
>    $$\sum_{i} \text{Size}(\text{Locality Set}_i) > \text{Total Physical Memory Frame Count}$$[cite: 8]
>    *(The sum of the working sets across all running processes exceeds total available RAM)*[cite: 8].
> 3. **Over-allocation**: Scheduling too many concurrent processes (excessive degree of multiprogramming)[cite: 8].
> 4. **Mitigation**: Using priority or local page replacement algorithms, reducing the degree of multiprogramming, and maintaining working-set models[cite: 8].

```mermaid
flowchart LR
    A["Increasing Degree of Multiprogramming"] --> B["Active Pages Exceed Physical Memory"]
    B --> C["Continuous Page Faults"]
    C --> D["Disk Queue Saturated (Thrashing)"]
    D --> E["CPU Utilization Collapses to ~0%"]
```

> [!definition] Dynamic Loading
> In dynamic loading, software routines and library binaries are kept on secondary storage in a relocatable format and are loaded into physical main memory only when they are explicitly called during runtime[cite: 8].
> * **Primary Benefit**: Unused routines (e.g., extensive error-handling blocks) are never loaded into RAM, drastically saving main memory footprints on resource-constrained systems[cite: 8].
