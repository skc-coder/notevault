> [!definition] The Four Deadlock Handling Strategies
> Operating systems handle deadlocks using four broad paradigms:
> 1. **Ostrich Algorithm (Ignore the problem)**
> 2. **Deadlock Prevention**
> 3. **Deadlock Avoidance**
> 4. **Deadlock Detection and Recovery**

| Strategy | Principle | Dynamic Checking | Performance / Resource Overhead |
| :--- | :--- | :--- | :--- |
| **Ostrich Algorithm** | Pretend deadlock never happens; reboot if locked. | None. | Zero runtime overhead; potential manual restart cost. |
| **Prevention** | Constrain request protocols to invalidate at least $1$ Coffman condition. | Static protocol enforcement. | High conservatism; low resource utilization. |
| **Avoidance** | Inspect state transitions; allocate only if resulting state is **Safe**. | Requires a priori claim knowledge. | Overhead per resource request; rejects safe-returning paths. |
| **Detection & Recovery**| Let deadlocks occur; detect periodically and recover. | Graph reduction / matrix checks. | Preemption, process abort, and rollback costs. |

> [!definition] Ostrich Algorithm
> The operating system ignores the deadlock problem completely, sticking its head in the sand like an ostrich and assuming deadlocks occur rarely enough that runtime prevention costs are unjustified.
> * If the system locks up, recovery is performed manually by terminating processes or rebooting the machine.
> * **Real-World Reality**: Adopted by most general-purpose operating systems, including Unix, Linux, and Windows, balancing convenience against performance overheads.

> [!theorem] Deadlock Prevention: Attacking the Four Coffman Conditions
> Deadlock prevention guarantees that deadlock can never arise by designing structural resource request protocols that ensure at least one necessary condition cannot hold:
> 
> 1. **Attacking Mutual Exclusion**:
>    * Make resources shareable (e.g., read-only files).
>    * **Infeasibility**: Intrinsically non-shareable hardware (printers, speakers, tape drives) cannot be safely accessed concurrently without corruption; spooling can mitigate this for specific devices, but not all resources can be spooled.
> 
> 2. **Attacking Hold and Wait**:
>    * *Protocol 1 (Conservative / Hold All)*: A process must request and be allocated all of its required resources prior to execution start; if any resource is unavailable, it waits without holding any.
>      * *Drawback*: Severely reduces resource utilization and system concurrency; processes cannot accurately predict peak requirements in advance.
>    * *Protocol 2 (Release Before Request)*: A process can request resources only when it holds none; before requesting new resources, it must release all currently held allocations.
>      * *Drawback*: High overhead, starvation risk, and low throughput.
> 
> 3. **Attacking No Preemption**:
>    * If a process holding resources requests another resource that cannot be allocated immediately, all its currently held resources are forcibly preempted.
>    * **Infeasibility**: Applicable only to easily saved/restored stateful resources (CPU registers, memory pages); cannot be applied to physical devices like active printers or audio streams without corrupting jobs.
> 
> 4. **Attacking Circular Wait (Linear / Ordered Allocation Protocol)**:
>    * Define a one-to-one indexing function $F: R \to \mathbb{N}$ that assigns a global total ordering to all resource types.
>    * **Enforced Protocol**: A process holding resource $R_i$ can request resource $R_j$ if and only if $F(R_j) > F(R_i)$.
>    * If a process requires a lower-numbered resource $R_k < R_i$, it must first release all $R_m \ge R_k$.
>    * **Result**: Circular wait chains are mathematically impossible ($F(P_0) < F(P_1) < \dots < F(P_0)$ is a contradiction).
>    * **Assessment**: The most practical and widely implemented deadlock prevention technique.
