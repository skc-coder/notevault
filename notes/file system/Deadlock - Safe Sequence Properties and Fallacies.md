> [!theorem] Request Grant Invariants in Safe States
> Let a system have a known safe sequence $\langle P_3, P_1, P_0, P_2, P_4 \rangle$[cite: 1]:
> 1. **First Process Priority**: Any request made by the **first process in the safe sequence** ($P_3$) can be granted immediately without needing to re-run the safety check (provided $\text{Request} \le \text{Available}$)[cite: 1]. This holds because $P_3$ is already proven able to terminate using available resources alone and will return all its held resources[cite: 1].
> 2. **Requests from Other Processes**: Requests from any subsequent process ($P_1, P_0, \dots$) **cannot** be blindly granted; they must be evaluated via the full Banker's check[cite: 1].
> 3. **Trivial Denial**: If $\text{Request} > \text{Available}$, the request is immediately denied/deferred without running any safety check[cite: 1].

> [!trap] Common Exam Fallacies on Safe States
> * **Fallacy 1: "If $P_1$ is the first process in the only safe sequence, then $P_1$'s request is granted only if it arrives first."**
>   * **False**: Any process can request at any time; the algorithm runs dynamically based on available resources[cite: 1].
> * **Fallacy 2: "We can never satisfy requests out of the safe sequence order."**
>   * **False**: A safe sequence merely guarantees that at least one viable schedule exists to avoid deadlock[cite: 1]. It does not mandate that processes must arrive, execute, or be granted resources strictly in that sequence[cite: 1].
> * **Fallacy 3: "Unsafe state implies deadlock."**
>   * **False**: An unsafe state implies only the *possibility* of deadlock[cite: 1]. A deadlock occurs in an unsafe state only if all processes simultaneously demand their peak maximum claims[cite: 1].

> [!question] GATE CS Concept Check
> Which of the following statements is **NOT true**[cite: 1]?
> 1. *In deadlock prevention, the request for resources is not always granted if the resulting state is safe.*[cite: 1]
> 2. *Deadlock avoidance requires a priori knowledge of resource requirements.*[cite: 1]
> 3. *Deadlock avoidance is less restrictive than deadlock prevention.*[cite: 1]
> 
> **Analysis**:
> * Statement 1 is **False (NOT true)** regarding avoidance: checking whether the resulting state is safe is the hallmark of **Deadlock Avoidance**, not Deadlock Prevention[cite: 1]. Deadlock prevention enforces structural rules (like total resource ordering) regardless of state safety[cite: 1].
> * Statement 2 is **True**: Banker's algorithm requires maximum claims declared in advance[cite: 1].
> * Statement 3 is **True**: Prevention imposes rigid rules that restrict resource utilization, whereas avoidance grants requests as long as a safe path exists[cite: 1].
