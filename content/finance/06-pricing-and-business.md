## Markup, margin & selling price

Compare profit relative to cost (markup) and relative to selling price (margin).

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Cost per unit | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Known input | Selection | selling_price | Options: `selling_price`, `target_markup`, `target_margin`. |
| Selling price (known-input mode) | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Target markup or margin | Numeric expression | Blank — enter a value if applicable | Enter a fractional rate: 0.20 means 20%; expressions such as 20% are accepted. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Cost and selling price must be positive. Target margin must be less than 100%.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Cost per unit | 80 |
| Known input | selling_price |
| Selling price (known-input mode) | 100 |

**Expression example:** `markup(80,100)`

## Break-even & target profit

Find divisible and whole-unit sales requirements from positive contribution per unit.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Fixed costs | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Selling price per unit | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Variable cost per unit | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Target profit (0 for break-even) | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Fixed costs, variable cost and target profit are nonnegative; contribution must be positive.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Fixed costs | 1000 |
| Target profit (0 for break-even) | 500 |
| Selling price per unit | 25 |
| Variable cost per unit | 15 |

**Expression example:** `targetsales(1000,25,15,500)`

## Depreciation schedule

Straight-line, declining-balance or sum-of-years'-digits with a residual-value floor.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Acquisition cost | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Residual value | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Useful life (whole service years) | Whole-number expression | 5 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Method | Selection | straight_line | Options: `straight_line`, `declining_balance`, `sum_of_years`. |
| In-service date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Partial-period convention | Selection | calendar_actual_days | Options: `anniversary`, `calendar_actual_days`. Calendar mode splits each annual service-year charge by actual days; both table endpoints are inclusive. |
| Declining-balance input | Selection | factor | Options: `factor`, `rate`. |
| Declining factor (rate = factor ÷ life) | Numeric expression | 2 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Explicit declining annual rate | Numeric expression | Blank — enter a value if applicable | Enter a fractional rate: 0.20 means 20%; expressions such as 20% are accepted. |
| Catch up to residual in final period | Yes / No | Yes | For declining balance only; disabled allows the final book value to exceed residual. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Service-year charges use acquisition anniversaries. Calendar allocation respects leap years. This is generic mathematics, not tax-law depreciation.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Acquisition cost | 10000 |
| Useful life (whole service years) | 5 |
| Method | straight_line |
| Partial-period convention | calendar_actual_days |
| Residual value | 1000 |
| In-service date | 2026-07-01 |

## Proration

Allocate an amount by an explicit quantity ratio or an included calendar-day ratio.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Original amount | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Basis | Selection | dates | Options: `quantity`, `dates`. |
| Portion quantity (quantity basis) | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Full quantity (quantity basis) | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Full interval start | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Full interval end | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Include full start date | Yes / No | Yes | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Include full end date | Yes / No | Yes | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Portion interval start | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Portion interval end | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Include portion start date | Yes / No | Yes | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Include portion end date | Yes / No | Yes | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Negative amounts are allowed. Quantity ratios may exceed one; date portions must lie within the full included interval.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Original amount | 310 |
| Basis | dates |
| Full interval end | 2026-01-31 |
| Full interval start | 2026-01-01 |
| Portion interval end | 2026-01-31 |
| Portion interval start | 2026-01-17 |

**Expression example:** `prorate(310,15,31)`

## Monetary allocation

Distribute positive amounts or credits exactly at the chosen monetary precision using largest remainders.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Amount to allocate | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Weight interpretation | Selection | weights | Options: `weights`, `percentages`. |
| Recipients | Input table | Blank — enter a value if applicable | Nonnegative weights; percentages must add to 100. Ties use input order. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Recipients — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Name | text |  |
| Weight or percentage | number |  |

**Assumptions and boundaries**

- Original amount must be exactly representable at selected monetary precision. Allocated amounts always sum to that original amount; credits mirror positive allocations.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Amount to allocate | 100 |
| Weight interpretation | weights |

**Example: Recipients**

| Name | Weight or percentage |
| --- | --- |
| A | 1 |
| B | 1 |
| C | 1 |

## Cash-flow forecast

Project dated and recurring inflows/outflows, grouped balances, the lowest cash balance and first shortfall.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Starting cash | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Forecast start (inclusive) | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Forecast end (inclusive) | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Group periods | Selection | monthly | Options: `daily`, `weekly`, `monthly`, `quarterly`, `yearly`. |
| Dated transactions | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Recurring transactions | Input table | Blank — enter a value if applicable | Each occurrence is anchored to the original date; January 31 monthly becomes February 28 and March 31. Ends are inclusive; only forecast dates are used. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated transactions — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Description | text |  |
| Direction | choice | Options: inflow, outflow.  |
| Amount | number |  |

**Recurring transactions — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| First date | date |  |
| Last permitted date | date |  |
| Frequency | choice | Options: daily, weekly, monthly, quarterly, yearly.  |
| Description | text |  |
| Direction | choice | Options: inflow, outflow.  |
| Amount | number |  |

**Assumptions and boundaries**

- All same-day flows are netted before testing cash shortfall. Weekly buckets are anchored to forecast start; other multi-day groups follow calendar periods. Display rounding is explicitly separated from actual cash movements.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Forecast end (inclusive) | 2026-03-31 |
| Group periods | monthly |
| Forecast start (inclusive) | 2026-01-01 |
| Starting cash | 1000 |

**Example: Dated transactions**

| Date | Description | Direction | Amount |
| --- | --- | --- | --- |
| 2026-02-15 | Receipt | inflow | 500 |

**Example: Recurring transactions**

| First date | Last permitted date | Frequency | Description | Direction | Amount |
| --- | --- | --- | --- | --- | --- |
| 2026-01-31 | 2026-03-31 | monthly | Monthly cost | outflow | 600 |

## Constant-burn runway

Divide starting cash by net cash burn per user-defined period without inventing exhaustion when burn is zero or negative.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Starting cash | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Net burn per period | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- A period may be a month, week or another consistently chosen interval. This simple helper does not predict a calendar date.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Net burn per period | 1500 |
| Starting cash | 10000 |

**Expression example:** `runway(10000,1500)`

## Inventory-cost worksheet

Compare FIFO, moving weighted average and periodic weighted average with dated negative-stock validation.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Costing method | Selection | fifo | Options: `fifo`, `moving_average`, `periodic_average`. |
| Opening-stock date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Opening quantity | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Opening unit cost | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Dated receipts | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Dated issues / sales | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated receipts — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Description | text |  |
| Quantity | number |  |
| Unit cost | number |  |

**Dated issues / sales — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Description | text |  |
| Quantity | number |  |

**Assumptions and boundaries**

- Same-date receipts precede issues; ties within each type preserve input order. No negative stock is supported, even if later period receipts would cover an earlier shortage. Opening inventory is one cost layer. Periodic average uses all entered receipts; interim valuations are omitted because it is an end-period method.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Costing method | fifo |
| Opening quantity | 10 |
| Opening unit cost | 5 |
| Opening-stock date | 2026-01-01 |

**Example: Dated receipts**

| Date | Description | Quantity | Unit cost |
| --- | --- | --- | --- |
| 2026-01-05 | — | 10 | 7 |

**Example: Dated issues / sales**

| Date | Description | Quantity |
| --- | --- | --- |
| 2026-01-10 | — | 12 |

---

[User manual](../) · [Finance reference](./) · [Previous: Tax, VAT & invoices](05-tax-vat-and-invoices.md) · [Next: Investments, savings and economics](07-investments-savings-and-economics.md)
