> [!definition]
> **Multiple Access Control (MAC)** protocols govern transmission access across broadcast links. 
> - **ALOHA:** Random-access packet transmission without initial carrier sensing[cite: 2].
> - **CSMA/CD:** Carrier Sense Multiple Access with Collision Detection, where stations listen before transmitting and abort immediately upon detecting collision[cite: 2].

| Protocol | Vulnerable Period | Maximum Channel Throughput ($S_{\max}$) | Optimal Traffic Load ($G$) |
| :--- | :--- | :--- | :--- |
| **Pure ALOHA** | $2 \cdot T_t$[cite: 2] | $\frac{1}{2e} \approx 18.4\%$[cite: 1, 2] | $G = 0.5$[cite: 1, 2] |
| **Slotted ALOHA** | $1 \cdot T_t$[cite: 2] | $\frac{1}{e} \approx 36.8\%$[cite: 1, 2] | $G = 1.0$[cite: 2] |
| **CSMA/CD** | $2 \cdot T_p$ | $\eta = \frac{1}{1 + 6.44a}$[cite: 2] | Dynamic via Backoff ($K \cdot 2T_p$)[cite: 2] |

> [!formula]
> 1. **Throughput Equations:**
>    - Pure ALOHA: $S = G \cdot e^{-2G}$[cite: 1, 2]
>    - Slotted ALOHA: $S = G \cdot e^{-G}$[cite: 1, 2]
> 2. **CSMA/CD Collision Condition (The Golden Invariant):**  
>    To guarantee collision detection before the transmitter finishes placing the packet on the wire[cite: 1, 2]:
>    $$T_t \ge 2 \cdot T_p$$
>    $$\frac{L_{\min}}{B} \ge 2 \cdot \frac{d}{v} \implies L_{\min} = 2 \cdot \frac{d}{v} \cdot B$$
>    *(If a jamming signal duration $T_{\text{jam}}$ is specified)*[cite: 2]:
>    $$T_t \ge 2 \cdot T_p + T_{\text{jam}}$$

> [!trap]
> In CSMA/CD, if cable length ($d$) is doubled, $L_{\min}$ must be **doubled** to maintain detection[cite: 1]. If channel bandwidth ($B$) is doubled, $L_{\min}$ must also **double**[cite: 1]. If transmission rate increases without resizing $L_{\min}$, collisions cannot be detected, violating the MAC standard[cite: 1].

> [!question]
> **Q:** In an Ethernet network operating at $1\text{ Gbps}$ over a $1\text{ km}$ cable with a signal velocity $v = 2 \times 10^8\text{ m/s}$, what is the minimum frame size required for reliable collision detection?  
> (A) 1250 bytes  
> (B) 2500 bytes  
> (C) 10000 bits  
> (D) 5000 bits  
>
> **Answer:** **(C)**  
> **Explanation:**  
> 1. Compute propagation delay $T_p$[cite: 1]:  
>    $$T_p = \frac{d}{v} = \frac{1000\text{ m}}{2 \times 10^8\text{ m/s}} = 5 \times 10^{-6}\text{ s} = 5\ \mu\text{s}$$  
> 2. Apply $T_t \ge 2 T_p$[cite: 1]:  
>    $$\frac{L_{\min}}{B} \ge 2 \times (5 \times 10^{-6}\text{ s}) = 10 \times 10^{-6}\text{ s}$$  
> 3. Calculate $L_{\min}$[cite: 1]:  
>    $$L_{\min} = 10^{-5}\text{ s} \times 10^9\text{ bps} = 10,000\text{ bits} = 1250\text{ bytes}$$  
> Both $10,000\text{ bits}$ and $1250\text{ bytes}$ are equivalent; matching option (C)[cite: 1].
