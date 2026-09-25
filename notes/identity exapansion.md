For an $n$-bit binary pattern $(b_{n-1} b_{n-2} \dots b_1 b_0)$, let $U$ be its **unsigned value** and $S$ be its **2's complement signed value**.

  

### The Mathematical Relation

$$S = U - b_{n-1} \cdot 2^n$$

Equivalently:

  

$$S = \begin{cases} U, & \text{if } U < 2^{n-1} \quad (b_{n-1} = 0) \\ U - 2^n, & \text{if } U \ge 2^{n-1} \quad (b_{n-1} = 1) \end{cases}$$

### Derivation

- **Unsigned interpretation:**
    
      
    
    $$U = \sum_{i=0}^{n-1} b_i \cdot 2^i = b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$
    
- **2's complement interpretation:**
    
      
    
    $$S = -b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i$$
    

Subtracting $U$ from $S$:

  

$$S - U = -b_{n-1} \cdot 2^{n-1} - b_{n-1} \cdot 2^{n-1} = -b_{n-1} \cdot 2^n$$

$$S = U - b_{n-1} \cdot 2^n$$

### Quick Example ($n = 4$ bits, pattern `1101`)

- $U = 8 + 4 + 0 + 1 = 13$
    
      
    
- Since MSB $b_3 = 1$:
    
    $$S = 13 - 2^4 = 13 - 16 = -3$$