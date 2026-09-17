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

## 1. Problem Statement & Code

System with multiple threads of two types calling `routine(threadType)`:

```c
Semaphore semaX = 0; // Initial value = 0
Semaphore semaY = 0; // Initial value = 0

void routine(threadType) {
if (threadType == typeA) {
P(semaX);
V(semaY);
}
if (threadType == typeB) {
V(semaX);
V(semaX);
P(semaY);
}
DoIt();
}
````

Let:
- $a =$ number of `typeA` threads passing through `DoIt()`.
- $b =$ number of `typeB` threads passing through `DoIt()`.

**Target:** Find the invariant relationship that must ALWAYS hold at any point in the system.
- **Correct Option:** **$b \le a \le 2b$**

## 2. Rigorous Proof of the Invariant: $\#P_{\text{completed}}(S) \le \#V_{\text{completed}}(S)$

### 2.1 State Definitions
- $S_{\text{init}} = 0$
- $\#V_{\text{completed}}$: Total signals executed up to time $t$.
- $\#P_{\text{invoked}}$: Total threads that called/attempted `wait(S)` up to time $t$.
- $\#P_{\text{completed}}$: Total threads that successfully passed `wait(S)` up to time $t$.
- $w$: Total threads currently blocked/suspended in the queue at time $t$ ($w \ge 0$).

### 2.2 Invariant Equations

1. **Partition of Invocation:**

$$\#P_{\text{invoked}} = \#P_{\text{completed}} + w$$

2. **Internal Signed Counter (Dijkstra):**

$$\text{Value}(S) = S_{\text{init}} + \#V_{\text{completed}} - \#P_{\text{invoked}} = \#V_{\text{completed}} - \#P_{\text{invoked}}$$

### 2.3 Proof Across All Reachable States
- **Case 1: No blocked threads ($w = 0$):**
    - $\#P_{\text{invoked}} = \#P_{\text{completed}}$
    - $\text{Value}(S) \ge 0 \implies \#V_{\text{completed}} - \#P_{\text{completed}} \ge 0$
    - Therefore:

$$\#P_{\text{completed}} \le \#V_{\text{completed}}$$
- **Case 2: Blocked threads exist ($w > 0$):**
    - By definition of Dijkstra counting semaphore: $\text{Value}(S) = -w$
    - Substitute into counter formula:

$$-w = \#V_{\text{completed}} - \#P_{\text{invoked}}$$

$$-w = \#V_{\text{completed}} - (\#P_{\text{completed}} + w)$$

$$-w = \#V_{\text{completed}} - \#P_{\text{completed}} - w$$
    - Add $w$ to both sides:

$$\#P_{\text{completed}} = \#V_{\text{completed}}$$

$$\therefore \text{Under all conditions: } \#P_{\text{completed}}(S) \le \#V_{\text{completed}}(S)$$

## 3. Derivation of the Bounds ($b \le a \le 2b$)

### 3.1 Lower Bound ($b \le a$)
- To reach `DoIt()`, every `typeB` thread must complete $P(semaY)$.
- By the completion invariant:

$$\#P_{\text{completed}}(semaY) \le \#V_{\text{completed}}(semaY)$$
- The only source of $V(semaY)$ is `typeA` threads that passed their $P(semaX)$.
- Thus, total tokens ever added to $semaY \le a$:

$$b \le \#P_{\text{completed}}(semaY) \le \#V_{\text{completed}}(semaY) \le a \implies b \le a$$

### 3.2 Upper Bound ($a \le 2b$)
- Every `typeB` thread that executes injects $2$ tokens into `semaX` via `V(semaX); V(semaX);`.
- If $k$ threads of `typeB` enter and execute their signals, they produce $2k$ tokens on `semaX`.
- If $a$ threads of `typeA` consume these tokens, each runs `V(semaY)`, generating $a$ tokens on `semaY`.
- Since each blocked `typeB` requires only $1$ token from `semaY` to complete and reach `DoIt()`, whenever $a$ increases, it immediately unblocks the corresponding `typeB` threads.
- At maximum consumption:

$$a \le 2b$$

Combining both inequalities yields:

$$b \le a \le 2b$$

## 4. 30-Second Exam Elimination Blueprint

1. **Test Initial State ($a = 0, b = 0$):**
    - Option A ($a < 2b$) $\implies 0 < 0$ (False).
    - Option B ($b < 2a$) $\implies 0 < 0$ (False).
    - _Strict inequalities fail instantly at time $t=0$._

2. **Trace a Minimal Execution Step:**
    - Run 1 `typeB` into queue: produces $2$ on `semaX`, blocks on `semaY`.
    - Run 1 `typeA`: consumes $1$ from `semaX`, signals `semaY`, reaches `DoIt()` ($a=1$).
    - Unblocked `typeB` completes and reaches `DoIt()` ($b=1$).
    - State: $a=1, b=1 \implies 1 \le 1 \le 2$ (Holds for both C & D).
    - Run second `typeA` (consumes remaining token on `semaX`): reaches `DoIt()` ($a=2, b=1$).
    - Check Option D: $a \le b \le 2a \implies 2 \le 1 \le 4$ (**False** because $2 \le 1$ fails).
    - Check Option C: $b \le a \le 2b \implies 1 \le 2 \le 2$ (**True**).
    - **Mark C immediately.**

## 5. Variations Summary

| **Variation**                 | **Modified Logic**                                                         | **Resulting Bound**  |
| ----------------------------- | -------------------------------------------------------------------------- | -------------------- |
| **Production Inversion**      | `typeA` executes $2 \times V(semaY)$; `typeB` executes $1 \times V(semaX)$ | $a \le b \le 2a$     |
| **Initial Tokens**            | `semaX` initialized to $k > 0$                                             | $b \le a \le 2b + k$ |
| **Water Molecule Rendezvous** | $2 \text{ Hydrogen} + 1 \text{ Oxygen} \to H_2O$                           | $H = 2 \cdot O$      |
