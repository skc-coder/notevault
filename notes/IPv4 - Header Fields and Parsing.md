### Version (4 Bits)
Identifies the protocol version so intermediate routers know which format definition to apply when parsing subsequent fields[cite: 1]. For IPv4, the field value is $4$ (`0100`)[cite: 1].

### HLEN - Internet Header Length (4 Bits)
Because a 4-bit unsigned number ranges from $0$ to $15$ ($2^4 - 1$) and the actual header length spans $20$ to $60$ bytes, the field stores the header size divided by $4$[cite: 1]:

$$\text{Header Length in Bytes} = \text{HLEN} \times 4$$
[cite: 1]

* For a default $20$-byte header: $\text{HLEN} = 20 / 4 = 5$ (`0101`)[cite: 1].
* For a maximum $60$-byte header: $\text{HLEN} = 60 / 4 = 15$ (`1111`)[cite: 1].
* Any value of $\text{HLEN} < 5$ is invalid in IPv4[cite: 1].

> [!question] Calculating Options Size from HLEN
> If the $\text{HLEN}$ field of an IPv4 packet contains $(1110)_2$, what is the total length of the Options and Padding fields[cite: 1]?
> 
> *Step-by-step Solution*:
> 1. Convert binary $\text{HLEN}$ to decimal: $(1110)_2 = 14$[cite: 1].
> 2. Calculate actual header size:
>    $$\text{Header Size} = 14 \times 4\text{ B} = 56\text{ Bytes}$$[cite: 1]
> 3. Subtract mandatory fixed header size ($20\text{ B}$):
>    $$\text{Options + Padding} = 56\text{ B} - 20\text{ B} = \mathbf{36\text{ Bytes}}$$[cite: 1]

### Type of Service / DSCP (8 Bits)
Used to convey Quality of Service (QoS) requirements[cite: 1]. It instructs routers which routing parameters to prioritize for the datagram, such as low delay, high throughput, high reliability, or low cost[cite: 1].

### Total Length (16 Bits)
Defines the overall length of the IP datagram, comprising the IP header plus the data payload, specified in bytes[cite: 1].

> [!formula] Datagram Payload Calculation
> $$\text{Payload Size (Data Length)} = \text{Total Length} - (\text{HLEN} \times 4)$$[cite: 1]
> * $\text{Maximum Theoretical Datagram Size} = 2^{16} - 1 = 65{,}535\text{ Bytes}$[cite: 1].

> [!question] Extracting Data Size from Header Bits
> An IPv4 packet arrives with $\text{Total Length} = (0000\,0000\,1000\,0010)_2$ and $\text{HLEN} = (1100)_2$[cite: 1]. What is the size of the transport layer data payload[cite: 1]?
> 
> *Step-by-step Solution*:
> 1. Decimal $\text{Total Length} = 2^7 + 2^1 = 128 + 2 = 130\text{ Bytes}$[cite: 1].
> 2. Decimal $\text{HLEN} = (1100)_2 = 12$[cite: 1].
> 3. Compute Header Size:
>    $$\text{Header Length} = 12 \times 4 = 48\text{ Bytes}$$[cite: 1]
> 4. Compute Payload:
>    $$\text{Data Length} = 130\text{ B} - 48\text{ B} = \mathbf{82\text{ Bytes}}$$[cite: 1]
