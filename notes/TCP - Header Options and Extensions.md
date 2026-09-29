The TCP header contains an optional field of up to $40\text{ Bytes}$ allowing endpoints to negotiate advanced transmission parameters during connection establishment[cite: 1].

### 1. Maximum Segment Size (MSS)
* Advertised strictly during the 3-way handshake inside the SYN packet[cite: 1].
* Defines the maximum payload bytes of application layer data a host can receive in a single segment[cite: 1].

> [!formula] MSS Derivation from MTU
> $$\text{MSS} = \text{MTU} - (\text{IP Header Length} + \text{TCP Header Length})$$[cite: 1]
> * For standard Ethernet: $\text{MTU} = 1500\text{ Bytes}$.
> * Standard headers: $\text{IP} = 20\text{ Bytes}, \text{TCP} = 20\text{ Bytes}$.
> * $\text{MSS} = 1500 - (20 + 20) = \mathbf{1460\text{ Bytes}}$.
> * During setup, both ends announce their local MSS; the **smaller of the two** values is selected as the connection MSS[cite: 1].

> [!question] Application Layer Data Limit
> What is the maximum size of data that the Application Layer can pass down to the Transport Layer at one time[cite: 1]?
> * **Answer**: **Arbitrary / Any size**[cite: 1]. The application can pass an arbitrary data stream (e.g., gigabytes) to its socket buffer; the Transport Layer automatically segments this data stream into chunks bounded by the negotiated MSS[cite: 1].

### 2. Window Scale Option (Large Windows)
The TCP header's window size field is $16\text{ bits}$ wide, capping the advertised window at:
$$\text{Max Standard Window} = 2^{16} - 1 = 65{,}535\text{ Bytes}$$[cite: 1]
On high-bandwidth-delay product paths (Long Fat Networks — LFNs), a $64\text{ KB}$ window under-utilizes the link because the sender must stop and wait for ACKs once $65{,}535\text{ Bytes}$ are transmitted[cite: 1].

> [!formula] Window Scale Factor
> The Window Scale Option specifies a scale factor shift count $S$ (up to $14\text{ bits}$) negotiated during the SYN packet[cite: 1]:
> $$\text{True Receiver Window} = \text{Header rwnd Field} \times 2^S$$[cite: 1]
> This expands the maximum addressable receive window to:
> $$2^{16} \times 2^{14} = 2^{30}\text{ Bytes} \approx 1\text{ Gigabyte}$$[cite: 1]
### 3. The 16-Bit TCP Limit & The Window Scale Factor (WSF)

#### The Problem: A 16-Bit Hard Limit

In the original standard TCP header, the **Receive Window (`rwnd`)** field is strictly **16 bits wide**:

$$\text{Max Window Size} = 2^{16} - 1 = \mathbf{65{,}535\text{ Bytes}} \approx \mathbf{64\text{ KB}}$$

Now look at what happens on the satellite link above ($\text{BDP} = 62.5\text{ MB}$):

1. TCP can only advertise a maximum window of $64\text{ KB}$.
    
2. The sender transmits $64\text{ KB}$ of data in less than **half a millisecond**.
    
3. The sender **must pause and freeze**, waiting $500\text{ ms}$ for the ACK to return before it is legally allowed to send the next batch.
    
4. Maximum achievable throughput:
    
    $$\text{Max Throughput} = \frac{\text{Window Size}}{\text{RTT}} = \frac{65{,}535\text{ Bytes}}{0.5\text{ s}} \approx \mathbf{1.04\text{ Mbps}}$$
    
    You paid for a **$1\text{ Gbps}$** fiber/satellite line, but ancient 16-bit TCP limits you to **$1\text{ Mbps}$** (a **$99.9\%$ waste of bandwidth**)!
    

#### The Solution: TCP Window Scale Option (RFC 1323)

TCP cannot simply change the 16-bit header field because that would break backwards compatibility across the entire global Internet. Instead, during the initial 3-way handshake (`SYN`), both hosts negotiate an optional **Window Scale Factor ($S$)**:

$$\text{Effective Window} = \text{Advertised 16-bit Window} \times 2^S$$

- **Bit Shift in Hardware:** Multiplying by $2^S$ is an internal left bit-shift ($\ll S$).
    
- $S$ is a 1-byte value ranging from $0$ to $14$.
    
- If $S = 14$, the maximum window becomes:
    
    $$65{,}535 \times 2^{14} \approx 65{,}535 \times 16{,}384 \approx \mathbf{1{,}073{,}725{,}440\text{ Bytes}} \approx \mathbf{1\text{ Gigabyte!}}$$
    
- By left-shifting the 16-bit window up to 14 times, TCP can advertise buffer sizes over $1\text{ GB}$, fully saturating massive multi-gigabit LFN pipes.
> [!question] Window Scale RTT Bound Calculation
> A TCP connection operates over a link with bandwidth $BW = 1{,}048{,}560\text{ bps}$[cite: 1]. The maximum standard window size is $65{,}535\text{ Bytes}$[cite: 1]. Above what RTT will the connection require the Window Scale option to maintain full line-rate utilization without stalling[cite: 1]?
> * Link transmission speed in bytes:
>   $$\text{Speed} = \frac{1{,}048{,}560\text{ bps}}{8} = 131{,}070\text{ Bytes/sec}$$[cite: 1]
> * Time to exhaust the standard $65{,}535\text{ Byte}$ window:
>   $$\text{Time} = \frac{65{,}535\text{ Bytes}}{131{,}070\text{ Bytes/sec}} = 0.5\text{ sec} = \mathbf{500\text{ ms}}$$[cite: 1]
> * If $\text{RTT} > 500\text{ ms}$, the sender empties its window before receiving an ACK, necessitating the Window Scale Option[cite: 1].

### 3. Selective Acknowledgments (SACK)
* By default, TCP uses cumulative ACKs, forcing retransmission of all subsequent packets if a single packet in a burst is lost[cite: 1].
* The SACK option allows the receiver to explicitly inform the sender of non-contiguous, out-of-order blocks received successfully, allowing the sender to retransmit **only missing segments**[cite: 1].
