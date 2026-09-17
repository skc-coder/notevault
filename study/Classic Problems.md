## Classic Concurrency & Synchronization Problems

Synchronization problems represent recurring concurrency archetypes in operating systems. Understanding standard template solutions allows engineers to design robust concurrency controls and identify critical flaws like race conditions, deadlocks, and starvation.

### Core Synchronization Subtopics & Atomic Notes
- [[producer-consumer-problem]] - Bounded buffer, counting semaphores (`empty`, `full`, `mutex`), and deadlock wait-order traps.
- [[readers-writers-problem]] - Reader preference model, `readcount` invariant, writer lockout, and preemption/race condition edge cases.
- [[dining-philosophers-problem]] - Resource contention, naive circular wait deadlock, asymmetric imposter strategy, and capacity limits.
- [[synchronization-criteria-invariants]] - Mutual Exclusion, Progress, Bounded Waiting, and formal equivalence proofs.

---

## 1. Producer-Consumer Problem (Bounded Buffer)
![[producer-consumer-problem]]

---

## 2. Readers-Writers Problem
![[readers-writers-problem]]

---

## 3. Dining Philosophers Problem
![[dining-philosophers-problem]]

---

## 4. Critical Section Criteria & Invariants
![[synchronization-criteria-invariants]]
