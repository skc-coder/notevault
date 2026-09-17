> [!definition] Readers-Writers Specification
> Models concurrent access to a shared resource (such as a database or file):
> * **Readers** only read the shared data; multiple readers may access concurrently.
> * **Writers** modify data; a writer requires strictly exclusive access.

## Concurrency Rules
1. Any number of Readers can read simultaneously:
$$\text{Readers} \ge 0 \implies \text{Writers} = 0$$
2. At most one Writer can write at a time:
$$\text{Writers} = 1 \implies \text{Readers} = 0$$
3. If a writer is in the CS, no reader or writer may enter.

## Architectural Mechanism
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

## Implementation (First Readers-Writers Problem / Reader Preference)

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

## Edge Cases, Race Conditions & Structural Variations

> [!trap] Blunder A: Removing `mutex` Protection from `readcount` Updates
> If `readcount++` (line 5) and `readcount--` (line 11) run without `P(mutex)` and `V(mutex)` protection:
> * **Lost Updates / Race Condition**: Multiple reader threads modifying `readcount` simultaneously cause non-atomic read-modify-write operations, corrupting `readcount`.
> * **Negative Readcount**: Unsynchronized decrements can drive `readcount < 0`.
> * **Missed Signals**: If `readcount` fails to register $0$ due to a missed decrement, `V(wrt)` is never called, resulting in **permanent writer starvation / writer deadlock**.

> [!danger] Blunder B: Moving Conditionals Outside the Mutex Perimeter
> Placing the conditional checks for `readcount` outside the critical section governed by `mutex` breaks synchronization guarantees in two critical areas:

### 1. Exit Section: Moving `if (readcount == 0) V(wrt);` Outside
* **Deadlock via Preemption:** 
  1. Reader 1 decrements `readcount` to `0` inside the mutex and exits the critical section.
  2. Reader 1 is preempted before evaluating `if (readcount == 0)`.
  3. Reader 2 enters, acquires `mutex`, increments `readcount` from `0` to `1`, and enters the critical section.
  4. Reader 1 resumes and evaluates `readcount == 0`, which is now `false`. Reader 1 exits without signaling `V(wrt)`.
  5. `wrt` remains permanently locked, causing writers to deadlock.
* **Semaphore Corruption / Mutual Exclusion Violation:**
  * If two departing readers evaluate `readcount` concurrently outside the mutex, both might evaluate the condition as valid and invoke `V(wrt)` twice, artificially incrementing the semaphore and permitting multiple writers into the critical section simultaneously with readers.

---

### 2. Entry Section: Moving `if (readcount == 1) P(wrt);` Outside
* **Bypassing the Writer Lock:**
  1. Reader 1 increments `readcount` to `1` inside the mutex and exits before executing `P(wrt)`.
  2. Reader 2 arrives, enters the mutex, increments `readcount` to `2`, and exits the mutex.
  3. Reader 2 checks `if (readcount == 1)`, which evaluates to `false`, so it bypasses `P(wrt)` and enters the critical section directly.
  4. Reader 1 is preempted or delayed before calling `P(wrt)`.
  5. Writers can now enter the critical section concurrently with Reader 2, completely violating mutual exclusion.

> [!important] Core Invariant
> Any read, write, or conditional evaluation depending on `readcount` must remain strictly inside the critical section protected by `mutex`.

> [!property] Starvation Vulnerability
> The implementation above favors readers: as long as at least one reader remains active ($readcount \ge 1$), incoming readers continue entering immediately while writers queue indefinitely on `P(wrt)`. This leads to **writer starvation**.
