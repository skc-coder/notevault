A comparative reference of core application layer protocols, their transport prerequisites, session parameters, and default port bindings[cite: 1].

| Protocol | Underlying Transport | Server Port | Connection Type | State Maintenance | Band Type | Connection Count |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DNS**[cite: 1] | UDP (primary) / TCP[cite: 1] | 53[cite: 1] | Connectionless (UDP)[cite: 1] | Stateless[cite: 1] | In-band[cite: 1] | 1[cite: 1] |
| **HTTP 1.0**[cite: 1] | TCP[cite: 1] | 80[cite: 1] | Connection-Oriented[cite: 1] | Stateless[cite: 1] | In-band[cite: 1] | 1 per object[cite: 1] |
| **HTTP 1.1**[cite: 1] | TCP[cite: 1] | 80[cite: 1] | Connection-Oriented[cite: 1] | Stateless[cite: 1] | In-band[cite: 1] | 1 (Persistent)[cite: 1] |
| **SMTP**[cite: 1] | TCP[cite: 1] | 25[cite: 1] | Connection-Oriented[cite: 1] | Stateful[cite: 1] | In-band[cite: 1] | 1[cite: 1] |
| **POP3**[cite: 1] | TCP[cite: 1] | 110[cite: 1] | Connection-Oriented[cite: 1] | Stateless (across sessions)[cite: 1] | In-band[cite: 1] | 1[cite: 1] |
| **IMAP**[cite: 1] | TCP[cite: 1] | 143[cite: 1] | Connection-Oriented[cite: 1] | Stateful[cite: 1] | In-band[cite: 1] | 1 |
| **TELNET**[cite: 1] | TCP[cite: 1] | 23[cite: 1] | Connection-Oriented[cite: 1] | Stateful | In-band | 1 |
| **FTP**[cite: 1] | TCP[cite: 1] | 21 (Control), 20 (Data)[cite: 1] | Connection-Oriented[cite: 1] | Stateful[cite: 1] | **Out-of-band**[cite: 1] | **2 concurrent**[cite: 1] |
