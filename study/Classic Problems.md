## Lecture & Conceptual Walkthrough

Synchronization problems represent recurring concurrency archetypes in operating systems. Understanding standard template solutions allows engineers to design robust concurrency controls and identify critical flaws like race conditions, deadlocks, and starvation. 

The three foundational classic synchronization problems covered are:
1. **The Producer-Consumer (Bounded Buffer) Problem**
2. **The Readers-Writers Problem**
3. **The Dining Philosophers Problem**

---

### 1. Producer-Consumer Problem (Bounded Buffer)

> [!definition] Producer-Consumer Paradigm
> A multi-threaded system where one or more **Producer** threads generate data items into a shared finite buffer of size $N$, and one or more **Consumer** threads remove and process data from the buffer.

#### Core System Invariants & Requirements
* **Mutual Exclusion**: Only one thread (producer or consumer) can modify the buffer's internal data structures at any single instant. Buffer operations constitute a **Critical Section (CS)**.
* **No Overflow (Buffer-Full Invariant)**: A producer must block when the buffer contains $N$ items.
* **No Underflow (Buffer-Empty Invariant)**: A consumer must block when the buffer contains $0$ items.
* Production of an item occurs locally before buffering; consumption of an item occurs locally after removal.

```
[ Producer ]                                 [ Consumer ]
|                                            ^
v (local generate)                           | (local consume)
   +-----------------+                          +-----------------+
   | Item in Register|                          | Item in Register|
   +-----------------+                          +-----------------+
|                                            ^
| (append)                          (remove) |
+----------> [ Bounded Buffer ] -------------+
(Size N)
```

#### Semaphore Primitives & State Setup
A simple binary mutex over the buffer satisfies mutual exclusion but fails to coordinate buffer limits (overflow/underflow). To handle capacity constraints alongside mutual exclusion, three semaphores are deployed:

| Semaphore Name | Semaphore Type | Initial Value | Purpose / Invariant Tracked |
| :--- | :--- | :--- | :--- |
| `mutex` | Binary Semaphore | $1$ | Guarantees mutual exclusion over buffer modification. |
| `empty` | Counting Semaphore | $N$ | Tracks available free slots in the buffer. |
| `full` | Counting Semaphore | $0$ | Tracks occupied item slots in the buffer. |

> [!property] Counting Semaphore Invariant
> At any consistent system state:
> $$\text{empty} + \text{full} = N$$
> where $0 \le \text{full} \le N$ and $0 \le \text{empty} \le N$.

#### Implementation
- This implementation allows multiple producers and consumers
- Counting semaphore is used and hence
	- producer and consumer can work anytime (but not update the buffer)
- If we want alternation between producers and consumers `mutex` is not needed

```c
// Shared variables and semaphores
semaphore mutex = 1;
semaphore empty = N;
semaphore full  = 0;

void producer(void) {
while (true) {
/* Produce an item locally */
item_t item = produce_item();

P(empty);       // Line 1: Wait for a free slot (decrement empty)
P(mutex);       // Line 2: Acquire lock for Buffer Critical Section

/* CS: Add item to the shared buffer */
insert_into_buffer(item);

V(mutex);       // Line 3: Release buffer lock
V(full);        // Line 4: Signal new item available (increment full)
}
}

void consumer(void) {
while (true) {
P(full);        // Line 5: Wait for an available item (decrement full)
P(mutex);       // Line 6: Acquire lock for Buffer Critical Section

/* CS: Remove item from the shared buffer */
item_t item = remove_from_buffer();

V(mutex);       // Line 7: Release buffer lock
V(empty);       // Line 8: Signal free slot available (increment empty)

/* Consume the item locally */
consume_item(item);
}
}
```

#### Analytical Breakdown of Edge Cases & Blunders

> [!trap] Swapping Order of Wait Operations ($P(\text{empty}) \leftrightarrow P(\text{mutex})$ or $P(\text{full}) \leftrightarrow P(\text{mutex})$)
> If the order of acquisition is reversed in the producer:
> ```c
> P(mutex);   // Acquired first!
> P(empty);
> ```
> Assume the buffer is completely full ($\text{empty} = 0$). A producer executes `P(mutex)`, successfully acquiring the lock. It then calls `P(empty)` and blocks because $\text{empty} = 0$. 
> A consumer attempting to empty a slot calls `P(full)` followed by `P(mutex)`. However, the consumer blocks on `P(mutex)` because the producer holds it. 
> Result: **Deadlock**. Both processes are blocked indefinitely. 
>
 *Symmetric case*: Swapping the lines 5 and 6 in the consumer leads to deadlock when the buffer is empty ($\text{full} = 0$).
>
 **Rule**: Resource reservation semaphores (`empty`, `full`) must always be evaluated *before* the exclusion lock (`mutex`).

> [!property] Swapping Order of Signal Operations ($V(\text{mutex}) \leftrightarrow V(\text{full})$ or $V(\text{mutex}) \leftrightarrow V(\text{empty})$)
> Swapping line 3 with line 4, or line 7 with line 8, causes **no logical deadlock or correctness issues**. Releasing the mutex before signaling the resource merely affects scheduling efficiency; the mutex is held for an imperceptibly longer interval, slightly increasing contention.

---

### 2. Readers-Writers Problem

> [!definition] Readers-Writers Specification
> Models concurrent access to a shared resource (such as a database or file):
> * **Readers** only read the shared data; multiple readers may access concurrently.
> * **Writers** modify data; a writer requires strictly exclusive access.

#### Concurrency Rules
1. Any number of Readers can read simultaneously:
$$\text{Readers} \ge 0 \implies \text{Writers} = 0$$
2. At most one Writer can write at a time:
$$\text{Writers} = 1 \implies \text{Readers} = 0$$
3. If a writer is in the CS, no reader or writer may enter.

#### Architectural Mechanism
A single mutex across all operations would restrict readers to sequential execution, defeating concurrency. Writers-only mutex protection permits concurrent readers to collide with a writer.

The standard solution uses an integer counter `readcount` that tracks active readers:
* The **first reader** that arrives locks the shared resource against writers.
* Subsequent readers skip locking and enter directly.
* The **last reader** leaving unlocks the shared resource, allowing waiting writers to proceed.

| Variable    | Type             | Initial Value | Function                                                                    |
| :---------- | :--------------- | :------------ | :-------------------------------------------------------------------------- |
| `mutex`     | Binary Semaphore | $1$           | Protects critical updates to the shared `readcount` variable.               |
| `wrt`       | Binary Semaphore | $1$           | Provides mutual exclusion for writers; blocks readers when a writer writes. |
| `readcount` | Integer          | $0$           | Tracks the number of readers currently executing inside the read CS.        |

#### Implementation (First Readers-Writers Problem / Reader Preference)

```c
semaphore mutex = 1;
semaphore wrt   = 1;
int readcount   = 0;

void writer(void) {
while (true) {
P(wrt);             // Acquire exclusive write access

/* Writing occurs */
write_database();

V(wrt);             // Release exclusive write access
}
}

void reader(void) {
while (true) {
// --- Reader Entry Section ---
P(mutex);           // Line 4: Protect readcount
readcount++;        // Line 5: Register new reader
if (readcount == 1) {
P(wrt);         // Line 7: First reader locks out writers
}
V(mutex);           // Line 8: Release readcount lock

/* Reading occurs concurrently */
read_database();    // Line 9: Reader CS

// --- Reader Exit Section ---
P(mutex);           // Line 10: Protect readcount
readcount--;        // Line 11: Reader leaving
if (readcount == 0) {
V(wrt);         // Line 13: Last reader releases writer lock
}
V(mutex);           // Line 14: Release readcount lock
}
}
```

#### Edge Cases, Race Conditions & Structural Variations

> [!trap] Blunder A: Removing `mutex` Protection from `readcount` Updates
> If `readcount++` (line 5) and `readcount--` (line 11) run without `P(mutex)` and `V(mutex)` protection:
> * **Lost Updates / Race Condition**: Multiple reader threads modifying `readcount` simultaneously cause non-atomic read-modify-write operations, corrupting `readcount`.
> * **Negative Readcount**: Unsynchronized decrements can drive `readcount < 0`.
> * **Missed Signals**: If `readcount` fails to register $0$ due to a missed decrement, `V(wrt)` is never called, resulting in **permanent writer starvation / writer deadlock**.

> [!trap] Blunder B: Moving Conditionals Outside the Mutex Protection
> Moving lines 6–7 (`if (readcount == 1) P(wrt);`) or lines 12–13 (`if (readcount == 0) V(wrt);`) outside the `mutex` perimeter creates critical race windows:
> 1. **Premature Unlock**: Assume Reader 1 executes `readcount--` inside the mutex and drops `readcount` to $0$. Reader 1 is preempted *before* checking `if (readcount == 0)`.
> 2. Reader 2 arrives, enters the entry section, increments `readcount` from $0$ to $1$, and proceeds.
> 3. Reader 1 resumes and checks its cached condition or runs the delayed check. If Reader 1 evaluates `readcount == 0` (now false), it fails to execute `V(wrt)`. 
> 4. Conversely, if two readers both decrement to $0$ non-atomically, both might attempt to execute `V(wrt)`, corrupting semaphore state.
> 	1. Similarly wrt to to the `P(wrt)` the first reader's `readcount == 1` may be overwritten thus allowing the value of `wrt` to touch the moon! full concurrecny.
>
 **Rule**: Any evaluation depending on `readcount` must remain inside the critical section managed by `mutex`.

> [!property] Starvation Vulnerability
> The implementation above favors readers: as long as at least one reader remains active ($readcount \ge 1$), incoming readers continue entering immediately while writers queue indefinitely on `P(wrt)`. This leads to **writer starvation**.

---

### 3. Dining Philosophers Problem

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

#### Attempt 1: The Naive Solution (Symmetric Deadlock)
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

#### Deadlock Prevention Strategies

To eliminate deadlock, we must break at least one Coffman condition (typically **Hold and Wait** or **Circular Wait**).

##### Attempt 2: Asymmetric / Knowledgeable Philosopher (Breaking Circular Wait)
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

##### Attempt 3: Atomicity / "Both or None" (Breaking Hold and Wait)
Allow a philosopher to pick up chopsticks only if **both** are simultaneously available. This requires checking availability and claiming both forks inside a mutex-protected critical section.

##### Attempt 4: Capacity Restriction (Pigeonhole Constraint)
Limit the maximum number of philosophers allowed at the table simultaneously to $N-1$ (using a counting semaphore initialized to $N-1$). By the Pigeonhole Principle, with at most $N-1$ philosophers competing for $N$ forks, at least one philosopher is guaranteed to acquire two forks, eat, and release them.

---

### 4. Critical Section Criteria: Theoretical Properties & Mappings

The correctness of any solution addressing mutual exclusion relies on foundational criteria:

> [!definition] Core Synchronization Criteria
> 1. **Mutual Exclusion (Primary)**: If a process is executing in its critical section, no other process may execute in their critical section simultaneously.
> 2. **Progress (Primary)**: If no process is executing in its critical section and some processes wish to enter, only those processes not executing in their remainder sections can participate in deciding who enters next, and this selection cannot be postponed indefinitely. **Progress implies absence of deadlock.**
> 3. **Bounded Waiting (Secondary)**: There must be a bound on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.

#### Key Invariants & Relationships

> [!property] Formal Invariant Equivalences
> * **Progress $\implies$ No Deadlock**: If a system guarantees progress, it cannot enter a deadlock state.
> * **No Deadlock $\centernot\implies$ Progress**: A system may avoid complete deadlock while violating progress (e.g., livelock or strict alternation where a process outside the critical section prevents an active process from entering).
> * **Bounded Waiting $\perp$ Progress**: Bounded Waiting and Progress are mathematically independent. Progress ensures the system moves forward; Bounded Waiting ensures individual fairness.
> * **Starvation-Freedom**:
>   $$\text{Progress} + \text{Bounded Waiting} \implies \text{Starvation-Freedom}$$
>   Progress alone does **not** guarantee starvation-freedom, as an unlucky process can be bypassed indefinitely by other competing processes without violating overall system progress.

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->
