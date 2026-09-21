> [!definition]
> - **Clock Cycle Time ($T_p$)**: The time between successive clock pulses in a pipeline, determined by the slowest stage plus interface latch delay ($d$).
> - **Speedup ($S$)**: The ratio of execution time on a non-pipelined processor to that on a pipelined processor.

> [!formula]
> **Core Pipeline Formulas**:
> 1. **Pipeline Cycle Time**:
>    $$T_p = \max(t_1, t_2, \dots, t_k) + d$$
> 2. **Total Execution Time for $n$ Instructions on $k$ Stages**:
>    $$T_{\text{pipe}} = [k + (n - 1) + N_{\text{stalls}}] \cdot T_p$$
> 3. **Non-Pipelined Time ($T_n$)**:
>    $$T_{\text{non-pipe}} = n \cdot k \cdot T_p \quad \text{(or } n \sum t_i\text{)}$$
> 4. **Speedup ($S$)**:
>    $$S = \frac{T_{\text{non-pipe}}}{T_{\text{pipe}}} = \frac{n \cdot k}{k + (n - 1) + N_{\text{stalls}}}$$
>    $$\text{Asymptotic Maximum Speedup: } \lim_{n \to \infty} S = \frac{k}{\text{CPI}_{\text{pipe}}}$$
> 5. **Pipeline Efficiency ($\eta$) and Throughput ($W$)**:
>    $$\eta = \frac{S}{k} = \frac{n}{k + (n - 1) + N_{\text{stalls}}}$$
>    $$W = \frac{n}{T_{\text{pipe}}} \xrightarrow{n \to \infty} \frac{1}{T_p} = f$$

> [!formula]
> **Effective CPI with Stall Hazards**:
> $$\text{CPI}_{\text{eff}} = 1 + \text{Stall Cycles per Instruction} = 1 + \sum (p_i \times b_i)$$
> Where $p_i$ is the frequency of hazard event $i$, and $b_i$ is its penalty in stall cycles.

> [!trap]
> Latch delays accumulate differently in non-pipelined vs pipelined systems. In a pipelined system, each stage adds latch delay $d$. When calculating speedup against a non-pipelined system, verify whether the non-pipelined machine includes latch delay $d$ (usually non-pipelined systems use pure combinational logic with a single output latch).

> [!question]
> A 5-stage pipeline has stage delays of $2\text{ ns}$, $3\text{ ns}$, $7\text{ ns}$, $4\text{ ns}$, and $3\text{ ns}$. The interface register latch delay is $1\text{ ns}$. What is the total time required to execute 100 instructions on this pipeline in the absence of hazards?
> - (A) $800\text{ ns}$
> - (B) $832\text{ ns}$
> - (C) $1040\text{ ns}$
> - (D) $500\text{ ns}$
>
> **Correct Option**: **(B)**
> **Step-by-Step Calculation**:
> 1. Determine cycle time $T_p$:
>    $$T_p = \max(2, 3, 7, 4, 3) + 1 = 7 + 1 = 8\text{ ns}$$
> 2. Calculate clock cycles for $n = 100, \; k = 5$:
>    $$\text{Cycles} = k + (n - 1) = 5 + (100 - 1) = 104\text{ cycles}$$
> 3. Calculate total execution time:
>    $$T_{\text{pipe}} = 104 \times 8\text{ ns} = \mathbf{832\text{ ns}}$$
