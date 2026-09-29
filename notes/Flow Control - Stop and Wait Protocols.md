## Stop-and-Wait ARQ

In Stop-and-Wait Automatic Repeat reQuest (ARQ), the sender transmits exactly one data frame and halts, awaiting an acknowledgment (ACK) before transmitting the subsequent frame or timing out to retransmit[cite: 1].

```mermaid
sequenceDiagram
    participant S as Sender
    participant R as Receiver
    S->>R: Data Frame 0 (Tt)
    Note over S,R: Propagation (Tp)
    R-->>S: ACK 1 (Tack + Tp)
    Note over S: Total Cycle = Tt + 2Tp
```

> [!formula] Efficiency and Throughput in Stop-and-Wait
> For data frame transmission time $T_t$, round-trip propagation $2T_p$, and negligible ACK transmission time:
> 1. **Round Trip Time (RTT)**:
>    $$\text{RTT} = T_t + 2T_p$$[cite: 1]
> 2. **Link Utilization / Efficiency ($\eta$)**:
>    $$\eta = \frac{\text{Useful Time}}{\text{Total Cycle Time}} = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a}$$[cite: 1]
>    Where $a = \frac{T_p}{T_t}$ is the link latency ratio[cite: 1].
> 3. **Throughput**:
>    $$\text{Throughput} = \eta \times \text{Bandwidth} = \frac{L}{T_t + 2T_p}\text{ bps}$$[cite: 1]

> [!question] Efficiency Calculation Under Distance
> A $1000\text{-mile}$ error-free link operates at $1\text{ Mbps}$ with a propagation delay of $5\text{ }\mu\text{s/mile}$[cite: 1]. Determine link utilization for $1250\text{-byte}$ frames[cite: 1].
> * Total $T_p = 1000 \times 5\text{ }\mu\text{s} = 5000\text{ }\mu\text{s} = 5\text{ ms}$[cite: 1].
> * $T_t = \frac{1250 \times 8\text{ bits}}{10^6\text{ bps}} = \frac{10000}{10^6}\text{ s} = 10\text{ ms}$[cite: 1].
> * Total cycle time $= T_t + 2T_p = 10 + 2(5) = 20\text{ ms}$[cite: 1].
> * Utilization $\eta = \frac{10}{20} = 50\%$[cite: 1].

### Stop-and-Wait Retransmission Under Error

When frames or ACKs drop with independent error probability $p$[cite: 1]:
* Probability of successful transfer per attempt $= 1 - p$[cite: 1].
* The number of attempts follows a geometric distribution with mean:
  $$E[\text{Transmissions per packet}] = \frac{1}{1 - p}$$
[cite: 1]

> [!question] Stop-and-Wait Duration with Retransmissions
> Send a $100\text{ KB}$ file in $1\text{ KB}$ frames[cite: 1]. RTT $= 50\text{ ms}$, Timeout $= 200\text{ ms}$[cite: 1]. Frame loss probability $= 10\%$, ACK loss probability $= 10\%$ (independent)[cite: 1].
> 1. Overall round success probability:
>    $$P_{\text{succ}} = (1 - 0.1)(1 - 0.1) = 0.9 \times 0.9 = 0.81$$[cite: 1]
> 2. Total attempts for $100$ successful deliveries:
>    $$\text{Attempts} = \frac{100}{0.81} \approx 123.46$$[cite: 1]
>    $$\text{Retransmissions} = 123.46 - 100 = 23.46$$[cite: 1]
> 3. Total expected duration:
>    $$\text{Duration} = (100 \times \text{RTT}) + (23.46 \times \text{Timeout}) = (100 \times 50\text{ ms}) + (23.46 \times 200\text{ ms})$$[cite: 1]
>    $$\text{Duration} = 5000\text{ ms} + 4692\text{ ms} = 9692\text{ ms} \approx 9.69\text{ seconds}$$[cite: 1]

The **Timeout** period already includes the RTT of the failed attempt (either consider it as the retransmission time for the failed frames or the time for time taken in orignally trasnfering them, it automatically adjusts)!
When the sender transmits a frame, it starts a single timer initialized to `Timeout = 200 ms`.
```
[t = 0 ms]  Sender transmits Frame. Timer starts running down from 200 ms.
            │
            ├── (If successful): ACK arrives at t = RTT (50 ms). Timer stops!
            │
            └── (If frame or ACK is lost): No ACK arrives. 
                Timer keeps ticking all the way until t = 200 ms.
```
When a loss occurs, the sender spends **a total of 200 ms** waiting before it triggers a retransmission.
It does **NOT** wait $50\text{ ms} + 200\text{ ms} = 250\text{ ms}$. The 200 ms timer _is the entire elapsed wall-clock time_ spent on that failed attempt.

### 4. How High Bandwidth & Long Delay Affect Protocols

In any sliding window protocol, link utilization ($\eta$) depends on the ratio of transmission time ($T_t$) to propagation delay ($T_p$):

$$a = \frac{T_p}{T_t} = \frac{\text{Bandwidth} \times \text{Delay}}{\text{Frame Size}}$$

When a link has **High Bandwidth** and **Long Delay**, $T_p \gg T_t$, meaning **$a$ becomes enormous**.

```
Sender ────────── Packet (Tiny fraction of pipe) ──────────> Receiver
       [ Sender finishes sending in microseconds ]
       [ Sits idle for tens of milliseconds waiting for ACK ]
```

#### A. Stop-and-Wait (Catastrophic Collapse)

- **Rule:** Sender sends exactly $1$ packet and waits for its ACK before sending the next.
    
- **Efficiency:**
    
    $$\eta = \frac{1}{1 + 2a}$$
    
- **On an LFN:** When $a$ is huge (say $a = 1000$), efficiency collapses to:
    
    $$\eta = \frac{1}{1 + 2(1000)} \approx \frac{1}{2001} \approx \mathbf{0.05\%}$$
    
- **Verdict:** Stop-and-Wait is virtually unusable on high-speed, long-distance links.
    

#### B. Go-Back-N (GBN)

- **Rule:** Sender can send up to $N$ packets using cumulative ACKs. If a packet is lost, the sender must **retransmit the entire window of $N$ packets from the lost packet onward**.
    
- **On an LFN:**
    
    - To get $100\%$ link utilization, the window size $N$ must satisfy:
        
        $$N \ge 1 + 2a \quad (\text{Window Size } \ge \text{BDP})$$
        
    - Because $N$ must be thousands of packets wide to fill the LFN pipe, **a single dropped packet forces the sender to retransmit thousands of already-received packets**.
        
    - GBN wastes enormous amounts of high-speed bandwidth re-sending duplicate data.
        

#### C. Selective Repeat (SR)

- **Rule:** Receiver buffers out-of-order packets and independently ACKs individual packets. The sender **only retransmits the single dropped packet**.
    
- **On an LFN:**
    
    - Efficiently handles LFNs because only missing segments cross the wire again.
        
    - **The Trade-Off (Buffer Memory Explosion):** Both sender and receiver require massive window buffers:
        
        $$W_S = W_R = 2^{k-1} \ge \frac{1 + 2a}{2}$$
        
    - When $B \times RTT$ is tens of megabytes, both endpoints must allocate dedicated megabytes of high-speed memory just to maintain the receive and retransmit windows.
        

### Summary Checklist

| **Concept**              | **What It Is** | **Why It Matters / Exam Hook** |
| ------------------------ | -------------- | ------------------------------ |
| **BDP ($B \times RTT$)** | Volume of the  |                                |