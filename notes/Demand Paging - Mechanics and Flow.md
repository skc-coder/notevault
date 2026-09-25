## Demand Paging
In demand paging, pages are brought into physical main memory only when they are referenced (demanded) by the CPU during execution[cite: 1, 2].
* **Pure Demand Paging**: Execution starts with zero pages of the process in main memory; all pages reside initially on disk.
* Even if only a single page frame of memory is allocated, execution can proceed, bringing pages on demand.

## Page Fault Interrupt
When the CPU generates an address for a page that is marked invalid or absent from physical main memory, the hardware MMU triggers a special internal hardware trap/interrupt called a **Page Fault Interrupt**[cite: 2, 6].

### Complete Page Fault Handling Flow #revision
When a virtual address referencing an unmapped page is issued:
1. **Virtual Address Inspection**: CPU generates a virtual address $(\text{Page Number } p, \text{Offset } d)$[cite: 2, 6].
2. **Page Table Lookup**: The MMU checks the corresponding Page Table Entry (PTE). The valid/invalid bit is set to $0$ (Invalid/Not Present)[cite: 1, 2, 6].
3. **Trap to OS**: MMU issues a page fault interrupt, shifting control to the OS page fault handler routine[cite: 2, 6].
4. **Free Frame Check & Allocation**:
   * If a free frame exists in physical RAM, allocate it[cite: 3].
   * If no free frame exists, a **Page Replacement Algorithm** selects a victim page[cite: 3, 6].
5. **Dirty Bit Evaluation**: If the victim page's dirty (modified) flag is $1$ (True), write it back to secondary storage (disk); if $0$ (False), overwrite without disk write[cite: 3, 6].
6. **Invalidate Old Entry**: Mark the victim page's PTE as invalid and flush any matching TLB entries[cite: 3, 6].
7. **Disk I/O Transfer**: Bring the required page from disk into the allocated physical frame[cite: 2, 3, 6].
8. **Update PTE**: Write the new frame number into the PTE, set valid bit to $1$, and update TLB[cite: 1, 3, 6].
9. **Restart Instruction**: Return control to the user process and restart the faulting instruction from scratch[cite: 2, 6].

```mermaid
flowchart TD
    %% Node definitions
    CPU["CPU / Process"]
    MMU["Memory Management Unit (MMU)"]
    Trap["Page Fault Trap to OS Kernel"]
    Check{"3. Check Validity"}
    Terminate["Terminate Process<br/>(Segmentation Fault)"]
    FreeFrame["Find a Free Frame"]
    Disk[("Disk Storage")]
    ReadPage["4. Read Page from Disk"]
    UpdateTable["5. Update Page Table"]

    %% Flow connections
    CPU -->|"1. Access Page"| MMU
    MMU -->|"2. Page Not in Physical RAM"| Trap
    Trap --> Check
    Check -->|"Invalid"| Terminate
    Check -->|"Valid"| FreeFrame
    FreeFrame --> ReadPage
    Disk --> ReadPage
    ReadPage --> UpdateTable
    UpdateTable -->|"6. Restart Instruction"| CPU

    %% Styling
    classDef blueBox fill:#e1f0fa,stroke:#4a90e2,stroke-width:1.5px,color:#111;
    classDef greenBox fill:#e8f7ec,stroke:#52c41a,stroke-width:1.5px,color:#111;
    classDef yellowBox fill:#fefbe6,stroke:#fadb14,stroke-width:1.5px,color:#111;
    classDef redBox fill:#feebee,stroke:#f5222d,stroke-width:1.5px,color:#111;
    classDef grayBox fill:#f5f5f5,stroke:#8c8c8c,stroke-width:1.5px,color:#111;
    classDef purpleBox fill:#f3e8ff,stroke:#9254de,stroke-width:1.5px,color:#111;

    class CPU,UpdateTable blueBox;
    class MMU,FreeFrame greenBox;
    class Check yellowBox;
    class Terminate redBox;
    class Trap,Disk grayBox;
    class ReadPage purpleBox;
```