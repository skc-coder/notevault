Hamming codes are single-error-correcting linear block codes with $d_{\min} = 3$.
Why 3? Chaining any bit in the combined code needs two more bit filps to get a valid codeword.

> [!formula] Parity Bit Sizing Invariant (Hamming Rule)
> To correct all single-bit errors in an $m$-bit message word using $r$ parity bits (giving total codeword length $n = m + r$):
> $$2^r \ge m + r + 1$$
> Each of the $m+r$ bit locations could contain an error, plus one state to indicate zero errors, requiring at least $m + r + 1$ unique syndrome states.

> [!question] Parity Bit Sizing
> 1. Minimum parity bits for $m = 10\text{ bits}$:
>    * Try $r = 4$: $2^4 = 16$; $m + r + 1 = 10 + 4 + 1 = 15$. Since $16 \ge 15$, $r = 4\text{ bits}$ suffice.
> 2. Minimum parity bits for $m = 27\text{ bits}$:
>    * Try $r = 5$: $2^5 = 32$; $27 + 5 + 1 = 33$ ($32 < 33$, fails).
>    * Try $r = 6$: $2^6 = 64$; $27 + 6 + 1 = 34$ ($64 \ge 34$, holds).
>    * Minimum parity bits required $= 6$.

**NOTE: The positions are obtained by mixing the data and parity bits.** 

### Codeword Construction Rules (Even Parity)

1. Number bit positions starting from $1$ ($1, 2, 3, 4, 5, \dots, n$).
2. Positions that are powers of $2$ ($1, 2, 4, 8, 16, \dots$) are reserved strictly for parity bits ($P_1, P_2, P_4, P_8, \dots$).
3. All remaining bit positions are allocated to message data bits ($D_3, D_5, D_6, D_7, \dots$).
4. Parity bits cover bit positions that have a $1$ in their binary representation:
   * $P_1$ (bit 1, binary `...001`): Checks bits with LSB $= 1$ $\to 1, 3, 5, 7, 9, 11, \dots$ (Check 1, skip 1).
   * $P_2$ (bit 2, binary `...010`): Checks bits with 2nd bit $= 1$ $\to 2, 3, 6, 7, 10, 11, \dots$ (Check 2, skip 2).
   * $P_4$ (bit 4, binary `...100`): Checks bits $4, 5, 6, 7, 12, 13, \dots$ (Check 4, skip 4).
   * $P_8$ (bit 8, binary `...1000`): Checks bits $8, 9, 10, 11, 12, 13, 14, 15, \dots$ (Check 8, skip 8).

| Bit Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bit Type** | $P_1$ | $P_2$ | $D_3$ | $P_4$ | $D_5$ | $D_6$ | $D_7$ | $P_8$ | $D_9$ | $D_{10}$ | $D_{11}$ |
| $P_1$ Check | $\times$ | | $\times$ | | $\times$ | | $\times$ | | $\times$ | | $\times$ |
| $P_2$ Check | | $\times$ | $\times$ | | | $\times$ | $\times$ | | | $\times$ | $\times$ |
| $P_4$ Check | | | | $\times$ | $\times$ | $\times$ | $\times$ | | | | |
| $P_8$ Check | | | | | | | | $\times$ | $\times$ | $\times$ | $\times$ |

> [!question] Error Detection and Correction Trace
> Suppose a receiver receives the 7-bit codeword `1010111` (bit positions $1$ to $7$). Determine the corrected codeword assuming even parity.

* **Received Bits**:
  $b_1=1, b_2=0, b_3=1, b_4=0, b_5=1, b_6=1, b_7=1$.
* **Parity Checks**:
  * $P_1$ covers bits $1, 3, 5, 7$: $1 \oplus 1 \oplus 1 \oplus 1 = 0$ (Even count of $1$s $\implies$ **Pass**, parity bit $s_1 = 0$).
  * $P_2$ covers bits $2, 3, 6, 7$: $0 \oplus 1 \oplus 1 \oplus 1 = 1$ (Odd count of $1$s $\implies$ **Fail**, parity bit $s_2 = 1$).
  * $P_4$ covers bits $4, 5, 6, 7$: $0 \oplus 1 \oplus 1 \oplus 1 = 1$ (Odd count of $1$s $\implies$ **Fail**, parity bit $s_3 = 1$).
* **Syndrome Calculation**:
  $$\text{Syndrome} = s_3 s_2 s_1 = 110_2 = 6_{10}$$
  Failing parities $P_2$ and $P_4$ sum to position $2 + 4 = 6$.
* **Correction**: Invert bit $6$:
  $$b_6 = 1 \xrightarrow{\text{flip}} 0$$
* **Corrected Codeword**: `1010101`.
