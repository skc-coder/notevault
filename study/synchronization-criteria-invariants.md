> [!definition] Core Synchronization Criteria
> 1. **Mutual Exclusion (Primary)**: If a process is executing in its critical section, no other process may execute in their critical section simultaneously.
> 2. **Progress (Primary)**: If no process is executing in its critical section and some processes wish to enter, only those processes not executing in their remainder sections can participate in deciding who enters next, and this selection cannot be postponed indefinitely. **Progress implies absence of deadlock.**
> 3. **Bounded Waiting (Secondary)**: There must be a bound on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.

## Key Invariants & Relationships

> [!property] Formal Invariant Equivalences
> * **Progress $\implies$ No Deadlock**: If a system guarantees progress, it cannot enter a deadlock state.
> * **No Deadlock $\centernot\implies$ Progress**: A system may avoid complete deadlock while violating progress (e.g., livelock or strict alternation where a process outside the critical section prevents an active process from entering).
> * **Bounded Waiting $\perp$ Progress**: Bounded Waiting and Progress are mathematically independent. Progress ensures the system moves forward; Bounded Waiting ensures individual fairness.
> * **Starvation-Freedom**:
>   $$\text{Progress} + \text{Bounded Waiting} \implies \text{Starvation-Freedom}$$
>   Progress alone does **not** guarantee starvation-freedom, as an unlucky process can be bypassed indefinitely by other competing processes without violating overall system progress.
