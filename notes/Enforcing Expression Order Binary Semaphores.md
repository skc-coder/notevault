---
tags:
  - gate/cs/os
  - concurrency/semaphores
creation date: 2026-09-16
type: revision-note
mastery: new
review date: 2026-09-23
---


---

## 1. Problem Statement & Code Layout

Target mathematical expression to evaluate:
$$z = F_3(F_1(x),\, F_2(F_3(y)))$$

Variables $x, y,$ and $z$ are shared integers. The computation is partitioned across two concurrent threads:

| Thread $T_1$ | Thread $T_2$ |
| :--- | :--- |
| `y = F3(y);` | `y = F2(y);` |
| `x = F1(x);` | |
| `z = F3(x, y);` | |

**Question:** What is the **minimum number of binary semaphores** required to ensure this dependency order always holds regardless of CPU scheduling order?

* **Answer:** **2**

---

## 2. Core Intent & Dependency Mechanics

### 2.1 Bernstein’s Conditions & RAW Data Dependencies
To produce the exact target expression $z = F_3(F_1(x), F_2(F_3(y)))$, the individual statement evaluations must satisfy:
1. **$y = F_3(y)$ in $T_1$ MUST execute before $y = F_2(y)$ in $T_2$**
   $\to$ So that $F_2$ operates on the transformed $F_3(y)$, computing $F_2(F_3(y))$.
2. **$y = F_2(y)$ in $T_2$ MUST execute before $z = F_3(x, y)$ in $T_1$**
   $\to$ So that the outer $F_3$ receives the fully evaluated $F_2(F_3(y))$.
3. **$x = F_1(x)$ in $T_1$ has no data dependency on $y$**
   $\to$ It can execute anytime before $z = F_3(x, y)$. Intra-thread sequential execution order inside $T_1$ guarantees this naturally without extra locks.

### 2.2 The Ping-Pong Handshake Invariant
The inter-thread control flow forms a two-way serialized handshake:
$$T_1 \ (S_1) \longrightarrow T_2 \ (S_2) \longrightarrow T_1$$

* A single binary semaphore can only enforce **unidirectional** precedence ($A \to B$).
* A two-way alternating dependency ($T_1 \to T_2 \to T_1$) strictly requires **2 distinct binary semaphores** initialized to `0` to prevent deadlock and premature execution under arbitrary scheduling.

---

## 3. Minimal Semaphore Synchronization Solution

```c
// Binary semaphores initialized to 0
binary_semaphore s1 = 0; // Signals T2 that inner F3(y) is ready
binary_semaphore s2 = 0; // Signals T1 that F2(y) is ready

void T1() {
y = F3(y);       // 1. Compute inner F3(y)
V(s1);           // 2. Hand off control to T2

x = F1(x);       // Local computation (runs concurrently or sequentially)

P(s2);           // 3. Block until T2 finishes F2(y)
z = F3(x, y);    // 4. Compute final outer F3(F1(x), F2(F3(y)))
}

void T2() {
P(s1);           // 1. Block until T1 finishes inner F3(y)
y = F2(y);       // 2. Compute F2(F3(y))
V(s2);           // 3. Hand control back to T1
}
````

### Trace Under Edge Scheduling Orders
- **$T_2$ scheduled first:** Executes `P(s1)` $\implies s1$ was $0$, so $T_2$ blocks. $T_1$ runs `y = F3(y)` and signals `V(s1)`, awakening $T_2$.
- **$T_1$ scheduled first:** Runs `y = F3(y)`, signals `s1`, runs `x = F1(x)`, hits `P(s2)` $\implies s2$ was $0$, so $T_1$ blocks before touching `z`. $T_2$ unblocks, finishes `y = F2(y)`, and signals `s2`, allowing $T_1$ to complete `z`.

## 4. Problem Variations & Fast Heuristics

| **#**  | **Variation Scenario**                                                    | **Minimum Semaphores** | **Core Reason**                                                                                         |
| ------ | ------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------- |
| **V1** | **Move `x = F1(x)` to the top of $T_1$**                                  | **2**                  | $x$ has no dependency on $y$. The required cross-thread edges ($T_1 \to T_2 \to T_1$) remain identical. |
| **V2** | **Target: $z = F_3(F_1(x), y)$ where $T_2$ only consumes $y$ at the end** | **1**                  | Strict unidirectional flow ($T_1 \to T_2$). No return handshake required.                               |
| **V3** | **Alternating Print (`010101...`) between two threads**                   | **2**                  | Classic ping-pong turnstile: $T_A$ signals $T_B$, $T_B$ signals $T_A$ (initialized to `1` and `0`).     |
| **V4** | **3-Thread Pipeline: $T_1(F_3) \to T_2(F_2) \to T_3(F_{\text{outer}})$**  | **2**                  | Serial chain of 3 threads ($T_1 \to T_2 \to T_3$) needs 1 semaphore per transition edge ($2$ total).    |
