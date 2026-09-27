> [!definition] Internetwork and The Internet
> An **internetwork** (or **internet** with lowercase "i") is an interconnected system formed when multiple distinct computer networks are joined together to exchange data[cite: 1].
> 
> **The Internet** (noun, capitalized "I") refers to the specific, globally interconnected public network that uses the TCP/IP protocol suite to exchange data worldwide[cite: 1].

```mermaid
flowchart TD
    subgraph Core["Global Backbone Tier 1"]
        G1["Global Tier 1 ISP"] <-->|IXP| G2["Global Tier 1 ISP"]
    end
    subgraph Regional["Regional Tier 2"]
        R1["Regional ISP"]
        R2["Regional ISP"]
    end
    subgraph Access["Access Tier 3 / Last Mile"]
        A1["Access ISP (Home)"]
        A2["Access ISP (College)"]
        A3["Access ISP (Enterprise)"]
    end

    G1 <--> R1
    G2 <--> R2
    R1 <--> A1
    R1 <--> A2
    R2 <--> A3
```

> [!theorem] ISP Interconnection Invariants
> Connecting millions of individual Access ISPs directly point-to-point via a full mesh would require $O(n^2)$ physical links, which is practically and economically infeasible[cite: 1].
> * **Access ISPs** connect to **Regional ISPs**, which in turn aggregate traffic up to **Global (Tier 1) ISPs**[cite: 1].
> * Global ISPs interconnect and peer with each other through **Internet Exchange Points (IXPs)** based on commercial and economic peering agreements[cite: 1].
