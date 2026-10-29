**Rates are fractions.** `0.20` and `20%` both mean twenty percent. Plain `20` means twenty, equivalent to 2000%. A percentage label always states its interpretation. An expression such as `R0/100` can convert a register containing a whole percentage to a fraction.

**Money and quantities.** Use consistent currency units within a worksheet, except for the FX worksheet, which labels source and destination amounts separately. Quantities and unit costs must correspond. Monetary decimal places are an explicit override: use the precision appropriate to your currency, rather than assuming every currency has two decimals. Supported precision is zero through eight decimal places.

**Rate convention.** Effective annual is a one-year compound return. Nominal annual is an annual quoted rate divided into the explicitly selected compounding frequency. Periodic is the rate per repayment/contribution period. Equivalent periodic rates are obtained by compounding mathematics, not by indiscriminately dividing every annual rate by twelve. Beginning and end timing are separate selections.

**Dated accrual.** `actual/365` uses actual elapsed days divided by 365; `actual/360` uses actual days divided by 360; `actual/actual` splits the interval across calendar years and uses 365 or 366 for each year; `30/360` is explicitly European 30E/360, with month-end days capped at 30. The supported basis is shown by each dated tool. Ordinary periodic models and dated models are distinct.

**Rounding.** Display mode preserves internal calculation precision and rounds presented money only. Transaction mode rounds each booked monetary movement or schedule period at the selected precision, half away from zero. Tables may show an explicit display-rounding adjustment so independently rounded figures reconcile. Discrete gross-up and allocation choose monetary units deliberately; final payment/remainder adjustments are visible.

**Assumptions and status.** Taxes, deductibility, fees, repayment rules and accounting conventions are supplied by you. These are generic calculation worksheets. A modeled interest cost is not represented as a jurisdiction-compliant APR/THM. Results distinguish invalid input, unsupported models, non-convergence, non-unique solutions, insufficient funds and simulation horizons. A horizon limit does not prove a goal or repayment is impossible.

---

[User manual](../) · [Finance reference](./) · [Previous: Using the worksheets](01-using-the-worksheets.md) · [Next: Finding the right worksheet](03-finding-the-right-worksheet.md)
