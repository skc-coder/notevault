> [!definition] Producer-Consumer Paradigm
> A multi-threaded system where one or more **Producer** threads generate data items into a shared finite buffer of size $N$, and one or more **Consumer** threads remove and process data from the buffer.

## Core System Invariants & Requirements
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

## Semaphore Primitives & State Setup
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

## Implementation
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

## Analytical Breakdown of Edge Cases & Blunders

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
> *Symmetric case*: Swapping the lines 5 and 6 in the consumer leads to deadlock when the buffer is empty ($\text{full} = 0$).
>
> **Rule**: Resource reservation semaphores (`empty`, `full`) must always be evaluated *before* the exclusion lock (`mutex`).

> [!property] Swapping Order of Signal Operations ($V(\text{mutex}) \leftrightarrow V(\text{full})$ or $V(\text{mutex}) \leftrightarrow V(\text{empty})$)
> Swapping line 3 with line 4, or line 7 with line 8, causes **no logical deadlock or correctness issues**. Releasing the mutex before signaling the resource merely affects scheduling efficiency; the mutex is held for an imperceptibly longer interval, slightly increasing contention.
