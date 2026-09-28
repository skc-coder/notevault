Three contiguous fields in the IPv4 header coordinate fragmentation and reassembly[cite: 1]:

```mermaid
flowchart LR
    ID["Identification (16 bits)"] --- FL["Flags (3 bits)"] --- FO["Fragment Offset (13 bits)"]
```

### 1. Identification (16 Bits)
Assigned by the source to uniquely identify the original datagram[cite: 1]. Every fragment generated from the same original datagram retains the same Identification value, allowing the destination host to group related fragments together[cite: 1].

### 2. Flags (3 Bits)
Control bits regulating fragmentation behavior[cite: 1]:
* **Bit 0**: Reserved bit; must remain `0`[cite: 1].
* **Bit 1 - DF (Don't Fragment)**:
  * If $\text{DF} = 1$: Intermediate routers are not permitted to fragment the datagram[cite: 1]. If the packet exceeds the outgoing link MTU, the router discards it and returns an ICMP Destination Unreachable message (`Type 3, Code 4`: Fragmentation Needed and DF Set)[cite: 1].
  * If $\text{DF} = 0$: The datagram can be fragmented if necessary[cite: 1].
* **Bit 2 - MF (More Fragments)**:
  * If $\text{MF} = 1$: Indicates that more fragments follow this one (i.e., this is an initial or intermediate fragment)[cite: 1].
  * If $\text{MF} = 0$: Indicates that this is the final fragment of the original datagram (or the only packet, if not fragmented)[cite: 1].

### 3. Fragment Offset (13 Bits)
Indicates the position of the fragment's payload data relative to the beginning of the original unfragmented payload[cite: 1].

> [!formula] Fragment Offset Scaling Factor
> Because the datagram payload can be up to $65{,}515\text{ Bytes}$ long but the offset field is only $13\text{ bits}$ wide ($2^{13} = 8192$), the offset value is scaled by **$8\text{ Bytes}$**[cite: 1]:
> $$\text{Stored Offset Value} = \frac{\text{Byte Offset Position of Data}}{8}$$[cite: 1]
> $$\text{Absolute Data Starting Byte} = \text{Offset Value} \times 8$$[cite: 1]

> [!trap] The 8-Byte Divisibility Invariant
> The data payload of every non-terminal fragment ($\text{MF} = 1$) **must be an exact multiple of 8 bytes**[cite: 1]. If an MTU allows a larger size that is not divisible by 8, the router rounds the payload down to the nearest multiple of 8[cite: 1]. The final fragment ($\text{MF} = 0$) carries the remaining bytes and does not need to satisfy the 8-byte divisibility constraint[cite: 1].

### Distinguishing Fragment Positions Using Flags and Offset

| Fragment Offset | MF Flag | Inference / Position[cite: 1]                                                         |
| :-------------: | :-----: | :------------------------------------------------------------------------------------ |
|      $= 0$      |   $0$   | **Unfragmented Datagram**: The only packet sent (no fragmentation occurred)[cite: 1]. |
|      $= 0$      |   $1$   | **First Fragment**: Beginning of a fragmented sequence[cite: 1].                      |
|      $> 0$      |   $1$   | **Intermediate / Middle Fragment**: Sits within the sequence[cite: 1].                |
|      $> 0$      |   $0$   | **Last Fragment**: Terminal piece of the fragmented sequence[cite: 1].                |
