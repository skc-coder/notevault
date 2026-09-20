> [!definition] Effective Memory Access Time (EMAT)
> In a demand-paged system, effective memory access time measures the weighted average access latency accounting for the probability of incurring a page fault[cite: 3].

> [!formula] Primary EMAT Formula
> $$\text{EMAT} = (1 - p) \cdot m + p \cdot \text{PFS}$$[cite: 3]
> Where:
> * $p$: Page fault service probability ($0 \le p \le 1$)[cite: 3].
> * $m$: Physical memory access time ($\text{MAT}$)[cite: 3].
> * $\text{PFS}$: Page fault service time (includes OS interrupt handling, swap-out if dirty, swap-in from disk, updating PTE/TLB, and instruction restart memory access)[cite: 3].

> [!question] Performance Slowdown Calculation
> Given:
> * $m = 200\text{ ns} = 200 \times 10^{-9}\text{ s}$[cite: 3]
> * $\text{PFS} = 8\text{ ms} = 8 \times 10^{-3}\text{ s} = 8{,}000{,}000\text{ ns}$[cite: 3]
> * Find the slowdown if $p = \frac{1}{1000}$ ($1$ fault in every $1000$ page references)[cite: 3].
> 
> **Derivation**:
> $$\text{EMAT} = (1 - p) \cdot 200 + p \cdot (8{,}000{,}000) = 200 + p \cdot (7{,}999{,}800)\text{ ns}$$[cite: 3]
> For $p = 10^{-3}$:
> $$\text{EMAT} = 200 + 10^{-3} \times 7{,}999{,}800 \approx 200 + 7999.8 \approx 8200\text{ ns} = 8.2\text{ }\mu\text{s}$$[cite: 3]
> $$\text{Slowdown Factor} = \frac{8200\text{ ns}}{200\text{ ns}} = 41 \times \text{ slower}$$[cite: 3]
> *Even an extremely small page fault rate of $0.1\%$ degrades memory access performance by over $40\times$*[cite: 3].

> [!question] GATE CSE 2000: Access Time with Low Fault Rate
> Given:
> * $\text{Page fault service time} = 10\text{ ms}$[cite: 7]
> * $\text{Normal memory access time} = 1\text{ }\mu\text{s}$[cite: 7]
> * $\text{Page hit ratio} = 99.99\% \implies p = 0.01\% = 0.0001 = 10^{-4}$[cite: 7]
> 
> Calculate Average Access Time:
> $$\text{EMAT} = (1 - p) \cdot (1\text{ }\mu\text{s}) + p \cdot (10\text{ ms})$$[cite: 7]
> $$\text{EMAT} = 0.9999 \times 1\text{ }\mu\text{s} + 0.0001 \times 10{,}000\text{ }\mu\text{s} = 0.9999\text{ }\mu\text{s} + 1\text{ }\mu\text{s} = \mathbf{1.9999\text{ }\mu\text{s}}$$[cite: 7]
