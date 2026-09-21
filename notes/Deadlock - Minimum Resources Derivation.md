> [!theorem] The Pigeonhole Deadlock Prevention Invariant
> To guarantee that a system running $n$ concurrent processes will **never enter a deadlock**, the total available resource count $R$ must exceed the maximum worst-case allocation state where every process is stuck waiting for its final required unit[cite: 1].
> 
> If process $P_i$ requires a maximum of $Max_i$ resource units:
> * The worst-case non-deadlocking saturation occurs when every process $P_i$ holds $(Max_i - 1)$ units and none can proceed[cite: 1].
> * Adding just $1$ additional resource to this state guarantees that at least one process receives its full demand, finishes, and releases all its held resources back to the pool[cite: 1].

> [!formula] Minimum Resources to Avoid Deadlock
> For $n$ processes with maximum demands $Max_1, Max_2, \dots, Max_n$:
> $$R \ge \sum_{i=1}^{n} (Max_i - 1) + 1$$[cite: 1]
> 
> Conversely, if all $n$ processes have an identical peak demand $k$ ($Max_i = k$ for all $i$):
> $$R \ge n(k - 1) + 1$$[cite: 1]

> [!question] GATE Problem: Identical Demand per Process
> A system has $3$ processes sharing a resource type[cite: 1]. Each process requires a maximum of $k$ instances[cite: 1]. The system has $4$ total resource instances[cite: 1]. What is the largest value of $k$ that guarantees deadlock-free operation[cite: 1]?
> 
> **Mathematical Derivation**:
> * Number of processes $n = 3$[cite: 1].
> * Total resources $R = 4$[cite: 1].
> * Deadlock-free condition:
>   $$\sum (Max_i - 1) + 1 \le R$$[cite: 1]
>   $$3(k - 1) + 1 \le 4$$[cite: 1]
>   $$3k - 3 + 1 \le 4 \implies 3k - 2 \le 4 \implies 3k \le 6 \implies k \le 2$$[cite: 1]
> * For $k = 1$ or $k = 2$, deadlock is impossible[cite: 1].
> * The largest value of $k$ is **$2$**[cite: 1].

> [!question] GATE CS 1993: Maximum Processes Guaranteeing No Deadlock
> A computer system has $6$ tape drives with $n$ processes competing for them[cite: 1]. Each process may need a maximum of $3$ tape drives[cite: 1]. What is the maximum value of $n$ for which the system is guaranteed to be deadlock-free[cite: 1]?
> 
> **Mathematical Derivation**:
> * Total resources $R = 6$, $Max_i = 3$ for each process[cite: 1].
> * Condition to prevent deadlock:
>   $$n(Max - 1) + 1 \le R$$[cite: 1]
>   $$n(3 - 1) + 1 \le 6$$[cite: 1]
>   $$2n + 1 \le 6 \implies 2n \le 5 \implies n \le 2.5$$[cite: 1]
> * Since $n$ must be an integer, the maximum value of $n$ is **$2$**[cite: 1].

> [!question] GATE CS 1998: Variable Demand Resource Bound
> Consider a system with $m$ identical resource units shared by $3$ processes $A$, $B$, and $C$, which have peak demands of $3$, $4$, and $6$ respectively[cite: 1]. For what minimum value of $m$ will deadlock never occur[cite: 1]?
> 
> **Mathematical Derivation**:
> * Peak demands: $Max_A = 3$, $Max_B = 4$, $Max_C = 6$[cite: 1].
> * Saturated allocation where all processes are blocked:
>   $$R_{blocked} = (3 - 1) + (4 - 1) + (6 - 1) = 2 + 3 + 5 = 10\text{ units}$$[cite: 1]
> * Adding $1$ extra unit guarantees completion:
>   $$m \ge 10 + 1 = 11$$[cite: 1]
> * If $m \le 10$, deadlock is possible; hence minimum $m = \mathbf{11}$[cite: 1].

> [!question] General Inequality Proof for $n$ Processes
> Suppose $n$ processes share $m$ identical resource units where peak requirement of $P_i$ is $s_i$ ($s_i > 0$)[cite: 1]. Derive the condition sufficient to ensure no deadlock can occur[cite: 1].
> 
> **Proof**:
> * Worst-case allocation without completion:
>   $$\sum_{i=1}^{n} (s_i - 1) + 1 \le m$$[cite: 1]
>   $$\sum_{i=1}^{n} s_i - \sum_{i=1}^{n} 1 + 1 \le m$$[cite: 1]
>   $$\sum_{i=1}^{n} s_i - n + 1 \le m$$[cite: 1]
>   $$\sum_{i=1}^{n} s_i \le m + n - 1 \iff \mathbf{\sum_{i=1}^{n} s_i < m + n}$$[cite: 1]
