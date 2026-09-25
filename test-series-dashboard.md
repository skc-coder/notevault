---
cssclasses:
  - dashboard
  - cols-2
tags:
  - test-series
  - gateoverflow
  - goclasses
  - dashboard
---

# 🚀 Test Series Dashboard

Separate tracking for **GO Test Series (129)**, **GO Test Series DA (88)**, and **GATE Overflow 2027 (29)**.

---

## 🏛️ GO Test Series (129 Tests)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration,
  "[Online Test](" + url + ")" AS "Take Test"
FROM "tests/go test series"
SORT file.name ASC
```

---

## 📊 GO Test Series DA (88 Tests)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration,
  "[Online Test](" + url + ")" AS "Take Test"
FROM "tests/go test series da"
SORT file.name ASC
```

---

## ⚡ GATE Overflow 2027 (29 Tests)

```dataview
TABLE 
  choice(done, "✅", "❌") AS Done,
  file.link AS "Test Note",
  subject AS Subject,
  questions AS Questions,
  marks AS Marks,
  duration AS Duration,
  "[Online Test](" + url + ")" AS "Take Test"
FROM "tests/gate overflow 2027"
SORT file.name ASC
```
