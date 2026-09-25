# Module 5: Sequential Circuits & Counters (PSU Exam Reference)

---

## 1. Combinational vs. Sequential Circuits

| Feature                 | Combinational Circuits                       | Sequential Circuits                        |
| :---------------------- | :------------------------------------------- | :----------------------------------------- |
| **Output Dependency**   | Present inputs only                          | Present inputs + Past outputs (history)    |
| **Memory Element**      | Not present                                  | Present (Latches / Flip-Flops)             |
| **Feedback Path**       | Absent                                       | Present (mandatory)                        |
| **Clock Signal**        | Not required                                 | Required in synchronous circuits           |
| **Speed**               | Faster (propagation delay only)              | Slower (clock and propagation overhead)    |
| **Hardware Complexity** | Comparatively simpler                        | Complex                                    |
| **Examples**            | Adder, MUX, DEMUX, Decoder, Priority Encoder | Counters, Registers, FSMs, Shift Registers |

---

## 2. SR Latch (NOR & NAND Implementations)

A latch is an unclocked, level-sensitive, bistable multivibrator circuit.

### Cross-Coupled NOR Latch
- Characteristic Equation: $Q_{n+1} = S + R'Q_n$ with constraint $S \cdot R = 0$
- Active **HIGH** inputs.

| $S$ | $R$ |    $Q_{n+1}$     | State / Action           | Remarks                                                             |
| :-: | :-: | :--------------: | :----------------------- | :------------------------------------------------------------------ |
|  0  |  0  |      $Q_n$       | No Change (Hold)         | Latch retains previous state                                        |
|  0  |  1  |        0         | Reset                    | Forced low                                                          |
|  1  |  0  |        1         | Set                      | Forced high                                                         |
|  1  |  1  | 0 (both outputs) | **Invalid / Prohibited** | Violates $Q$ and $Q'$ complementarity; race on $1 \to 0$ transition |

### Cross-Coupled NAND Latch
- Inputs are active **LOW** (often labeled $\bar{S}\text{-}\bar{R}$).
- **Characteristic Equation (Active-Low Form):**
  $$Q_{n+1} = \bar{S}' + \bar{R}Q_n \quad (\text{Constraint: } \bar{S} + \bar{R} \neq 0)$$

- **Characteristic Equation (Active-High Mapping, where $S = \bar{S}'$ and $R = \bar{R}'$):**
  $$Q_{n+1} = S + R'Q_n \quad (\text{Constraint: } S \cdot R = 0)$$

| $\bar{S}$ | $\bar{R}$ |    $Q_{n+1}$     | State / Action           | Remarks                                                           |
| :-------: | :-------: | :--------------: | :----------------------- | :---------------------------------------------------------------- |
|     0     |     0     | 1 (both outputs) | **Invalid / Prohibited** | Both outputs go HIGH; indeterminate next state if switched to 1-1 |
|     0     |     1     |        1         | Set                      | Active-low set activated                                          |
|     1     |     0     |        0         | Reset                    | Active-low reset activated                                        |
|     1     |     1     |      $Q_n$       | No Change (Hold)         | Quiescent state                                                   |

---

## 3. Flip-Flops: Operation, Tables, & Equations

A flip-flop is a clocked, edge-triggered storage element.

### A. SR Flip-Flop
- **Characteristic Equation:** $Q_{n+1} = S + R'Q_n$ (Subject to $SR = 0$)

| $S$ | $R$ | $Q_n$ | $Q_{n+1}$ | State                         |
| :-: | :-: | :---: | :-------: | :---------------------------- |
|  0  |  0  |   0   |     0     | No Change                     |
|  0  |  0  |   1   |     1     | No Change                     |
|  0  |  1  |   0   |     0     | Reset                         |
|  0  |  1  |   1   |     0     | Reset                         |
|  1  |  0  |   0   |     1     | Set                           |
|  1  |  0  |   1   |     1     | Set                           |
|  1  |  1  |   X   |     X     | **Indeterminate / Forbidden** |

### B. D Flip-Flop (Delay / Data / Transparent)
- Built by passing $D$ directly to $S$ and $D'$ to $R$.
- **Characteristic Equation:** $Q_{n+1} = D$

| $D$ | $Q_n$ | $Q_{n+1}$ | State |
| :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | Reset |
| 0 | 1 | 0 | Reset |
| 1 | 0 | 1 | Set |
| 1 | 1 | 1 | Set |

### C. JK Flip-Flop (Universal Flip-Flop)
- Resolves the invalid state of the SR flip-flop by feeding outputs back: $S = J\cdot Q'$, $R = K\cdot Q$.
- **Characteristic Equation:** $Q_{n+1} = J Q_n' + K' Q_n$

| $J$ | $K$ | $Q_n$ | $Q_{n+1}$ | State |
| :---: | :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | 0 | No Change |
| 0 | 0 | 1 | 1 | No Change |
| 0 | 1 | 0 | 0 | Reset |
| 0 | 1 | 1 | 0 | Reset |
| 1 | 0 | 0 | 1 | Set |
| 1 | 0 | 1 | 1 | Set |
| 1 | 1 | 0 | 1 | Toggle ($Q_n'$) |
| 1 | 1 | 1 | 0 | Toggle ($Q_n'$) |

### D. T Flip-Flop (Toggle)
- Obtained by tying $J$ and $K$ inputs together ($J = K = T$).
- **Characteristic Equation:** $Q_{n+1} = T \oplus Q_n = T Q_n' + T' Q_n$

| $T$ | $Q_n$ | $Q_{n+1}$ | State  |
| :-: | :---: | :-------: | :----- |
|  0  |   0   |     0     | Hold   |
|  0  |   1   |     1     | Hold   |
|  1  |   0   |     1     | Toggle |
|  1  |   1   |     0     | Toggle |

---

### Excitation Tables (Crucial for Design Problems)

| $Q_n \to Q_{n+1}$ | $S$ | $R$ | $J$ | $K$ | $D$ | $T$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 $\to$ 0** | 0 | X | 0 | X | 0 | 0 |
| **0 $\to$ 1** | 1 | 0 | 1 | X | 1 | 1 |
| **1 $\to$ 0** | 0 | 1 | X | 1 | 0 | 1 |
| **1 $\to$ 1** | X | 0 | X | 0 | 1 | 0 |

---

## 4. Race-Around Condition, Master-Slave & Edge Triggering

### The Race-Around Condition
- **Definition:** In a level-triggered JK flip-flop, when $J = 1$, $K = 1$, and clock pulse width $t_p > t_{pd}$ (propagation delay of the flip-flop), the output toggles repeatedly within the same clock pulse duration, leaving the final output indeterminate when the clock returns to zero.
- **Occurrence Condition:** 
  $$t_{pd(FF)} < t_p < T_{clk}$$
- **Remedies:**
  1. $t_p < t_{pd}$ (Impractical because propagation delays are inherently small).
  2. Use **Edge-Triggering** (RC differentiating circuit with diode clipping).
  3. Use a **Master-Slave JK Flip-Flop**.

### Master-Slave JK Flip-Flop
- Consists of two cascaded flip-flops:
  - **Master:** Level-triggered, responds during the active clock level ($CLK = 1$).
  - **Slave:** Level-triggered with an inverted clock, responds when $CLK = 0$.
- **Operation:**
  - When $CLK = 1$: Master is enabled, takes inputs $J, K$, and determines internal state. Slave is disabled (isolated).
  - When $CLK = 0$: Master is disabled (inputs isolated). Slave is enabled and copies the master's state to external outputs ($Q, Q'$).
- **Result:** The overall flip-flop behaves as a negative-edge-triggered device. Output updates strictly on the falling edge, eliminating the race-around condition.
- **Data Lock-Out:** Changes at $J, K$ during the clock cycle do not affect the output once the clock goes low.

### Setup and Hold Time
- **Setup Time ($t_s$):** Minimum time for which data inputs must remain stable **before** the active clock edge arrives.
- **Hold Time ($t_h$):** Minimum time for which data inputs must remain stable **after** the active clock edge has passed.
- **Violation:** Leads to **Metastability** (output oscillates or remains at an intermediate logic voltage before settling randomly).

---

## 5. Finite State Machines: Mealy vs. Moore

| Parameter                    | Mealy Machine                                                       | Moore Machine                                                          |
| :--------------------------- | :------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| **Output Depends On**        | Present State AND Present Inputs                                    | Present State ONLY                                                     |
| **Output Timing**            | Asynchronous with clock (can change immediately when input changes) | Synchronous with clock (changes only during state transitions)         |
| **Number of States**         | Requires **fewer or equal** states compared to Moore                | Usually requires **more** states                                       |
| **Hardware Complexity**      | Less hardware (fewer flip-flops)                                    | More hardware                                                          |
| **Glitch Susceptibility**    | High (input variations cause output glitches)                       | Low / Glitch-free outputs                                              |
| **Circuit Speed**            | Reacts faster to inputs                                             | Slower (requires an extra clock edge for input to propagate to output) |
| **Sequence Detector States** | For detecting an $N$-bit sequence: **$N$ states**                   | For detecting an $N$-bit sequence: **$N + 1$ states**                  |

---

## 6. Asynchronous (Ripple) Counters

In ripple counters, only the first flip-flop is driven by an external clock. Every subsequent flip-flop is clocked by the output ($Q$ or $Q'$) of the preceding flip-flop.

### Up-Counter vs. Down-Counter Identification Rules
Let flip-flops be in toggle mode ($T = 1$ or $J = K = 1$):

| Trigger Type | Clock Fed From | Counting Direction |
| :--- | :--- | :--- |
| **Negative Edge Trigger ($\downarrow$)** | Normal output ($Q$) | **UP Counter** |
| **Negative Edge Trigger ($\downarrow$)** | Inverted output ($Q'$) | **DOWN Counter** |
| **Positive Edge Trigger ($\uparrow$)** | Normal output ($Q$) | **DOWN Counter** |
| **Positive Edge Trigger ($\uparrow$)** | Inverted output ($Q'$) | **UP Counter** |

> **Mnemonic:** 
> - Opposites attract: (- edge) + ($Q$) = UP; (+ edge) + ($Q'$) = UP
> - Likes repel: (- edge) + ($Q'$) = DOWN; (+ edge) + ($Q$) = DOWN

### Modulus and Frequency Division
- An $n$-bit counter has $2^n$ natural states: Modulus $\le 2^n$.
- Output frequency at the $k$-th stage:
  $$f_{out} = \frac{f_{in}}{2^k}$$
  For modulus $M$: $f_{out} = \frac{f_{in}}{M}$.

### Mod-N (Truncated) Counter Using Asynchronous Clear
- To construct a Mod-$M$ counter (where $M < 2^n$):
  - Find minimum $n$ such that $2^{n-1} \le M \le 2^n$.
  - Express $M$ in binary.
  - Connect all flip-flop outputs that are logic '1' in state $M$ to an active-low asynchronous clear pin ($\overline{CLR}$) via a **NAND gate**.
  - **Example (Mod-6 counter):** States $0 \to 5$. State 6 ($110_2 = Q_2 Q_1 Q_0$) triggers reset. Connect $Q_2$ and $Q_1$ to a NAND gate whose output drives $\overline{CLR}$.

### Propagation Delay & Maximum Operating Frequency
- Cumulative delay for $n$ flip-flops:
  $$t_{total} = n \cdot t_{pd}$$
- For reliable operation:
  $$T_{clk} \ge n \cdot t_{pd} + t_s \implies f_{max} \le \frac{1}{n \cdot t_{pd}}$$

---

## 7. Synchronous Counters: Analysis & Design

All flip-flops share a single, common clock signal. State transitions occur simultaneously.

### Analysis Procedure
1. Inspect the circuit to write input equations for each flip-flop (e.g., $J_A, K_A, D_B$).
2. Substitute into characteristic equations to obtain next-state equations ($Q_{A(n+1)}, Q_{B(n+1)}$).
3. Construct the state transition table (Present State $\to$ Next State).
4. Draw the State Diagram to determine the counting sequence, modulus, and check for unused states / self-starting behavior.

### Design Procedure
1. Formulate state diagram and state table from specification.
2. Select flip-flop type (T or JK preferred for minimal gate count; D for routing simplicity).
3. Use the **Excitation Table** of the chosen flip-flop to determine the required excitation values for each state transition.
4. Simplify excitation inputs using Karnaugh Maps (treating unused states as don't cares `X`).
5. Realize the logic circuit using combinational gates driving the flip-flop inputs.

### Unused States & Lockout Elimination
- An $n$-bit counter with $M$ states has $(2^n - M)$ unused states.
- **Lockout:** A condition where the counter enters an unused state and continuously cycles among unused states without returning to the main valid sequence.
- **Self-Starting Counter:** A design where, if the counter accidentally powers up in an unused state, it transitions into one of the valid operational states within a finite number of clock cycles.

### Timing Advantage
- Unlike ripple counters, the maximum frequency of a synchronous counter is independent of the number of flip-flops $n$:
  $$T_{clk} \ge t_{pd(FF)} + t_{comb(logic)} + t_{setup} \implies f_{max} = \frac{1}{t_{pd(FF)} + t_{comb} + t_s}$$

---

## 8. Ring Counter vs. Johnson Counter

Both are synchronous shift-register counters formed by cascading $n$ flip-flops.

| Parameter                      | Ring Counter                                   | Twisted Ring / Johnson Counter                       |
| :----------------------------- | :--------------------------------------------- | :--------------------------------------------------- |
| **Feedback Connection**        | Straight feedback: $Q_{last} \to D_0$          | Inverted feedback: $Q'_{last} \to D_0$               |
| **Number of Flip-Flops**       | $n$                                            | $n$                                                  |
| **Modulus (Number of States)** | **$n$**                                        | **$2n$**                                             |
| **Output Waveform Frequency**  | $f_{clk} / n$                                  | $f_{clk} / 2n$                                       |
| **Unused States**              | $2^n - n$                                      | $2^n - 2n$                                           |
| **Starting State (Typical)**   | $1000\dots$ (circulating single '1')           | $0000\dots$ (fills with 1s, then 0s)                 |
| **Self-Starting?**             | No (requires explicit preset logic)            | No (requires initializing logic or correction gates) |
| **Decoding Gates Needed**      | None (each state directly readable from $Q_i$) | Simple 2-input AND/NOR gates                         |

### 4-Bit State Sequences (Illustrative)
- **4-Bit Ring Counter ($MOD = 4$):**
  $$1000 \to 0100 \to 0010 \to 0001 \to 1000 \dots$$
- **4-Bit Johnson Counter ($MOD = 8$):**
  $$0000 \to 1000 \to 1100 \to 1110 \to 1111 \to 0111 \to 0011 \to 0001 \to 0000 \dots$$

---

## Quick Revision Summary (High-Yield Formulae & Edge Cases)

1. **Characteristic Equations:**
   - SR: $Q_{n+1} = S + R'Q_n \quad (SR = 0)$
   - JK: $Q_{n+1} = J Q_n' + K' Q_n$
   - D: $Q_{n+1} = D$
   - T: $Q_{n+1} = T \oplus Q_n$

2. **Excitation Short Cuts ($Q_n \to Q_{n+1}$):**
   - $0 \to 0 \implies (J=0, K=X) \mid (S=0, R=X) \mid D=0 \mid T=0$
   - $0 \to 1 \implies (J=1, K=X) \mid (S=1, R=0) \mid D=1 \mid T=1$
   - $1 \to 0 \implies (J=X, K=1) \mid (S=0, R=1) \mid D=0 \mid T=1$
   - $1 \to 1 \implies (J=X, K=0) \mid (S=X, R=0) \mid D=1 \mid T=0$

3. **Ripple Counter Up/Down Rule:**
   - Positive edge + $Q = \text{Down}$
   - Positive edge + $Q' = \text{Up}$
   - Negative edge + $Q = \text{Up}$
   - Negative edge + $Q' = \text{Down}$

4. **Maximum Frequency Comparison:**
   - Asynchronous: $f_{max} = \frac{1}{n \cdot t_{pd}}$
   - Synchronous: $f_{max} = \frac{1}{t_{pd} + t_{comb} + t_{setup}}$

5. **Shift Register Counters ($n$ flip-flops):**
   - Ring Counter: $\text{States} = n$, $\text{Unused} = 2^n - n$
   - Johnson Counter: $\text{States} = 2n$, $\text{Unused} = 2^n - 2n$
   - Binary Ripple/Sync Counter: $\text{States} = 2^n$, $\text{Unused} = 0$

6. **Sequence Detector FSM:**
   - $N$-bit sequence detector in Mealy: $N$ states
   - $N$-bit sequence detector in Moore: $N + 1$ states
   - Mealy outputs depend on Input + State; Moore outputs depend strictly on State.