In general `i1`, `i2` should be subtracted by the `li1`, `li2` of the element whose address is given. (`i1 - li1`).

| **Array Type** | **Size Notation**                                   | **Offset Formula**                                                | **Address Formula**                                                                                                               |
| -------------- | --------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **1D Array**   | $A[i_1]$                                            | $\text{Offset} = i_1$                                             | $\text{Address} = \text{Base} + i_1 \cdot \text{sizeof}(\text{element})$                                                          |
| **2D Array**   | $A[i_1][i_2]$<br> $(N_1 \times N_2)$                | $\text{Offset} = i_1 \cdot N_2 + i_2$                             | $\text{Address} = \text{Base} + (i_1 \cdot N_2 + i_2) \cdot \text{sizeof}(\text{element})$                                        |
| **3D Array**   | $A[i_1][i_2][i_3]$<br>$(N_1 \times N_2 \times N_3)$ | $\text{Offset} = i_1 \cdot (N_2 \cdot N_3) + i_2 \cdot N_3 + i_3$ | $\text{Address} = \text{Base} + \left( i_1 \cdot N_2 \cdot N_3 + i_2 \cdot N_3 + i_3 \right) \cdot \text{sizeof}(\text{element})$ |
|                |                                                     |                                                                   |                                                                                                                                   |

## Concrete Example (3D Array)

Given an array declared as `int arr[2][3][4]`:
* Dimension sizes: $N_1 = 2, N_2 = 3, N_3 = 4$
* $\text{Base Address} = 1000$
* $\text{sizeof}(\text{int}) = 4 \text{ bytes}$

### Target Element: `arr[1][2][1]`

1. **Calculate Linear Offset:**
   $$\text{Offset} = (1 \cdot 3 \cdot 4) + (2 \cdot 4) + 1 = 12 + 8 + 1 = 21$$

2. **Calculate Final Address:**
   $$\text{Address} = 1000 + (21 \cdot 4) = 1000 + 84 = 1084$$