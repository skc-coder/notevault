> [!formula] EMAT Computational Approaches (Without Page Faults)
> Let $t_{tlb}$ be TLB search latency, $m$ be physical memory access time, and $h$ be TLB hit ratio[cite: 6].
> 
> * **Approach 1 (Hierarchical / Standard Textbooks)**:
>   Access TLB first; on miss, access page table in RAM, then access target data:
>   $$\text{EMAT} = h \cdot (t_{tlb} + m) + (1 - h) \cdot (t_{tlb} + m + m)$$[cite: 6]
>   $$\text{EMAT} = t_{tlb} + m + (1 - h) \cdot m$$[cite: 6]
> 
> * **Approach 2 (Strict Additive Decomposition)**:
>   $$\text{EMAT} = t_{tlb} + (1 - h) \cdot m_{\text{table}} + m_{\text{data}}$$[cite: 6]
>   *(Every access requires TLB check and the final operand memory access; intermediate page table access is incurred strictly on a miss)*[cite: 6].

> [!trap] TLB Hit Implies No Page Fault
> If a translation hits in the TLB, the target frame is definitively present in physical RAM; a **TLB hit cannot cause a page fault**[cite: 6, 8].
> A page fault can only occur following a TLB miss during the page table traversal in RAM[cite: 6, 8].

> [!question] GATE CSE 2014: Basic TLB EMAT
> Given:
> * TLB access time $t_{tlb} = 10\text{ ms}$ (or ns)[cite: 6]
> * Memory access time $m = 80\text{ ms}$ (or ns)[cite: 6]
> * TLB hit probability $h = 0.6$[cite: 6]
> * Assume no page faults[cite: 6].
> 
> $$\text{EMAT} = h(t_{tlb} + m) + (1 - h)(t_{tlb} + 2m)$$[cite: 6]
> $$\text{EMAT} = 0.6(10 + 80) + 0.4(10 + 160) = 0.6(90) + 0.4(170) = 54 + 68 = \mathbf{122\text{ ms}}$$[cite: 6]

> [!question] GATE IT 2004: Instruction Time with Page Fault Rate
> An instruction takes $i\text{ ms}$ to execute[cite: 6]. A page fault takes an additional $j\text{ ms}$[cite: 6].
> On average, a page fault occurs once every $k$ instructions[cite: 6].
> Determine the effective instruction execution time[cite: 6].
> 
> Derivation:
> * Page fault probability per instruction $= \frac{1}{k}$[cite: 6].
> * Added penalty per instruction $= \frac{1}{k} \cdot j = \frac{j}{k}$[cite: 6].
> $$\text{Effective Time} = \mathbf{i + \frac{j}{k}}$$[cite: 6]

> [!question] Comprehensive Multi-Tier EMAT (GATE CSE 2020 Variant)
> System Specifications:
> * Single-level page table resident in physical memory[cite: 7].
> * Address translation uses a TLB[cite: 7].
> * Memory access time ($m$) $= 100\text{ ns}$[cite: 7].
> * TLB access time ($t_{tlb}$) $= 20\text{ ns}$[cite: 7].
> * TLB hit ratio ($h$) $= 95\% = 0.95$[cite: 7].
> * Page fault rate ($f$) $= 10\% = 0.10$ (occurs strictly on a TLB miss)[cite: 7, 8].
> * Page transfer time to/from disk $= 5000\text{ ns}$[cite: 7].
> * Out of all replaced pages, $20\%$ are dirty ($p_{dirty} = 0.20$)[cite: 7].
> * TLB update time is negligible ($0\text{ ns}$)[cite: 7].
> 
> **Mathematical Derivation**:
> 1. **Page Fault Service Time ($\text{PFS}$)**:
>    * Clean victim ($80\%$): Read required page from disk $= 5000\text{ ns}$[cite: 7, 8].
>    * Dirty victim ($20\%$): Write dirty page to disk $+$ Read required page from disk $= 5000 + 5000 = 10{,}000\text{ ns}$[cite: 7, 8].
>    $$\text{PFS} = 5000 + 0.20 \times 5000 = 5000 + 1000 = 6000\text{ ns}$$[cite: 7]
> 
> 2. **Time on TLB Hit ($T_{hit}$)**:
>    $$T_{hit} = t_{tlb} + m = 20 + 100 = 120\text{ ns}$$[cite: 8]
> 
> 3. **Time on TLB Miss ($T_{miss}$)**:
>    On a TLB miss, we pay $t_{tlb} + m_{\text{table}}$ to inspect the page table in memory[cite: 8]:
>    * Case A: No Page Fault (Probability $= 1 - f = 0.90$):
>      Target data is accessed: $+ m_{\text{data}}$[cite: 8].
>      $$T_{\text{no\_pf}} = m_{\text{table}} + m_{\text{data}} = 100 + 100 = 200\text{ ns}$$[cite: 8]
>    * Case B: Page Fault (Probability $= f = 0.10$):
>      Incurs disk service penalty and instruction completion access[cite: 7, 8]:
>      $$T_{pf} = m_{\text{table}} + \text{PFS} + m_{\text{data}} = 100 + 6000 + 100 = 6200\text{ ns}$$[cite: 7, 8]
>    $$T_{miss} = t_{tlb} + \Big[ (0.90 \times 200) + (0.10 \times 6200) \Big]$$[cite: 8]
>    $$T_{miss} = 20 + [180 + 620] = 20 + 800 = 820\text{ ns}$$[cite: 8]
> 
> 4. **Effective Memory Access Time ($\text{EMAT}$)**:
>    $$\text{EMAT} = h \cdot T_{hit} + (1 - h) \cdot T_{miss}$$[cite: 8]
>    $$\text{EMAT} = (0.95 \times 120) + (0.05 \times 820) = 114 + 41 = \mathbf{155\text{ ns}}$$[cite: 8]
