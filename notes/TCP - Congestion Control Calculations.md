> [!question] Step-by-Step Reno Window Trajectory
> Consider a TCP connection with an initial $\text{ssthresh} = 32\text{ KB}$ and initial $\text{cwnd} = 1\text{ MSS} = 2\text{ KB}$[cite: 1].
> * The connection experiences a **Timeout** when `cwnd` reaches $32\text{ KB}$[cite: 1].
> * How long (in RTTs and ms) does it take for `cwnd` to recover back to $32\text{ KB}$ if $\text{RTT} = 100\text{ ms}$ and no further loss occurs[cite: 1]?

* **Step 1: Calculate state immediately following Timeout at $\text{cwnd} = 32\text{ KB} = 16\text{ MSS}$**:
  $$\text{ssthresh} = \frac{\text{cwnd}}{2} = \frac{16\text{ MSS}}{2} = 8\text{ MSS} = 16\text{ KB}$$
[cite: 1]
  $$\text{cwnd} = 1\text{ MSS} = 2\text{ KB}$$
[cite: 1]
* **Step 2: Slow Start Growth ($\text{cwnd} \to \text{ssthresh} = 8\text{ MSS}$)**:
  * Start: $\text{cwnd} = 1\text{ MSS}$
  * After RTT 1: $\text{cwnd} = 2\text{ MSS}$
  * After RTT 2: $\text{cwnd} = 4\text{ MSS}$
  * After RTT 3: $\text{cwnd} = 8\text{ MSS} = \text{ssthresh}$[cite: 1]
* **Step 3: Congestion Avoidance Growth ($\text{cwnd} \ge 8\text{ MSS}$)**:
  From $8\text{ MSS}$ to $16\text{ MSS}$ requires additive increments ($+1\text{ MSS}$ per RTT)[cite: 1]:
  $$\Delta \text{cwnd} = 16 - 8 = 8\text{ MSS} \implies 8\text{ additional RTTs}$$
[cite: 1]
* **Total Time**:
  $$\text{Total RTTs} = 3\text{ (Slow Start)} + 8\text{ (Congestion Avoidance)} = 11\text{ RTTs}$$
[cite: 1]
  $$\text{Total Time} = 11 \times 100\text{ ms} = \mathbf{1100\text{ ms}}$$
[cite: 1]

---

> [!question] File Transfer Volume over TCP
> A sender transfers a $250{,}000\text{-Byte}$ file over TCP with $\text{MSS} = 1000\text{ Bytes}$ and no network packet loss[cite: 1]. Initial $\text{cwnd} = 1\text{ MSS}$ and $\text{ssthresh}$ is large[cite: 1]. How many RTTs are required to transmit the entire file, including the connection setup handshake[cite: 1]?

* **Step 1: Connection Setup**:
  * 3-way handshake consumes $1\text{ RTT}$[cite: 1]. Data can be piggybacked on the 3rd packet or sent immediately in the subsequent burst[cite: 1].
* **Step 2: Determine total MSS chunks to transfer**:
  $$\text{Total Segments} = \frac{250{,}000\text{ B}}{1000\text{ B}} = 250\text{ MSS}$$
[cite: 1]
* **Step 3: Trace exponential slow-start delivery per RTT**:

| RTT Index | Operation / Phase | Segments Sent This RTT | Cumulative Segments Sent |
| :--- | :--- | :--- | :--- |
| $\text{RTT}_0$ | Connection Setup (3-way handshake) | $0\text{ data}$[cite: 1] | $0$[cite: 1] |
| $\text{RTT}_1$ | Data Transmission ($\text{cwnd} = 1$) | $1\text{ MSS}$[cite: 1] | $1$[cite: 1] |
| $\text{RTT}_2$ | Data Transmission ($\text{cwnd} = 2$) | $2\text{ MSS}$[cite: 1] | $3$[cite: 1] |
| $\text{RTT}_3$ | Data Transmission ($\text{cwnd} = 4$) | $4\text{ MSS}$[cite: 1] | $7$[cite: 1] |
| $\text{RTT}_4$ | Data Transmission ($\text{cwnd} = 8$) | $8\text{ MSS}$[cite: 1] | $15$ |
| $\text{RTT}_5$ | Data Transmission ($\text{cwnd} = 16$) | $16\text{ MSS}$[cite: 1] | $31$ |
| $\text{RTT}_6$ | Data Transmission ($\text{cwnd} = 32$) | $32\text{ MSS}$[cite: 1] | $63$[cite: 1] |
| $\text{RTT}_7$ | Data Transmission ($\text{cwnd} = 64$) | $64\text{ MSS}$[cite: 1] | $127$[cite: 1] |
| $\text{RTT}_8$ | Data Transmission ($\text{cwnd} = 128$) | Remaining $123\text{ MSS}$ (can send up to 128)[cite: 1] | $250$[cite: 1] |

* **Total RTTs required**: $1\text{ (Setup)} + 8\text{ (Data bursts)} = \mathbf{9\text{ RTTs}}$[cite: 1].
