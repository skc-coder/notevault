> [!question] Step-by-Step Reno Window Trajectory
> Consider a TCP connection with an initial $\text{ssthresh} = 32\text{ KB}$ and initial $\text{cwnd} = 1\text{ MSS} = 2\text{ KB}$.
> * The connection experiences a **Timeout** when `cwnd` reaches $32\text{ KB}$.
> * How long (in RTTs and ms) does it take for `cwnd` to recover back to $32\text{ KB}$ if $\text{RTT} = 100\text{ ms}$ and no further loss occurs?

* **Step 1: Calculate state immediately following Timeout at $\text{cwnd} = 32\text{ KB} = 16\text{ MSS}$**:
  $$\text{ssthresh} = \frac{\text{cwnd}}{2} = \frac{16\text{ MSS}}{2} = 8\text{ MSS} = 16\text{ KB}$$
  $$\text{cwnd} = 1\text{ MSS} = 2\text{ KB}$$

* **Step 2: Slow Start Growth ($\text{cwnd} \to \text{ssthresh} = 8\text{ MSS}$)**:
  * Start: $\text{cwnd} = 1\text{ MSS}$
  * After RTT 1: $\text{cwnd} = 2\text{ MSS}$
  * After RTT 2: $\text{cwnd} = 4\text{ MSS}$
  * After RTT 3: $\text{cwnd} = 8\text{ MSS} = \text{ssthresh}$
* **Step 3: Congestion Avoidance Growth ($\text{cwnd} \ge 8\text{ MSS}$)**:
  From $8\text{ MSS}$ to $16\text{ MSS}$ requires additive increments ($+1\text{ MSS}$ per RTT):
  $$\Delta \text{cwnd} = 16 - 8 = 8\text{ MSS} \implies 8\text{ additional RTTs}$$

* **Total Time**:
  $$\text{Total RTTs} = 3\text{ (Slow Start)} + 8\text{ (Congestion Avoidance)} = 11\text{ RTTs}$$
  $$\text{Total Time} = 11 \times 100\text{ ms} = \mathbf{1100\text{ ms}}$$

---

> [!question] File Transfer Volume over TCP
> A sender transfers a $250{,}000\text{-Byte}$ file over TCP with $\text{MSS} = 1000\text{ Bytes}$ and no network packet loss. Initial $\text{cwnd} = 1\text{ MSS}$ and $\text{ssthresh}$ is large. How many RTTs are required to transmit the entire file, including the connection setup handshake?

* **Step 1: Connection Setup**:
  * 3-way handshake consumes $1\text{ RTT}$. Data can be piggybacked on the 3rd packet or sent immediately in the subsequent burst.
* **Step 2: Determine total MSS chunks to transfer**:
  $$\text{Total Segments} = \frac{250{,}000\text{ B}}{1000\text{ B}} = 250\text{ MSS}$$

* **Step 3: Trace exponential slow-start delivery per RTT**:

| RTT Index | Operation / Phase | Segments Sent This RTT | Cumulative Segments Sent |
| :--- | :--- | :--- | :--- |
| $\text{RTT}_0$ | Connection Setup (3-way handshake) | $0\text{ data}$ | $0$ |
| $\text{RTT}_1$ | Data Transmission ($\text{cwnd} = 1$) | $1\text{ MSS}$ | $1$ |
| $\text{RTT}_2$ | Data Transmission ($\text{cwnd} = 2$) | $2\text{ MSS}$ | $3$ |
| $\text{RTT}_3$ | Data Transmission ($\text{cwnd} = 4$) | $4\text{ MSS}$ | $7$ |
| $\text{RTT}_4$ | Data Transmission ($\text{cwnd} = 8$) | $8\text{ MSS}$ | $15$ |
| $\text{RTT}_5$ | Data Transmission ($\text{cwnd} = 16$) | $16\text{ MSS}$ | $31$ |
| $\text{RTT}_6$ | Data Transmission ($\text{cwnd} = 32$) | $32\text{ MSS}$ | $63$ |
| $\text{RTT}_7$ | Data Transmission ($\text{cwnd} = 64$) | $64\text{ MSS}$ | $127$ |
| $\text{RTT}_8$ | Data Transmission ($\text{cwnd} = 128$) | Remaining $123\text{ MSS}$ (can send up to 128) | $250$ |

* **Total RTTs required**: $1\text{ (Setup)} + 8\text{ (Data bursts)} = \mathbf{9\text{ RTTs}}$.
