### Reassembly Algorithm at the Destination
The destination host reconstructs the original datagram using the received fragments:
1. Buffers fragments matching the same Source IP, Destination IP, and Identification fields[cite: 1].
2. The total data payload length of each fragment is computed:
   $$\text{Data Length}_i = \text{Total Length}_i - (\text{HLEN}_i \times 4)$$
[cite: 1]
3. Fragments are arranged in increasing order of their Fragment Offset values[cite: 1].
4. The starting byte of fragment $i$ is placed at byte index $\text{Offset}_i \times 8$[cite: 1].
5. Reassembly completes once the buffer contains a contiguous sequence of bytes from offset $0$ up to the end of the fragment with $\text{MF} = 0$[cite: 1].

> [!question] Finding the Final Offset in an Incomplete Chain
> A packet is split into 3 fragments[cite: 1]. The first fragment has $\text{Total Length} = 100\text{ B}$, $\text{Offset} = 0$[cite: 1]. The second fragment has $\text{Total Length} = 116\text{ B}$, $\text{Offset} = 10$[cite: 1]. All headers are $20\text{ Bytes}$[cite: 1]. What is the Fragment Offset value of the third (last) fragment[cite: 1]?
> 
> *Step-by-step Solution*:
> 1. Data in $F_1 = 100 - 20 = 80\text{ Bytes}$ (covers bytes $0$ to $79$)[cite: 1].
> 2. Verified offset for $F_2 = 80 / 8 = 10$[cite: 1].
> 3. Data in $F_2 = 116 - 20 = 96\text{ Bytes}$ (covers bytes $80$ to $175$)[cite: 1].
> 4. Starting byte for $F_3 = 80 + 96 = 176$[cite: 1].
> 5. Offset of $F_3$:
>    $$\text{Offset}_3 = \frac{176}{8} = \mathbf{22}$$[cite: 1]

### Impact of Fragmentation on Network Reliability
Fragmentation increases the probability that a datagram will be dropped[cite: 1]. If any single fragment of a datagram is corrupted or dropped, the destination host cannot complete reassembly[cite: 1]. It discards all received fragments for that datagram once the reassembly timer expires, forcing the transport layer (e.g., TCP) to retransmit the entire original segment[cite: 1].

> [!question] End-to-End Success Probability with Dropping Links
> An IPv4 datagram of $1280\text{ Bytes}$ with a $40\text{-byte}$ header traverses $3$ routers and $4$ links[cite: 1]. Each link has an independent link-loss error rate of $50\%$ ($p = 0.5$)[cite: 1]. The intermediate links enforce an $\text{MTU} = 660\text{ Bytes}$[cite: 1]. What is the probability that the datagram reaches the destination intact[cite: 1]?
> 
> *Step-by-step Solution*:
> 1. Data payload $= 1280 - 40 = 1240\text{ Bytes}$[cite: 1].
> 2. Payload per fragment for $\text{MTU} = 660\text{ B}$: $660 - 40 = 620\text{ Bytes}$ (divisible by 8: $620 / 8 = 77.5$ — adjust: nearest multiple of 8 is $616\text{ B}$, but according to the note specifications, it is split into two $620\text{ B}$ payloads)[cite: 1].
> 3. The datagram splits into $2$ fragments ($F_1$ and $F_2$)[cite: 1].
> 4. For a fragment to arrive safely across 4 successive independent links:
>    $$P(\text{Fragment arrives safely}) = (1 - 0.5)^4 = \left(\frac{1}{2}\right)^4 = \frac{1}{16}$$[cite: 1]
> 5. Both fragments must arrive independently for successful reassembly:
>    $$P(\text{Datagram Delivered}) = P(F_1) \times P(F_2) = \left(\frac{1}{16}\right) \times \left(\frac{1}{16}\right) = \frac{1}{256}$$[cite: 1]
