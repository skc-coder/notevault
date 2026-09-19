## 1. The Core Multiplicative Relationship
Every price-consumption problem is governed by a product identity:

$$\text{Expenditure } (E) = \text{Price } (P) \times \text{Consumption } (C)$$

When changes occur, each variable is scaled by a **Multiplying Factor ($M$)**:
* $E_{\text{final}} = E_{\text{initial}} \times M_E$
* $P_{\text{final}} = P_{\text{initial}} \times M_P$
* $C_{\text{final}} = C_{\text{initial}} \times M_C$

Substituting these into the fundamental equation:

$$E_{\text{initial}} \cdot M_E = (P_{\text{initial}} \cdot M_P) \times (C_{\text{initial}} \cdot M_C)$$

Because $E_{\text{initial}} = P_{\text{initial}} \times C_{\text{initial}}$, baseline values cancel out:

$$M_E = M_P \times M_C \implies M_C = \frac{M_E}{M_P}$$

---

## 2. Terminology: The **Fractional Multiplier Transform (FMT)**
The process of mapping percentage changes into unit-normalized factors is called the **Fractional Multiplier Transform (FMT)**.

Instead of working with decimals or running lengthy percentage formulas, express the percentage shift as a reduced fraction $\frac{a}{b}$:

$$\text{Multiplier } (M) = 1 \pm \frac{a}{b} = \frac{b \pm a}{b}$$

### Transform Lookup
* **Percentage Increase ($+x\%$):**
  $$+x\% = +\frac{a}{b} \implies M = 1 + \frac{a}{b} = \frac{b + a}{b}$$
* **Percentage Decrease ($-x\%$):**
  $$-x\% = -\frac{a}{b} \implies M = 1 - \frac{a}{b} = \frac{b - a}{b}$$

| Shift Percentage | Reduced Fraction $\left(\pm \frac{a}{b}\right)$ | Transform Formula | Multiplying Factor ($M$) |
| :--- | :--- | :--- | :--- |
| $+20\%$ | $+\frac{1}{5}$ | $1 + \frac{1}{5}$ | $\frac{6}{5}$ ($1.20$) |
| $+25\%$ | $+\frac{1}{4}$ | $1 + \frac{1}{4}$ | $\frac{5}{4}$ ($1.25$) |
| $+33\frac{1}{3}\%$ | $+\frac{1}{3}$ | $1 + \frac{1}{3}$ | $\frac{4}{3}$ |
| $-20\%$ | $-\frac{1}{5}$ | $1 - \frac{1}{5}$ | $\frac{4}{5}$ ($0.80$) |
| $-16\frac{2}{3}\%$ | $-\frac{1}{6}$ | $1 - \frac{1}{6}$ | $\frac{5}{6}$ |
| $-12.5\%$ | $-\frac{1}{8}$ | $1 - \frac{1}{8}$ | $\frac{7}{8}$ |

---

## 3. Case A: Fixed Expenditure Shift ($M_E = 1$)
When total expenditure is kept strictly constant ($E_{\text{final}} = E_{\text{initial}}$):

$$M_E = 1 \implies M_P \times M_C = 1 \implies M_C = \frac{1}{M_P}$$

### The $\frac{a}{b} \to \frac{a}{b+a}$ Compensation Rule
* If price **increases** by $\frac{a}{b}$:
  $$M_P = \frac{b + a}{b} \implies M_C = \frac{b}{b + a}$$
  $$\Delta C = 1 - \frac{b}{b + a} = -\frac{a}{b + a}$$
  > **Rule:** An increase of $\frac{a}{b}$ in price requires an exact decrease of $\mathbf{\frac{a * 100}{b+a}}$ % in consumption.

* If price **decreases** by $\frac{a}{b}$:
  $$M_P = \frac{b - a}{b} \implies M_C = \frac{b}{b - a}$$
  $$\Delta C = \frac{b}{b - a} - 1 = +\frac{a}{b - a}$$
  > **Rule:** A decrease of $\frac{a}{b}$ in price allows an increase of $\mathbf{\frac{a}{b-a}}$ in consumption.

---

## 4. Case B: Simultaneous Shift ($M_E \neq 1$)
When expenditure is allowed to change alongside price, **never subtract percentages directly**. Always use the multiplier ratio:

$$M_C = \frac{M_E}{M_P}$$

### Worked Example
* **Condition:** Price rises by $20\%$ ($M_P = 1 + \frac{1}{5} = \frac{6}{5}$), expenditure rises by $8\%$ ($M_E = 1 + \frac{2}{25} = \frac{27}{25}$).
* **Calculation:**
  $$M_C = \frac{\frac{27}{25}}{\frac{6}{5}} = \frac{27}{25} \times \frac{5}{6} = \frac{9}{10}$$
* **Interpretation:**
  $$M_C = \frac{9}{10} = 1 - \frac{1}{10} \implies 10\% \text{ decrease in consumption.}$$

---

## 5. Summary Cheat Sheet
* **Product Form:** $M_E = M_P \times M_C$
* **Targeting Consumption:** $M_C = \frac{M_E}{M_P}$
* **Fixed Expenditure:** $M_C = \frac{1}{M_P}$
* **Quick Rule:** $+ \frac{a}{b} \implies - \frac{a}{b+a} \quad \Big| \quad - \frac{a}{b} \implies + \frac{a}{b-a}$

## 6. Questions

> [!question]
> **Original Price Computation**
> If a reduction of $10\%$ in the price of rice enables a person to obtain $22\text{ kg}$ more for Rs. $250$, then find the original price of rice per kg[cite: 1].
> - (A) $1.25$
> - (B) $2.42$
> - (C) $1.86$
> - (D) $1.62$[cite: 1]
> 
> *Solution:*
> 1. Ratio formulation:
>    Reduction $= 10\% = \frac{1}{10} \implies \text{Price ratio} = 10 : 9$[cite: 1].
>    Consumption ratio $= 9 : 10$[cite: 1].
> 2. Real difference:
>    $$\Delta Q = 10\text{ units} - 9\text{ units} = 1\text{ unit} = 22\text{ kg}$$[cite: 1]
>    Original quantity $= 9\text{ units} = 9 \times 22 = 198\text{ kg}$[cite: 1].
> 3. Original price per kg:
>    $$\text{Price}_{\text{orig}} = \frac{\text{Total Expenditure}}{\text{Original Quantity}} = \frac{250\text{ Rs}}{198\text{ kg}} \approx 1.262 \approx 1.25\text{ Rs/kg}$$[cite: 1]
> **Correct Option: (A)**[cite: 1]

> [!question]
> **Reduced Price Computation (CDS 1 2026)**
> A reduction of $10\%$ in the price of sugar enables a person to buy $6.2\text{ kg}$ more for Rs. $2790$[cite: 1]. What is the reduced price per kilogram?[cite: 1]
> - (a) Rs. $50$
> - (b) Rs. $48$
> - (c) Rs. $45$
> - (d) Rs. $42$[cite: 1]
> 
> *Solution:*
> 1. Ratio Analysis:
>    $$10\% \text{ reduction} = \frac{1}{10} \implies \text{Price} = 10 : 9 \implies \text{Quantity} = 9 : 10$$[cite: 1]
> 2. Unit scaling:
>    $$1\text{ unit} = 6.2\text{ kg}$$[cite: 1]
>    $$\text{New (Final) Quantity} = 10\text{ units} = 10 \times 6.2 = 62\text{ kg}$$[cite: 1]
> 3. Reduced price calculation:
>    $$\text{Reduced Price} = \frac{\text{Total Expenditure}}{\text{New Quantity}} = \frac{\text{Rs. } 2790}{62\text{ kg}} = \text{Rs. } 45/\text{kg}$$[cite: 1]
> **Correct Option: (c)**[cite: 1]

> [!question]
> **Q4: Constant Expenditure on Sugar**
> If the price of sugar increases by $20\%$, by what percentage must consumption be reduced so that expenditure remains unchanged?[cite: 1]
> - A. $16\frac{2}{3}\%$
> - B. $34\%$
> - C. $66\%$
> - D. $17\%$[cite: 1]
> 
> *Solution:*
> Price increase $= +20\% = +\frac{1}{5} \implies \text{Price ratio} = 5 \to 6$[cite: 1].
> Since Expenditure is constant, Consumption ratio $= 6 \to 5$[cite: 1].
> Reduction $= \frac{1}{6} \times 100 = 16\frac{2}{3}\%$[cite: 1].
> **Correct Option: A**[cite: 1]

> [!question]
> **Q5: Constant Area of Rectangle**
> If the length of a rectangle is decreased by $30\%$, by what percentage must its breadth be increased so that the area remains unchanged?[cite: 1]
> - A. $42\frac{6}{7}\%$
> - B. $\frac{3}{7}\%$
> - C. $\frac{6}{5}\%$
> - D. $\frac{3}{5}\%$[cite: 1]
> 
> *Solution:*
> Length decrease $= -30\% = -\frac{3}{10}$[cite: 1].
> Length ratio $= 10 \to 7$[cite: 1].
> Breadth ratio must be the reciprocal: $7 \to 10$[cite: 1].
> Required Breadth increase $= \frac{10 - 7}{7} = \frac{3}{7}$[cite: 1].
> In percentage:
> $$\frac{3}{7} \times 100 = \frac{300}{7}\% = 42\frac{6}{7}\%$$[cite: 1]
> **Correct Option: A**[cite: 1]

> [!question]
> **CDS 1 2023: Rectangle Length and Width**
> If the length of a rectangle is increased by $66\frac{2}{3}\%$, then by what percent should the width be decreased to maintain the same area?[cite: 1]
> - (a) $50\%$
> - (b) $45\%$
> - (c) $40\%$
> - (d) $35\%$[cite: 1]
> 
> *Solution:*
> $$66\frac{2}{3}\% = \frac{200}{3}\% = \frac{2}{3}$$[cite: 1]
> Length increases from $3$ to $3 + 2 = 5$[cite: 1].
> Length ratio $= 3 : 5 \implies$ Width ratio $= 5 : 3$[cite: 1].
> Width reduction $= \frac{5 - 3}{5} = \frac{2}{5}$[cite: 1].
> $$\% \text{ reduction} = \frac{2}{5} \times 100 = 40\%$$[cite: 1]
> **Correct Option: (c)**[cite: 1]

> [!question]
> **Homework Problem (AFCAT 1 2025)**
> If length of a rectangle is increased by $60\%$, then by what percentage breadth be decreased to maintain no change in area?[cite: 1]
> - (a) $\frac{300}{8}\%$
> - (b) $60\%$
> - (c) $30\%$
> - (d) None[cite: 1]
> 
> *Solution:*
> Increase $= +60\% = +\frac{3}{5} \implies \text{Length ratio} = 5 \to 8$.
> Breadth ratio must be $8 \to 5$.
> Breadth reduction $= \frac{8 - 5}{8} = \frac{3}{8}$.
> $$\% \text{ reduction} = \frac{3}{8} \times 100 = \frac{300}{8}\% = 37.5\%$$[cite: 1]
> **Correct Option: (a)**[cite: 1]

> [!question]
> **CDS 2 2024: Data Sufficiency on Petrol Expenditure**
> **Question**: If the price of petrol goes up by $20\%$, by what percentage should the consumption be reduced so that the expenditure remains the same?[cite: 1]
> - Statement-I: Price of petrol per litre was Rs. $90$[cite: 1].
> - Statement-II: Consumption was $24\text{ litres}$ before price hike[cite: 1].
> 
> *Options:*
> - (a) Can be answered by using one statement alone[cite: 1].
> - (b) Can be answered by using either statement alone[cite: 1].
> - (c) Can be answered by using both statements together[cite: 1].
> - (d) The Question can be answered even without using any of the Statements[cite: 1].
> 
> *Solution:*
> Percentage reduction in consumption depends solely on the percentage change of price:
> $$\Delta P = +20\% = +\frac{1}{5} \implies \text{Price ratio} = 5 : 6 \implies \text{Consumption ratio} = 6 : 5$$[cite: 1]
> Reduction $= \frac{1}{6} \times 100 = 16\frac{2}{3}\%$[cite: 1].
> No absolute values from Statement-I or Statement-II are required[cite: 1].
> **Correct Option: (d)**[cite: 1]
