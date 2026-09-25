# Growth Ladder (Asymptotic Order of Growth)

> [!tip] Rule of Thumb
> Always evaluate asymptotic growth from **slowest to fastest** when comparing time complexities.
> 
> $$1 < \log n < \sqrt{n} < n < n \log n < n^2 < n^3 < 2^n < n! < n^n$$

---

### Ranked Order (Slowest $\to$ Fastest)

1. **Constant:** $\mathcal{O}(1)$
2. **Logarithmic:** $\mathcal{O}(\log n)$
3. **Sub-linear / Fractional Power:** $\mathcal{O}(\sqrt{n})$ or $\mathcal{O}(n^{1/2})$
4. **Linear:** $\mathcal{O}(n)$
5. **Linearithmic / Quasilinear:** $\mathcal{O}(n \log n)$
6. **Quadratic:** $\mathcal{O}(n^2)$
7. **Cubic:** $\mathcal{O}(n^3)$
8. **Exponential:** $\mathcal{O}(2^n)$
9. **Factorial:** $\mathcal{O}(n!)$
10. **Super-Exponential:** $\mathcal{O}(n^n)$

---

### Comparison Table

| Rank | Function | Complexity Class | Example Algorithm / Operation |
| :---: | :--- | :--- | :--- |
| **1** | $1$ | Constant | Accessing an array element |
| **2** | $\log n$ | Logarithmic | Binary search |
| **3** | $\sqrt{n}$ | Fractional polynomial | Primality test (trial division) |
| **4** | $n$ | Linear | Linear search, array traversal |
| **5** | $n \log n$ | Linearithmic | Merge Sort, Heap Sort |
| **6** | $n^2$ | Quadratic | Bubble Sort, Selection Sort |
| **7** | $n^3$ | Cubic | Standard matrix multiplication |
| **8** | $2^n$ | Exponential | Recursive Fibonacci, $0/1$ Knapsack (brute-force) |
| **9** | $n!$ | Factorial | Generating all permutations, Traveling Salesperson (brute-force) |
| **10** | $n^n$ | Super-Exponential | Brute-force state-space search |

---

### Extended Relative Comparisons

> [!note] Useful In-Between Identities
> - **Double Logarithmic:** $\log \log n < \log n$
> - **Polylogarithmic vs. Fractional:** $(\log n)^k < n^\epsilon \quad (\forall \, k > 0, \, \epsilon > 0)$
> - **Base of Exponents:** $2^n < 3^n < e^n$
> - **Stirling's Approximation:** $n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n \implies 2^n < n! < n^n$