
A subnetted Class B network has the direct broadcast address **`144.16.95.255`**. Which of the following can be its subnet mask?

- **A.** `255.255.224.0`
- **B.** `255.255.240.0`
- **C.** `255.255.248.0`
- **D.** Any of the above

---

Let's convert the 3rd and 4th octets of the broadcast address (`95.255`) into binary:
$$\text{3rd Octet } (95_{10}) = \mathbf{01011111}_2$$
$$\text{4th Octet } (255_{10}) = \mathbf{11111111}_2$$
Combined 16-bit suffix:  
`0 1 0 1 1 1 1 1` `1 1 1 1 1 1 1 1`
Notice that the trailing sequence of **1s** in the 3rd octet is **5 ones long** (`11111`).

For a mask to be valid, all bits in the broadcast address corresponding to **Host bits** in the mask **MUST be 1**.

| Option | Subnet Mask | 3rd Octet Mask (Binary) | Subnet Bits | Host Bits | Host Portion in 3rd Octet | Valid Broadcast Ending? |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **A** | `255.255.224.0` | `11100000` | 3 | **5** | Last 5 bits (`11111`) | **YES** (`010` + `11111`) |
| **B** | `255.255.240.0` | `11110000` | 4 | **4** | Last 4 bits (`1111`) | **YES** (`0101` + `1111`) |
| **C** | `255.255.248.0` | `11111000` | 5 | **3** | Last 3 bits (`111`) | **YES** (`01011` + `111`) |

