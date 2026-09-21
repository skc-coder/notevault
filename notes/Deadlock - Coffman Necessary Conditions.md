> [!definition] The Four Coffman Conditions
> A deadlock can arise if and only if the following four operational conditions hold simultaneously in the system[cite: 1]:
> 1. **Mutual Exclusion**: At least one resource must be held in a non-shareable mode; only one process can use the resource at any given instant[cite: 1].
> 2. **Hold and Wait**: A process must currently be holding at least one resource and concurrently waiting to acquire additional resources that are currently being held by other processes[cite: 1].
> 3. **No Preemption**: Resources cannot be preempted forcibly from a process; a resource can be released only voluntarily by the process holding it after it has completed its task[cite: 1].
> 4. **Circular Wait**: A closed chain of processes $\{P_0, P_1, \dots, P_n\}$ exists such that $P_0$ is waiting for a resource held by $P_1$, $P_1$ is waiting for a resource held by $P_2$, ..., and $P_n$ is waiting for a resource held by $P_0$[cite: 1].

> [!theorem] The Four-Legged Table Invariant
> * The four Coffman conditions are **necessary conditions**, but they are **not individually sufficient**[cite: 1].
> * Analogous to the four legs of a table: if even one single leg (condition) is broken, a deadlock **cannot** occur[cite: 1].
> * If all $4$ conditions are satisfied simultaneously, a deadlock **may or may not** occur (depending on instance counts and allocation states)[cite: 1].
> 
> | Condition Status | System Deadlock State |
> | :--- | :--- |
> | Any $1$ of the $4$ conditions negated | Deadlock is **impossible**[cite: 1] |
> | All $4$ conditions satisfied | Deadlock is **possible** (May or may not occur)[cite: 1] |

> [!trap] Circular Wait vs Hold and Wait
> Circular wait implies the hold-and-wait condition, but circular wait specifically requires the waiting dependency graph to form a directed closed loop[cite: 1]. If processes require at most $1$ resource at any given time, hold and wait is violated, rendering deadlock strictly impossible[cite: 1].
