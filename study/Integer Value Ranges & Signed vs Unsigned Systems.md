---
title: Integer Value Ranges & Signed vs Unsigned Systems
tags:
  - clang
  - c-language
  - integer-representation
  - study
---

# Integer Value Ranges & Signed vs Unsigned Systems

Different binary encoding systems define distinct numerical bounds for $k$-bit integers.

## Signed Binary Systems Comparison

For an $n$-bit total representation ($1$ sign bit + $n-1$ magnitude bits):

| System | $+0$ | $-0$ | Minimum Value | Maximum Value |
| :--- | :--- | :--- | :--- | :--- |
| **Sign-Magnitude** | $0\underbrace{00\dots0}_{n-1}$ | $1\underbrace{00\dots0}_{n-1}$ | $-(2^{n-1}-1)$ | $2^{n-1}-1$ |
| **1's Complement** | $0\underbrace{00\dots0}_{n-1}$ | $1\underbrace{11\dots1}_{n-1}$ | $-(2^{n-1}-1)$ | $2^{n-1}-1$ |
| **2's Complement** | $0\underbrace{00\dots0}_{n-1}$ | *(none)* | $-2^{n-1}$ | $2^{n-1}-1$ |

> [!important] Why Two's Complement Superiority?
> Two's complement is universally preferred in modern computer hardware because:
> 1. **Unique Zero:** Eliminates dual representation of zero ($+0$ vs $-0$).
> 2. **Full Code Utilization:** Maximizes total $2^n$ distinct bit patterns (gaining $-2^{n-1}$).
> 3. **Simplified Arithmetic Logic:** Addition and subtraction use identical adder circuitry.

---

## Value Ranges for $k$-bit Integers

> [!property] Range Formulations
> For any $k$-bit integer container in C:
> - **Unsigned Range:**
>   $$[0,\; 2^k - 1]$$
> - **Signed (Two's Complement) Range:**
>   $$[-2^{k-1},\; 2^{k-1} - 1]$$
> 
> *The asymmetry in signed range arises because zero consumes one non-negative code pattern: `00...0`.*

---

## Related Notes
- [[Two's Complement Fundamentals & Weight Method]]
- [[Integer Promotion Rules in C]]
- [[Overflow Definition & Detection Rules]]
