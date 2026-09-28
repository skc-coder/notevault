An IPv4 datagram consists of a mandatory header (20 bytes), optional fields (0 to 40 bytes), and the data payload encapsulated from upper transport protocols (TCP, UDP, ICMP).
![[IPv4 - Header Format and Structure-1790594187193.webp]]

| Row | Focus Category | Contiguous Header Fields (Left to Right) | Mnemonic Story Link |
| :--- | :--- | :--- | :--- |
| **Row 0** | Length & Format | VER (4b) → HLEN (4b) → TOS (8b) → Total Length (16b) | **Police check the cut chocolate lengths** |
| **Row 1** | Fragmentation | Identification (16b) → Flags (3b) → Fragment Offset (13b) | **Chopping the pieces up** |
| **Row 2** | Life & Verification | TTL (8b) → Protocol (8b) → Header Checksum (16b) | **Someone sees; kill and clear** |
| **Row 3** | Source | Source IP Address (32b) | **Originator of the packet** |
| **Row 4** | Destination | Destination IP Address (32b) | **Final target of the packet** |

| Field Name                 | Size (Bits)   | Description                                                                                    |
| :------------------------- | :------------ | :--------------------------------------------------------------------------------------------- |
| **Version**                | 4 bits        | Specifies IP version (value `4` for IPv4, `6` for IPv6)[cite: 1].                              |
| **HLEN (Header Length)**   | 4 bits        | Length of the IP header expressed in 4-byte (32-bit) words[cite: 1].                           |
| **Type of Service (TOS)**  | 8 bits        | Specifies service quality metrics: delay, throughput, reliability[cite: 1].                    |
| **Total Length**           | 16 bits       | Total size of datagram (Header + Payload) in bytes[cite: 1].                                   |
| **Identification**         | 16 bits       | Unique datagram identifier used to reassemble fragments[cite: 1].                              |
| **Flags**                  | 3 bits        | Control bits: `[Reserved(0), DF, MF]`[cite: 1].                                                |
| **Fragment Offset**        | 13 bits       | Position of fragment data relative to the start of original payload, in 8-byte units[cite: 1]. |
| **Time to Live (TTL)**     | 8 bits        | Hop count / lifespan limit to prevent routing loops[cite: 1].                                  |
| **Protocol**               | 8 bits        | Demultiplexing key indicating the upper-layer payload protocol[cite: 1].                       |
| **Header Checksum**        | 16 bits       | 1's complement sum error detection over the header only[cite: 1].                              |
| **Source IP Address**      | 32 bits       | IPv4 address of the sender host[cite: 1].                                                      |
| **Destination IP Address** | 32 bits       | IPv4 address of the recipient host[cite: 1].                                                   |
| **Options + Padding**      | 0 to 40 Bytes | Optional debugging, routing, and timestamp extensions[cite: 1].                                |

