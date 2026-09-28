Application processes generate network traffic at bursty, unpredictable rates (alternating between periods of silence and high-volume bursts)[cite: 1]. Injecting bursty traffic directly into network links causes buffer overflows and packet drops at intermediate routers[cite: 1].

> [!definition] Traffic Shaping
> Traffic shaping regulates the rate and volume of traffic transmitted into the network, smoothing out bursty transmission spikes into a steady, predictable output stream[cite: 1].

```mermaid
flowchart LR
    App["Bursty Application Traffic"] --> Shaper["Traffic Shaper<br/>(Leaky / Token Bucket)"]
    Shaper --> Net["Regulated Uniform Flow into Network"]
```

### Leaky Bucket vs. Token Bucket

```mermaid
flowchart TD
    subgraph LB["Leaky Bucket Algorithm"]
        In1["Bursty Input Packets"] --> B1["Bucket / Buffer (FIFO Queue)"]
        B1 --> Leak["Fixed Constant Flow (Hole at Bottom)"]
    end

    subgraph TB["Token Bucket Algorithm"]
        Gen["Token Generator (Constant Rate r)"] --> TPool["Token Bucket (Capacity C)"]
        In2["Incoming Packets"] --> Match{"Token Available?"}
        TPool --> Match
        Match -- Yes --> OutBurst["Transmit Packet immediately (Bursts allowed)"]
        Match -- No --> DropQueue["Queue or Discard"]
    end
```

| Dimension | Leaky Bucket | Token Bucket |
| :--- | :--- | :--- |
| **Output Rate** | Strictly fixed, constant rate[cite: 1]. | Variable average rate; permits controlled bursts up to bucket capacity. |
| **Burst Handling** | Eliminates all bursts; excess packets are queued or discarded[cite: 1]. | Allows traffic bursts if enough tokens have accumulated. |
| **Data Queuing** | Packets are stored directly in a FIFO queue and leak out at a constant rate[cite: 1]. | Tokens are stored; packets are transmitted immediately upon consuming a token. |
| **Token Mechanism** | No tokens; operates purely on water-in-a-leaky-bucket physics[cite: 1]. | Tokens generate at rate $r$; bucket holds up to $C$ tokens. |
