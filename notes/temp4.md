---
tags:
  - os
  - memory-management
  - emat
  - gate-cse
aliases:
  - Effective Memory Access Time
  - Unified EMAT
date_created: 2026-09-25
---
**Effective Memory Access Time (EMAT)** measures the weighted average access latency accounting for TLB search latency, cache hits/misses, page table walks, and page fault handling.
## Quick Summary Table

| Access Architecture           | Translation Latency Formula ($T_{\text{translation}}$)                                                                     |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **Hierarchical (Sequential)** | $T_{\text{tlb}} + m_{\text{tlb}} \cdot \big[ T_{\text{pt}} + p_{\text{fault}} \cdot \text{PFS} \big]$                      |
| **Simultaneous (Parallel)**   | $h_{\text{tlb}} \cdot T_{\text{tlb}} + m_{\text{tlb}} \cdot \big[ T_{\text{pt}} + p_{\text{fault}} \cdot \text{PFS} \big]$ |

*Note: For an $n$-level page table, $T_{\text{pt}} = n \times T_{\text{mem}}$ (or $n \times T_{\text{data}}$ if page table entries reside in cache).*

| Access Architecture           | Data Access Latency Formula ($T_{\text{data}}$)                                   |
| :---------------------------- | :-------------------------------------------------------------------------------- |
| **Hierarchical (Sequential)** | $T_{\text{cache}} + m_{\text{cache}} \cdot T_{\text{mem}}$                        |
| **Simultaneous (Parallel)**   | $h_{\text{cache}} \cdot T_{\text{cache}} + m_{\text{cache}} \cdot T_{\text{mem}}$ |

## 1. Generalized Multi-Level Recursive Rule

For an arbitrary $k$-level hierarchy $L_1, L_2, \dots, L_k$ at any level (multi-level TLBs, multi-tier page tables, or $L_1/L_2/L_3$ cache blocks):

$$\text{Latency}(L_i) = \begin{cases} 
T_i + m_i \cdot \text{Latency}(L_{i+1}) & \text{Hierarchical (Serial)} \\
h_i \cdot T_i + m_i \cdot \text{Latency}(L_{i+1}) & \text{Simultaneous (Parallel)} 
\end{cases}$$

---

## 2. The Unified Decomposition Principle

$$\mathbf{\text{EMAT} = T_{\text{translation}} + T_{\text{data}}}$$

> [!important] The Decoupling Invariant
> - **$T_{\text{translation}}$** accounts strictly for: TLB lookup $+$ (on TLB miss: Page Table Walk $+$ Page Fault penalty).
> - **$T_{\text{data}}$** accounts strictly for: Accessing the resolved physical address across the cache and main memory hierarchy.
> - Regardless of whether address translation hits or misses, the CPU must **always** perform $T_{\text{data}}$ to fetch the actual operand.

---

## 3. Phase 1: Address Translation Latency ($T_{\text{translation}}$)

### Parameters
- $h_{\text{tlb}}$: TLB hit ratio ($m_{\text{tlb}} = 1 - h_{\text{tlb}}$: TLB miss ratio)
- $T_{\text{tlb}}$: TLB search latency
- $p_{\text{fault}}$: Page fault rate (defined strictly over TLB misses)
- $T_{\text{pt}}$: Latency of a page table walk ($n \times T_{\text{mem}}$ for an $n$-level page table)
- $\text{PFS}$ / $T_{\text{fault}}$: Page Fault Service time (disk I/O, OS trap, updating PTE/TLB)

#### Case A: Hierarchical (Serial) Translation
The TLB is queried first. On a miss, translation incurs the TLB search time plus the memory lookup penalty:

$$T_{\text{translation}} = T_{\text{tlb}} + m_{\text{tlb}} \cdot \Big[ (1 - p_{\text{fault}}) \cdot T_{\text{pt}} + p_{\text{fault}} \cdot (T_{\text{pt}} + \text{PFS}) \Big]$$

Factoring out $T_{\text{pt}}$:

$$T_{\text{translation}} = T_{\text{tlb}} + m_{\text{tlb}} \cdot \Big[ T_{\text{pt}} + p_{\text{fault}} \cdot \text{PFS} \Big]$$

#### Case B: Simultaneous (Parallel) Translation
TLB and Page Table lookup are evaluated as mutually exclusive paths:

$$T_{\text{translation}} = h_{\text{tlb}} \cdot T_{\text{tlb}} + m_{\text{tlb}} \cdot \Big[ T_{\text{pt}} + p_{\text{fault}} \cdot \text{PFS} \Big]$$

> [!trap] Critical Invariants for Gate & Systems Design
> 1. **TLB Hit Implies No Page Fault**: A TLB entry only exists if the corresponding page is present in physical memory. A page fault **cannot** occur on a TLB hit.
> 2. **Page Fault Occurrence**: A page fault can only trigger after a TLB miss during the page table traversal in RAM.
> 3. Page fault and memory acces are not done parallely! 

---

## 4. Phase 2: Physical Data Access Latency ($T_{\text{data}}$)

### Parameters
- $h_{\text{cache}}$: Cache hit ratio ($m_{\text{cache}} = 1 - h_{\text{cache}}$: Cache miss ratio)
- $T_{\text{cache}}$: Cache access latency
- $T_{\text{mem}}$: Main memory access latency

### Mathematical Formulations

#### Case A: Hierarchical (Serial) Cache Access
L1 Cache is probed first. On a miss, the request cascades down to physical memory:

$$T_{\text{data}} = T_{\text{cache}} + m_{\text{cache}} \cdot T_{\text{mem}}$$

#### Case B: Simultaneous (Parallel) Cache Access
Cache and Main Memory access initiate concurrently:

$$T_{\text{data}} = h_{\text{cache}} \cdot T_{\text{cache}} + m_{\text{cache}} \cdot T_{\text{mem}}$$

---


---

## 6. Worked Exam Problems & Derivations

> [!question] Comprehensive Multi-Tier EMAT (GATE CSE 2020 Variant)
> **Specifications:**
> - Single-level page table resident in physical memory
> - Memory access time ($m$) $= 100\text{ ns}$
> - TLB access time ($T_{\text{tlb}}$) $= 20\text{ ns}$
> - TLB hit ratio ($h_{\text{tlb}}$) $= 0.95 \implies m_{\text{tlb}} = 0.05$
> - Page fault rate ($f$) $= 0.10$ (defined strictly on a TLB miss)
> - Page transfer time to/from disk $= 5000\text{ ns}$
> - Proportion of dirty pages replaced $= 20\%$ ($p_{\text{dirty}} = 0.20$)
> - No separate cache ($T_{\text{data}} = m = 100\text{ ns}$)
> 
> **Step 1: Page Fault Service Time ($\text{PFS}$)**
> $$\begin{aligned}
> \text{PFS} &= \text{Read Disk} + p_{\text{dirty}} \cdot (\text{Write Disk}) \\
> &= 5000 + 0.20 \times 5000 = 5000 + 1000 = \mathbf{6000\text{ ns}}
> \end{aligned}$$
> 
> **Step 2: Translation Phase ($T_{\text{translation}}$)**
> $$\begin{aligned}
> T_{\text{translation}} &= T_{\text{tlb}} + m_{\text{tlb}} \cdot \Big[ T_{\text{pt}} + f \cdot \text{PFS} \Big] \\
> &= 20 + 0.05 \cdot \Big[ 100 + 0.10 \times 6000 \Big] \\
> &= 20 + 0.05 \cdot \Big[ 100 + 600 \Big] \\
> &= 20 + 0.05 \times 700 = 20 + 35 = \mathbf{55\text{ ns}}
> \end{aligned}$$
> 
> **Step 3: Data Access Phase ($T_{\text{data}}$)**
> $$T_{\text{data}} = 100\text{ ns}$$
> 
> **Step 4: Final EMAT**
> $$\text{EMAT} = T_{\text{translation}} + T_{\text{data}} = 55\text{ ns} + 100\text{ ns} = \mathbf{155\text{ ns}}$$

---

> [!question] Performance Slowdown Under Demand Paging
> **Specifications:**
> - Normal physical memory access time ($m$) $= 200\text{ ns}$
> - Page Fault Service Time ($\text{PFS}$) $= 8\text{ ms} = 8{,}000{,}000\text{ ns}$
> - Fault rate $p = \frac{1}{1000} = 10^{-3}$
> 
> **Derivation:**
> Here are given two mutually exclusive cases. Hence we use the simaultaneous formula.
> $$\begin{aligned}
> \text{EMAT} &= (1 - p) \cdot m + p \cdot \text{PFS} \\
> &= (1 - 10^{-3}) \cdot 200 + 10^{-3} \cdot 8{,}000{,}000 \\
> &= 199.8 + 8000 \approx \mathbf{8199.8\text{ ns}} \approx \mathbf{8.2\text{ }\mu\text{s}}
> \end{aligned}$$
> 
> $$\text{Slowdown Factor} = \frac{8199.8\text{ ns}}{200\text{ ns}} \approx \mathbf{41\times\text{ slowdown}}$$
> 
> *Takeaway:* A microscopic page fault rate of $0.1\%$ degrades memory throughput by over $40\times$ due to the millisecond-scale latency of secondary storage I/O.

---

> [!question] GATE IT 2004: Instruction Cycle Execution Time
> An instruction takes $i\text{ ms}$ to execute. A page fault takes an additional $j\text{ ms}$. On average, a page fault occurs once every $k$ instructions.
> 
> **Derivation:**
> - Page fault probability per instruction $= \frac{1}{k}$
> - Added penalty per instruction $= \frac{1}{k} \cdot j = \frac{j}{k}$
> 
> $$\mathbf{\text{Effective Execution Time} = i + \frac{j}{k}}$$

---

