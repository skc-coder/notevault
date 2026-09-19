> [!theorem]
> **Power Homogeneity Principle for Equal Ratios**
> If a continuous equality holds across multiple ratios:
> $$\frac{A}{B} = \frac{C}{D} = \frac{E}{F} = k$$[cite: 1]
> Then for any real weighting coefficients $p, Q, R$ and power $n$:
> $$\frac{p A^n + Q C^n + R E^n}{p B^n + Q D^n + R F^n} = k^n$$[cite: 1]
> 
> **Proof**:
> Substitute $A = kB, C = kD, E = kF$[cite: 1]:
> $$\frac{p(kB)^n + Q(kD)^n + R(kF)^n}{p B^n + Q D^n + R F^n} = \frac{k^n(p B^n + Q D^n + R F^n)}{p B^n + Q D^n + R F^n} = k^n$$[cite: 1]

> [!question]
> **Type 10: Equal Ratio Power Evaluation**
> If $\frac{A}{B} = \frac{C}{D} = \frac{E}{F} = 8$, find the value of:
> $$\frac{9A^2 + 12C^2 + 15E^2}{12B^2 + 16D^2 + 20F^2}$$[cite: 1]
> 
> *Solution:*
> Factor out common scalar coefficients from numerator and denominator[cite: 1]:
> - Numerator: $3(3A^2 + 4C^2 + 5E^2)$[cite: 1]
> - Denominator: $4(3B^2 + 4D^2 + 5F^2)$[cite: 1]
> Rewrite the expression:
> $$\frac{3}{4} \cdot \left(\frac{3A^2 + 4C^2 + 5E^2}{3B^2 + 4D^2 + 5F^2}\right)$$[cite: 1]
> Apply the Power Homogeneity Theorem with $k = 8$ and $n = 2$[cite: 1]:
> $$\frac{3A^2 + 4C^2 + 5E^2}{3B^2 + 4D^2 + 5F^2} = k^2 = 8^2 = 64$$[cite: 1]
> Multiply by the extracted scalar ratio:
> $$\text{Result} = \frac{3}{4} \times 64 = 3 \times 16 = 48$$[cite: 1]
