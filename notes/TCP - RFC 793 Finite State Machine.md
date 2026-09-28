TCP connection lifecycles transition through eleven distinct formal states defined in RFC 793[cite: 1].

| State Name | Endpoint Type | Functional Description |
| :--- | :--- | :--- |
| **CLOSED** | Both | Fictional state; no active connection exists[cite: 1]. |
| **LISTEN** | Server | Passive open; server waits for incoming connection requests[cite: 1]. |
| **SYN-SENT** | Client | Active open; client sent SYN segment and awaits SYN+ACK[cite: 1]. |
| **SYN-RECEIVED** | Server | Server received SYN, sent SYN+ACK, and awaits client's final ACK[cite: 1]. |
| **ESTABLISHED** | Both | Connection is operational; full-duplex data transfer active[cite: 1]. |
| **FIN-WAIT-1** | Client (Active Close) | Host initiated termination by sending FIN; awaits ACK or FIN[cite: 1]. |
| **FIN-WAIT-2** | Client (Active Close) | Host received ACK for its FIN; awaits peer's FIN[cite: 1]. |
| **CLOSE-WAIT** | Server (Passive Close) | Host received FIN, sent ACK; waiting for local application to close[cite: 1]. |
| **LAST-ACK** | Server (Passive Close) | Host sent its own FIN; awaits final terminating ACK[cite: 1]. |
| **TIME-WAIT** | Client (Active Close) | Host sent final ACK; waits $2 \times \text{MSL}$ to ensure network is clear[cite: 1]. |
| **CLOSING** | Both (Simultaneous Close)| Rare; both sides sent FIN simultaneously and await mutual ACKs. |

```mermaid
sequenceDiagram
    participant C as Client (Active)
    participant S as Server (Passive)

    Note over C: CLOSED
    Note over S: CLOSED
    S->>S: Passive Open -> LISTEN
    C->>S: Active Open: SYN [Seq=X]
    Note over C: SYN-SENT
    Note over S: SYN-RCVD
    S->>C: SYN+ACK [Seq=Y, Ack=X+1]
    Note over C: ESTABLISHED
    C->>S: ACK [Ack=Y+1]
    Note over S: ESTABLISHED
    Note over C,S: DATA TRANSFER
    C->>S: Active Close: FIN [Seq=u]
    Note over C: FIN-WAIT-1
    Note over S: CLOSE-WAIT
    S->>C: ACK [Ack=u+1]
    Note over C: FIN-WAIT-2
    S->>C: Passive Close: FIN [Seq=v]
    Note over S: LAST-ACK
    Note over C: TIME-WAIT (2*MSL)
    C->>S: ACK [Ack=v+1]
    Note over S: CLOSED
    Note over C: Waits 2*MSL -> CLOSED
```
