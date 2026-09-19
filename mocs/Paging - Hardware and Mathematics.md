## Paging Hardware Architecture & Mathematical Formulation

Every active process maintains its own independent **Page Table** in physical memory. The operating system tracks the base of this table using the **PTBR (Page Table Base Register)**.

```
Logical Address (LA):                Physical Address (PA):
+---------------------+--------+     +----------------------+--------+
|   Page Number (p)   | Offset |     |   Frame Number (f)   | Offset |
|      (n - k) bits   | k bits |     |     (m - k) bits     | k bits |
+----------+----------+---+----+     +----------+-----------+----+---+
           |              |                     ^                |
           v              |                     |                |
     Page Table           |                     |                |
   +----+-------+         |                     |                |
   | p  |   f   |---------+---------------------+                |
   +----+-------+         |                                      |
   | .. |  ...  |         +--------------------------------------+
```

> [!formula] Fundamental Structural Identities
> Let:
> * Logical Address Space $= 2^n\text{ Bytes} \implies n\text{-bit } LA$
> * Physical Address Space $= 2^m\text{ Bytes} \implies m\text{-bit } PA$
> * Page Size $=$ Frame Size $= 2^k\text{ Bytes} \implies k\text{ offset bits}$
>
> Then:
> 1. $\text{Number of Pages} = \frac{\text{Size of } LAS}{\text{Page Size}} = \frac{2^n}{2^k} = 2^{n-k}$
> 2. $\text{Page Number Bits } (p) = n - k$
> 3. $\text{Number of Frames} = \frac{\text{Size of } PAS}{\text{Frame Size}} = \frac{2^m}{2^k} = 2^{m-k}$
> 4. $\text{Frame Number Bits } (f) = m - k$
> 5. $\text{Number of Page Table Entries (PTEs)} = \text{Number of Pages} = 2^{n-k}$

> [!property] Offset Invariant
> The internal byte offset within a page is identical to the byte offset within the mapped frame:
> $$\text{Page Offset} \equiv \text{Frame Offset} = k\text{ bits}$$
> While total bits in $LA$ and $PA$ usually differ ($n \ne m$), their offset bit-width is identical because $\text{Page Size} = \text{Frame Size}$.

### Integer Division and Modulo Analogy
Just as dividing a decimal number by $10^k$ yields the prefix via integer division (`//`) and the suffix via remainder (`%`):
* Decimal:
  $$\frac{1234}{10} \implies 1234 \mathbin{/\!/} 10 = 123, \quad 1234 \mathbin{\%} 10 = 4$$
  $$\frac{1234}{100} \implies 1234 \mathbin{/\!/} 100 = 12, \quad 1234 \mathbin{\%} 100 = 34$$
* Binary ($2^k$):
  Dividing an $n$-bit binary address by $2^k$ assigns:
  * The lower $k$ bits to the internal **Offset**: $d = LA \mathbin{\%} 2^k$
  * The remaining upper $(n - k)$ bits to the **Page Number**: $p = LA \mathbin{/\!/} 2^k$

### Physical Address Calculation
$$\text{Physical Address } (PA) = (\text{Frame Number} \times \text{Frame Size}) + \text{Offset}$$

`Frame Number` is 0 indexed.
