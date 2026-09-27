> [!question] Comprehensive Structure Alignment Case Studies
> Assume standard 64-bit architecture data widths: `char` = 1B, `short` = 2B, `int` = 4B, `long` / `double` = 8B[cite: 1].

### Case 1: `struct a`
```c
struct a {
    int i;   /* 4B: offset 0..3 */
    char c;  /* 1B: offset 4 */
};           /* Padding: 3B at offset 5..7 (max member is int = 4B) */
/* Total Size = 8 Bytes */
```

### Case 2: `struct b`
```c
struct b {
    long l;  /* 8B: offset 0..7 */
    char c;  /* 1B: offset 8 */
};           /* Padding: 7B at offset 9..15 (max member is long = 8B) */
/* Total Size = 16 Bytes */
```

### Case 3: `struct c`
```c
struct c {
    int i;   /* 4B: offset 0..3 */
             /* 4B padding at offset 4..7 to align next 8B long */
    long l;  /* 8B: offset 8..15 */
    char c;  /* 1B: offset 16 */
};           /* Padding: 7B at offset 17..23 (max member is long = 8B) */
/* Total Size = 24 Bytes */
```

### Case 4: `struct d` (Reordered Optimization)
```c
struct d {
    long l;  /* 8B: offset 0..7 */
    int i;   /* 4B: offset 8..11 */
    char c;  /* 1B: offset 12 */
};           /* Padding: 3B at offset 13..15 (total must divide by 8) */
/* Total Size = 16 Bytes (reordering saved 8 bytes!) */
```

### Case 5: `struct e`
```c
struct e {
    double d; /* 8B: offset 0..7 */
    int i;    /* 4B: offset 8..11 */
    char c;   /* 1B: offset 12 */
};            /* Padding: 3B at offset 13..15 (divisible by 8) */
/* Total Size = 16 Bytes */
```

### Case 6: `struct f`
```c
struct f {
    int i;    /* 4B: offset 0..3 */
              /* 4B padding at offset 4..7 to align 8B double */
    double d; /* 8B: offset 8..15 */
    char c;   /* 1B: offset 16 */
};            /* Padding: 7B at offset 17..23 (divisible by 8) */
/* Total Size = 24 Bytes */
```

### Case 7: `struct g`
```c
struct g {
    short s;  /* 2B: offset 0..1 */
    char c;   /* 1B: offset 2 */
              /* 1B padding at offset 3 to align 4B int */
    int a;    /* 4B: offset 4..7 */
    long l;   /* 8B: offset 8..15 */
};            /* Total Size = 16 Bytes (divisible by max member 8B) */
```

### Case 8: `struct h`
```c
struct h {
    short s;  /* 2B: offset 0..1 */
              /* 2B padding at offset 2..3 to align 4B int */
    int a;    /* 4B: offset 4..7 */
    char c;   /* 1B: offset 8 */
              /* 7B padding at offset 9..15 to align 8B long */
    long l;   /* 8B: offset 16..23 */
};            /* Total Size = 24 Bytes */
```

### Case 9: `struct j` (Array Members)
```c
struct j {
    short a[5]; /* 5 * 2B = 10B: offset 0..9 */
                /* 6B padding at offset 10..15 to align 8B long */
    long b;     /* 8B: offset 16..23 */
};              /* Total Size = 24 Bytes */
```
