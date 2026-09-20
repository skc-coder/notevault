> [!definition] Deadlock Detection and Recovery
> Rather than restricting allocations in advance, Deadlock Detection and Recovery allows the OS to grant requests unhindered, periodically executing a detection algorithm to check if processes are blocked in a deadlock.
> * **Detection Routine**: Checks the current allocation and pending request matrices.
> * **Key Difference from Banker's Algorithm**:
>   * Avoidance uses the **$\text{Need}$ matrix** (worst-case maximum potential claims).
>   * Detection uses the **$\text{Request}$ matrix** (active, currently pending requests).

> [!question] Deadlock Detection Matrix Walkthrough
> Consider $5$ processes $\{P_0, P_1, P_2, P_3, P_4\}$ and $3$ resource types $(A, B, C)$:
> * $\text{Available} = [0, 0, 0]$
> 
> | Process | Allocation $[A, B, C]$ | Request $[A, B, C]$ |
> | :--- | :--- | :--- |
> | $P_0$ | $[0, 1, 0]$ | $[0, 0, 0]$ |
> | $P_1$ | $[2, 0, 0]$ | $[2, 0, 2]$ |
> | $P_2$ | $[3, 0, 3]$ | $[0, 0, 0]$ |
> | $P_3$ | $[2, 1, 1]$ | $[1, 0, 0]$ |
> | $P_4$ | $[0, 0, 2]$ | $[0, 0, 2]$ |
> 
> **Step-by-step Detection Trace**:
> 1. $\text{Work} = [0, 0, 0]$.
> 2. $P_0$ has $\text{Request}[0] = [0, 0, 0] \le [0, 0, 0]$:
>    * $P_0$ executes and releases $[0, 1, 0]$.
>    * $\text{Work} = [0, 0, 0] + [0, 1, 0] = [0, 1, 0]$.
> 3. $P_2$ has $\text{Request}[2] = [0, 0, 0] \le [0, 1, 0]$:
>    * $P_2$ executes and releases $[3, 0, 3]$.
>    * $\text{Work} = [0, 1, 0] + [3, 0, 3] = [3, 1, 3]$.
> 4. Evaluate remaining requests against $\text{Work} = [3, 1, 3]$:
>    * $P_3$ requests $[1, 0, 0] \le [3, 1, 3] \implies$ finishes, yields $\text{Work} = [3, 1, 3] + [2, 1, 1] = [5, 2, 4]$.
>    * $P_1$ requests $[2, 0, 2] \le [5, 2, 4] \implies$ finishes, yields $\text{Work} = [5, 2, 4] + [2, 0, 0] = [7, 2, 4]$.
>    * $P_4$ requests $[0, 0, 2] \le [7, 2, 4] \implies$ finishes, yields $\text{Work} = [7, 2, 4] + [0, 0, 2] = [7, 2, 6]$.
> 5. A valid execution order $\langle P_0, P_2, P_3, P_1, P_4 \rangle$ finishes all processes.
> * **Conclusion**: The system is **Not in Deadlock** as of the current snapshot.

> [!theorem] Recovery Mechanisms from Deadlock
> Once deadlock is identified, the OS breaks the cycle via one of three mechanisms:
> 1. **Process Termination (Abort)**:
>    * Abort all deadlocked processes (expensive, all partial work lost).
>    * Abort one process at a time until the deadlock cycle is broken (requires running the detection algorithm after each termination).
> 2. **Resource Preemption**:
>    * Successively preempt allocated resources from processes and assign them to others until deadlock is resolved.
>    * **Rollback**: Offending processes must be rolled back to a previous safe checkpoint and restarted.
> 3. **Manual System Restart**: The entire system is rebooted.
