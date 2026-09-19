> [!definition] Paged Segmentation (Segmentation with Paging)
> Paged segmentation combines the logical convenience of segmentation (modular program units: code, data, stack) with the allocation efficiency of paging (eliminating external fragmentation).
> * The process is logically divided into variable-sized **Segments**.
> * Each segment is subsequently divided into fixed-size **Pages**.
> * Physical memory is partitioned into standard fixed-sized page frames.

> [!formula] Logical Address Decomposition in Paged Segmentation
> $$\text{Virtual Address} = [s \mid p \mid d]$$
> * $s$: Segment Number (indexes the Process Segment Table)
> * $p$: Page Number within the segment (indexes the Segment's Page Table)
> * $d$: Offset within the referenced page

```mermaid
flowchart TD
    VA["VA: [ Seg No (s) | Page No (p) | Offset (d) ]"]
    STBR["Segment Table Base Register"] --> ST["Segment Table"]
    VA -.->|Index s| ST
    ST -->|Yields Base of PT| PT["Page Table of Segment s"]
    VA -.->|Index p| PT
    PT -->|Yields Frame Number (f)| PA["Physical Address: [ Frame (f) | Offset (d) ]"]
    VA -.->|Offset d| PA
    PA --> RAM["Physical Memory (RAM)"]
```

> [!question] Sizing Calculations: Paged Segmentation
> System Details:
> * A task is divided into $4$ equal-sized segments.
> * The system maintains an $8$-entry page table for each individual segment.
> * Page Size $= 2\text{ KB} = 2^{11}\text{ B}$.
> 
> Calculations:
> 1. **Maximum size of each segment**:
>    $$\text{Max Seg Size} = \text{Entries per PT} \times \text{Page Size} = 8 \times 2\text{ KB} = \mathbf{16\text{ KB}}$$
> 2. **Maximum Logical Address Space for the task**:
>    $$\text{Max LAS} = \text{Total Segments} \times \text{Max Seg Size} = 4 \times 16\text{ KB} = \mathbf{64\text{ KB}}$$
