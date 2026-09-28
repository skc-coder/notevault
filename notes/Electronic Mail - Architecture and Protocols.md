Electronic Mail (E-mail) is an asynchronous, store-and-forward communication medium[cite: 1]. The sender and receiver do not need to be online concurrently to exchange messages[cite: 1].

### Core Architectural Components
1. **User Agent (UA)**: The client application (mail reader) allowing users to compose, send, read, and organize email messages (e.g., Gmail, Outlook, Thunderbird, CLI mutt)[cite: 1].
2. **Message Transfer Agent (MTA)**: A background server process running continuously on mail hosts that routes and relays email messages across networks from source to destination[cite: 1].
3. **Mail Server**: Hosts user mailboxes and manages active mail transfer queues[cite: 1]. Mail servers must remain online continuously so incoming mail can be accepted at any time, even while the recipient user agent is disconnected[cite: 1].

```mermaid
flowchart LR
    Sender["Alice (User Agent)"] -->|SMTP / HTTP| MS1["Alice's Mail Server (MTA)"]
    MS1 -->|SMTP (Inter-server relay)| MS2["Bob's Mail Server (MTA)"]
    MS2 -->|POP3 / IMAP / HTTP| Receiver["Bob (User Agent)"]
```

### Mail Protocol Specifications

| Protocol | Full Form | Transport | Server Port | Operational Direction / Role |
| :--- | :--- | :--- | :--- | :--- |
| **SMTP** | Simple Mail Transfer Protocol[cite: 1] | TCP[cite: 1] | **25**[cite: 1] | **Push Protocol**: Uploads email from sender UA to sender mail server, and relays email between intermediate mail servers[cite: 1]. |
| **POP3** | Post Office Protocol version 3[cite: 1] | TCP[cite: 1] | **110**[cite: 1] | **Pull / Access Protocol**: Retrieves messages from mail server to local client machine; stateless across sessions by default[cite: 1]. |
| **IMAP** | Internet Message Access Protocol[cite: 1] | TCP[cite: 1] | **143**[cite: 1] | **Pull / Access Protocol**: Maintains stateful server synchronization, folders, and server-side search capabilities[cite: 1]. |
| **MIME** | Multipurpose Internet Mail Extensions[cite: 1] | — | — | Supplement to SMTP allowing non-ASCII multimedia, attachments, images, and audio encoding over standard text streams[cite: 1]. |

> [!theorem] Web-Based Mail Protocol Usage
> When accessing email via a modern web browser, the user agent communicates with the webmail server using **HTTP/HTTPS** for both message drafting/sending and reading[cite: 1]. However, inter-server communications between disparate mail transfer servers strictly utilize **SMTP** over TCP port 25[cite: 1].
