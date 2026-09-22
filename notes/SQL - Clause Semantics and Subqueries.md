> [!definition]
> The core SQL query block executes in a strictly defined logical lifecycle[cite: 2]:
> 1. `FROM` (Evaluates cross-products / joins)[cite: 2]
> 2. `WHERE` (Tuple-level filter using selection predicate $\sigma$)[cite: 2]
> 3. `GROUP BY` (Partitions qualifying tuples into aggregated groups)[cite: 2]
> 4. `HAVING` (Group-level filter using aggregate conditions)[cite: 2]
> 5. `SELECT` (Projects requested attributes $\pi$)[cite: 2]
> 6. `DISTINCT` (Eliminates duplicate projections)[cite: 2]
> 7. `ORDER BY` (Sorts final result set)[cite: 2]

> [!theorem]
> **Subquery Comparison Equivalences:**
> * `X IN (Subquery)` $\equiv$ `X = ANY (Subquery)`[cite: 2]
> * `X NOT IN (Subquery)` $\equiv$ `X <> ALL (Subquery)`[cite: 2]
> * `EXISTS (Subquery)` evaluates to `TRUE` if the subquery returns at least one record; can replace conditional joins[cite: 2].

> [!trap]
> **`GROUP BY` Projection Rule & `HAVING` Constraints:**
> * If a query uses `GROUP BY`, the `SELECT` clause can only contain attributes that appear in the `GROUP BY` clause or expressions with aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)[cite: 2]. Selecting un-grouped attributes results in a syntax error[cite: 2].
> * `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after grouping[cite: 2]. `HAVING` cannot reference unaggregated non-grouping attributes[cite: 2].

> [!question]
> **PSU CBT Practice Drill:**
> Consider the schema `book(title, price)` with distinct book prices[cite: 1]. What does the following SQL query evaluate to[cite: 1]?
> ```sql
> SELECT title
> FROM book AS B
> WHERE (SELECT COUNT(*)
>        FROM book AS T
>        WHERE T.price > B.price) < 5;
> ```
> (A) Titles of the four most expensive books[cite: 1]
> (B) Title of the fifth most expensive book[cite: 1]
> (C) Titles of the five most expensive books[cite: 1]
> (D) Titles of the five least expensive books[cite: 1]
>
> **Step-by-Step Resolution:**
> 1. The inner correlated query counts how many books $T$ have a price strictly greater than the outer book $B$ (`T.price > B.price`)[cite: 1, 2].
> 2. For the most expensive book: $0$ books are more expensive ($0 < 5 \implies \text{True}$)[cite: 1].
> 3. For the 2nd most expensive book: $1$ book is more expensive ($1 < 5 \implies \text{True}$)[cite: 1].
> 4. For the 3rd, 4th, and 5th most expensive books: counts are $2, 3, 4$ respectively (all $< 5 \implies \text{True}$)[cite: 1].
> 5. For the 6th most expensive book: $5$ books are more expensive ($5 < 5 \implies \text{False}$)[cite: 1].
> 6. Hence, exactly the $5$ most expensive books satisfy the condition[cite: 1].
>
> **Correct Answer:** (C) Titles of the five most expensive books[cite: 1]
