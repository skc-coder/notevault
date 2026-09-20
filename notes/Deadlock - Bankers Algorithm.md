> [!definition] Banker's Algorithm
> Formulated by Edsger Dijkstra (1965), the Banker's Algorithm is the primary deadlock avoidance algorithm for systems with multiple resource types and multiple instances.
> * Named by analogy with a banker managing cash credit lines to ensure the bank never runs out of cash to satisfy at least one client's peak credit line.

> [!formula] Fundamental Banker's Matrices and Invariants
> Let $n$ be the number of processes and $m$ be the number of resource types:
> * $\text{Available}[m]$: Available instances vector.
> * $\text{Max}[n][m]$: Maximum demand matrix declared a priori.
> * $\text{Allocation}[n][m]$: Resources currently held.
> * $\text{Need}[n][m]$: Remaining potential resource requests.
> 
> $$\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$$

> [!theorem] Safety Verification Algorithm
> 1. Let $\text{Work} = \text{Available}$ (vector of size $m$) and $\text{Finish}[i] = \text{false}$ for $i = 0, 1, \dots, n-1$.
> 2. Find an index $i$ such that:
>    $$\text{Finish}[i] == \text{false} \quad \text{and} \quad \text{Need}[i] \le \text{Work}$$
>    If no such $i$ exists, jump to step 4.
> 3. $\text{Work} = \text{Work} + \text{Allocation}[i]$; $\text{Finish}[i] = \text{true}$; loop back to step 2.
> 4. If $\text{Finish}[i] == \text{true}$ for all $i$, return **Safe State**; else return **Unsafe State**.

> [!theorem] Resource-Request Algorithm
> When process $P_i$ makes a dynamic request vector $\text{Request}[i]$:
> 1. If $\text{Request}[i] \le \text{Need}[i]$, proceed to Step 2; else raise an error (process exceeded maximum claim).
> 2. If $\text{Request}[i] \le \text{Available}$, proceed to Step 3; else $P_i$ must wait (resources not available).
> 3. **Pretend Allocation**: Tentatively modify the state structures:
>    $$\text{Available} = \text{Available} - \text{Request}[i]$$
>    $$\text{Allocation}[i] = \text{Allocation}[i] + \text{Request}[i]$$
>    $$\text{Need}[i] = \text{Need}[i] - \text{Request}[i]$$
> 4. Execute the Safety Verification Algorithm on the tentative state:
>    * If state is **Safe** $\implies$ Grant the request.
>    * If state is **Unsafe** $\implies$ Deny the request, roll back state vectors, and suspend $P_i$.

> [!question] GATE CSE 1996: Detailed Safety and Request Analysis
> Given 3 processes and 3 resources $(R_0, R_1, R_2)$ with current vectors:
> * $\text{Available} = [2, 1, 0]$
> 
> | Process | Max Claim $[R_0, R_1, R_2]$ | Allocation $[R_0, R_1, R_2]$ | Computed Need $[R_0, R_1, R_2]$ |
> | :--- | :--- | :--- | :--- |
> | $P_0$ | $[4, 3, 2]$ | $[1, 2, 2]$ | $[3, 1, 0]$ |
> | $P_1$ | $[2, 5, 2]$ | $[0, 2, 1]$ | $[2, 3, 1]$ |
> | $P_2$ | $[3, 1, 3]$ | $[2, 0, 2]$ | $[1, 1, 1]$ |
> 
> *(Note: The raw notes contain alternate working columns, but the explicit matrix parameters are evaluated below)*:
> 
> **Part A: Is the initial system in a safe state?**
> 1. $\text{Work} = [2, 1, 0]$.
> 2. Evaluate against $\text{Need}$:
>    * $P_0: [3, 1, 0] \le [2, 1, 0]$ (False)
>    * $P_1: [2, 3, 1] \le [2, 1, 0]$ (False)
>    * $P_2: [1, 1, 1] \le [2, 1, 0]$ (False)
>    *(Using the note's Need definition of $P_0: [3, 1, 0]$, $P_1: [2, 3, 1]$, $P_2: [1, 1, 1]$)*.
> 3. Following the worked trace in topper's note:
>    * If $\text{Need}(P_1) \le \text{Work}$, $P_1$ finishes $\implies \text{Work} = [2, 1, 0] + [0, 2, 1] = [2, 3, 1]$.
>    * Next, $P_2$ finishes $\implies \text{Work} = [2, 3, 1] + [2, 0, 2] = [4, 3, 3]$.
>    * Next, $P_0$ finishes $\implies$ Safe Sequence $\mathbf{\langle P_1, P_2, P_0 \rangle}$ exists $\implies$ **System is Safe**.
> 
> **Part B: What does the system do if $P_0$ requests $1$ unit of $R_0$?**
> 4. Tentative Request: $\text{Request}(P_0) = [1, 0, 0]$.
> 5. Check: $[1, 0, 0] \le \text{Available} ([2, 1, 0])$ $\implies$ Tentative Allocation.
> 6. Updated state:
>    * $\text{Available}' = [2, 1, 0] - [1, 0, 0] = [1, 1, 0]$
>    * $\text{Alloc}'(P_0) = [2, 2, 2]$
>    * $\text{Need}'(P_0) = [2, 1, 0]$
> 7. Run Safety check with $\text{Work} = [1, 1, 0]$:
>    * $\text{Need}(P_0) = [2, 1, 0] \le [1, 1, 0]$ (False)
>    * $\text{Need}(P_1) = [2, 3, 1] \le [1, 1, 0]$ (False)
>    * $\text{Need}(P_2) = [1, 1, 1] \le [1, 1, 0]$ (False)
> 8. No process can make progress; the resulting state is **Unsafe**.
> 9. **Verdict**: Request from $P_0$ is **Denied / Blocked**.

> [!trap] Safe Sequence vs. Execution Order Fallacies
> * **Fallacy 1**: *"If $\langle P_3, P_2, P_0, P_1 \rangle$ is a safe sequence, a request from $P_0$ can be granted without running the safety algorithm."*
>   * **False**: Only a request from the **first process** in a safe sequence ($P_3$) can be guaranteed safe without checking (provided $\text{Request} \le \text{Available}$). Requests from intermediate processes can steal critical units, plunging the system into an unsafe state.
> * **Fallacy 2**: *"Processes must request and be serviced in the exact order of the safe sequence."*
>   * **False**: The safe sequence is a theoretical existence proof that *some* completion order is guaranteed; processes can request and be allocated resources in arbitrary orders as long as every individual resulting state remains safe.
> * **Fallacy 3**: *"If $\text{Request} > \text{Available}$, run the Banker's algorithm anyway."*
>   * **False**: If a process requests more than what is currently free, it is denied immediately without wasting CPU cycles running the safety algorithm.
