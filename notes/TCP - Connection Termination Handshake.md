TCP connection teardown is asymmetric; each half of the full-duplex channel is terminated independently[cite: 1]. It typically operates as a 4-way handshake, though it can collapse to 3 packets if the responding party piggybacks its FIN with its ACK[cite: 1].

```mermaid
sequenceDiagram
    autonumber
    participant HostA as Host A (Active Close)
    participant HostB as Host B (Passive Close)

    Note over HostA: Established
    Note over HostB: Established
    HostA->>HostB: 1. FIN = 1, Seq = u [Host A stops sending data]
    Note over HostA: FIN-WAIT-1
    Note over HostB: CLOSE-WAIT
    HostB-->>HostA: 2. ACK = 1, Ack No = u + 1
    Note over HostA: FIN-WAIT-2
    Note over HostB: Host B can still send data to A
    HostB->>HostA: 3. FIN = 1, Seq = v [Host B finishes sending data]
    Note over HostB: LAST-ACK
    Note over HostA: TIME-WAIT
    HostA-->>HostB: 4. ACK = 1, Ack No = v + 1
    Note over HostB: CLOSED
    Note over HostA: Wait 2 * MSL, then CLOSED
```

### Half-Closed Connection Properties
* After Host $A$ sends its FIN and receives an ACK, it enters `FIN-WAIT-2`[cite: 1].
* Host $A$ can **no longer send data**, but it **can still receive data** sent by Host $B$[cite: 1].
* Host $B$ resides in `CLOSE-WAIT` until its application finishes sending remaining data and closes its socket[cite: 1].

> [!trap] Number of Segments to Close a TCP Connection
> A TCP connection requires **either 3 or 4 segments** to close[cite: 1]:
> * **4 Segments**: Standard independent termination ($\text{FIN} \to \text{ACK} \to \text{FIN} \to \text{ACK}$)[cite: 1].
> * **3 Segments**: If Host $B$ has no pending data, it combines its ACK and FIN into a single segment ($\text{FIN} \to [\text{FIN}+\text{ACK}] \to \text{ACK}$)[cite: 1].
