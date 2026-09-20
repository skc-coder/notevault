> [!definition] Deadlock Detection and Recovery
> In this approach, the OS does not perform dynamic safety checks on every request, allowing requests to be granted immediately whenever resources are available[cite: 1]. Instead:
> * The system invokes a **Deadlock Detection Algorithm** periodically to check if a cycle/deadlock has formed[cite: 1].
> * If detected, a **Recovery Scheme** is triggered to restore system throughput[cite: 1].

> [!theorem] Deadlock Detection vs Avoidance Matrices
> The detection algorithm utilizes an identical structure to the Banker's safety algorithm, with one fundamental structural difference[cite: 1]:
> * Avoidance uses the **$\text{Need}$ matrix** ($\text{Max} - \text{Allocated}$), representing potential *future* claims[cite: 1].
> * Detection uses the **$\text{Request}$ matrix**, representing *actual outstanding requests* currently blocking processes[cite: 1].

> [!theorem] Recovery Mechanisms
> Once deadlock is detected, the OS can recover via[cite: 1]:
> 1. **Process Termination**:
>    * Abort all deadlocked processes (simplest, but costly)[cite: 1].
>    * Abort processes one by one until the deadlock cycle is broken[cite: 1].
> 2. **Resource Preemption**:
>    * **Selecting a victim**: Determine which process holds resources that can be preempted with minimum cost[cite: 1].
>    * **Rollback**: Roll back the victim process to a safe checkpoint state[cite: 1].
>    * **Starvation prevention**: Ensure the same process is not consistently selected as the victim[cite: 1].

> [!question] Deadlock Detection Matrix Walkthrough
> State of system with processes $P_0, P_1, P_2, P_3, P_4$ and resource types $A, B, C$[cite: 1]:
> 
> | Process | Allocation $(A, B, C)$ | Request $(A, B, C)$ |
> | :--- | :--- | :--- |
> | $P_0$ | $(0, 1, 0)$[cite: 1] | $(0, 0, 0)$[cite: 1] |
> | $P_1$ | $(2, 0, 0)$[cite: 1] | $(2, 0, 2)$[cite: 1] |
> | $P_2$ | $(3, 0, 3)$[cite: 1] | $(0, 0, 0)$[cite: 1] |
> | $P_3$ | $(2, 1, 1)$[cite: 1] | $(1, 0, 0)$[cite: 1] |
> | $P_4$ | $(0, 0, 2)$[cite: 1] | $(0, 0, 2)$[cite: 1] |
> 
> $\text{Available} = (0, 0, 0)$[cite: 1].
> 
> **Detection Trace**:
> 1. $P_0$ has an outstanding request of $(0, 0, 0)$[cite: 1]. It requires no additional resources to finish[cite: 1].
>    * $P_0$ completes and releases its allocation: $\text{Available} \to (0, 0, 0) + (0, 1, 0) = (0, 1, 0)$[cite: 1].
> 2. Next, $P_2$ has request $(0, 0, 0)$[cite: 1]. It can finish immediately[cite: 1].
>    * $P_2$ releases allocation: $\text{Available} \to (0, 1, 0) + (3, 0, 3) = (3, 1, 3)$[cite: 1].
> 3. Now $\text{Available} = (3, 1, 3)$:
>    * $P_3$ requires $(1, 0, 0) \le (3, 1, 3) \implies P_3$ finishes and releases $(2, 1, 1) \implies \text{Available} \to (5, 2, 4)$[cite: 1].
>    * $P_1$ requires $(2, 0, 2) \le (5, 2, 4) \implies P_1$ finishes and releases $(2, 0, 0) \implies \text{Available} \to (7, 2, 4)$[cite: 1].
>    * $P_4$ requires $(0, 0, 2) \le (7, 2, 4) \implies P_4$ finishes[cite: 1].
> 4. All processes successfully complete in order $\langle P_0, P_2, P_3, P_1, P_4 \rangle$[cite: 1].
> 5. **Conclusion**: The system is **not in deadlock**[cite: 1].
