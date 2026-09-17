> [!definition] Dining Philosophers Model
> $N$ philosophers sit around a circular table with $N$ chopsticks (or forks) arranged such that each chopstick lies between two adjacent philosophers. A philosopher alternates between thinking and eating. To eat, a philosopher must acquire both the left and right chopsticks.

```
P_0
(1) /   \ (0)
P_4   P_1
(4) \   / (1)
P_3---P_2
(2)
Philosopher P_i shares:
Left Fork  = i
Right Fork = (i + 1) % N
```

## Attempt 1: The Naive Solution (Symmetric Deadlock)
Every philosopher $P_i$ grabs the left fork first, then grabs the right fork:

```c
semaphore fork[N] = {1, 1, ..., 1};

void philosopher(int i) {
    while (true) {
        think();
        P(fork[i]);                 // Pick up left fork
        P(fork[(i + 1) % N]);       // Pick up right fork

        eat();

        V(fork[(i + 1) % N]);       // Put down right fork
        V(fork[i]);                 // Put down left fork
    }
}
```

> [!trap] Circular Wait Deadlock
> If all $N$ philosophers become hungry simultaneously and every philosopher picks up their left fork `fork[i]` at the exact same moment:
> * Each philosopher holds their left fork.
> * Each philosopher blocks indefinitely waiting for their right fork `fork[(i + 1) % N]`.
> * This satisfies all 4 Coffman conditions (Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait), triggering a **total system deadlock**.

## Deadlock Prevention Strategies

To eliminate deadlock, we must break at least one Coffman condition (typically **Hold and Wait** or **Circular Wait**).

### Attempt 2: Asymmetric / Knowledgeable Philosopher (Breaking Circular Wait)
Break the symmetry of resource allocation. Number philosophers from $0$ to $N-1$:
* Philosophers $P_0$ through $P_{N-2}$ pick up the **left fork first**, then the right.
* The last philosopher $P_{N-1}$ (the "odd/imposter" philosopher) picks up the **right fork first**, then the left.

```c
void philosopher(int i) {
    while (true) {
        think();
        if (i == N - 1) {
            P(fork[(i + 1) % N]);   // Pick right first
            P(fork[i]);             // Pick left second
        } else {
            P(fork[i]);             // Pick left first
            P(fork[(i + 1) % N]);   // Pick right second
        }

        eat();

        V(fork[i]);
        V(fork[(i + 1) % N]);
    }
}
```
*Result*: Eliminates the cycle in the Resource Allocation Graph (RAG). **Deadlock-free and starvation-free** under a fair scheduler.

### Attempt 3: Atomicity / "Both or None" (Breaking Hold and Wait)
Allow a philosopher to pick up chopsticks only if **both** are simultaneously available. This requires checking availability and claiming both forks inside a mutex-protected critical section.

### Attempt 4: Capacity Restriction (Pigeonhole Constraint)
Limit the maximum number of philosophers allowed at the table simultaneously to $N-1$ (using a counting semaphore initialized to $N-1$). By the Pigeonhole Principle, with at most $N-1$ philosophers competing for $N$ forks, at least one philosopher is guaranteed to acquire two forks, eat, and release them.
