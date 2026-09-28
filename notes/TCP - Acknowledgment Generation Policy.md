While TCP uses cumulative acknowledgments, it optimizes network bandwidth by delaying ACKs under RFC 1122 and RFC 5681 guidelines[cite: 1].

```mermaid
flowchart TD
    Recv["Segment Arrives at Receiver"] --> DataCheck{"Does Receiver have data to send back?"}
    DataCheck -- Yes --> Piggy["Send ACK immediately<br/>piggybacked with data"]
    DataCheck -- No --> OrderCheck{"Is incoming segment in-order?"}
    OrderCheck -- Out-of-order --> ImmACK["Send ACK immediately<br/>(Forces duplicate ACK for fast retransmit)"]
    OrderCheck -- In-order --> UnackCheck{"Are there other unacknowledged segments?"}
    UnackCheck -- "1 unacknowledged segment exists" --> Delay["Wait up to 500ms for next segment"]
    UnackCheck -- "2 in-order segments unacknowledged" --> SendNow["Send cumulative ACK immediately"]
```

### Cumulative ACK Rules
1. **Piggybacking**: If the receiver has outgoing data, it piggybacks the ACK number in the outgoing data segment[cite: 1].
2. **Delayed ACK**: If an in-order segment arrives and no data is ready to transmit, the receiver waits up to $500\text{ ms}$ for the next segment to arrive so it can acknowledge both with a single ACK[cite: 1].
3. **At Least One ACK per 2 Segments**: The receiver must not delay ACKs for more than $2$ consecutive full-sized in-order segments[cite: 1].
4. **Immediate Out-of-Order ACK**: If an out-of-order segment arrives (gap detected), an ACK indicating the expected in-order byte must be generated immediately[cite: 1].
