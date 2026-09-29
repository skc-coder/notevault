Electronic Mail (E-mail) is an asynchronous, store-and-forward communication medium[cite: 1]. The sender and receiver do not need to be online concurrently to exchange messages[cite: 1].
![](attachments/Pasted%20image%2020260429102326.webp)
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

| Protocol | Full Form                                      | Transport    | Server Port      | Operational Direction / Role                                                                                                            |
| :------- | :--------------------------------------------- | :----------- | :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **SMTP** | Simple Mail Transfer Protocol[cite: 1]         | TCP[cite: 1] | **25**[cite: 1]  | **Push Protocol**: Uploads email from sender UA to sender mail server, and relays email between intermediate mail servers[cite: 1].     |
| **POP3** | Post Office Protocol version 3[cite: 1]        | TCP[cite: 1] | **110**[cite: 1] | **Pull / Access Protocol**: Retrieves messages from mail server to local client machine; stateless across sessions by default[cite: 1]. |
| **IMAP** | Internet Message Access Protocol[cite: 1]      | TCP[cite: 1] | **143**[cite: 1] | **Pull / Access Protocol**: Maintains stateful server synchronization, folders, and server-side search capabilities[cite: 1].           |
| **MIME** | Multipurpose Internet Mail Extensions[cite: 1] | —            | —                | Supplement to SMTP allowing non-ASCII multimedia, attachments, images, and audio encoding over standard text streams[cite: 1].          |

> [!theorem] Web-Based Mail Protocol Usage
> When accessing email via a modern web browser, the user agent communicates with the webmail server using **HTTP/HTTPS** for both message drafting/sending and reading[cite: 1]. However, inter-server communications between disparate mail transfer servers strictly utilize **SMTP** over TCP port 25[cite: 1].

### 1. The Core Analogy: Mail Delivery vs. Mailbox Pickup

To never confuse them, separate email into **Sending (Push)** vs. **Retrieving (Pull)**:

  

```
Sender (You) ────[SMTP: Push]────► Your Server ────[SMTP: Push Relay]────► Recipient's Server ────[POP3 / IMAP: Pull]────► Recipient
```

- **SMTP (Simple Mail Transfer Protocol):** The **Postman on a Bicycle** who takes letters out of your hands and delivers them to the destination post office.
    
      
    
- **POP3 / IMAP:** The **Recipient Opening Their Mailbox** to grab the mail that arrived.
    
      
    

### 2. How Each Protocol Works

#### A. SMTP: The "Push" Protocol

- **Role:** Transmits mail **forward** (pushes up from sender client to sender server, and relays between intermediate servers).
    
      
    
- **Direction:** Client $\to$ Server, and Server $\to$ Server.
    
      
    
- **Port:** **TCP Port 25**.
    
      
    
- **Limitation:** SMTP is inherently text-only (7-bit ASCII). To send photos, PDFs, or audio attachments, it requires **MIME** (Multipurpose Internet Mail Extensions) to encode binary files into text format.
    
      
    

#### B. POP3: The "Download & Erase" Pull Protocol

- **Role:** Connects to the server mailbox, **downloads all messages to your local hard drive**, and typically deletes them from the server.
    
      
    
- **State:** **Stateless** across sessions.
    
      
    
- **Port:** **TCP Port 110**.
    
      
    
- **The Analogy (The Physical Post Office Box):**
    
      
    - You go to your physical PO box, empty it completely into your backpack, and go home.
        
          
        
    - Your PO box is now empty. If you check your mail from another device (e.g., your laptop instead of your desktop), you see nothing because the mail only exists on your first device!
        
          
        

#### C. IMAP: The "Cloud Sync" Pull Protocol

- **Role:** Keeps all emails, folders, tags, and read/unread states **permanently on the server** and simply synchronizes the view across all your devices.
    
      
    
- **State:** **Stateful** (maintains continuous server synchronization and supports server-side search).
    
      
    
- **Port:** **TCP Port 143**.
    
      
    
- **The Analogy (The Cloud / Bulletin Board):**
    
      
    - The letter stays pinned to a shared bulletin board.
        
          
        
    - If you view it on your phone, mark it "Read", or move it into a "Work" folder, those exact changes instantly reflect when you log in from your laptop.
        
          
        

### 3. Memory Tricks & Mnemonics

|**Protocol**|**Port**|**Role**|**Direct O(1) Mental Hook**|
|---|---|---|---|
|**SMTP**|**25**|**Push** (Send & Relay)|**S-M-T-P** = **S**end **M**ail **T**o **P**eople! (Christmas day is Dec **25** $\to$ send gifts/mail).|
|**POP3**|**110**|**Pull** (Download & Delete)|**"Pop" the bubble** $\to$ once you pop it and grab it, it’s gone from the server!|
|**IMAP**|**143**|**Pull** (Sync & Keep on Server)|**I-M-A-P** = **I** **M**ap **A**ll **P**hones (mirrors/maps across all your devices at once).|

### 4. What About Webmail (Gmail / Outlook in a Browser)?

When you compose or read emails on `mail.google.com`:

  

- **Between Your Browser and Gmail:** Uses standard **HTTP / HTTPS** (Port 443) for both drafting/sending and reading.
    
      
    
- **Between Google and Yahoo/Outlook Servers:** The background servers strictly talk to each other using **SMTP over TCP Port 25**.