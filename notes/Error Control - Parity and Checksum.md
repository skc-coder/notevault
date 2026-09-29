## Simple Parity and Internet Checksum

### Simple Single-Bit Parity

Appends a single bit such that the total count of $1$s in the codeword satisfies the parity rule:
* **Even Parity**: Total number of $1$s is even ($P = D_1 \oplus D_2 \oplus \dots \oplus D_m$).
* **Odd Parity**: Total number of $1$s is odd ($P = \sim(D_1 \oplus D_2 \oplus \dots \oplus D_m)$).

> [!theorem] Parity Invariants
> * For single parity codes, changing $1$ bit yields an invalid codeword; changing a second bit restores valid parity. Thus, $d_{\min} = 2$.
> * Single parity detects **all odd counts of bit errors** ($1, 3, 5, \dots$) and fails on **all even counts of bit errors** ($2, 4, 6, \dots$).

### Internet Checksum (1's Complement Arithmetic)

Used widely across TCP, UDP, and IP headers.
[IPv4 Checksum](IPv4%20Checksum.md)
#### Sender Algorithm
1. The data payload is grouped into 16-bit binary integer words.
2. Compute the sum using 1's complement addition (any carry bit emerging from the MSB is wrapped around and added to the LSB).
3. Take the 1's complement (bitwise NOT) of the wrapped sum; this value is the **Checksum**.
4. Append the checksum to the payload.

#### Receiver Verification
1. Sum all incoming 16-bit words, including the appended checksum, using wrapped 1's complement addition.
2. If the wrapped sum equals `0xFFFF` (all $1$s), or equivalently if the bitwise complement of the sum is `0x0000`, the packet is accepted as error-free; otherwise, it is rejected.

> [!question] Worked Checksum Example
> Given the data words in hexadecimal: `0001`, `f204`, `f4f5`, `f6f7`. Calculate the checksum and verify reception.

* **Summation**:
  $$\mathtt{0001}_{16} + \mathtt{f204}_{16} + \mathtt{f4f5}_{16} + \mathtt{f6f7}_{16} = \mathtt{2ddf1}_{16}$$
* **Wrap Carry Around**:
  $$\text{Sum} = \mathtt{ddf1}_{16} + \mathtt{2}_{16} = \mathtt{ddf3}_{16}$$
* **Negate (Bitwise NOT)**:
  $$\text{Checksum} = \sim \mathtt{ddf3}_{16} = \mathtt{220C}_{16}$$
* **Codeword**: `0001 f204 f4f5 f6f7 220C`.
* **Receiver Verification**:
  $$\mathtt{ddf3}_{16} + \mathtt{220C}_{16} = \mathtt{FFFF}_{16}$$
  $$\sim \mathtt{FFFF}_{16} = \mathtt{0000}_{16} \implies \text{Accepted as valid}$$.
