> [!definition]
> **Sliding Window Protocols** enable pipelined transmission of multiple frames before waiting for an ACK, maximizing link utilization over high Bandwidth-Delay Product ($\text{BDP}$) channels[cite: 2].

| Attribute | Stop-and-Wait | Go-Back-N (GBN) | Selective Repeat (SR) |
| :--- | :--- | :--- | :--- |
| **Sender Window ($W_S$)** | $1$[cite: 1, 2] | $N$ ($W_S = 2^k - 1$)[cite: 1, 2] | $N$ ($W_S = 2^{k-1}$)[cite: 1, 2] |
| **Receiver Window ($W_R$)** | $1$[cite: 1, 2] | $1$[cite: 1, 2] | $W_R = W_S = 2^{k-1}$[cite: 1, 2] |
| **Acknowledgement Type** | Cumulative/Independent | **Cumulative** (Next expected frame)[cite: 2] | **Independent / Selective ACK**[cite: 2] |
| **Out-of-Order Acceptance** | Rejected[cite: 2] | Discarded entirely[cite: 2] | Accepted & buffered in window[cite: 2] |
| **Retransmission on Loss** | Single frame[cite: 2] | Entire window of $N$ unacked frames | Only the corrupted/timed-out frame[cite: 2] |
| **Sender Timers** | 1 timer[cite: 2] | 1 timer (for oldest unacked frame)[cite: 2] | Individual timer per unacked frame[cite: 2] |
| **Total Sequence Numbers** | $2$ ($k=1$ bit)[cite: 2] | $N + 1 \le 2^k \implies W_S + 1$[cite: 2] | $2N \le 2^k \implies W_S + W_R$[cite: 2] |
| **Efficiency ($\eta$)** | $\frac{1}{1 + 2a}$[cite: 1] | $\min\left(1, \frac{W_S}{1 + 2a}\right)$[cite: 2] | $\min\left(1, \frac{W_S}{1 + 2a}\right)$[cite: 1, 2] |

> [!formula]
> **Sequence Number and Window Constraints:**
> 1. General sliding window condition to prevent overlap between new and retransmitted frames:
>    $$W_S + W_R \le 2^k \quad (k = \text{number of bits in sequence field})$$
> 2. For GBN: $W_R = 1 \implies W_S \le 2^k - 1$[cite: 2].
> 3. For SR: $W_S = W_R \implies 2 W_S \le 2^k \implies W_S \le 2^{k-1}$[cite: 1, 2].
> 4. To achieve $100\%$ efficiency ($\eta = 1$):
>    $$W_S \ge 1 + 2a$$
>    $$\text{Minimum bits } k = \lceil \log_2(W_S + W_R) \rceil$$

> [!trap]
> In GBN, an acknowledgment for frame $n$ ($ACK = n+1$) is **cumulative**; it confirms reception of all frames prior to $n+1$[cite: 2]. In SR, acknowledgments are **individual**; losing an ACK does not validate whether subsequent buffered packets arrived safely[cite: 2].

> [!question]
> **Q:** A $128\text{ kbps}$ satellite channel has a one-way propagation delay of $150\text{ ms}$. Frame size is $1\text{ KB}$ ($1024\text{ bytes}$). Assuming an error-free channel and Selective Repeat protocol, what is the minimum number of bits required in the sequence number field to achieve $100\%$ link utilization?  
> (A) 3  
> (B) 4  
> (C) 5  
> (D) 6  
>
> **Answer:** **(B)**  
> **Explanation:**  
> 1. Calculate transmission delay $T_t$[cite: 1]:  
>    $$T_t = \frac{L}{B} = \frac{1024 \times 8\text{ bits}}{128 \times 10^3\text{ bps}} = \frac{8192}{128000} = 0.064\text{ s} = 64\text{ ms}$$  
> 2. Calculate parameter $a$[cite: 1]:  
>    $$a = \frac{T_p}{T_t} = \frac{150\text{ ms}}{64\text{ ms}} = 2.34375$$  
> 3. For $\eta = 100\%$ ($1.0$), sender window $W_S$ must be[cite: 1]:  
>    $$W_S \ge 1 + 2a = 1 + 2(2.34375) = 5.6875 \implies W_S = \lceil 5.6875 \rceil = 6$$  
> 4. For Selective Repeat, $W_R = W_S = 6$[cite: 1].  
>    $$\text{Total Sequence Numbers Needed } N_{\text{seq}} \ge W_S + W_R = 6 + 6 = 12\text{ states}$$  
> 5. Number of bits $k = \lceil \log_2(12) \rceil = 4\text{ bits}$[cite: 1].
