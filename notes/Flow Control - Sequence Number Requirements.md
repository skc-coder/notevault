## Sequence Number Bounds and Window Sizing

To prevent ambiguous duplicate frame acceptances across wrap-around boundaries, the available sequence numbers must be bounded relative to window sizes[cite: 1].

> [!theorem] Fundamental Window Sizing Invariant
> For any sliding window ARQ protocol:
> $$W_s + W_r \le \text{Available Sequence Numbers (ASN)}$$[cite: 1]
> If $k$ bits are allocated for sequence numbers, then $\text{ASN} = 2^k$[cite: 1]:
> $$W_s + W_r \le 2^k$$[cite: 1]

### Bounds by Architecture

* **Stop-and-Wait**:
  $$W_s = 1, \, W_r = 1 \implies 1 + 1 = 2 \le 2^k \implies k \ge 1\text{ bit}$$
[cite: 1]
  *(Known as the Alternating Bit Protocol)*[cite: 1].
* **Go-Back-N**:
  $$W_r = 1 \implies W_s + 1 \le 2^k \implies W_s \le 2^k - 1$$
[cite: 1]
* **Selective Repeat**:
  To prevent overlapping receive windows upon total ACK loss, sender and receiver windows are chosen equal ($W_s = W_r$)[cite: 1]:
  $$W_s + W_s \le 2^k \implies 2W_s \le 2^k \implies W_s \le 2^{k-1}$$
[cite: 1]

> [!question] Sequence Bit Sizing Exercises
> 1. A sliding window protocol uses $W_s = 200$[cite: 1]. Find minimum sequence bits:
>    * GBN ($W_r = 1$): $\text{ASN} \ge 200 + 1 = 201 \implies k = \lceil \log_2(201) \rceil = 8\text{ bits}$[cite: 1].
>    * SR ($W_r = 200$): $\text{ASN} \ge 200 + 200 = 400 \implies k = \lceil \log_2(400) \rceil = 9\text{ bits}$[cite: 1].
> 2. A duplex link has $T_p = 25\text{ ms}$, frame transmission time $T_t = 1\text{ ms}$, and ACK packet size equal to data packet size[cite: 1]. How many bits are required to maximally pack the link in transit[cite: 1]?
  Window Sizing & Sequence Bits ($T_p = 25\text{ms}, T_t = 1\text{ms}$)
> * **Standard ($T_{\text{ack}} = 0$):** $W_{\text{opt}} = 1 + 2a = 51$ frames $\implies$ **GBN:** 6 bits ($\lceil\log_2 52\rceil$), **SR:** 7 bits ($\lceil\log_2 102\rceil$)
> * **Strict Duplex ($T_{\text{ack}} = 1\text{ms}$):** $W_{\text{opt}} = \frac{1+25+1+25}{1} = 52$ frames $\implies$ **GBN:** 6 bits ($\lceil\log_2 53\rceil$), **SR:** 7 bits ($\lceil\log_2 104\rceil$)
> * **Key Takeaway:** Both models require $\ge 6$ bits (GBN) or $7$ bits (SR); taking $T_p/T_t = 25 \implies 5$ bits is mathematically invalid.
