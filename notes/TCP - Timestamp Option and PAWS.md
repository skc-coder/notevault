The Timestamp Option adds a timestamp to the TCP header for two distinct purposes[cite: 1]:
1. **Precise RTT Measurement**: The sender attaches current transmission time; the receiver echoes it back in the ACK, allowing the sender to compute exact RTT without synchronized system clocks[cite: 1].
2. **Protection Against Wrapped Sequence Numbers (PAWS)**[cite: 1].

> [!definition] Sequence Number Wrap-Around
> Sequence numbers are $32\text{ bits}$ wide, yielding $2^{32} \approx 4.29 \times 10^9$ unique sequence numbers[cite: 1]. On high-speed networks, sequence numbers cycle through all $2^{32}$ states and wrap around within seconds[cite: 1].

> [!theorem] PAWS Condition
> If sequence numbers wrap around faster than the Maximum Segment Lifetime ($\text{Wrap-Around Time} < \text{MSL}$), an old delayed segment trapped in the network could reappear with a sequence number matching a new, active segment[cite: 1].
> * To prevent silent data corruption, the receiver inspects the timestamp on incoming segments:
>   $$\text{Wrap-Around Time} > \text{MSL}$$[cite: 1]
> * If a segment arrives with an older timestamp than currently active data, it is rejected as an obsolete duplicate from a previous cycle[cite: 1].

> [!question] Sequence Number Wrap-Around Time Derivation
> A TCP connection operates over a link with bandwidth $BW = 1\text{ Gbps} = 10^9\text{ bps}$[cite: 1]. Calculate the minimum time required for sequence numbers to wrap around[cite: 1].
> * Total sequence space: $2^{32}\text{ distinct bytes}$[cite: 1].
> * Transfer speed in bytes:
>   $$\text{Byte Rate} = \frac{10^9}{8} = 1.25 \times 10^8\text{ Bytes/sec}$$[cite: 1]
> * Wrap-around duration:
>   $$\text{Wrap Time} = \frac{2^{32}\text{ Bytes}}{1.25 \times 10^8\text{ Bytes/sec}} = \frac{4{,}294{,}967{,}296 \times 8}{10^9} \approx \mathbf{34.36\text{ seconds}}$$[cite: 1]
> * If link bandwidth is $2^{30}\text{ bps}$, then:
>   $$\text{Wrap Time} = \frac{2^{32}\text{ Bytes}}{\frac{2^{30}}{8}\text{ Bytes/sec}} = \frac{2^{32}}{2^{27}} = 2^5 = \mathbf{32\text{ seconds}}$$[cite: 1]
