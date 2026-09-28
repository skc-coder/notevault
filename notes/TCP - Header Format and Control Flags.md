The TCP header consists of a mandatory $20\text{-Byte}$ base followed by up to $40\text{ Bytes}$ of optional header parameters ($20\text{ to } 60\text{ Bytes}$ total)[cite: 1].

| Bit Offset | Field Name | Width | Functional Description |
| :--- | :--- | :--- | :--- |
| $0 - 15$ | **Source Port** | $16\text{ bits}$ | Sending process port number[cite: 1]. |
| $16 - 31$ | **Destination Port** | $16\text{ bits}$ | Receiving process port number[cite: 1]. |
| $32 - 63$ | **Sequence Number** | $32\text{ bits}$ | Sequence number of the segment's first data byte (or ISN if SYN is set)[cite: 1]. |
| $64 - 95$ | **Acknowledgment Number** | $32\text{ bits}$ | Next expected sequence byte from sender (valid if ACK flag is set)[cite: 1]. |
| $96 - 99$ | **Header Length (HLEN / Data Offset)** | $4\text{ bits}$ | Length of TCP header expressed in **4-byte words** (scaling factor of $4$)[cite: 1]. |
| $100 - 105$ | **Reserved** | $6\text{ bits}$ | Reserved for future standardization (set to 0)[cite: 1]. |
| $106 - 111$ | **Control Flags (URG, ACK, PSH, RST, SYN, FIN)** | $6\text{ bits}$ | $1\text{ bit}$ operational flags governing connection state[cite: 1]. |
| $112 - 127$ | **Receiver Window Size (rwnd)** | $16\text{ bits}$ | Number of available buffer bytes receiver can accept (flow control)[cite: 1]. |
| $128 - 143$ | **Checksum** | $16\text{ bits}$ | Mandatory error detection covering header, payload, and pseudo-header[cite: 1]. |
| $144 - 159$ | **Urgent Pointer** | $16\text{ bits}$ | Offset pointing to the end of urgent data (valid only if URG flag is set)[cite: 1]. |
| $160 - \dots$ | **Options & Padding** | $0 - 40\text{ Bytes}$ | Optional extensions (MSS, Window Scale, SACK, Timestamps) padded to 32 bits[cite: 1]. |

> [!formula] Header Length (HLEN) Scaling Invariant
> The 4-bit HLEN field represents values from $0$ to $15$ ($0000_2$ to $1111_2$)[cite: 1]:
> $$\text{Header Size in Bytes} = \text{HLEN Value} \times 4\text{ Bytes}$$[cite: 1]
> * Minimum Header ($20\text{ Bytes}$): $\text{HLEN} = \frac{20}{4} = 5$ ($0101_2$)[cite: 1].
> * Maximum Header ($60\text{ Bytes}$): $\text{HLEN} = \frac{60}{4} = 15$ ($1111_2$)[cite: 1].
> * Values $0$ through $4$ are strictly invalid for TCP[cite: 1].

### The 6 Control Flags
* **URG (Urgent)**: When set to $1$, indicates that the Urgent Pointer field contains valid data requiring immediate processing[cite: 1].
* **ACK (Acknowledgment)**: When set to $1$, indicates that the Acknowledgment Number field contains a valid sequence byte[cite: 1]. Every packet after the initial SYN packet has the ACK flag asserted[cite: 1].
* **PSH (Push)**: Commands the receiving TCP entity to push buffered data up to the receiving application immediately without waiting for receive buffers to fill up to the Maximum Segment Size (MSS)[cite: 1].
* **RST (Reset)**: Resets and abruptly terminates a confused connection (e.g., when receiving an unexpected segment, wrong port request, or unmapped connection state)[cite: 1].
* **SYN (Synchronize)**: Synchronizes sequence numbers during connection establishment[cite: 1]. Set only in the first two packets of the 3-way handshake[cite: 1].
* **FIN (Finish)**: Initiates connection termination; indicates that the sender has finished transmitting its data stream[cite: 1].

> [!trap] SYN and FIN Sequence Number Consumption
> Although control packets with pure SYN or FIN carry **zero bytes of application data**, they **strictly consume exactly $1$ sequence number** because they must be reliably acknowledged by the other endpoint[cite: 1]. A pure ACK packet carries no data and consumes **no** sequence number[cite: 1].
