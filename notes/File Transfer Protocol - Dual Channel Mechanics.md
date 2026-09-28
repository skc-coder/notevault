File Transfer Protocol (FTP) provides interactive network file transfer between a client and a remote server[cite: 1].

> [!definition] Out-of-Band Architecture
> FTP differs fundamentally from unified-stream protocols like HTTP because it separates control commands from actual data payloads across **two distinct, concurrent TCP connections** (an **out-of-band** design)[cite: 1]:
> 1. **Control Connection (Port 21)**: Transmits client commands, user authentication credentials, directory navigation requests, and server status response codes[cite: 1].
> 2. **Data Connection (Port 20)**: Exclusively carries file data streams and directory listings[cite: 1].

```mermaid
flowchart LR
    Client["FTP Client"] <-->|Port 21: Control Connection (Persistent)| Server["FTP Server"]
    Client <-->|Port 20: Data Connection (Non-Persistent per file)| Server
```

> [!theorem] FTP Connection Persistence Invariants
> * **Control Connection**: Remains open and **persistent** throughout the entire interactive client session[cite: 1].
> * **Data Connection**: **Non-persistent**[cite: 1]. A new, dedicated TCP data connection is spawned dynamically for each individual file transfer or directory listing command, and is automatically torn down immediately upon transfer completion[cite: 1].
