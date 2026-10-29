## Add tax

Calculate net, tax and gross using a user-supplied fractional rate.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Net amount | Numeric expression | Blank — enter a value if applicable | Negative values represent credits or reversals. |
| Tax rate (fraction) | Numeric expression | Blank — enter a value if applicable | 0.20 = 20%; rates are not country-specific. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Fractional rates; user-defined tax rules.
- Display-only or transaction rounding at the selected currency precision.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Net amount | 100 |
| Tax rate (fraction) | 0.20 |

**Expression example:** `taxadd(100,0.20)`

## Remove included tax

Calculate net, tax and gross using a user-supplied fractional rate.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Gross amount | Numeric expression | Blank — enter a value if applicable | Negative values represent credits or reversals. |
| Tax rate (fraction) | Numeric expression | Blank — enter a value if applicable | 0.20 = 20%; rates are not country-specific. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Fractional rates; user-defined tax rules.
- Display-only or transaction rounding at the selected currency precision.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Gross amount | 120 |
| Tax rate (fraction) | 0.20 |

**Expression example:** `taxremove(120,0.20)`

## Extract included tax

Calculate net, tax and gross using a user-supplied fractional rate.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Gross amount | Numeric expression | Blank — enter a value if applicable | Negative values represent credits or reversals. |
| Tax rate (fraction) | Numeric expression | Blank — enter a value if applicable | 0.20 = 20%; rates are not country-specific. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Fractional rates; user-defined tax rules.
- Display-only or transaction rounding at the selected currency precision.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Gross amount | 120 |
| Tax rate (fraction) | 0.20 |

**Expression example:** `taxpart(120,0.20)`

## Progressive tax

Apply marginal rates to ordered tax brackets, with separate deductions and credits.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Income / taxable base before deductions | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Tax-base deduction | Numeric expression | 0 | Reduces taxable base; does not represent an additional cash deduction. |
| Tax credit | Numeric expression | 0 | Subtracted from tax after applying brackets. |
| Refundable credit | Yes / No | No | If enabled, excess credit may produce negative tax. |
| Tax brackets | Input table | Blank — enter a value if applicable | Lower thresholds, ascending from 0. The final bracket is unlimited. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Tax brackets — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Lower threshold | number | First threshold is 0; subsequent thresholds strictly increase. |
| Marginal rate (fraction) | number | 0.20 means 20%; the final bracket has no upper limit. |

**Assumptions and boundaries**

- Effective tax rate uses income before deductions as denominator.
- At an exact bracket boundary, the next bracket's rate is marginal.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Tax credit | 500 |
| Tax-base deduction | 2000 |
| Income / taxable base before deductions | 40000 |
| Refundable credit | No |

**Example: Tax brackets**

| Lower threshold | Marginal rate (fraction) |
| --- | --- |
| 0 | 0.10 |
| 10000 | 0.20 |
| 30000 | 0.30 |

**Expression example:** `brackettax(40000,[0,0.10;10000,0.20;30000,0.30],2000,500,0)`

## Net-to-gross solver

Find the smallest gross monetary amount that reaches the requested net, including tax, contributions and fees.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Requested net | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Tax model | Selection | flat | Options: `flat`, `progressive`. |
| Flat tax rate (fraction) | Numeric expression | Blank — enter a value if applicable | Used only for the flat model. |
| Progressive tax brackets | Input table | Blank — enter a value if applicable | Used only for the progressive model; starts at 0. |
| Tax-base allowance | Numeric expression | 0 | Reduces the tax base only. |
| Tax credit | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Refundable credit | Yes / No | No | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Contributions / gross (fraction) | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Other deductions / gross (fraction) | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fixed cash deduction / fees | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Progressive tax brackets — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Lower threshold | number | First threshold is 0; subsequent thresholds strictly increase. |
| Marginal rate (fraction) | number | 0.20 means 20%; the final bracket has no upper limit. |

**Assumptions and boundaries**

- All deduction rates apply to gross, except tax applied after its allowance.
- Every bracket's combined marginal deduction rate must remain below 100%.
- Returns the smallest nonnegative gross minor unit achieving at least the target.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Contributions / gross (fraction) | 0.05 |
| Fixed cash deduction / fees | 20 |
| Monetary decimal places (explicit override) | 2 |
| Flat tax rate (fraction) | 0.20 |
| Monetary rounding | transaction |
| Requested net | 1000 |
| Tax model | flat |

**Example: Progressive tax brackets**

| Lower threshold | Marginal rate (fraction) |
| --- | --- |
| 0 | 0.10 |
| 10000 | 0.20 |
| 30000 | 0.30 |

**Expression example:** `grossup(1000,0.20)`

## Invoice calculation

Calculate mixed-rate invoices with explicit discount ordering and reconciled rounding.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Invoice lines | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Invoice discount type | Selection | percentage | Options: `percentage`, `fixed`. |
| Invoice discount | Numeric expression | 0 | Percentage is a fraction. Fixed invoice discount is a net amount allocated across lines. |
| Discount ordering | Selection | line_then_invoice | Options: `line_then_invoice`, `invoice_then_line`. |
| Rounding scope | Selection | line | Options: `line`, `invoice`. Invoice scope rounds total net and each tax-rate subtotal; remainders follow input order. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Invoice lines — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Description | text |  |
| Quantity | number |  |
| Unit price | number |  |
| Price interpretation | choice | Options: net, inclusive.  |
| Line discount type | choice | Options: percentage, fixed.  |
| Line discount | number | Percentage is a fraction; a fixed amount follows the price's net/inclusive interpretation. |
| Tax rate (fraction) | number |  |

**Assumptions and boundaries**

- Nonnegative quantities and prices; fixed discounts cannot exceed available value.
- Fixed line discounts follow price interpretation; fixed invoice discounts are net.
- Largest-remainder allocation, with original line order breaking ties.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Discount ordering | line_then_invoice |
| Invoice discount | 23 |
| Invoice discount type | fixed |
| Rounding scope | invoice |
| Monetary rounding | transaction |

**Example: Invoice lines**

| Description | Quantity | Unit price | Price interpretation | Line discount type | Line discount | Tax rate (fraction) |
| --- | --- | --- | --- | --- | --- | --- |
| Product A | 2 | 100 | net | percentage | 0.10 | 0.20 |
| Product B | 1 | 55 | inclusive | fixed | 0 | 0.10 |

## VAT settlement worksheet

Combine output VAT, explicitly deductible input VAT and signed adjustments.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| VAT entries | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Explicit adjustments | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**VAT entries — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Description | text |  |
| Kind | choice | Options: output, input.  |
| Amount interpretation | choice | Options: net, vat.  |
| Net base / VAT amount | number | Net base multiplied by the rate, or VAT directly when interpretation is vat. |
| VAT rate / rate group (fraction) | number |  |
| Deductible input fraction | number | Input VAT only: 1 = fully deductible; 0.5 = half; 0 = none. |

**Explicit adjustments — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Description | text |  |
| Signed adjustment | number | Positive increases payable VAT; negative reduces it. |

**Assumptions and boundaries**

- Deductibility is entirely user-specified; descriptions have no legal effect.
- A positive balance is payable; a negative balance is recoverable.
- Generic worksheet, not an automatically compliant national tax return.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

**Example: VAT entries**

| Description | Kind | Amount interpretation | Net base / VAT amount | VAT rate / rate group (fraction) | Deductible input fraction |
| --- | --- | --- | --- | --- | --- |
| Sales | output | net | 1000 | 0.20 | 1 |
| Partially deductible expense | input | net | 500 | 0.20 | 0.50 |

**Example: Explicit adjustments**

| Description | Signed adjustment |
| --- | --- |
| User adjustment | -10 |

---

[User manual](../) · [Finance reference](./) · [Previous: Loans and borrowing](04-loans-and-borrowing.md) · [Next: Pricing & business](06-pricing-and-business.md)
