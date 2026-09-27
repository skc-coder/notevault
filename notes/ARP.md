**ARP** is a Layer 2 (Data Link Layer) protocol used to map a dynamic **IPv4 address** (Layer 3) to a fixed physical **MAC address** (Layer 2) within a local network segment (LAN/subnet).

ARP allows a host to learn about other host in its network to be able to talk to them without help of router. 

---

## 1. Core Concepts

* **IP Address (Logical):** Used for routing packets across distinct, interconnected networks.
* **MAC Address (Physical):** Used by switches and Network Interface Cards (NICs) to deliver frames to the correct local physical interface.
* **Scope:** ARP functions **only** within a single broadcast domain / local subnet. Routers break ARP broadcast domains.

---

## 2. Key Components

| Term               | Type                            | Description                                                                                 |
| :----------------- | :------------------------------ | :------------------------------------------------------------------------------------------ |
| **ARP Request**    | Broadcast (`FF:FF:FF:FF:FF:FF`) | "Who has IP `X.X.X.X`? Tell `Y.Y.Y.Y`."                                                     |
| **ARP Reply**      | Unicast                         | "`X.X.X.X` is at `MAC_ADDR`."                                                               |
| **ARP Cache**      | Dynamic RAM Table               | Holds IP-to-MAC mappings temporarily with TTL (Time-To-Live).                               |
| **Gratuitous ARP** | Unsolicited Broadcast           | A host broadcasts its own IP-to-MAC mapping to announce an IP change or detect IP conflict. |

---

## 3. Resolution Workflow

```
[ Host A ]                                         [ Host B ]
IP:  192.168.1.10                                 IP:  192.168.1.20
MAC: AA:AA:AA:AA:AA:AA                            MAC: BB:BB:BB:BB:BB:BB
    |                                                  |
    |---- 1. Check ARP Cache (Miss) -------------------|
    |---- 2. Broadcast ARP Request (FF:FF:FF:FF:FF:FF)->|
    |                                                  | (Filters: Target IP matches)
    |<--- 3. Unicast ARP Reply (BB:BB:BB:BB:BB:BB)-----|
    |                                                  |
    |---- 4. Update ARP Cache & Send Frame ------------>|
```

### Steps
Suppose **Computer A** wants to send data to **Computer B** on the same local network (`192.168.1.0/24`).
1. **Cache Lookup:** Sender checks local ARP table for the destination IP.
2. **ARP Request:** If absent, sender sends a broadcast frame asking for the target MAC.
3. **ARP Reply:** Target device receives the broadcast, recognises its IP, and sends a unicast reply directly to the sender.
4. **Cache Store:** Sender updates its ARP cache with the received mapping and encapsulates the IP packet into an Ethernet frame.

---

## 4. Specialized ARP Variant

- **RARP (Reverse ARP):** Legacy protocol; resolves MAC addresses to IP addresses (superseded by DHCP).

---


## 6. Command Cheat Sheet

```bash
# Windows / Linux / macOS: View current ARP cache
arp -a

# Delete ARP entry (requires admin/root)
arp -d 192.168.1.20    # Windows/macOS
ip neighbor del 192.168.1.20 dev eth0   # Linux (iproute2)

# Add static ARP entry
arp -s 192.168.1.20 BB-BB-BB-BB-BB-BB
```

---
