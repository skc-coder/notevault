### The 3-Step Universal Framework

Every loop counting problem, no matter how complex, reduces to three systematic steps:

  

1. **Find the sequence of the loop variable:** Write the value of the loop control variable after $k$ iterations (starting at $k = 0, 1, 2, \dots$).
    
      
    
2. **Apply the termination condition:** Set the expression for the $k$-th iteration against the loop condition to solve for the maximum number of iterations $k_{max}$.
    
      
    
3. **Classify dependency and sum:**
    
      
    - If nested loops are **independent**, multiply their respective iteration counts: $T(n) = (\text{iterations of outer}) \times (\text{iterations of inner})$.
        
          
        
    - If nested loops are **dependent**, express the inner loop’s work as a function of the outer loop’s current value, then evaluate the summation across all outer iterations.
        
          
        

### The Fundamental Progression Archetypes

#### 1. Additive / Linear ($i \leftarrow i + c$)

At step $k$, $i_k = i_0 + k \cdot c$.

For condition $i \le n$, $i_0 + k \cdot c \le n \implies k \approx \frac{n - i_0}{c}$.

The time complexity is $\Theta(n)$.

  

#### 2. Multiplicative / Doubling ($i \leftarrow i \times 2$) or Halving ($i \leftarrow i / 2$)

At step $k$, $i_k = i_0 \cdot 2^k$.

For condition $i \le n$ starting at $i_0 = 1$, $2^k \le n \implies k \le \log_2 n$.

The total number of iterations is $\lfloor \log_2 n \rfloor + 1 = \Theta(\log n)$.

Similarly, if $i$ starts at $n$ and halves until reaching $1$, $n / 2^k \ge 1 \implies 2^k \le n$, giving the same $\Theta(\log n)$ iterations.

  

#### 3. Quadratic / Polynomial Condition ($i \times i \le n$)

At step $k$ with $i$ incrementing by $1$, $i_k = k$.

The loop condition is $i^2 \le n \implies k^2 \le n \implies k \le \sqrt{n}$.

The loop executes $\lfloor \sqrt{n} \rfloor$ times, giving $\Theta(\sqrt{n})$.

  

#### 4. Successive Squaring ($i \leftarrow i^2$)

At step $k$ starting with $i_0 = 2$:

  

- $k = 0 \implies i = 2 = 2^{2^0}$
    
      
    
- $k = 1 \implies i = 2^2 = 2^{2^1}$
    
      
    
- $k = 2 \implies i = (2^2)^2 = 2^4 = 2^{2^2}$
    
      
    
- Step $k \implies i_k = 2^{2^k}$
    
      
    

Setting $i_k \le n$:

  

$$2^{2^k} \le n \implies 2^k \le \log_2 n \implies k \le \log_2(\log_2 n)$$

The total iterations equal $\lfloor \log_2 \log_2 n \rfloor + 1 = \Theta(\log \log n)$.

  

#### 5. Successive Square-Rooting ($i \leftarrow \sqrt{i}$)

Starting with $i_0 = n$ and terminating when $i \le 2$:

At step $k$, $i_k = n^{(1/2)^k} = n^{2^{-k}}$.

Setting $n^{2^{-k}} \le 2$ and taking $\log_2$ twice:

  

$$2^{-k} \log_2 n \le 1 \implies 2^k \ge \log_2 n \implies k \ge \log_2 \log_2 n$$

This also yields $\Theta(\log \log n)$ iterations.

  

### Classic Nested Loop Patterns Solved

#### Pattern 1: Multiplicative Outer, Dependent Linear Inner (The Classic Trap)

C

```
for (int i = 1; i <= n; i *= 2) {
    for (int j = 1; j <= i; j++) {
        count++;
    }
}
```

The outer loop variable $i$ assumes values $2^0, 2^1, 2^2, \dots, 2^k$ where $2^k \le n$, so $k_{max} = \lfloor \log_2 n \rfloor$.

For each outer step, the inner loop executes exactly $i$ times.

The total operations form a geometric progression:

  

$$T(n) = \sum_{k=0}^{\lfloor \log_2 n \rfloor} 2^k = 2^{\lfloor \log_2 n \rfloor + 1} - 1 \approx 2n - 1 = \Theta(n)$$

Notice that while the outer loop runs $\log n$ times and the inner loop can reach $n$, the total time is **not** $\Theta(n \log n)$ because the inner loop only reaches $n$ on the very last step. The earlier steps are exponentially smaller.

  

#### Pattern 2: Halving Outer, Linear Inner

C

```
for (int i = n; i > 0; i /= 2) {
    for (int j = 0; j < i; j++) {
        count++;
    }
}
```

The outer loop variable starts at $n$ and halves each time: $n, n/2, n/4, \dots, 1$.

The inner loop runs $i$ times.

Summing the total steps:

  

$$T(n) = n + \frac{n}{2} + \frac{n}{4} + \dots + 1 = n \left(1 + \frac{1}{2} + \frac{1}{4} + \dots\right) < 2n = \Theta(n)$$

#### Pattern 3: Linear Outer, Doubling Inner

C

```
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j *= 2) {
        count++;
    }
}
```

For a given $i$, the inner loop executes $\lfloor \log_2 i \rfloor + 1$ times.

The total number of operations is:

  

$$T(n) = \sum_{i=1}^n (\log_2 i + 1) = n + \sum_{i=1}^n \log_2 i = n + \log_2(n!)$$

Using Stirling’s approximation ($\log_2(n!) = \Theta(n \log n)$):

  

$$T(n) = \Theta(n \log n)$$

#### Pattern 4: Sieve / Harmonic Step Pattern

C

```
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j += i) {
        count++;
    }
}
```

For a fixed $i$, $j$ starts at $i$ and increments by $i$ up to $n$. The number of executions is $\lfloor n / i \rfloor$.

Summing over all $i$ from $1$ to $n$:

  

$$T(n) = \sum_{i=1}^n \left\lfloor \frac{n}{i} \right\rfloor \approx n \sum_{i=1}^n \frac{1}{i}$$

The sum $\sum_{i=1}^n \frac{1}{i}$ is the harmonic series $H_n = \ln n + \gamma + O(1/n)$.

Therefore:

  

$$T(n) = n \ln n + O(n) = \Theta(n \log n)$$

#### Pattern 5: Squaring Outer, Linear Inner

C

```
for (int i = 2; i <= n; i = i * i) {
    for (int j = 1; j <= i; j++) {
        count++;
    }
}
```

At step $k$ of the outer loop, $i_k = 2^{2^k}$.

The outer loop stops when $2^{2^m} \le n$, where $m = \lfloor \log_2 \log_2 n \rfloor$.

The inner loop executes $i_k$ times:

  

$$T(n) = 2^{2^0} + 2^{2^1} + 2^{2^2} + \dots + 2^{2^m}$$

In a doubly-exponential series, the last term $2^{2^m}$ dominates the sum:

  

$$2^{2^0} + 2^{2^1} + \dots + 2^{2^m} < 2 \cdot 2^{2^m} \le 2n$$

Hence, $T(n) = \Theta(n)$.

  

#### Pattern 6: Squaring Outer, Doubling Inner

C

```
for (int i = 2; i <= n; i = i * i) {
    for (int j = 1; j <= i; j *= 2) {
        count++;
    }
}
```

At step $k$, $i = 2^{2^k}$.

The inner loop variable $j$ doubles up to $i$, executing $\log_2(i) = \log_2(2^{2^k}) = 2^k$ times.

The outer loop runs for $k = 0, 1, 2, \dots, \lfloor \log_2 \log_2 n \rfloor$.

Summing the operations:

  

$$T(n) = \sum_{k=0}^{\lfloor \log_2 \log_2 n \rfloor} 2^k = 2^{\lfloor \log_2 \log_2 n \rfloor + 1} - 1 \approx 2 \log_2 n - 1 = \Theta(\log n)$$

### Quick Reference Rules

1. When a loop counter changes by addition ($+c$ or $-c$), it produces linear or polynomial counts ($\Theta(n)$ or $\Theta(n^k)$).
    
      
    
2. When a loop counter changes by multiplication ($\times c$ or $/c$), it produces logarithmic counts ($\Theta(\log n)$).
    
      
    
3. When a loop counter changes by powers ($i^2$ or $\sqrt{i}$), it produces double-logarithmic counts ($\Theta(\log \log n)$).
    
      
    
4. For nested loops where the inner loop's work doubles each time (such as $1 + 2 + 4 + \dots + n$), the total is strictly bounded by $2n = \Theta(n)$, not $O(n \log n)$.
    
      
    
5. For nested loops where the inner work is $n/i$, the harmonic summation always produces $\Theta(n \log n)$.