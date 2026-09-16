---
tags:
  - gate/cs/os
  - concurrency/semaphores
creation date: 2026-09-16
type: revision-note
mastery: new
review date: 2026-09-23
---

# Counting Semaphores: DAG Precedence & Internal Invariants

---

## 1. Core Theory & Invariants

### 1.1 Dijkstra Implementation Semantics
```c
wait(S) / P(S):
    S->value--;              // Decrements FIRST (Invoked count increments)
    if (S->value < 0) {
        add thread to S->queue;
        block();             // Halts execution; NOT yet completed
    }

signal(S) / V(S):
    S->value++;
    if (S->value <= 0) {
        remove thread from S->queue;
        wakeup(thread);
    }
````

### 1.2 State Equations & Invariants
- **Internal Signed Counter:**

    $$\text{Value}(S) = S_{\text{init}} + \#V_{\text{completed}} - \#P_{\text{invoked}}$$
- **Blocked Thread Representation:**

    $$\text{If } \text{Value}(S) < 0 \implies \text{Blocked threads } (w) = -\text{Value}(S)$$
- **Partition of Invoked Waits:**

    $$\#P_{\text{invoked}} = \#P_{\text{completed}} + \text{Blocked threads } (w)$$
- **Tokens Completed (Production Invariant):**

    $$\text{Completed } P(S) \le \text{Total Tokens Produced} = S_{\text{init}} + \#V_{\text{completed}}$$

    When $w > 0$ (threads blocked), all tokens are exhausted:

    $$\#P_{\text{completed}} = S_{\text{init}} + \#V_{\text{completed}} = m - w$$

> [!CAUTION] Common Trap
>
> Counter decrement occurs on **invocation/attempt**, not completion.
>
> Therefore: $k + n + w = \#P_{\text{invoked}} \ (m)$, **not** $\#P_{\text{completed}}$.
>
>

## 2. Minimal Precedence Mapping (DAGs)

### Rules of Thumb:
- **Counting Semaphores:** Need **1 semaphore per synchronization frontier (rank cut)**.
    - **Fork ($1 \to M$):** 1 semaphore ($S=0$). Predecessor executes $M \times V(S)$; each successor executes $1 \times P(S)$.
    - **Join ($K \to 1$):** 1 semaphore ($S=0$). Each predecessor executes $1 \times V(S)$; successor executes $K \times P(S)$.
- **Binary Semaphores:** Require **1 semaphore per graph edge** (unless auxiliary shared counters with mutexes are used) because binary semaphores cannot accumulate tokens.

## 3. Original Problem Analysis

**Graph:** $T_1 \to \{T_2, T_3\} \to T_4$

**Question:** Minimum counting semaphores needed?
- **Answer:** **2**
- **Frontiers:**
    - Cut 1 ($T_1 \to T_2, T_3$): Semaphore $S_1 = 0$
    - Cut 2 ($T_2, T_3 \to T_4$): Semaphore $S_2 = 0$
- **Execution Pattern:**
    - $T_1$: computes $\to V(S_1), V(S_1)$
    - $T_2$: $P(S_1) \to$ computes $\to V(S_2)$
    - $T_3$: $P(S_1) \to$ computes $\to V(S_2)$
    - $T_4$: $P(S_2), P(S_2) \to$ computes

## 4. Problem Variations & Quick Review

| **#**  | **Scenario / Variation**                                                                                                                               | **Key Mechanics / Answer**                                                                                                                                      |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **V1** | **Asymmetric Diamond:**<br>$T_1 \to \{T_2, T_3, T_4\}$;<br>$\{T_2, T_3\} \to T_5$; $T_4$ independent of $T_5$. | **2 counting semaphores**<br>$S_1=0$ for fork from $T_1$ ($3 \times V$).<br>$S_2=0$ for join into $T_5$ ($2 \times P$). |
| **V2** | **Formula Derivation:**<br>Init = $k$, Signals = $n$, Attempts = $m$, Blocked = $w > 0$. Find completed $P$.                       | **$\#P_{\text{completed}} = m - w = k + n$**<br>_(Note: $m = k + n + w$)_                                                                   |
| **V3** | **Join Independence:**<br>$A \to C$ and $B \to C$ via shared semaphore $S=0$. Can $C$ run with only one finished?                  | **No (Guaranteed correct)**<br>$C$ requires 2 tokens ($P(S), P(S)$). Since $A$ and $B$ emit 1 token each, both must finish.                 |
| **V4** | **Hourglass DAG ($3 \to 1$):**<br>$\{T_1, T_2, T_3\} \to T_4$. Minimal semaphores for Counting vs. Binary.                         | **Counting = 1** (Successor calls $3 \times P$)<br>**Binary = 3** (1 per dependency edge to prevent lost signals)                           |
