> [!definition]
> * **Two-Phase Locking Protocol (2PL):** A transaction acquires locks during its growing phase and releases locks during its shrinking phase[cite: 2]. Once the first lock is released, no new lock can be requested[cite: 2].
> * **Lock Point:** The point in execution where a transaction holds its final required lock[cite: 2].
> * **Basic TS Ordering:** Serializability order is determined strictly by transaction startup timestamps $TS(T)$[cite: 2].

| Protocol | Guarantees Serializability | Guarantees Strict Recoverable | Deadlock Free | Starvation Free |
| :--- | :--- | :--- | :--- | :--- |
| **Basic 2PL** | Yes (Conflict)[cite: 2] | No[cite: 2] | No[cite: 2] | No[cite: 2] |
| **Strict 2PL** | Yes (Conflict)[cite: 2] | Yes (holds Exclusive locks till commit)[cite: 2] | No[cite: 2] | No[cite: 2] |
| **Rigorous 2PL** | Yes (Conflict)[cite: 2] | Yes (holds All locks till commit)[cite: 2] | No[cite: 2] | No[cite: 2] |
| **Conservative 2PL** | Yes (Conflict)[cite: 2] | No[cite: 2] | Yes (Pre-claims all locks)[cite: 2] | No[cite: 2] |
| **Basic TS Ordering** | Yes (Conflict)[cite: 2] | No[cite: 2] | Yes[cite: 2] | No[cite: 2] |
| **Thomas Write Rule** | Yes (View Serializability)[cite: 2] | No[cite: 2] | Yes[cite: 2] | No[cite: 2] |

> [!theorem]
> **Thomas Write Rule Logic:**
> When transaction $T$ issues $W(Q)$:
> 1. If $R\text{-}TS(Q) > TS(T)$: Rollback $T$[cite: 2].
> 2. If $W\text{-}TS(Q) > TS(T)$: **Ignore the write operation** and continue execution (obsolete write protocol)[cite: 2].
> 3. Otherwise: Execute $W(Q)$, and set $W\text{-}TS(Q) = TS(T)$[cite: 2].

> [!question]
> **PSU CBT Practice Drill:**
> Which of the following concurrency control protocols guarantees View Serializability without strictly ensuring Conflict Serializability, while remaining Deadlock-Free[cite: 2]?
> (A) Strict 2PL[cite: 2]
> (B) Conservative 2PL[cite: 2]
> (C) Thomas Write Rule Timestamp Ordering[cite: 2]
> (D) Rigorous 2PL[cite: 2]
>
> **Step-by-Step Resolution:**
> 1. 2PL variants enforce conflict serializability by constraining graph precedence[cite: 2].
> 2. Conservative 2PL prevents deadlocks, but guarantees conflict serializability[cite: 2].
> 3. Thomas Write Rule allows obsolete writes to be bypassed, producing schedules that are view serializable but not conflict serializable, while remaining deadlock-free since transactions never wait for locks[cite: 2].
>
> **Correct Answer:** (C)[cite: 2]
