The Network Layer provides a best-effort (eg. error, fragmentation service), connectionless datagram service without built-in error control or delivery guarantees[cite: 1]. The Internet Control Message Protocol (ICMP) operates alongside IP to provide error reporting and diagnostic queries[cite: 1].

```mermaid
flowchart LR
    DLL["Ethernet Frame"] --> IP["IP Datagram (Protocol = 1)"]
    IP --> ICMP["ICMP Message"]
```

> [!definition] ICMP Architectural Layering
> ICMP is an integral part of the Network Layer[cite: 1]. However, ICMP messages are not sent directly to the Data Link Layer[cite: 1]. Instead, they are encapsulated within standard IPv4 datagrams with the Protocol field set to `1`[cite: 1].

### Classes of ICMP Messages
1. **Error Reporting Messages**: Notify the source host when an intermediate router or destination node encounters an error while processing a datagram[cite: 1].
2. **Query Messages**: Used by network administrators and diagnostic tools to test host reachability, measure round-trip times, and synchronize clock parameters[cite: 1].
