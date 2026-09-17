---
title: Enumerations & Struct Bit-Fields
tags:
  - clang
  - c-language
  - data-structures
  - study
---

# Enumerations & Struct Bit-Fields

Enumeration constants and struct bit-fields rely directly on Integer Constant Expressions (ICE) in C grammar.

---

## Enumerations (`enum`)

Enumeration constants are defined by C grammar to be Integer Constant Expressions:

```c
enum Status { 
    OK = 1, 
    ERROR = 1 << 2, 
    TIMEOUT = ERROR + 10 
};
```

---

## Struct Bit-Fields

Struct bit-fields require an ICE to specify the exact bit allocation width:

```c
struct Packet { 
    unsigned int flag : 1; 
    unsigned int priority : 3; 
};
```

---

## Related Notes
- [[Integer Constant Expressions (ICE)]]
- [[Switch Statement & Duff's Device]]
