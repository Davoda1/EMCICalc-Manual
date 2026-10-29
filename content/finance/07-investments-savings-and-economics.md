## Net present value (explicit time zero)

Discount cash flows with an explicit initial investment at time zero.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Initial cash flow at time zero | Numeric expression | Blank — enter a value if applicable | Negative = outlay; positive = receipt. |
| Subsequent flow timing | Selection | end | Options: `end`, `beginning`. End: subsequent flows at 1,2,...; beginning: at 0,1,...; initial flow always at zero. |
| Evenly spaced subsequent cash flows | Input table | Blank — enter a value if applicable | Negative outlays, positive receipts. One row per equal period. |
| Discount rate per cash-flow period (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Evenly spaced subsequent cash flows — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Cash flow | number |  |

**Assumptions and boundaries**

- Initial cash flow is at time zero. Rates are fractions; 0.05 means 5%.
- Rate is per equal cash-flow period.
- Negative = outlay; positive = receipt.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| frequency | 1 |
| Initial cash flow at time zero | -1000 |
| maximum_rate | 100 |
| minimum_rate | -0.9999 |
| Discount rate per cash-flow period (fraction) | 0.10 |
| search_steps | 384 |
| Subsequent flow timing | end |

**Example: Evenly spaced subsequent cash flows**

| Cash flow |
| --- |
| 400 |
| 400 |
| 400 |

**Expression example:** `npv0(0.1,[-1000,400,400,400])`

## Internal rate of return (IRR)

Find and report converged rates, including multiple and tangent roots found by a bounded search.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Initial cash flow at time zero | Numeric expression | Blank — enter a value if applicable | Negative = outlay; positive = receipt. |
| Subsequent flow timing | Selection | end | Options: `end`, `beginning`. End: subsequent flows at 1,2,...; beginning: at 0,1,...; initial flow always at zero. |
| Evenly spaced subsequent cash flows | Input table | Blank — enter a value if applicable | Negative outlays, positive receipts. One row per equal period. |
| Minimum search rate (fraction) | Numeric expression | -0.9999 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Maximum search rate (fraction) | Numeric expression | 100 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Search subdivisions | Whole-number expression | 384 | 64 to 4096; repeated roots are searched using stationary points. |
| Cash-flow periods per year | Whole-number expression | 1 | Used only to show the equivalent annual rate. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Evenly spaced subsequent cash flows — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Cash flow | number |  |

**Assumptions and boundaries**

- Initial cash flow is at time zero. Rates are fractions; 0.05 means 5%.
- Rate is per equal cash-flow period.
- A finite numerical search cannot establish uniqueness.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Cash-flow periods per year | 1 |
| Initial cash flow at time zero | -1000 |
| Maximum search rate (fraction) | 100 |
| Minimum search rate (fraction) | -0.9999 |
| rate | 0.10 |
| Search subdivisions | 384 |
| Subsequent flow timing | end |

**Example: Evenly spaced subsequent cash flows**

| Cash flow |
| --- |
| 400 |
| 400 |
| 400 |

**Expression example:** `irr([-1000,400,400,400])`

## Dated net present value (XNPV)

Discount cash flows with an explicit initial investment at time zero.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Initial cash flow at time zero | Numeric expression | Blank — enter a value if applicable | Negative = outlay; positive = receipt. |
| Time-zero date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Date basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Dated subsequent cash flows | Input table | Blank — enter a value if applicable | Ordered dates on or after time zero; duplicate dates are combined for IRR. |
| Annual effective discount rate (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated subsequent cash flows — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Cash flow | number |  |

**Assumptions and boundaries**

- Initial cash flow is at time zero. Rates are fractions; 0.05 means 5%.
- Annual effective rate using the selected date basis.
- Negative = outlay; positive = receipt.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Date basis | actual/365 |
| frequency | 1 |
| Initial cash flow at time zero | -1000 |
| maximum_rate | 100 |
| minimum_rate | -0.9999 |
| Annual effective discount rate (fraction) | 0.10 |
| search_steps | 384 |
| timing | end |
| Time-zero date | 2026-01-01 |

**Example: Dated subsequent cash flows**

| Date | Cash flow |
| --- | --- |
| 2027-01-01 | 400 |
| 2028-01-01 | 400 |
| 2029-01-01 | 400 |

**Expression example:** `xnpv(0.1,[-1000,400,400,400],[datejd(2026,1,1),datejd(2027,1,1),datejd(2028,1,1),datejd(2029,1,1)])`

## Dated internal rate of return (XIRR)

Find and report converged rates, including multiple and tangent roots found by a bounded search.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Initial cash flow at time zero | Numeric expression | Blank — enter a value if applicable | Negative = outlay; positive = receipt. |
| Time-zero date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Date basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Dated subsequent cash flows | Input table | Blank — enter a value if applicable | Ordered dates on or after time zero; duplicate dates are combined for IRR. |
| Minimum search rate (fraction) | Numeric expression | -0.9999 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Maximum search rate (fraction) | Numeric expression | 100 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Search subdivisions | Whole-number expression | 384 | 64 to 4096; repeated roots are searched using stationary points. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated subsequent cash flows — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Cash flow | number |  |

**Assumptions and boundaries**

- Initial cash flow is at time zero. Rates are fractions; 0.05 means 5%.
- Annual effective rate using the selected date basis.
- A finite numerical search cannot establish uniqueness.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Date basis | actual/365 |
| frequency | 1 |
| Initial cash flow at time zero | -1000 |
| Maximum search rate (fraction) | 100 |
| Minimum search rate (fraction) | -0.9999 |
| rate | 0.10 |
| Search subdivisions | 384 |
| timing | end |
| Time-zero date | 2026-01-01 |

**Example: Dated subsequent cash flows**

| Date | Cash flow |
| --- | --- |
| 2027-01-01 | 400 |
| 2028-01-01 | 400 |
| 2029-01-01 | 400 |

**Expression example:** `xirr([-1000,400,400,400],[datejd(2026,1,1),datejd(2027,1,1),datejd(2028,1,1),datejd(2029,1,1)])`

## Savings-goal planner

Project a balance, solve a recurring contribution, or simulate time to a goal with changing contributions and dated withdrawals.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Calculate | Selection | future-balance | Options: `future-balance`, `contribution`, `time`. |
| Initial balance | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Assumed return (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Return convention | Selection | effective-annual | Options: `effective-annual`, `nominal-annual`, `periodic`. |
| Nominal compounding periods/year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Contributions per year | Whole-number expression | 12 | Supported: 1, 2, 3, 4, 6, 12, 26, 52 or 365. |
| Contribution timing | Selection | end | Options: `end`, `beginning`. |
| Start date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Periods / simulation horizon | Whole-number expression | 120 | 1 to 12000. Time-to-goal checks period-end balances. |
| Base recurring contribution | Numeric expression | Blank — enter a value if applicable | When solving contribution, changes still replace this base on their entered dates. |
| Target balance | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Growth accrual | Selection | periodic | Options: `periodic`, `dated`. Periodic growth uses the exact fraction of each calendar contribution interval between withdrawals; dated growth uses the selected date basis and annual effective return. |
| Date basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Contribution amount changes | Input table | Blank — enter a value if applicable | Strictly ordered dates; new amount replaces the base at the next contribution on or after that date. |
| Dated withdrawals | Input table | Blank — enter a value if applicable | Strictly ordered dates within the horizon. Combine same-day withdrawals. |
| Fixed fee per period | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fee on period-end balance (fraction) | Numeric expression | 0 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Modeled tax on positive growth (fraction) | Numeric expression | 0 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Modeled taxable growth | Selection | positive-growth | Options: `positive-growth`, `positive-growth-less-fees`. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Contribution amount changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New recurring amount | number |  |

**Dated withdrawals — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Withdrawal | number |  |

**Assumptions and boundaries**

- No national tax assumptions. Positive growth taxed each period; no tax credits for losses.
- Fixed and percentage fees apply at period end; percentage fee uses the balance after contributions and withdrawals.
- Beginning/end contributions and dated withdrawals split growth accrual. Negative balances are unsupported.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Base recurring contribution | 100 |
| Contributions per year | 12 |
| Initial balance | 1000 |
| Periods / simulation horizon | 120 |
| Assumed return (fraction) | 0.05 |
| Start date | 2026-01-01 |
| Target balance | 20000 |

## Compound annual growth rate

Annualized growth between two values.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Starting value | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Ending value | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Elapsed years | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- Start > 0; end ≥ 0; years > 0. Result is a fractional annual rate.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Ending value | 121 |
| Starting value | 100 |
| Elapsed years | 2 |

**Expression example:** `cagr(100,121,2)`

## Real return after inflation

Exact purchasing-power return, using matching periods.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Nominal return (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Inflation (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- (1 + nominal return) / (1 + inflation) − 1. Rates use the same period.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Inflation (fraction) | 0.03 |
| Nominal return (fraction) | 0.08 |

**Expression example:** `realreturn(0.08,0.03)`

## Inflation and purchasing power

Project an amount needed to preserve purchasing power, or express a destination-period amount in starting-period purchasing power.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Amount | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Price-level source | Selection | constant-rate | Options: `constant-rate`, `index-series`. |
| Conversion direction | Selection | preserve-purchasing-power | Options: `preserve-purchasing-power`, `express-in-start-period`. |
| Inflation per period (fraction) | Numeric expression | Blank — enter a value if applicable | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Number of periods | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Starting index date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Destination index date | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Price-index series | Input table | Blank — enter a value if applicable | Positive indices, ordered dates. Exact entries for both dates required; no hidden interpolation. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Price-index series — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Date | date |  |
| Index | number |  |

**Assumptions and boundaries**

- Constant rates compound over the specified number of matching periods.
- Index factor = destination index / starting index; multiply to preserve purchasing power, divide to express a destination amount in starting-period money.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Amount | 1000 |
| Inflation per period (fraction) | 0.03 |
| Number of periods | 5 |

**Expression example:** `inflationadjust(1000,0.03,5)`

## Currency conversion after fees

Calculate net proceeds and compare conversion offers at equal total source outlay.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Source amount / common offer budget | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Source currency | Text | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Destination currency | Text | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Exchange rate | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Rate direction | Selection | destination-per-source | Options: `destination-per-source`, `source-per-destination`. |
| Spread / conversion fee (fraction) | Numeric expression | 0 | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Fixed source-currency fee | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Source fee treatment | Selection | deducted | Options: `deducted`, `additional`. In offer comparisons the entered amount is always the same total budget, including this fee. |
| Fixed destination-currency fee | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Rate source | Text | user-entered | User-entered or the existing cached currency source. |
| Available rate timestamp | Text | not supplied | Preserved with the result; use the source's actual timestamp. |
| Optional offers for the same total source outlay | Input table | Blank — enter a value if applicable | All offers spend the same total source amount, including source fees. Empty table calculates the single offer above. |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Optional offers for the same total source outlay — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Offer name | text |  |
| Exchange rate | number |  |
| Rate direction | choice | Options: destination-per-source, source-per-destination.  |
| Spread (fraction) | number | Enter 0.05 for 5%; expressions such as 5% are also accepted. |
| Source fee | number |  |
| Destination fee | number |  |
| Rate source | text |  |
| Timestamp | text |  |

**Assumptions and boundaries**

- Normalize rate to destination currency per source currency.
- Source fee → convert principal → percentage fee on converted value → destination fee.
- Effective all-in rate = net destination receipt / total source outlay. Offer comparisons use equal source outlay.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Source amount / common offer budget | 1000 |
| Destination currency | HUF |
| Fixed destination-currency fee | 100 |
| Exchange rate | 400 |
| Rate source | user-entered |
| Source currency | EUR |
| Fixed source-currency fee | 2 |
| Spread / conversion fee (fraction) | 0.01 |

**Expression example:** `fxnet(1000,400,0.01,2,100)`

---

[User manual](../) · [Finance reference](./) · [Previous: Pricing & business](06-pricing-and-business.md) · [Next: Callable expression helpers](08-callable-expression-helpers.md)
