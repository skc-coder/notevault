> [!definition] Longest Prefix Match (LPM)
> When a packet arrives at a router, the router examines its forwarding table and may find multiple route entries matching the packet's destination IP address.
> * The **Longest Prefix Matching Rule** dictates that the router must forward the packet using the matching entry that has the **longest prefix length (highest number of prefix mask bits)**.
> * The longest prefix corresponds to the smallest, most specific destination network.

```mermaid
flowchart TD
    Pkt["Incoming Packet Dest IP"] --> Match{"Evaluate Matching Routes"}
    Match --> R1["Prefix /22 (4096 hosts)"]
    Match --> R2["Prefix /24 (256 hosts)"]
    Match --> R3["Prefix /32 (Single host)"]
    R3 --> Select["Select Longest Prefix (/32): Most Specific Route"]
```

> [!question] LPM Route Lookup Trace
> Given the routing table:
> 
> | Destination Prefix | Next Hop / Interface |
> | :--- | :--- |
> | `192.15.7.0/24` | Port 1 |
> | `192.15.7.0/26` | Port 2 |
> | `192.15.7.3/32` | Port 3 |
> | `Default` (`0.0.0.0/0`) | Port 4 |
> 
> Determine the output port for:
> 1. `192.15.7.3`
> 2. `192.15.7.4`
> 3. `192.14.13.12`
> 4. `192.14.6.255`

### Lookup Trace

1. `192.15.7.3`: Matches $/24$, $/26$, $/32$, and Default. The longest prefix is $/32 \implies \mathbf{\text{Port 3}}$.
2. `192.15.7.4`: Matches $/24$, $/26$ (since $4 \le 63$), and Default. Longest prefix is $/26 \implies \mathbf{\text{Port 2}}$.
3. `192.14.13.12`: Does not match any `192.15.x.x` route; matches only Default $\implies \mathbf{\text{Port 4}}$.
4. `192.14.6.255`: Matches only Default $\implies \mathbf{\text{Port 4}}$.
