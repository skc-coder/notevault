> [!trap] Theoretical vs. Practical Subnet Masks
> While RFC standards mandate that subnet masks must consist of contiguous `1`s followed by contiguous `0`s, theoretical exam questions may specify non-contiguous subnet masks[cite: 1].
> * Under non-contiguous masks, standard bitwise AND remains strictly applicable to check if two IP addresses yield identical Network IDs[cite: 1].

> [!question] Non-Contiguous Subnet Mask Pair Verification
> A network has the non-contiguous subnet mask `255.255.31.0`[cite: 1]. Which of the following pairs of IP addresses belong to the same network[cite: 1]?
> * A. `172.57.88.62` and `172.56.87.23`[cite: 1]
> * B. `10.35.28.2` and `10.35.29.4`[cite: 1]
> * C. `191.203.31.87` and `191.240.31.28`[cite: 1]
> * D. `128.8.123.43` and `128.8.161.55`[cite: 1]

### Analytical Solution

* Mask: `255.255.31.0`[cite: 1]
* Byte 1 and Byte 2 are $255$ $\implies$ both IPs in the pair must match exactly in the first two bytes[cite: 1]:
  * Eliminates Option A: Byte 2 differs ($57 \neq 56$)[cite: 1].
  * Eliminates Option C: Byte 2 differs ($203 \neq 240$)[cite: 1].
* Check 3rd byte for Option B:
  * Mask 3rd byte: $31_{10} = 00011111_2$[cite: 1]
  * First IP: $28_{10} = 00011100_2 \implies 00011100_2 \mathbin{\&} 00011111_2 = 00011100_2 = 28$
  * Second IP: $29_{10} = 00011101_2 \implies 00011101_2 \mathbin{\&} 00011111_2 = 00011101_2 = 29$
  * The results differ ($28 \neq 29$) $\implies$ Option B hosts are in different subnets[cite: 1].
* Check 3rd byte for Option D:
  * First IP: $123_{10} = 01111011_2 \implies 01111011_2 \mathbin{\&} 00011111_2 = 00011011_2 = 27$
  * Second IP: $161_{10} = 10100001_2 \implies 10100001_2 \mathbin{\&} 00011111_2 = 00000001_2 \neq 27$
  *(Note: If evaluated on identical binary masking bits, pair B / D must match across active mask bits)*[cite: 1].
