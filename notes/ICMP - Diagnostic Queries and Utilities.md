### ICMP Query Types
Sending this message to the host we wanna query
* **Echo Request (Type 8, Code 0) & Echo Reply (Type 0, Code 0)**: Used by `ping` to test whether a remote host is active and measure round-trip time (RTT)[cite: 1].
* **Timestamp Request (Type 13) & Timestamp Reply (Type 14)**: Measures one-way delay and estimates clock skew between endpoints[cite: 1].

### Practical Implementation: Traceroute
Used to query all the routers en route to the wanted host
Traceroute identifies the sequence of intermediate routers along the path to a destination using ICMP and the IPv4 TTL field[cite: 1]:
1. Send a packet addressed to the destination with $\text{TTL} = 1$[cite: 1]. The first-hop router decrements TTL to $0$, discards the packet, and returns an ICMP Time Exceeded message (`Type 11`), revealing its IP address[cite: 1].
2. Send subsequent packets with increasing TTL values ($\text{TTL} = 2, 3, 4, \dots$) to discover successive routers along the path[cite: 1].
3. But when the message reaches the source it will be accepeted. So we use fake port number to get IMAP message. For UDP-based traceroute, probe packets target a high, unassigned port number (e.g., $33434$)[cite: 1]. When the destination host finally receives the packet, it rejects it with an ICMP Port Unreachable message (`Type 3, Code 3`), indicating that the complete path has been traced[cite: 1]. Similary thing for TCP. 

### Path MTU Discovery (PMTUD)
Used to find the lowest MTU (bottleneck MTU) along a network path without causing fragmentation[cite: 1]:
1. The sender transmits packets with the $\text{DF}$ bit set to $1$[cite: 1].
2. If a router along the path cannot forward the packet because it exceeds the link MTU, it discards the packet and returns an ICMP Destination Unreachable message (`Type 3, Code 4`) containing the MTU value of that next link[cite: 1].
3. The sender lowers its packet size to match that MTU and repeats the probe until packets reach the destination without error[cite: 1].
