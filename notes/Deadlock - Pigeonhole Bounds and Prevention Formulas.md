> [!theorem] The Pigeonhole Deadlock-Free Guarantee
> Consider $n$ competing processes and a pool of $R$ identical, reusable instances of a single resource type.
> Let process $P_i$ require a maximum of $\text{max}_i$ resource instances to complete.
> * **Worst-Case Allocation (Deadlock State)**: Each process $P_i$ is allocated exactly $(\text{max}_i - 1)$ instances and is waiting for its final $1$ instance.
> * The system is completely deadlocked if all resources are exhausted in this state:
>   $$R_{\text{deadlock}} = \sum_{i=1}^{n} (\text{max}_i - 1)$$
> * **Deadlock-Free Invariant**: To guarantee that deadlock **can never occur**, the total available resource units $R$ must exceed the worst-case allocation by at least $1$ additional resource (so at least one process can finish, release all its held resources, and trigger a cascade of completions):
>   $$R \ge \sum_{i=1}^{n} (\text{max}_i - 1) + 1$$

> [!formula] Uniform Demand Specialization
> When all $n$ processes have the identical maximum demand $k$ (i.e., $\text{max}_i = k$ for all $i$):
> $$R \ge n(k - 1) + 1$$
> Solving for the maximum allowable peak demand $k$:
> $$n(k - 1) + 1 \le R \implies k \le \left\lfloor \frac{R - 1}{n} \right\rfloor + 1$$
> Solving for the maximum concurrent processes $n$ supported:
> $$n(k - 1) + 1 \le R \implies n \le \left\lfloor \frac{R - 1}{k - 1} \right\rfloor$$

> [!question] GATE CSE 1993: Homogeneous Competing Processes
> A computer system has $3$ processes sharing $4$ instances of the same resource type. Each process can request a maximum of $k$ instances. What is the largest value of $k$ that will always avoid deadlock?
> 
> **Derivation**:
> * Number of processes $n = 3$, Total resources $R = 4$.
> * Allocate $(k - 1)$ to each process, plus $1$ extra to guarantee progress:
>   $$3(k - 1) + 1 \le 4$$
>   $$3(k - 1) \le 3 \implies k - 1 \le 1 \implies k \le 2$$
> * Largest value of $k = \mathbf{2}$.

> [!question] GATE Question: Competing Tape Drives
> A computer system has $6$ tape drives with $n$ processes competing for them. Each process may need a maximum of $3$ tape drives. What is the maximum value of $n$ to guarantee no deadlock?
> 
> **Derivation**:
> * Total resources $R = 6$, per-process peak demand $k = 3$.
> * Worst-case demand per process $= k - 1 = 3 - 1 = 2$.
> * Deadlock-free formula:
>   $$n(3 - 1) + 1 \le 6 \implies 2n + 1 \le 6 \implies 2n \le 5 \implies n \le 2.5$$
> * Since $n$ must be an integer: $\mathbf{n = 2}$.

> [!question] GATE CSE 1993: Variable Peak Demands
> A system has $m$ resources of the same type shared by $3$ processes $A, B, C$ having peak demands of $3, 4,$ and $6$ respectively. For what value of $m$ will deadlock not occur?
> 
> **Derivation**:
> * Max requirements: $\text{max}_A = 3$, $\text{max}_B = 4$, $\text{max}_C = 6$.
> * Total worst-case non-progress allocation:
>   $$(3 - 1) + (4 - 1) + (6 - 1) = 2 + 3 + 5 = 10$$
> * If $m \le 10$, a deadlock state is possible.
> * To guarantee deadlock can never occur:
>   $$m \ge 10 + 1 \implies \mathbf{m \ge 11}$$

> [!question] GATE CSE Standard Property: Sum of Demands Bound
> Suppose $n$ processes share $m$ identical resource units, and the peak requirement of process $P_i$ is $s_i$ where $s_i > 0$. Which condition is sufficient to ensure that deadlock will never occur?
> 
> **Mathematical Proof**:
> * By the Pigeonhole allocation invariant, deadlock-free execution requires:
>   $$\sum_{i=1}^{n} (s_i - 1) + 1 \le m$$
> * Expanding the summation:
>   $$\left( \sum_{i=1}^{n} s_i - \sum_{i=1}^{n} 1 \right) + 1 \le m \implies \sum_{i=1}^{n} s_i - n + 1 \le m$$
>   $$\sum_{i=1}^{n} s_i \le m + n - 1 \iff \mathbf{\sum_{i=1}^{n} s_i < m + n}$$

> [!question] GATE CSE 2006: Deadlock State Snapshot Analysis
> Consider a snapshot of a system running $n$ processes where all instances of resource type $R$ are fully occupied. Each process $P_i$ is currently holding $x_i$ instances and has placed a pending request for $y_i$ additional instances ($y_i > 0$). Which condition is sufficient to guarantee that the system is **not currently in deadlock**?
> 
> **Analysis**:
> * If there exist any two processes $P_p$ and $P_q$ such that $y_p + y_q = 0$ (or if any process has no further pending requests: $y_i = 0$), then that process can execute to completion and release its held resources.
> * However, the system currently being deadlock-free does not guarantee that future deadlock is impossible without further coordination.
