> [!question] GATE Examination Conceptual Review
> Evaluate the truth values of the following core propositions:
> 1. *"In deadlock prevention, the request for resources is always granted if the resulting state is safe."*
>    * **False**: This is the precise definition of **Deadlock Avoidance**, not Deadlock Prevention. Prevention relies on structural request protocols and does not evaluate safe states dynamically.
> 2. *"Deadlock avoidance requires a priori knowledge of resource requests."*
>    * **True**: It mandates knowledge of every process's declared maximum potential requirements ($\text{Max}$ matrix).
> 3. *"Deadlock avoidance is less restrictive than deadlock prevention."*
>    * **True**: Prevention imposes static conditions (such as rigid ordering or prohibiting hold-and-wait) that reject valid requests even when safe, leading to lower utilization. Avoidance permits flexible access patterns as long as a safe completion path exists.

> [!theorem] Efficiency and Restrictiveness Spectrum
> The strategies exist along a strict trade-off axis balancing run-time overhead against resource utilization:
> 
> | Feature | Deadlock Prevention | Deadlock Avoidance | Deadlock Detection |
> | :--- | :--- | :--- | :--- |
> | **Resource Utilization** | Lowest (highly conservative). | Moderate to High. | Highest (resources allocated freely until locked). |
> | **Knowledge Needed** | None. | Declared peak demands ($\text{Max}$ matrix). | Current pending requests ($\text{Request}$ matrix). |
> | **Runtime Algorithm Cost** | Low (protocol validation). | High (evaluates safety on every single request). | Periodic invocation cost. |
> | **Main Inefficiency** | Rejects requests due to structural rules. | Rejects unsafe states that might never actually deadlock. | Cost of preemption, rollbacks, and aborted processes. |
