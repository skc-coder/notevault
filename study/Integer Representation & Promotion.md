## 1. Two's Complement Fundamentals & Weight Method

In C, signed integer types are standardly represented using two's complement notation.

> [!definition] Two's Complement
> The two's complement of an $n$-bit binary integer is formed by inverting all bits (1's complement) and adding $1$ to the least significant bit (LSB):
> $$\text{Two's Complement}(A) = \sim A + 1$$

> [!important] 
In two's complement system the positive number have simply the normal binary representation but negative number have the 2's complement representation of their absolute value. 

Hence, redundant sign bits can be added or eliminated without altering the numeric value:
* For positive numbers: `0001` $\equiv$ `01` (even tough in 2's complement adding 0 changes value)
* For negative numbers: `11101` $\equiv$ `101`

### Direct Evaluation via Negative MSB Weight
An $n$-bit signed binary number $b_{n-1}b_{n-2}\dots b_1b_0$ can be directly converted to its decimal equivalent by assigning a negative positional weight to the Most Significant Bit (MSB):

> [!formula] Direct Two's Complement Formula
> $$V = -b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$

**Examples:**
* Evaluating `1011` ($4$-bit signed):
  $$V = -1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = -8 + 0 + 2 + 1 = -5$$
* Evaluating `0101` ($4$-bit signed):
  $$V = -0 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 0 + 4 + 0 + 1 = 5$$

Alternatively:
* If $\text{MSB} = 0$: The number is positive; perform standard binary-to-decimal conversion.
* If $\text{MSB} = 1$: The number is negative; take the two's complement of the pattern, convert to decimal, and prepend a minus sign ($-$).

---

## 2. Value Ranges for $k$-bit Integers

> [!property] Range of $k$-bit Integer Representations
> For an integer represented using $k$ bits:
> * **Unsigned Range:**
>   $$[0,\; 2^k - 1]$$
> * **Signed (Two's Complement) Range:**
>   $$[-2^{k-1},\; 2^{k-1} - 1]$$
>   *(The asymmetry arises because zero consumes one non-negative code: `00...0`)*

---

## 3. Integer Promotion Rules

> [!definition] Integer Promotion
> CPU registers and arithmetic logic units operate most efficiently on natural word boundaries (typically $32$-bit or $64$-bit). Therefore, before evaluating expressions or passing arguments through variadic parameters (such as `printf`), C automatically promotes smaller integer types (`char`, `signed char`, `unsigned char`, `short`, `unsigned short`, `_Bool`) to `int` or `unsigned int`.
>
> * If `int` can represent all values of the original type, the value is converted to `int`.
> * Otherwise, it is converted to `unsigned int`.

### Character Literal Type Discrepancy
In C, a character literal such as `'a'` has type `int` ($4$ bytes) with ASCII value `97`. Assigning it to `char` truncates the upper $3$ bytes:
```c
char c = 'a'; // 'a' is a 4-byte int (0x00000061); 3 bytes are truncated to fit 1 byte
```
*(Note: In C++, `'a'` is natively typed as `char` of $1$ byte).*

---

## Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->
