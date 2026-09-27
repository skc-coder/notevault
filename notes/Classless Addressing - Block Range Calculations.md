> [!question] CIDR Range and Boundary Derivation
> Given the classless address `167.199.170.82/27`, calculate:
> 1. Total number of addresses in the block[cite: 1]
> 2. Number of usable host addresses[cite: 1]
> 3. The Network Address[cite: 1]
> 4. The Direct Broadcast Address[cite: 1]

### Step-by-Step Derivation

1. **Host Bits and Capacity**:
   * Prefix bits $n = 27$[cite: 1]
   * Host bits $h = 32 - 27 = 5\text{ bits}$[cite: 1]
   * Total Addresses $= 2^5 = \mathbf{32}$[cite: 1]
   * Usable Host Addresses $= 32 - 2 = \mathbf{30}$[cite: 1]

2. **Binary Breakdown of the 4th Octet**:
   * Fourth octet value $= 82_{10} = 01010010_2$[cite: 1]
   * Since $n = 27 = 24 + 3$, the first $3$ bits of the 4th octet belong to the prefix: `010`[cite: 1].
   * The remaining $5$ bits belong to the host suffix: `10010`[cite: 1].

3. **Network Address**:
   * Set the last $5$ host bits to `0`:
     $$010\mathbf{00000}_2 = 64_{10}$$
[cite: 1]
   * $\text{Network Address} = \mathbf{167.199.170.64/27}$[cite: 1]

4. **Direct Broadcast Address**:
   * Set the last $5$ host bits to `1`:
     $$010\mathbf{11111}_2 = 64 + 31 = 95_{10}$$
[cite: 1]
   * $\text{Broadcast Address} = \mathbf{167.199.170.95}$[cite: 1]
   * Address block range: `167.199.170.64` to `167.199.170.95`[cite: 1].

---

> [!question] Equivalence of CIDR Network Identifiers
> Which of the following network prefixes represent the exact same block as `152.3.128.0/17`[cite: 1]?
> * A. `152.3.128.75/17`[cite: 1]
> * B. `152.3.178.75/17`[cite: 1]
> * C. `152.3.129.75/17`[cite: 1]
> * D. `152.3.192.128/17`[cite: 1]

### Analysis

* Prefix length $/17$ implies the first $17$ bits must be identical[cite: 1].
* $152.3$ accounts for the first $16$ bits[cite: 1].
* The 17th bit is the MSB of the 3rd octet[cite: 1]:
  $$128_{10} = \mathbf{1}0000000_2 \implies \text{17th bit is } 1$$
* Any address having the 17th bit as `1` in the range `152.3.128.0` to `152.3.255.255` belongs to this network[cite: 1]:
  * $128 \to \mathbf{1}0000000_2$ (Bit 17 is 1)[cite: 1]
  * $178 \to \mathbf{1}0110010_2$ (Bit 17 is 1)[cite: 1]
  * $129 \to \mathbf{1}0000001_2$ (Bit 17 is 1)[cite: 1]
  * $192 \to \mathbf{1}1000000_2$ (Bit 17 is 1)[cite: 1]
* When specified with the slash notation $/17$, all candidate addresses have the exact same prefix bits and identify the exact same network block[cite: 1].
