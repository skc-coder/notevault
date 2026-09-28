In IEEE 802.3 Ethernet networks, MAC addresses are 48 bits (6 octets) long, organized to support unicast, multicast, and broadcast addressing modes[cite: 1].

> [!definition] Ethernet Multicast Address Rule
> An Ethernet MAC address is classified as a **multicast address** if and only if the **Least Significant Bit (LSB) of the most significant byte** (first octet) is set to `1`[cite: 1].
> 
> In standard hex representation `b0:b1:b2:b3:b4:b5`:
> * The first octet `b0` determines address type via its least significant bit[cite: 1].
> * If $\text{LSB} = 0$: Unicast MAC address[cite: 1].
> * If $\text{LSB} = 1$: Multicast MAC address (or Broadcast when all 48 bits are `1`)[cite: 1].

### IPv4 to Ethernet Multicast Mapping
For IP multicast delivery, IPv4 Class D addresses ($224.0.0.0$ to $239.255.255.255$) are mapped directly into a reserved Ethernet MAC address range[cite: 1]:

> [!formula] IANA Multicast MAC Address Range
> All Ethernet multicast addresses mapped from IPv4 multicast traffic share the upper 24-bit Organizationally Unique Identifier (OUI) prefix `01:00:5E`[cite: 1]:
> $$\text{Range: } \mathbf{01:00:5E:00:00:00} \quad \text{to} \quad \mathbf{01:00:5E:7F:FF:FF}$$[cite: 1]

* The first byte is `0x01` ($00000001_2$); its lowest bit is `1`, satisfying the Ethernet multicast standard[cite: 1].
* Of the 28 bits of host multicast space in an IPv4 Class D address, exactly 23 bits are copied directly into the lower 23 bits of the Ethernet MAC address[cite: 1].
* **Address Overlap**: Because 5 address bits are unmapped ($28 - 23 = 5$), exactly $2^5 = 32$ distinct IPv4 multicast group addresses map onto the same Ethernet MAC address[cite: 1].
