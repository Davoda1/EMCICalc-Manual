## Loan summary

Solve payment or duration and inspect reconciled loan cash flows, dated rate changes and the full repayment schedule.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Loan amount | Numeric expression | Blank — enter a value if applicable | Advance before deducted fees. |
| Interest rate | Numeric expression | Blank — enter a value if applicable | Fractional rate: 0.05 or 5%, not 5. |
| Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Nominal compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Calculate from | Selection | term | Options: `term`, `payment`. term: required payment; payment: payoff duration. |
| Contractual term (payments) | Whole-number expression | 60 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Specified regular payment | Numeric expression | 0 | Used for payment solving; excludes recurring fees. |
| Simulation horizon (payments) | Whole-number expression | 1200 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payment timing | Selection | end | Options: `end`, `beginning`. |
| Loan start date | ISO date | 2026-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Interest accrual | Selection | periodic | Options: `periodic`, `simple_dated`, `compound_dated`. Dated models split every rate change and extra payment at its exact date. |
| Dated day-count basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Fees paid separately upfront | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees deducted from advance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees added to loan balance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fee per scheduled payment | Numeric expression | 0 | Paid separately from loan instalment. |
| Initial interest-only payments | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Final balloon | Numeric expression | 0 | Included in the final scheduled payment. |
| Adjust final contractual payment | Yes / No | Yes | Enabled: clear the remaining debt at term end. Disabled: show residual debt. |
| On interest-rate change | Selection | keep_payment | Options: `keep_payment`, `recalculate`. |
| Dated interest-rate changes | Input table | Blank — enter a value if applicable | Changes on payment dates apply after that payment. |
| Query balance after payment (0 disables) | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Query balance at date (blank disables) | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated interest-rate changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New rate | number |  |

**Assumptions and boundaries**

- All rates are fractions, e.g. 0.05 or 5%. Fees paid separately, deducted and financed have distinct cash-flow treatment.
- Simple dated: nominal quote × day fraction; effective/periodic quotes first annualize. Compound dated: exact equivalent annual growth raised to the day fraction.
- Dated changes apply from their date; a change on a payment date follows that payment. Periodic mode accepts only payment-date events.
- Beginning timing starts at the loan start date. A contractual balloon forms part of the last payment. A final adjustment pays any remaining balance.
- No national APR/THM or legal minimum-payment rule is assumed.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Interest accrual | periodic |
| Adjust final contractual payment | Yes |
| Loan amount | 10000 |
| Query balance after payment (0 disables) | 12 |
| Query balance at date (blank disables) | 2027-01-01 |
| Final balloon | 500 |
| Nominal compounding per year | 12 |
| Dated day-count basis | actual/365 |
| Fees deducted from advance | 25 |
| Fees added to loan balance | 100 |
| Payments per year | 12 |
| Simulation horizon (payments) | 1200 |
| Initial interest-only payments | 0 |
| Specified regular payment | 0 |
| Monetary decimal places (explicit override) | 2 |
| Interest rate | 0.06 |
| On interest-rate change | keep_payment |
| Rate convention | nominal |
| Fee per scheduled payment | 2 |
| Monetary rounding | transaction |
| Calculate from | term |
| Loan start date | 2026-01-01 |
| Contractual term (payments) | 24 |
| Payment timing | end |
| Fees paid separately upfront | 50 |

## Repayment schedule

Solve payment or duration and inspect reconciled loan cash flows, dated rate changes and the full repayment schedule.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Loan amount | Numeric expression | Blank — enter a value if applicable | Advance before deducted fees. |
| Interest rate | Numeric expression | Blank — enter a value if applicable | Fractional rate: 0.05 or 5%, not 5. |
| Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Nominal compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Calculate from | Selection | term | Options: `term`, `payment`. term: required payment; payment: payoff duration. |
| Contractual term (payments) | Whole-number expression | 60 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Specified regular payment | Numeric expression | 0 | Used for payment solving; excludes recurring fees. |
| Simulation horizon (payments) | Whole-number expression | 1200 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payment timing | Selection | end | Options: `end`, `beginning`. |
| Loan start date | ISO date | 2026-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Interest accrual | Selection | periodic | Options: `periodic`, `simple_dated`, `compound_dated`. Dated models split every rate change and extra payment at its exact date. |
| Dated day-count basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Fees paid separately upfront | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees deducted from advance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees added to loan balance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fee per scheduled payment | Numeric expression | 0 | Paid separately from loan instalment. |
| Initial interest-only payments | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Final balloon | Numeric expression | 0 | Included in the final scheduled payment. |
| Adjust final contractual payment | Yes / No | Yes | Enabled: clear the remaining debt at term end. Disabled: show residual debt. |
| On interest-rate change | Selection | keep_payment | Options: `keep_payment`, `recalculate`. |
| Dated interest-rate changes | Input table | Blank — enter a value if applicable | Changes on payment dates apply after that payment. |
| Query balance after payment (0 disables) | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Query balance at date (blank disables) | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated interest-rate changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New rate | number |  |

**Assumptions and boundaries**

- All rates are fractions, e.g. 0.05 or 5%. Fees paid separately, deducted and financed have distinct cash-flow treatment.
- Simple dated: nominal quote × day fraction; effective/periodic quotes first annualize. Compound dated: exact equivalent annual growth raised to the day fraction.
- Dated changes apply from their date; a change on a payment date follows that payment. Periodic mode accepts only payment-date events.
- Beginning timing starts at the loan start date. A contractual balloon forms part of the last payment. A final adjustment pays any remaining balance.
- No national APR/THM or legal minimum-payment rule is assumed.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Interest accrual | periodic |
| Adjust final contractual payment | Yes |
| Loan amount | 10000 |
| Query balance after payment (0 disables) | 12 |
| Query balance at date (blank disables) | 2027-01-01 |
| Final balloon | 500 |
| Nominal compounding per year | 12 |
| Dated day-count basis | actual/365 |
| Fees deducted from advance | 25 |
| Fees added to loan balance | 100 |
| Payments per year | 12 |
| Simulation horizon (payments) | 1200 |
| Initial interest-only payments | 0 |
| Specified regular payment | 0 |
| Monetary decimal places (explicit override) | 2 |
| Interest rate | 0.06 |
| On interest-rate change | keep_payment |
| Rate convention | nominal |
| Fee per scheduled payment | 2 |
| Monetary rounding | transaction |
| Calculate from | term |
| Loan start date | 2026-01-01 |
| Contractual term (payments) | 24 |
| Payment timing | end |
| Fees paid separately upfront | 50 |

## Overpayment comparison

Compare recurring and dated extra payments, including recasting or a shorter term and early-repayment charges.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Loan amount | Numeric expression | Blank — enter a value if applicable | Advance before deducted fees. |
| Interest rate | Numeric expression | Blank — enter a value if applicable | Fractional rate: 0.05 or 5%, not 5. |
| Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Nominal compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Calculate from | Selection | term | Options: `term`, `payment`. term: required payment; payment: payoff duration. |
| Contractual term (payments) | Whole-number expression | 60 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Specified regular payment | Numeric expression | 0 | Used for payment solving; excludes recurring fees. |
| Simulation horizon (payments) | Whole-number expression | 1200 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payment timing | Selection | end | Options: `end`, `beginning`. |
| Loan start date | ISO date | 2026-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Interest accrual | Selection | periodic | Options: `periodic`, `simple_dated`, `compound_dated`. Dated models split every rate change and extra payment at its exact date. |
| Dated day-count basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Fees paid separately upfront | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees deducted from advance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fees added to loan balance | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fee per scheduled payment | Numeric expression | 0 | Paid separately from loan instalment. |
| Initial interest-only payments | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Final balloon | Numeric expression | 0 | Included in the final scheduled payment. |
| Adjust final contractual payment | Yes / No | Yes | Enabled: clear the remaining debt at term end. Disabled: show residual debt. |
| On interest-rate change | Selection | keep_payment | Options: `keep_payment`, `recalculate`. |
| Dated interest-rate changes | Input table | Blank — enter a value if applicable | Changes on payment dates apply after that payment. |
| Query balance after payment (0 disables) | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Query balance at date (blank disables) | ISO date | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Recurring extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Dated one-off extra payments | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Overpayment effect | Selection | reduce_term | Options: `reduce_term`, `recast`. |
| Charge per extra-payment event | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Charge as fraction of extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Dated interest-rate changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New rate | number |  |

**Dated one-off extra payments — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Payment date | date |  |
| Extra amount | number |  |

**Assumptions and boundaries**

- All rates are fractions, e.g. 0.05 or 5%. Fees paid separately, deducted and financed have distinct cash-flow treatment.
- Simple dated: nominal quote × day fraction; effective/periodic quotes first annualize. Compound dated: exact equivalent annual growth raised to the day fraction.
- Dated changes apply from their date; a change on a payment date follows that payment. Periodic mode accepts only payment-date events.
- Beginning timing starts at the loan start date. A contractual balloon forms part of the last payment. A final adjustment pays any remaining balance.
- No national APR/THM or legal minimum-payment rule is assumed.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Interest accrual | simple_dated |
| Adjust final contractual payment | Yes |
| Loan amount | 10000 |
| Query balance after payment (0 disables) | 12 |
| Query balance at date (blank disables) | 2027-01-01 |
| Final balloon | 500 |
| Nominal compounding per year | 12 |
| Dated day-count basis | actual/365 |
| Fees deducted from advance | 25 |
| Charge per extra-payment event | 1 |
| Charge as fraction of extra payment | 0.01 |
| Recurring extra payment | 50 |
| Overpayment effect | reduce_term |
| Fees added to loan balance | 100 |
| Payments per year | 12 |
| Simulation horizon (payments) | 1200 |
| Initial interest-only payments | 0 |
| Specified regular payment | 0 |
| Monetary decimal places (explicit override) | 2 |
| Interest rate | 0.06 |
| On interest-rate change | keep_payment |
| Rate convention | nominal |
| Fee per scheduled payment | 2 |
| Monetary rounding | transaction |
| Calculate from | term |
| Loan start date | 2026-01-01 |
| Contractual term (payments) | 24 |
| Payment timing | end |
| Fees paid separately upfront | 50 |

**Example: Dated interest-rate changes**

| Effective date | New rate |
| --- | --- |
| 2027-02-15 | 0.065 |

**Example: Dated one-off extra payments**

| Payment date | Extra amount |
| --- | --- |
| 2026-06-15 | 500 |

## Credit minimum-payment comparison

Simulate minimum only, fixed payment and minimum plus extra using explicit percentage rules.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Initial credit balance | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Interest rate | Numeric expression | Blank — enter a value if applicable | Fraction: 0.24 or 24%. |
| Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Start date | ISO date | 2026-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Minimum-payment rule | Selection | balance_percent | Options: `balance_percent`, `principal_plus_costs`, `fixed`. |
| Percentage calculation balance | Selection | after_interest_fees | Options: `before_interest_fees`, `after_interest_fees`. |
| Minimum-payment fraction | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fixed minimum floor | Numeric expression | 25 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fixed scenario payment | Numeric expression | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Recurring extra above minimum | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Fee added each period | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Maximum simulated payments | Whole-number expression | 1200 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Assumptions and boundaries**

- End-of-period payments; no new spending. Interest and fees are added to the balance before payment.
- principal_plus_costs means percentage × selected balance + current interest + fees, subject to the fixed floor.
- A fixed-payment rule uses fixed_payment. All final payments are capped at the amount due.
- A constant non-decreasing balance recurrence is identified as proven non-repaying; otherwise an unfinished simulation is only a horizon limit.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Initial credit balance | 3000 |
| Percentage calculation balance | after_interest_fees |
| Compounding per year | 12 |
| Recurring extra above minimum | 50 |
| Fixed minimum floor | 25 |
| Fixed scenario payment | 150 |
| Payments per year | 12 |
| Maximum simulated payments | 1200 |
| Minimum-payment fraction | 0.03 |
| Minimum-payment rule | balance_percent |
| Monetary decimal places (explicit override) | 2 |
| Interest rate | 0.24 |
| Rate convention | nominal |
| Fee added each period | 1 |
| Monetary rounding | transaction |
| Start date | 2026-01-01 |

## Refinancing comparison

Compare existing and replacement loans including fees, optional extras, common-date debt and lasting break-even.

| Input | Format | Initial setting | Meaning / choices |
| --- | --- | --- | --- |
| Existing — Loan amount | Numeric expression | Blank — enter a value if applicable | Advance before deducted fees. |
| Existing — Interest rate | Numeric expression | Blank — enter a value if applicable | Fractional rate: 0.05 or 5%, not 5. |
| Existing — Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Existing — Nominal compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Existing — Contractual term (payments) | Whole-number expression | 60 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Payment timing | Selection | end | Options: `end`, `beginning`. |
| Existing — Loan start date | ISO date | 2026-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Interest accrual | Selection | periodic | Options: `periodic`, `simple_dated`, `compound_dated`. Dated models split every rate change and extra payment at its exact date. |
| Existing — Dated day-count basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Existing — Fee per scheduled payment | Numeric expression | 0 | Paid separately from loan instalment. |
| Existing — Initial interest-only payments | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Final balloon | Numeric expression | 0 | Included in the final scheduled payment. |
| Existing — Adjust final contractual payment | Yes / No | Yes | Enabled: clear the remaining debt at term end. Disabled: show residual debt. |
| Existing — On interest-rate change | Selection | keep_payment | Options: `keep_payment`, `recalculate`. |
| Existing — Dated interest-rate changes | Input table | Blank — enter a value if applicable | Changes on payment dates apply after that payment. |
| Existing — Recurring extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Dated one-off extra payments | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Overpayment effect | Selection | reduce_term | Options: `reduce_term`, `recast`. |
| Existing — Charge per extra-payment event | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing — Charge as fraction of extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Interest rate | Numeric expression | Blank — enter a value if applicable | Fractional rate: 0.05 or 5%, not 5. |
| Replacement — Rate convention | Selection | nominal | Options: `nominal`, `effective`, `periodic`. |
| Replacement — Nominal compounding per year | Whole-number expression | 12 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Payments per year | Whole-number expression | 12 | 1, 2, 4, 12, 26, 52 or 365. |
| Replacement — Contractual term (payments) | Whole-number expression | 60 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Payment timing | Selection | end | Options: `end`, `beginning`. |
| Replacement — Interest accrual | Selection | periodic | Options: `periodic`, `simple_dated`, `compound_dated`. Dated models split every rate change and extra payment at its exact date. |
| Replacement — Dated day-count basis | Selection | actual/365 | Options: `actual/365`, `actual/360`, `actual/actual`, `30/360`. 30/360 means European 30E/360; actual/actual splits calendar years. |
| Replacement — Fee per scheduled payment | Numeric expression | 0 | Paid separately from loan instalment. |
| Replacement — Initial interest-only payments | Whole-number expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Final balloon | Numeric expression | 0 | Included in the final scheduled payment. |
| Replacement — Adjust final contractual payment | Yes / No | Yes | Enabled: clear the remaining debt at term end. Disabled: show residual debt. |
| Replacement — On interest-rate change | Selection | keep_payment | Options: `keep_payment`, `recalculate`. |
| Replacement — Dated interest-rate changes | Input table | Blank — enter a value if applicable | Changes on payment dates apply after that payment. |
| Replacement — Recurring extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Dated one-off extra payments | Input table | Blank — enter a value if applicable | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Overpayment effect | Selection | reduce_term | Options: `reduce_term`, `recast`. |
| Replacement — Charge per extra-payment event | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Replacement — Charge as fraction of extra payment | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Existing-loan exit charge | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Exit-charge payment | Selection | immediate | Options: `immediate`, `financed`. |
| Arrangement fee paid immediately | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Other fees paid immediately | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Arrangement fee financed | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Other fees financed | Numeric expression | 0 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Common comparison date | ISO date | 2028-01-01 | Use this worksheet's model and the [units and rate conventions](02-units-rates-dates-and-rounding.md). |
| Monetary decimal places (explicit override) | Whole-number expression | 2 | Choose the required currency precision, including zero, three or four decimal places where applicable. |
| Monetary rounding | Selection | display | Options: `display`, `transaction`. display keeps internal precision and rounds presentation only; transaction rounds each booked monetary amount, half away from zero. |

**Existing — Dated interest-rate changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New rate | number |  |

**Existing — Dated one-off extra payments — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Payment date | date |  |
| Extra amount | number |  |

**Replacement — Dated interest-rate changes — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Effective date | date |  |
| New rate | number |  |

**Replacement — Dated one-off extra payments — table columns**

| Column | Format | Meaning / choices |
| --- | --- | --- |
| Payment date | date |  |
| Extra amount | number |  |

**Assumptions and boundaries**

- All rates are fractions, e.g. 0.05 or 5%. Fees paid separately, deducted and financed have distinct cash-flow treatment.
- Simple dated: nominal quote × day fraction; effective/periodic quotes first annualize. Compound dated: exact equivalent annual growth raised to the day fraction.
- Dated changes apply from their date; a change on a payment date follows that payment. Periodic mode accepts only payment-date events.
- Beginning timing starts at the loan start date. A contractual balloon forms part of the last payment. A final adjustment pays any remaining balance.
- No national APR/THM or legal minimum-payment rule is assumed.
- Existing amount is outstanding debt at the common start; historical fees are sunk and excluded.
- Replacement principal pays off existing debt. Financed charges add to the replacement balance; immediate charges are cash outlay.
- Break-even compares cumulative cash paid plus remaining debt every calendar day across both schedules, with no discounting.

**Load example**

Select Load example to fill these values; fields not listed below retain their documented initial settings.

| Example input | Value |
| --- | --- |
| Arrangement fee financed | 0 |
| Arrangement fee paid immediately | 150 |
| Common comparison date | 2028-01-01 |
| Existing-loan exit charge | 100 |
| Exit-charge payment | immediate |
| Replacement — Interest accrual | periodic |
| Replacement — Adjust final contractual payment | Yes |
| Replacement — Final balloon | 0 |
| Replacement — Nominal compounding per year | 12 |
| Replacement — Dated day-count basis | actual/365 |
| Replacement — Charge per extra-payment event | 0 |
| Replacement — Charge as fraction of extra payment | 0 |
| Replacement — Recurring extra payment | 0 |
| Replacement — Overpayment effect | reduce_term |
| Replacement — Payments per year | 12 |
| Replacement — Initial interest-only payments | 0 |
| Replacement — Interest rate | 0.05 |
| Replacement — On interest-rate change | keep_payment |
| Replacement — Rate convention | nominal |
| Replacement — Fee per scheduled payment | 0 |
| Replacement — Contractual term (payments) | 48 |
| Replacement — Payment timing | end |
| Existing — Interest accrual | periodic |
| Existing — Adjust final contractual payment | Yes |
| Existing — Loan amount | 10000 |
| Existing — Final balloon | 0 |
| Existing — Nominal compounding per year | 12 |
| Existing — Dated day-count basis | actual/365 |
| Existing — Charge per extra-payment event | 0 |
| Existing — Charge as fraction of extra payment | 0 |
| Existing — Recurring extra payment | 0 |
| Existing — Overpayment effect | reduce_term |
| Existing — Payments per year | 12 |
| Existing — Initial interest-only payments | 0 |
| Existing — Interest rate | 0.08 |
| Existing — On interest-rate change | keep_payment |
| Existing — Rate convention | nominal |
| Existing — Fee per scheduled payment | 0 |
| Existing — Loan start date | 2026-01-01 |
| Existing — Contractual term (payments) | 36 |
| Existing — Payment timing | end |
| Other fees financed | 0 |
| Other fees paid immediately | 0 |
| Monetary decimal places (explicit override) | 2 |
| Monetary rounding | transaction |

---

[User manual](../) · [Finance reference](./) · [Previous: Finding the right worksheet](03-finding-the-right-worksheet.md) · [Next: Tax, VAT & invoices](05-tax-vat-and-invoices.md)
