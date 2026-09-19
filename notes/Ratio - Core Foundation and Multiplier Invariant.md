> **Homogeneous Invariant Corollary**:
> For any homogeneous rational function $f(A_1, \dots, A_n)$ of degree $0$ (where the sum of powers in every term of the numerator equals that of the denominator), the scale factor $k^d$ cancels identically[cite: 1]:
> $$\frac{P(r_1 k, \dots, r_n k)}{Q(r_1 k, \dots, r_n k)} = \frac{k^d \cdot P(r_1, \dots, r_n)}{k^d \cdot Q(r_1, \dots, r_n)} = \frac{P(r_1, \dots, r_n)}{Q(r_1, \dots, r_n)}$$[cite: 1]
> In all such homogeneous expressions, real quantities can be directly replaced with their raw ratio values ($k = 1$)[cite: 1].

```mermaid
flowchart LR
    A["Raw Ratio: a : b : c"] --> B["Total Units = a + b + c"]
    B --> C["Scale Factor: k = Total Sum / Total Units"]
    C --> D["Real Quantities: A = a*k, B = b*k, C = c*k"]
```


> [!question]
> **Type 1: Basic Distribution (Classroom Strength)**
> If the ratio of boys and girls is $5 : 8$ and the total strength of the class is $156$, find the number of girls in the class[cite: 1].
> - 1. $96$
> - 2. $100$
> - 3. $30$
> - 4. $15$[cite: 1]
> 
> *Solution:*
> Let $\text{Boys} = 5x$ and $\text{Girls} = 8x$[cite: 1].
> Total units $= 5x + 8x = 13x$[cite: 1].
> $$13x = 156 \implies x = \frac{156}{13} = 12$$[cite: 1]
> $$\text{Number of Girls} = 8x = 8 \times 12 = 96$$[cite: 1]
> **Correct Option: 1**[cite: 1]

> [!question]
> **Type 2: Homogeneous vs Non-Homogeneous Expressions**
> If $a : b = 5 : 3$, evaluate:
> 1. $\frac{a^3 - b^3}{a^3 + b^3}$[cite: 1]
> 2. $\frac{a^3 - b^3}{a^2 + ab + b^2}$[cite: 1]
> 
> *Solution:*
> Let $a = 5x, b = 3x$[cite: 1].
> 1. Both numerator and denominator have degree $3$ (homogeneous of degree $0$)[cite: 1]:
>    $$\frac{(5x)^3 - (3x)^3}{(5x)^3 + (3x)^3} = \frac{125x^3 - 27x^3}{125x^3 + 27x^3} = \frac{98x^3}{152x^3} = \frac{98}{152} = \frac{49}{76} \quad (98 : 152)$$[cite: 1]
> 2. Numerator has degree $3$, while denominator has degree $2$:
>    $$\frac{125x^3 - 27x^3}{25x^2 + 15x^2 + 9x^2} = \frac{98x^3}{49x^2} = 2x$$[cite: 1]
>    Since the value depends on $x$, it **cannot be determined**[cite: 1].

> [!question]
> **PYQ (CDS 1 2024): Radical Ratio Homogeneity**
> If $a : b : c : d = \sqrt{4} : \sqrt{3} : \sqrt{2} : \sqrt{1}$, then what is the value of $\frac{-a^2 + b^2 + c^2 + d^2}{a^2 - b^2 + c^2 - d^2}$?[cite: 1]
> - (a) $1$
> - (b) $2$
> - (c) $3$
> - (d) $6$[cite: 1]
> 
> *Solution:*
> Let $a = 2x, b = \sqrt{3}x, c = \sqrt{2}x, d = 1x$[cite: 1].
> Square each term: $a^2 = 4x^2, b^2 = 3x^2, c^2 = 2x^2, d^2 = x^2$[cite: 1].
> Numerator:
> $$-4x^2 + 3x^2 + 2x^2 + x^2 = 2x^2$$[cite: 1]
> Denominator:
> $$4x^2 - 3x^2 + 2x^2 - x^2 = 2x^2$$[cite: 1]
> Expression:
> $$\frac{2x^2}{2x^2} = 1$$[cite: 1]
> **Correct Option: (a)**[cite: 1]

> [!question]
> **PYQ (CDS 1 2024): Independent Multiplier Pairs**
> If $m : n = 1 : 2$ and $p : q = 3 : 4$, then what is $(2m + 4p) : (n + 3q)$ equal to?[cite: 1]
> - (a) $1 : 1$
> - (b) $1 : 3$
> - (c) $2 : 1$
> - (d) $2 : 3$[cite: 1]
> 
> *Solution:*
> Let $m = x, n = 2x$ and $p = 3y, q = 4y$[cite: 1].
> Ratio expression:
> $$\frac{2m + 4p}{n + 3q} = \frac{2(x) + 4(3y)}{2x + 3(4y)} = \frac{2x + 12y}{2x + 12y} = \frac{1}{1}$$[cite: 1]
> The coefficients align identically, making the expression $1 : 1$ independent of $x$ and $y$[cite: 1].
> **Correct Option: (a)**[cite: 1]

> [!question]
> **PYQ (CDS 1 2025): Cyclic Pair Sums**
> If $(x + y) : (y + z) : (z + x) = 3 : 5 : 6$ and $x + y + z = 14$, then what is $x^2 + y^2 + z^2$ equal to?[cite: 1]
> - (a) $81$
> - (b) $84$
> - (c) $87$
> - (d) $90$[cite: 1]
> 
> *Solution:*
> Set up cyclic equations using scale factor $k$[cite: 1]:
> 1. $x + y = 3k$[cite: 1]
> 2. $y + z = 5k$[cite: 1]
> 3. $z + x = 6k$[cite: 1]
> Summing all three equations:
> $$2(x + y + z) = 14k \implies x + y + z = 7k$$[cite: 1]
> Given $x + y + z = 14 \implies 7k = 14 \implies k = 2$[cite: 1].
> Substitute $k = 2$ back to isolate each variable[cite: 1]:
> - $z = (x + y + z) - (x + y) = 7k - 3k = 4k = 4(2) = 8$[cite: 1]
> - $x = (x + y + z) - (y + z) = 7k - 5k = 2k = 2(2) = 4$[cite: 1]
> - $y = (x + y + z) - (z + x) = 7k - 6k = 1k = 1(2) = 2$[cite: 1]
> Now evaluate $x^2 + y^2 + z^2$:
> $$x^2 + y^2 + z^2 = 4^2 + 2^2 + 8^2 = 16 + 4 + 64 = 84$$[cite: 1]
> **Correct Option: (b)**[cite: 1]

> [!question]
> **PYQ (CDS 1 2025): Componendo and Dividendo Application**
> The ratio of sum of two numbers to their difference is $5 : 1$[cite: 1]. What is the ratio of the sum of their squares to the difference of their squares?[cite: 1]
> - (a) $13 : 5$
> - (b) $25 : 1$
> - (c) $9 : 4$
> - (d) $16 : 1$[cite: 1]
> 
> *Solution:*
> Given $\frac{x + y}{x - y} = \frac{5}{1}$[cite: 1].
> Cross-multiplying:
> $$x + y = 5x - 5y \implies 4x = 6y \implies \frac{x}{y} = \frac{6}{4} = \frac{3}{2}$$[cite: 1]
> Let $x = 3k, y = 2k$[cite: 1].
> Compute ratio of squares:
> $$\frac{x^2 + y^2}{x^2 - y^2} = \frac{(3k)^2 + (2k)^2}{(3k)^2 - (2k)^2} = \frac{9k^2 + 4k^2}{9k^2 - 4k^2} = \frac{13k^2}{5k^2} = \frac{13}{5}$$[cite: 1]
> **Correct Option: (a)**[cite: 1]

> [!question]
> **PYQ (CDS 1 2024): Cyclic Homogeneous Evaluation**
> If $(a + b) : (b + c) : (c + a) = 5 : 7 : 6$, then what is the value of $(a - b + c) : (a + b - c)$?[cite: 1]
> - (a) $1 : 1$
> - (b) $2 : 3$
> - (c) $3 : 1$
> - (d) $4 : 3$[cite: 1]
> 
> *Solution:*
> Let $a + b = 5k$, $b + c = 7k$, $c + a = 6k$[cite: 1].
> Summing equations:
> $$2(a + b + c) = 18k \implies a + b + c = 9k$$[cite: 1]
> Extract each variable:
> - $c = 9k - 5k = 4k$[cite: 1]
> - $a = 9k - 7k = 2k$[cite: 1]
> - $b = 9k - 6k = 3k$[cite: 1]
> Evaluate the target expression:
> $$\frac{a - b + c}{a + b - c} = \frac{2k - 3k + 4k}{2k + 3k - 4k} = \frac{3k}{k} = \frac{3}{1}$$[cite: 1]
> **Correct Option: (c)**[cite: 1]
