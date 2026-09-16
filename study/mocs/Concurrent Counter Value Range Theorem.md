---
tags:
  - gate/cs/os
  - concurrency/semaphores
creation date: 2026-09-16
type: revision-note
mastery: new
review date: 2026-09-23
---

# Concurrent Counter Range Theorem ($V_{\min}$ & $V_{\max}$)

---

## 1. The Core Theorem & Range Equations

Two concurrent processes $P_1$ and $P_2$ execute non-atomic updates (`Load`, `Modify`, `Store`) on a shared variable `total` initialized to $0$.

### 1.1 Unit Step Increments ($+1, +1$)
* **Symmetric / Multi-Iteration Case ($n \ge 2$ and $m \ge 2$):**
  $$V_{\min} = 2, \quad V_{\max} = n + m$$
  $$\text{Reachable Set} = \{v \in \mathbb{Z} \mid 2 \le v \le n + m\}$$

* **Single-Iteration Boundary Case ($\min(n, m) = 1$):**
  $$V_{\min} = 1, \quad V_{\max} = n + m$$
  $$\text{Reachable Set} = \{v \in \mathbb{Z} \mid 1 \le v \le n + m\}$$

* **$K$ Concurrent Processes ($K \ge 2$):**
  $$V_{\min} = 2 \quad (\text{if all } n_i \ge 2), \quad V_{\max} = \sum_{i=1}^K n_i$$

---

### 1.2 Non-Unit / Distinct Step Sizes ($+s_1, +s_2$)
For $P_1$ adding step $s_1$ ($n \ge 2$) and $P_2$ adding step $s_2$ ($m \ge 2$):
$$V_{\min} = s_1 + s_2$$
$$V_{\max} = n \cdot s_1 + m \cdot s_2$$

> [!CAUTION] The Single-Thread Double-Step Trap ($2 \times s_1$)
> $2 \times s_1$ is **physically impossible** when $n, m \ge 2$.
> A thread executes its loop strictly sequentially ($i = 1 \to 2 \to \dots \to n$). Its private register does not persist values across intermediate loop iterations. To wipe out all iterations of the competing thread, the final write must be performed by the **other** thread's last iteration loading $s_1$, yielding $s_1 + s_2$.

---

### 1.3 Mixed Operations (Increments $+1 \times n$ vs. Decrements $-1 \times m$)
* **Maximum Value:** $V_{\max} = +n$ (all $m$ decrements are wiped out by $P_1$'s first store).
* **Minimum Value:** $V_{\min} = -m$ (all $n$ increments are wiped out by $P_2$'s first store).
$$\text{Reachable Set} = [-m,\, n]$$

---

## 2. Rigorous Mechanical Execution Traces

### 2.1 Why $V_{\min} = 2$ for Unit Steps ($n = 3, m = 3$)
1. **$P_1$ Anchor:** $P_1$ (iter 1) executes `Load R1, [total]` ($R_1 = 0$). **Preempt $P_1$**.
2. **$P_2$ Partial Drain:** $P_2$ executes iterations $1$ and $2$ completely (`total` becomes $2$).
3. **$P_1$ First Overwrite:** $P_1$ resumes iter 1: `R1 = 0 + 1 = 1`, `Store [total], 1` (`total = 1`). All prior work of $P_2$ is wiped out.
4. **$P_2$ Final Trap:** $P_2$ begins its final iteration ($j = 3$), executes `Load R2, [total]` ($R_2 = 1$). **Preempt $P_2$**.
5. **$P_1$ Full Drain:** $P_1$ executes its remaining iterations ($i = 2$ and $i = 3$) completely (`total` climbs to $3$). $P_1$ terminates.
6. **$P_2$ Final Overwrite:** $P_2$ resumes iter 3: `R2 = 1 + 1 = 2`, `Store [total], 2` (`total = 2`). $P_2$ terminates.
* **Final Result:** **$2$**.

---

### 2.2 Proof Trace: $V_{\min} = s_1 + s_2 = 5$ for Steps $+2, +3$ ($n \ge 2, m \ge 2$)

| Phase | Acting Process & Iteration | Micro-Instruction | Local Action | RAM (`total`) | Synchronization State |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **1** | $P_1$ (iter $i = 1$) | `Load` | $R_1 \leftarrow 0$ | $0$ | $P_1$ grabs initial $0$, then **preempted**. |
| **2** | $P_2$ (iter $j = 1 \dots m-1$) | Full Loop Exec | $P_2$ runs $m-1$ iterations | $(m-1) \times 3$ | Intermediate increments run. |
| **3** | $P_1$ (iter $i = 1$) | `Add, Store` | $R_1 = 0 + 2 = 2$; `Store` | **$2$** | Resumes iter 1. Overwrites memory with **$2$**. |
| **4** | $P_2$ (iter $j = m$) | `Load` | $R_2 \leftarrow 2$ | $2$ | Starts its **last** iteration, loads $2$, then **preempted**. |
| **5** | $P_1$ (iter $i = 2 \dots n$) | Full Loop Exec | $P_1$ finishes all iterations | $2 + (n-1) \times 2$ | $P_1$ completely finishes and **terminates**. |
| **6** | $P_2$ (iter $j = m$) | `Add, Store` | $R_2 = 2 + 3 = 5$; `Store` | **$5$** | Overwrites everything with **$5$**. $P_2$ **terminates**. |

---

## 3. Fast Exam Verification Matrix

| Question Configuration     | Parameters                                            | $V_{\min}$ | $V_{\max}$ | Reachable Values                                                |
| :------------------------- | :---------------------------------------------------- | :--------: | :--------: | :-------------------------------------------------------------- |
| **GATE Standard Question** | $P_1 (+1 \times 3), P_2 (+1 \times 3)$                |  **$2$**   |  **$6$**   | $\{2, 3, 4, 5, 6\}$ *(Options 3, 5, 6 are valid; 1 is invalid)* |
| **Single Iteration Trap**  | $P_1 (+1 \times 1), P_2 (+1 \times 100)$              |  **$1$**   | **$101$**  | $\{1, 2, \dots, 101\}$                                          |
| **$K$-Process System**     | 5 processes, each $+1 \times 10$                      |  **$2$**   |  **$50$**  | $\{2, 3, \dots, 50\}$                                           |
| **Different Steps**        | $P_1 (+2 \times n), P_2 (+3 \times m)$ ($n, m \ge 2$) |  **$5$**   | $2n + 3m$  | Minimum is $s_1 + s_2 = 2 + 3 = 5$                              |
| **Opposing Signs**         | $P_1 (+1 \times n), P_2 (-1 \times m)$                |  **$-m$**  |  **$+n$**  | $[-m, n]$                                                       |
