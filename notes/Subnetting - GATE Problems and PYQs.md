> [!question] GATE CS 2004 / 2006: Subnet Number Identification
> An organization uses class-based addressing and is assigned the Class A address `18.26.0.127`. The administrator decides to split the network into $32$ distinct subnets.
> 1. Determine the subnet mask.
> 2. Determine the subnet number to which this host IP belongs.

### Step-by-Step Solution

1. **Subnet Mask**:
   * Class A default network ID $= 8\text{ bits}$.
   * Subnets required $= 32 = 2^5 \implies$ borrow $5$ bits for subnetting.
   * Subnet mask width $= 8 + 5 = 13\text{ bits}$ ($/13$).
   * Second byte bit pattern: `11111000` $\implies 128 + 64 + 32 + 16 + 8 = 248$.
   * $\text{Subnet Mask} = \mathbf{255.248.0.0}$.

2. **Subnet Number**:
   * The subnet number is determined by the borrowed 5 bits in the 2nd octet.
   * Second octet value $= 26_{10} = \mathbf{00011}010_2$.
   * The first 5 bits are `00011`.
   * Decimal value of `00011` $= 3$.
   * The host belongs to **Subnet 3** (indexed from 0; or the 4th subnet if 1-indexed).

---

> [!question] Asymmetric Subnet Mask Visibility
> Two computers $C_1$ and $C_2$ are configured on a local network:
> * $C_1$: IP = `203.197.2.53`, Mask = `255.255.128.0` ($/17$)
> * $C_2$: IP = `203.197.75.201`, Mask = `255.255.192.0` ($/18$)
> 
> Can $C_1$ and $C_2$ send packets directly to each other without a router?

### Resolution

* **From $C_1$'s perspective**:
  * Applies its own mask (`/17`) to both IPs:
    * $C_1$ Network ID: `203.197.2.53 & 255.255.128.0 = 203.197.0.0/17`
    * $C_2$ 3rd octet bitwise AND: $75_{10} = 01001011_2 \mathbin{\&} 10000000_2 = 0 \implies \text{Net ID} = `203.197.0.0/17`$
  * $C_1$ concludes that $C_2$ is in the **same network** and attempts to deliver packets directly via ARP.
* **From $C_2$'s perspective**:
  * Applies its own mask (`/18`) to both IPs:
    * $C_2$ Network ID: $75_{10} = 01001011_2 \mathbin{\&} 11000000_2 = 64 \implies `203.197.64.0/18`$
    * $C_1$ Network ID: $2_{10} = 00000010_2 \mathbin{\&} 11000000_2 = 0 \implies `203.197.0.0/18`$
  * $C_2$ concludes that $C_1$ is in a **different network** and forwards replies to its default gateway.
* **Conclusion**: Communication is asymmetric; $C_1$ treats $C_2$ as local, whereas $C_2$ treats $C_1$ as remote.
