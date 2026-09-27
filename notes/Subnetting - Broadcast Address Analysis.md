> [!question] GATE IT 2006: Subnet Mask from Broadcast Address
> A subnetted Class B network has the direct broadcast address `144.16.95.255`[cite: 1]. Which of the following can be its subnet mask[cite: 1]?
> * A. `255.255.224.0`[cite: 1]
> * B. `255.255.240.0`[cite: 1]
> * C. `255.255.248.0`[cite: 1]
> * D. Any of the above[cite: 1]

### Mathematical Deduction

* Class B default: First $16$ bits (`144.16`) are fixed network bits[cite: 1].
* Direct Broadcast Address has all host bits set to `1`[cite: 1].
* Inspect the 3rd and 4th octets in binary:
  * 3rd octet $= 95_{10} = \mathbf{01011111}_2$[cite: 1]
  * 4th octet $= 255_{10} = \mathbf{11111111}_2$[cite: 1]
* Combined suffix bits: `0101 1111 1111 1111`[cite: 1].
* If the subnet mask is contiguous:
  * Mask must have contiguous `1`s ending before the contiguous trailing `1`s of the broadcast address[cite: 1].
  * The trailing ones in $95_{10}$ are the last $5$ bits (`11111`), preceded by a `0` at bit position 5[cite: 1].
  * Therefore, the host field must be at least $8 + 5 = 13\text{ bits}$ wide[cite: 1].
  * The subnet portion can use at most $3$ bits in the 3rd octet (`010`)[cite: 1]:
    * Using $3$ subnet bits $\implies$ Mask = `255.255.224.0` (Binary `11100000`)[cite: 1]
* For Option B (`255.255.240.0` $\implies$ 4 bits `11110000`), bit 4 would be a subnet bit, but in the broadcast address bit 4 is `1`, meaning bit 4 cannot be fixed to `0`[cite: 1].
* Thus, the contiguous mask must be **`255.255.224.0`** (or non-contiguous theoretical variants matching the bit pattern)[cite: 1].
