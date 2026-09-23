> [!definition]
> The core SQL query block executes in a strictly defined logical lifecycle[cite: 2]:
> 1. `FROM` (Evaluates cross-products / joins)[cite: 2]
> 2. `WHERE` (Tuple-level filter using selection predicate $\sigma$)[cite: 2]
> 3. `GROUP BY` (Partitions qualifying tuples into aggregated groups)[cite: 2]
> 4. `HAVING` (Group-level filter using aggregate conditions)[cite: 2]
> 5. `SELECT` (Projects requested attributes $\pi$)[cite: 2]
> 6. `DISTINCT` (Eliminates duplicate projections)[cite: 2]
> 7. `ORDER BY` (Sorts final result set)[cite: 2]

Filthy Women Get Horny, Stripping Down Online

| **Letter** | **Pedagogy: Plain-English Meaning & Definition Link**                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| **F**      | **Where is the data?** Loads tables and resolves joins to build the raw candidate data.                      |
| **W**      | **Which rows qualify?** Filters individual rows (_tuples_) _before_ any summary math happens.                |
| **G**      | **How to bucket them?** Collapses qualifying rows into partitioned summary groups.                           |
| **H**      | **Which buckets qualify?** Filters the summarized buckets using aggregate conditions (`COUNT`, `SUM`, etc.). |
| **S**      | **What columns to keep?** Projects and calculates the requested columns/expressions.                         |
| **D**      | **Any duplicates?** De-duplicates identical output rows.                                                     |
| **O**      | **How to present them?** Sorts the final result set for viewing.                                             |


> [!theorem]
> **Subquery Comparison Equivalences:**
> * `X IN (Subquery)` $\equiv$ `X = ANY (Subquery)`[cite: 2]
> * `X NOT IN (Subquery)` $\equiv$ `X <> ALL (Subquery)`[cite: 2]
> * `EXISTS (Subquery)` evaluates to `TRUE` if the subquery returns at least one record; can replace conditional joins[cite: 2].

> [!trap]
> **`GROUP BY` Projection Rule & `HAVING` Constraints:**
> * If a query uses `GROUP BY`, the `SELECT` clause can only contain attributes that appear in the `GROUP BY` clause or expressions with aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)[cite: 2]. Selecting un-grouped attributes results in a syntax error[cite: 2].
> * `WHERE` filters rows before grouping; `HAVING` filters aggregated groups after grouping[cite: 2]. `HAVING` cannot reference unaggregated non-grouping attributes[cite: 2].

### The Professional "Box Packing" Mental Model

Think of packaging items into sealed delivery boxes in a warehouse:

- **[WHERE](https://www.google.com/search?q=https://en.wikipedia.org/wiki/Where_\(SQL\)&utm_source=gemini&authuser=2)**: Inspects **individual items** on the conveyor belt before packing.
    
    - _Example:_ "Is this item broken?" If yes, discard it before boxing.
        
- **[GROUP BY](https://en.wikipedia.org/wiki/Group_by_\(SQL\)?utm_source=gemini)**: Packs individual items into **sealed category boxes**.
    
    - _Example:_ Pack all items by `department` into separate, sealed boxes.
        
- **[HAVING](https://en.wikipedia.org/wiki/Having_\(SQL\)?utm_source=gemini)** & **[SELECT](https://en.wikipedia.org/wiki/Select_\(SQL\)?utm_source=gemini)**: Can only inspect the **box label** or **measure the whole box**.
    
    - The individual items are sealed inside and cannot be seen one-by-one.
        
    - You can only check the label (`department`) or calculate [aggregate functions](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini) across the box contents, such as [COUNT](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [SUM](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [AVG](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [MAX](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), or [MIN](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini).
        

### The 5-Second Safe Cheat Code

- **[WHERE](https://www.google.com/search?q=https://en.wikipedia.org/wiki/Where_\(SQL\)&utm_source=gemini&authuser=2):** Filters individual rows _before_ grouping happens.
    
- **[GROUP BY](https://en.wikipedia.org/wiki/Group_by_\(SQL\)?utm_source=gemini):** Collapses rows into categorized groups.
    
- **[HAVING](https://en.wikipedia.org/wiki/Having_\(SQL\)?utm_source=gemini) & [SELECT](https://en.wikipedia.org/wiki/Select_\(SQL\)?utm_source=gemini):** Must reference the group key or an [aggregate function](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini) ([COUNT](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [SUM](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [AVG](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [MAX](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini), [MIN](https://en.wikipedia.org/wiki/Aggregate_function?utm_source=gemini)). Selecting un-grouped, individual attributes results in a syntax error.
- 
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
