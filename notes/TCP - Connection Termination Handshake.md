# TCP Connection Teardown & MSL

## 1. Core Principles
* **Full-Duplex Teardown**: TCP operates two independent simplex channels ($A \to B$ and $B \to A$). Each direction must be explicitly terminated with its own `FIN`.
* **No Abrupt Shutdowns**:
  * Host A cannot unilaterally kill the connection because Host B may still have unread or buffered data to send ($B \to A$).
  * Host B cannot silently vanish when finished, or Host A would remain in limbo wondering if B crashed or has more data.
* **Segments Required**:
  * **4 Segments (Standard)**: $\text{FIN} \to \text{ACK} \to \text{FIN} \to \text{ACK}$.
  * **3 Segments (Piggybacked)**: If Host B has no pending data, it combines steps 2 and 3 into $[\text{FIN}+\text{ACK}]$.

---

## 2. State Progression & Handshake
http://www.tcpipguide.com/free/t_TCPConnectionTermination-2.htm
![[TCP - Connection Termination Handshake-1790677838885.webp]]

```mermaid
sequenceDiagram
    autonumber
    participant A as Host A (Active Close)
    participant B as Host B (Passive Close)

    Note over A,B: ESTABLISHED
    A->>B: FIN (Seq = u)
    activate A
    Note over A: FIN-WAIT-1
    Note over B: CLOSE-WAIT
    B-->>A: ACK (Ack = u + 1)
    Note over A: FIN-WAIT-2
    Note over B: (Half-Closed: B can still send data)
    B->>A: FIN (Seq = v)
    Note over B: LAST-ACK
    Note over A: TIME-WAIT
    A-->>B: ACK (Ack = v + 1)
    deactivate A
    Note over B: CLOSED (Immediate)
    Note over A: Waits 2 * MSL -> CLOSED
````

### State Mnemonics

|**State**|**Host**|**Mental Hook**|**Meaning**|
|---|---|---|---|
|**FIN-WAIT-1**|A|Waiting for **ACK #1**|Sent 1st FIN; waiting for B's ACK.|
|**FIN-WAIT-2**|A|Waiting for **FIN #2**|Outbox closed; idling until B finishes and sends its FIN.|
|**TIME-WAIT**|A|Waiting on the **Clock**|Sent final ACK; lingering for $2 \times \text{MSL}$.|
|**CLOSE-WAIT**|B|Waiting for **Local Close**|Kernel ACKed A's FIN; waiting for the local app to call `close()`.|
|**LAST-ACK**|B|Waiting for **Last ACK**|App sent FIN; needs only the final ACK to terminate.|

> [!tip] Quick Rule
> 
>   
> 
> - **Host A (Active Close)** enters only **WAIT** states (`FIN-WAIT-1` $\to$ `FIN-WAIT-2` $\to$ `TIME-WAIT`).
>     
>       
>     
> - **Host B (Passive Close)** handles work and exits (`CLOSE-WAIT` $\to$ `LAST-ACK`).
>     
>       
>     

## 3. MSL & Why Host A Waits $2 \times \text{MSL}$

- **What is MSL?**
    - Maximum Segment Lifetime: The estimated upper bound for how long an IP packet can survive in transit before being dropped.
    - Not a packet header field (unlike TTL / Hop Limit); it is an internal OS configuration value (RFC 793 recommends 2 min; Linux defaults to 30–60 s).
- **Why 2 MSL ($1\text{ MSL} + 1\text{ MSL}$)?**
    - **Outbound Trip ($1\text{ MSL}$)**: Time for Host A's final ACK (Packet 4) to reach Host B[cite: 1].        
    - **Inbound Trip ($1\text{ MSL}$)**: If Packet 4 is lost, Host B retransmits its `FIN`[cite: 1]. That duplicate `FIN` takes up to $1\text{ MSL}$ to reach Host A[cite: 1].
    - Waiting $2 \times \text{MSL}$ guarantees Host A survives long enough to re-acknowledge any lost final handshake packets without throwing an unexpected `RST`[cite: 1].
- **Bonus Protection (Ghost Packets)**:     
    - Ensures delayed duplicate packets trapped in slow routes or buffers die off before the OS reassigns the same 4-tuple $(\text{IP}_A, \text{Port}_A, \text{IP}_B, \text{Port}_B)$ to a future connection.

## 4. Why Host B Closes Immediately (No TIME-WAIT)

1. **Definitive Completion**: Receiving Packet 4 (the final ACK) gives Host B $100\%$ confirmation that Host A cleanly agreed to terminate[cite: 1]
2. **Tuple Locked by Host A**: Host B can safely reopen its port because Host A keeps the connection 4-tuple $(\text{IP}_A, \text{Port}_A, \text{IP}_B, \text{Port}_B)$ locked in `TIME-WAIT`, preventing collision.