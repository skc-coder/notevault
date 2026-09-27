> [!question] Identification of Class and Network ID
> Identify the class, Network ID, and number of available host addresses for the following IP addresses:
> 1. `00000001.00001010.00000000.00000001`
> 2. `11000000.10101000.00000001.00000001`
> 3. `227.12.14.87`
> 4. `193.14.56.22`
> 5. `132.6.17.85`
> 6. `201.180.56.5`

### Analytical Solutions

1. `00000001...`: The first bit is `0` $\implies$ **Class A**.
2. `11000000...`: The leading bits are `110` $\implies$ **Class C**.
3. `227.12.14.87`: The first byte is $227_{10} = 11100011_2$. The leading four bits are `1110` (range $224 - 239$) $\implies$ **Class D** (Multicast Address).
4. `193.14.56.22`: The first byte is $193$ (range $192 - 223$, binary `11000001`) $\implies$ **Class C**.
5. `132.6.17.85`:
   * First byte is $132$ (range $128 - 191$, binary starts with `10`) $\implies$ **Class B**.
   * Network ID consumes the first $16$ bits: `132.6.0.0`.
1. `201.180.56.5`:
   * First byte is $201$ (range $192 - 223$, binary starts with `110`) $\implies$ **Class C**.
   * Network ID consumes the first $24$ bits: `201.180.56.0`.
