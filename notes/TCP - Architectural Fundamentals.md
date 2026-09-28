> [!definition] Transmission Control Protocol (TCP)
> TCP is a connection-oriented, reliable, full-duplex, byte-stream transport layer protocol providing in-order, error-free delivery over an unreliable network[cite: 1].

### Core Invariants of TCP
1. **Connection-Oriented**: Communicating endpoints must execute a 3-way handshake prior to data exchange to initialize sequence numbers and negotiate receiver preferences[cite: 1].
2. **Reliable Transfer over Unreliable Network**: Although the underlying Network Layer (IP) is best-effort and can drop, delay, duplicate, or reorder packets, TCP hides this entirely by implementing acknowledgments, checksums, retransmission timers, and resequencing buffers[cite: 1].
3. **Full-Duplex Communication**: Once connected, both endpoints can transmit and receive application payload data simultaneously over the same logical connection[cite: 1].
4. **Byte-Stream Oriented Protocol**: TCP views application data as an unstructured, continuous stream of bytes[cite: 1]. Every individual byte transmitted in each direction is numbered sequentially with a unique $32$-bit sequence number[cite: 1]. (Contrasted with Data Link protocols which are discrete frame-oriented)[cite: 1].
