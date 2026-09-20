> [!theorem] Comprehensive Strategy Trade-Off Comparison
> The four strategies exhibit distinct trade-offs between runtime overhead, hardware utilization, and implementation complexity[cite: 1]:
> 
> | Strategy | A Priori Knowledge Needed? | Resource Utilization | Runtime Overhead | Recovery Overhead |
> | :--- | :--- | :--- | :--- | :--- |
> | **Ignorance** | None[cite: 1] | High (until deadlock hits)[cite: 1] | None[cite: 1] | Manual reboot / Data loss[cite: 1] |
> | **Prevention** | None[cite: 1] | **Very Low** (rigid constraints like resource ordering or simultaneous request)[cite: 1] | Low (enforced at compile/request time)[cite: 1] | None (deadlock never occurs)[cite: 1] |
> | **Avoidance** | **Yes** (Peak maximum claims per process)[cite: 1] | Medium-High[cite: 1] | **High** (evaluates safety algorithm on every grant)[cite: 1] | None (prevents unsafe states)[cite: 1] |
> | **Detection & Recovery** | None (evaluates current requests)[cite: 1] | High[cite: 1] | Periodic (detection runs on interval)[cite: 1] | High (process termination, rollbacks, victim preemption)[cite: 1] |
