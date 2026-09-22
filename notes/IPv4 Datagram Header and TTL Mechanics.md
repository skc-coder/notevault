> [!definition]
> The **IPv4 Datagram Header** prefixes data packets at Layer 3 to provide routing, addressing, lifetime control, and reassembly information across network hops[cite: 2].

| Byte Offset | Bit Width | Field Name | Purpose & Exam Traps |
| :--- | :--- | :--- | :--- |
| Row 0 | 4 bits | **VER** (Version) | Holds `4` for IPv4 ($0100_2$)[cite: 2] |
| Row 0 | 4 bits | **HLEN** (Header Length) | Value multiplied by **scaling factor of 4**. Range: $5 \text{ to } 15 \implies 20 \text{ to } 60\text{ bytes}$[cite: 1, 2] |
| Row 0 | 8 bits | **TOS / Services** | DiffServ, precedence, and QoS priority tagging[cite: 2] |
| Row 0 | 16 bits | **Total Length** | $\text{Header} + \text{Payload}$ in bytes (Max $2^{16}-1 = 65,535\text{ bytes}$)[cite: 2] |
| Row 1 | 16 bits | **Identification** | Unique ID shared by all fragments of the parent packet[cite: 1, 2] |
| Row 1 | 3 bits | **Flags** | Bit 0: Reserved (`0`). Bit 1: **DF** (Don't Fragment). Bit 2: **MF** (More Fragments)[cite: 1, 2] |
| Row 1 | 13 bits | **Fragment Offset** | Byte position divided by **scaling factor of 8**[cite: 1, 2] |
| Row 2 | 8 bits | **TTL (Time to Live)** | Hop counter to eliminate routing loops. Decremented by 1 at each router[cite: 1, 2] |
| Row 2 | 8 bits | **Protocol** | Demultiplexes payload: ICMP=`1`, IGMP=`2`, TCP=`6`, UDP=`17`[cite: 2] |
| Row 2 | 16 bits | **Header Checksum** | Covers **header only** (recomputed at every hop due to TTL decrement)[cite: 1, 2] |
| Row 3 | 32 bits | **Source IP Address** | Original transmitting interface address[cite: 2] |
| Row 4 | 32 bits | **Destination IP** | Final target interface address[cite: 2] |
| Row 5+ | 0 - 40 B | **Options + Padding** | Strict/loose routing, timestamping (padded to 32-bit boundary)[cite: 1, 2] |

> [!formula]
> 1. $\text{Header Length (bytes)} = \text{HLEN} \times 4$
> 2. $\text{Payload Size} = \text{Total Length} - (\text{HLEN} \times 4)$[cite: 1]
> 3. $\text{Fragment Offset Value} = \frac{\text{Byte Offset Number}}{8}$[cite: 1]

> [!trap]
> - When a router receives an IPv4 datagram with $\text{TTL} = 1$, it decrements it to $0$, discards the packet, and transmits an **ICMP Time Exceeded (Type 11)** message back to the source[cite: 1, 2].
> - Intermediate routers modify **two mandatory fields** during basic forwarding: **TTL** (decrements by 1) and **Header Checksum** (recalculated)[cite: 1, 2].

> [!question]
> **Q:** If the HLEN field in an IPv4 packet contains the binary value $1000_2$ and the Total Length field contains $0000010000000000_2$, what is the size of the data payload?  
> (A) 1004 bytes  
> (B) 992 bytes  
> (C) 1024 bytes  
> (D) 960 bytes  
>
> **Answer:** **(B)**  
> **Explanation:**  
> 1. $\text{HLEN} = 1000_2 = 8$. Header size $= 8 \times 4 = 32\text{ bytes}$.  
> 2. $\text{Total Length} = 0000010000000000_2 = 2^{10} = 1024\text{ bytes}$.  
> 3. $\text{Payload Size} = \text{Total Length} - \text{Header Size} = 1024 - 32 = \mathbf{992\text{ bytes}}$.
