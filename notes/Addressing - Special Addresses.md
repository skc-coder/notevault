# Special In-Block Reserved Addresses

Within any IPv4 network block, two addresses are reserved by default and **cannot be assigned to regular hosts**:

1. **Network Address (Network ID):** 
   - **Definition:** The very first IP address in the network block.
   - **Derivation:** Obtained by setting all host ID bits to `0`.
   - **Purpose:** Identifies the network segment itself. Used by routers in routing tables to aggregate and route packets toward the target network.
2. **Direct Broadcast Address (DBA):** 
   - **Definition:** The very last IP address in the network block.
   - **Derivation:** Obtained by setting all host ID bits to `1`.
   - **Purpose:** Delivers a packet simultaneously to every host inside that specific target network block. Can originate from an external network and be routed to the target subnet before being broadcasted locally.

---

## Usable Host Addresses Formula

For a subnet mask allocated $h$ host bits:

$$\text{Total Addresses} = 2^h$$

$$\text{Usable Host Addresses} = 2^h - 2$$

> [!note] Why subtract 2?
> The two subtracted addresses account for:
> - $1 \times \text{Network ID}$ (all host bits set to `0`)
> - $1 \times \text{Direct Broadcast Address}$ (all host bits set to `1`)

---

## Global & System Reserved Class A Networks

Apart from individual in-block host address reservations, entire network blocks are reserved by IANA under **RFC 1122**:

- **`0.0.0.0/8` ("This Network" / Self):** 
  - Used during initial system startup and host bootstrapping (e.g., DHCP Discover requests where the source address is set to `0.0.0.0`).
  - Cannot be assigned as a standard host IP.
- **`127.0.0.0/8` (Loopback Address):** 
  - Reserved for internal host communications (`127.0.0.1` is `localhost`). Packets sent here never hit the network hardware interface.

---

## Limited Broadcast Address vs. Direct Broadcast Address

```
               [ Sender Host ]
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
Limited Broadcast           Directed Broadcast
(255.255.255.255)         (e.g., 192.168.1.255)
        │                           │
  Stays on local             Traverses routers
  physical wire              to target subnet
        │                           │
   Blocked by                  Forwarded to
    Routers                   Target Subnet
```

### 1. Limited Broadcast Address (`255.255.255.255`)
- **Structure:** An address with all 32 bits set to 1 (`11111111.11111111.11111111.11111111`).
- **Scope:** Local physical wire / link-local segment only.
- **Purpose:** Used when a host doesn't know its own IP address or subnet mask (e.g., local service discovery, DHCP).
- **Router Rule:** Routers drop and **never forward** `255.255.255.255` across network boundaries to prevent broadcast storms.

### 2. Directed Broadcast Address (DBA)
- **Structure:** Network bits keep their target subnet values; host bits are all set to 1 (e.g., `192.168.1.255` for `192.168.1.0/24`).
- **Scope:** Targets a specific destination subnet from anywhere across an internetwork.
- **Purpose:** Used for remote management tasks like Wake-on-LAN (WoL) across subnets.
- **Router Rule:** Intermediary routers route it as standard unicast until it hits the final destination router, which then broadcasts it to its local LAN segment (*Note: Typically disabled by default on modern enterprise routers due to Smurf DDoS security risks*).