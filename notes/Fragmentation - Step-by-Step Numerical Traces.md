> [!question] Standard MTU Fragmentation Trace
> A router receives a $1500\text{-byte}$ IPv4 packet (including a default $20\text{-byte}$ header) with $\text{Identification} = X$[cite: 1]. It must forward this packet over a link with an $\text{MTU} = 500\text{ Bytes}$[cite: 1]. Determine the parameters for each fragment[cite: 1].

### Derivation Steps:
1. $\text{Total Packet Size} = 1500\text{ B} \implies \text{Data Payload} = 1500 - 20 = 1480\text{ Bytes}$[cite: 1].
2. Outgoing $\text{MTU} = 500\text{ Bytes}$[cite: 1].
3. Maximum data payload per fragment:
   $$\text{Max Data} \le 500 - 20 = 480\text{ Bytes}$$
[cite: 1]
   Check divisibility by 8: $480 \pmod 8 = 0$ (valid)[cite: 1].
4. Partition the $1480\text{ Bytes}$ into chunks:
   * Fragment 1: $480\text{ B}$ (bytes $0$ to $479$)[cite: 1]
   * Fragment 2: $480\text{ B}$ (bytes $480$ to $959$)[cite: 1]
   * Fragment 3: $480\text{ B}$ (bytes $960$ to $1439$)[cite: 1]
   * Fragment 4: Remaining $40\text{ B}$ (bytes $1440$ to $1479$)[cite: 1]

| Frag No | Identification | Total Length | Data Size | Offset Value | MF | DF |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $X$[cite: 1] | $500\text{ B}$[cite: 1] | $480\text{ B}$[cite: 1] | $0 / 8 = \mathbf{0}$[cite: 1] | $1$[cite: 1] | $0$[cite: 1] |
| **2** | $X$[cite: 1] | $500\text{ B}$[cite: 1] | $480\text{ B}$[cite: 1] | $480 / 8 = \mathbf{60}$[cite: 1] | $1$[cite: 1] | $0$[cite: 1] |
| **3** | $X$[cite: 1] | $500\text{ B}$[cite: 1] | $480\text{ B}$[cite: 1] | $960 / 8 = \mathbf{120}$[cite: 1] | $1$[cite: 1] | $0$[cite: 1] |
| **4** | $X$[cite: 1] | $60\text{ B}$[cite: 1] | $40\text{ B}$[cite: 1] | $1440 / 8 = \mathbf{180}$[cite: 1] | $0$[cite: 1] | $0$[cite: 1] |

> [!trap] Transport Header Placement
> When an IPv4 datagram carrying a TCP segment is fragmented, **only the first fragment carries the TCP header**[cite: 1]. Subsequent fragments carry raw byte segments of the TCP payload[cite: 1]. However, **every** fragment receives its own independent IPv4 header[cite: 1].

---

> [!question] Re-fragmentation Across Heterogeneous Links
> An IPv4 packet of total length $250\text{ Bytes}$ ($\text{Header} = 20\text{ B}$, $\text{Data} = 230\text{ B}$) is sent from host A to host B[cite: 1]. Path links have MTUs of $120\text{ Bytes}$ and $80\text{ Bytes}$ respectively[cite: 1]:
> $$A \xrightarrow{\text{MTU } = 120\text{ B}} R \xrightarrow{\text{MTU } = 80\text{ B}} B$$[cite: 1]
> Trace all fragments generated across both links[cite: 1].

### Step 1: Hop 1 Across MTU = 120 Bytes
* Available payload capacity: $120 - 20 = 100\text{ Bytes}$[cite: 1].
* Largest multiple of 8: $\lfloor 100 / 8 \rfloor \times 8 = 96\text{ Bytes}$[cite: 1].
* Fragmentation of $230\text{ Bytes}$ payload:
  * Chunk 1: $96\text{ B}$[cite: 1]
  * Chunk 2: $96\text{ B}$[cite: 1]
  * Chunk 3: $230 - (96 + 96) = 38\text{ Bytes}$[cite: 1]

### Step 2: Hop 2 Across MTU = 80 Bytes
* Available payload capacity: $80 - 20 = 60\text{ Bytes}$[cite: 1].
* Largest multiple of 8: $\lfloor 60 / 8 \rfloor \times 8 = 56\text{ Bytes}$[cite: 1].
* Router $R$ processes each incoming fragment:
  * **Chunk 1 ($96\text{ B}$)** breaks into:
    * $F_1$: $56\text{ B}$ (Data: $[0 \dots 55]$) $\implies \text{Offset} = 0$, $\text{Total Len} = 76\text{ B}$, $\text{MF} = 1$[cite: 1].
    * $F_2$: $40\text{ B}$ (Data: $[56 \dots 95]$) $\implies \text{Offset} = 56/8 = 7$, $\text{Total Len} = 60\text{ B}$, $\text{MF} = 1$[cite: 1].
  * **Chunk 2 ($96\text{ B}$)** breaks into:
    * $F_3$: $56\text{ B}$ (Data: $[96 \dots 151]$) $\implies \text{Offset} = 96/8 = 12$, $\text{Total Len} = 76\text{ B}$, $\text{MF} = 1$[cite: 1].
    * $F_4$: $40\text{ B}$ (Data: $[152 \dots 191]$) $\implies \text{Offset} = 152/8 = 19$, $\text{Total Len} = 60\text{ B}$, $\text{MF} = 1$[cite: 1].
  * **Chunk 3 ($38\text{ B}$)**:
    * Fits within MTU: $38 + 20 = 58\text{ B} \le 80\text{ B}$[cite: 1].
    * $F_5$: $38\text{ B}$ (Data: $[192 \dots 229]$) $\implies \text{Offset} = 192/8 = 24$, $\text{Total Len} = 58\text{ B}$, $\text{MF} = 0$[cite: 1].

| Fragment | Total Length | Data Bytes | Stored Offset | MF Flag |
| :---: | :---: | :---: | :---: | :---: |
| **$F_1$** | $76\text{ B}$[cite: 1] | $56\text{ B}$[cite: 1] | $0$[cite: 1] | $1$[cite: 1] |
| **$F_2$** | $60\text{ B}$[cite: 1] | $40\text{ B}$[cite: 1] | $7$[cite: 1] | $1$[cite: 1] |
| **$F_3$** | $76\text{ B}$[cite: 1] | $56\text{ B}$[cite: 1] | $12$[cite: 1] | $1$[cite: 1] |
| **$F_4$** | $60\text{ B}$[cite: 1] | $40\text{ B}$[cite: 1] | $19$[cite: 1] | $1$[cite: 1] |
| **$F_5$** | $58\text{ B}$[cite: 1] | $38\text{ B}$[cite: 1] | $24$[cite: 1] | $0$[cite: 1] |
