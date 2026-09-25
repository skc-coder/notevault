---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
hardness: mid
importance: Important
revision: "1"
---
Software and hardware solutions utilize three core coordination abstractions:

| Primitive                  | Metaphor & Role                             | Entry Protocol               |
| :------------------------- | :------------------------------------------ | :--------------------------- |
| **Lock** (`lock`)          | Loo gate                                    | `while(lock); lock=1;`       |
| **Turn** (`turn`)          | Token                                       | `while(turn != i);`          |
| **Flag** (`want[i]`)       | Raising hand                                | `want[i]=1; while(want[j]);` |
| **Hardware Lock** (`lock`) | Atomic CPU Read-Modify-Write (`TestAndSet`) | `while(TestAndSet(&lock));`  |

| Attempt               |     Mutual Exclusion      |         Progress          |      Bounded Waiting      | Root Cause of Failure                         |
| :-------------------- | :-----------------------: | :-----------------------: | :-----------------------: | :-------------------------------------------- |
| **Attempt 1 (Lock)**  |   $\boldsymbol{\times}$   | $\boldsymbol{\checkmark}$ |   $\boldsymbol{\times}$   | Non-atomic check and set instructions         |
| **Attempt 2 (Turn)**  | $\boldsymbol{\checkmark}$ |   $\boldsymbol{\times}$   | $\boldsymbol{\checkmark}$ | Rigid alternation; inactive peer blocks entry |
| **Attempt 3 (Flags)** | $\boldsymbol{\checkmark}$ |   $\boldsymbol{\times}$   |   $\boldsymbol{\times}$   | Symmetric intent declaration creates deadlock |
| **Hardware Lock **    | $\boldsymbol{\checkmark}$ | $\boldsymbol{\checkmark}$ |   $\boldsymbol{\times}$   | Busy waiting                                  |

---

## 1. Attempt 1: Single Shared Lock Variable

```c
// Shared variable: 0 = free, 1 = occupied
int lock = 0;

// Process P0                     // Process P1
while (lock);               while (lock);
lock = 1;                   lock = 1;
/* Critical Section */            /* Critical Section */
lock = 0;                   lock = 0;
```

- **Mutual Exclusion Check:** Assume $P_0$ executes `while (lock);` and reads $0$. Before it can execute `lock = 1`, it is preempted. $P_1$ runs, tests `lock`, reads $0$, sets `lock = 1`, and enters the CS. $P_0$ resumes, sets `lock = 1`, and enters the CS concurrently. **Violated **.
- **Progress Check:** If the CS is idle ($\text{lock} = 0$), any requesting process immediately proceeds past the loop. No process outside the CS blocks entry. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Bounded Waiting Check:** A fast process exiting the CS can immediately loop around and re-acquire the lock before a preempted waiting peer executes its store. **Violated **.

> [!trap] The Test-and-Set Separation Trap
> Separating the check of a condition (`while (lock)`) from its update (`lock = 1`) into distinct, non-atomic instructions will invariably violate Mutual Exclusion whenever preemption occurs between them.

---

## 2. Attempt 2: Strict Alternation (Turn Variable)

```c
// Shared variable: 0 for P0, 1 for P1
int turn = 0;

// Process P0                     // Process P1
while (turn != 0);                while (turn != 1);
/* Critical Section */            /* Critical Section */
turn = 1;                         turn = 0;
```

- **Mutual Exclusion Check:** Since $\text{turn} \in \{0, 1\}$, the predicates $(\text{turn} == 0)$ and $(\text{turn} == 1)$ cannot evaluate to true simultaneously. At most one process enters. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Progress Check:** Suppose $P_0$ executes its CS, sets $\text{turn} = 1$, and enters a long remainder section. $P_1$ executes its CS, sets $\text{turn} = 0$, and finishes. If $P_1$ wants to re-enter the CS immediately, it is blocked at `while (turn != 1)` because $\text{turn} = 0$. $P_0$ is in its remainder section and has no desire to enter the CS, yet it prevents $P_1$ from entering. **Violated **.
- **Bounded Waiting Check:** Neither process can enter twice consecutively. Once a process requests entry, it waits for at most one entry of the other process. **Satisfied ($\boldsymbol{\checkmark}$)**.

> [!trap] Strict Alternation Remainder Fault
> Never use pure turn-taking when processes run at differing frequencies. If process $P_i$ terminates in its remainder section while $\text{turn} = i$, all other processes are permanently blocked from the CS, resulting in a fatal progress failure.

---

## 3. Attempt 3: Per-Process Intent Flags

```c
// Shared variable
int want[2] = {0, 0};

// Process P0                     // Process P1
want[0] = 1;                      want[1] = 1;
while (want[1] == 1);             while (want[0] == 1);
/* Critical Section */            /* Critical Section */
want[0] = 0;                      want[1] = 0;
```

- **Mutual Exclusion Check:** For $P_0$ to enter the CS, it must observe $\text{want}[1] == 0$. For $P_1$ to enter, it must observe $\text{want}[0] == 0$. Since each process asserts its own flag before testing the other's, both cannot simultaneously observe the other's flag as $0$. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Progress Check:** If $P_0$ executes `want[0] = 1` and is immediately preempted, and $P_1$ executes `want[1] = 1`, both reach their respective `while` loops. $P_0$ tests $\text{want}[1] == 1$ (true) and spins; $P_1$ tests $\text{want}[0] == 1$ (true) and spins. Both processes are deadlocked, and neither enters the empty CS. **Violated **.
- **Bounded Waiting Check:**  **Satisfied ($\boldsymbol{\checkmark}$)**.

---

## 4. Hardware Lock (`TestAndSet`)

- **Semantic Role:** Shared binary state ($0 = \text{free}, 1 = \text{held}$) manipulated via atomic Read-Modify-Write CPU instructions (`TestAndSet`, `Swap`, `XCHG`).
- **Entry Protocol:** `while (TestAndSet(&lock));`
- **Exit Protocol:** `lock = 0;`
- **Operational Failure:** Eliminates race conditions during entry checks via hardware bus locking, but burns CPU cycles spinning and lacks inherent ordering, causing potential starvation without auxiliary queueing.

---

