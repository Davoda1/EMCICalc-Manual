Arguments are positional. Square brackets in a signature mark optional arguments; vector values use actual square brackets. Matrices use commas between columns and semicolons between rows. All rates below are fractions, and all money values use consistent units. Existing engine functions keep their existing definitions. `npv0` is the explicit time-zero wrapper.

Numeric examples are ordinary DEC-mode calculations and can contain registers: assign `R0 := 100`, then `taxadd(R0,20%)` gives `120`. Assignments use the usual explicit evaluation behavior.

## taxadd

`taxadd(net,rate)`

net is the amount before tax; rate is the non-negative fractional tax rate. Returns gross = net × (1 + rate). Negative money values can represent credits.

**Example:** `taxadd(100,0.20) = 120`

## taxremove

`taxremove(gross,rate)`

gross includes tax; rate is the non-negative fractional tax rate. Returns net = gross / (1 + rate).

**Example:** `taxremove(120,0.20) = 100`

## taxpart

`taxpart(gross,rate)`

gross includes tax; rate is the non-negative fractional tax rate. Returns the tax contained in gross.

**Example:** `taxpart(120,0.20) = 20`

## markup

`markup(cost,price)`

cost and price are positive money amounts per unit. Returns profit divided by cost as a fraction.

**Example:** `markup(80,100) = 0.25`

## margin

`margin(cost,price)`

cost and price are positive money amounts per unit. Returns profit divided by selling price as a fraction.

**Example:** `margin(80,100) = 0.20`

## pricefrommarkup

`pricefrommarkup(cost,rate)`

cost is positive unit cost; rate is target markup relative to cost, greater than -1. Returns selling price.

**Example:** `pricefrommarkup(80,0.25) = 100`

## pricefrommargin

`pricefrommargin(cost,rate)`

cost is positive unit cost; rate is target margin relative to selling price and must be below 1. Returns selling price.

**Example:** `pricefrommargin(80,0.20) = 100`

## breakeven

`breakeven(fixed,price,variable)`

fixed is non-negative fixed cost; price and variable are selling price and variable cost per unit. Price must exceed non-negative variable cost. Returns divisible-unit quantity; use ceil(...) for a whole-unit requirement.

**Example:** `breakeven(1000,25,15) = 100`

## targetsales

`targetsales(fixed,price,variable,profit)`

fixed, price and variable have the break-even meanings; profit is non-negative target profit in the same currency. Returns divisible-unit quantity.

**Example:** `targetsales(1000,25,15,500) = 150`

## prorate

`prorate(amount,part,total)`

amount is a money amount, optionally negative for a credit; part is the non-negative used quantity; total is the positive full quantity in the same units. Returns amount × part / total.

**Example:** `prorate(1200,3,12) = 300`

## runway

`runway(cash,positive_burn)`

cash is non-negative available cash; positive_burn is positive net cash consumption per matching period. Returns periods of runway. Zero or negative burn has no finite quotient; use the worksheet for its no-exhaustion result.

**Example:** `runway(12000,1500) = 8`

## cagr

`cagr(start,end,years)`

start is positive starting value; end is non-negative ending value; years is positive elapsed years, including fractional years. Returns an annual fractional growth rate.

**Example:** `cagr(100,121,2) = 0.10`

## realreturn

`realreturn(nominal,inflation)`

nominal and inflation are fractional returns for the same period. Nominal must be at least -1 and inflation greater than -1. Returns (1 + nominal) / (1 + inflation) − 1.

**Example:** `realreturn(0.20,0.10) = 1/11`

## inflationadjust

`inflationadjust(amount,rate,periods)`

amount is starting-period money; rate is inflation per period, greater than -1; periods is non-negative and uses that same period. Returns the destination amount needed to preserve purchasing power. Use the worksheet for the reverse direction or an index series.

**Example:** `inflationadjust(100,0.10,2) = 121`

## fxnet

`fxnet(amount,destination_per_source,spread,source_fee,destination_fee)`

amount is the total source-currency budget; destination_per_source is a positive exchange rate; spread is a fraction from 0 to 1; source_fee is deducted from the budget before conversion; destination_fee is deducted after conversion and percentage fee. Fees are non-negative and cannot exceed available amounts. Returns net destination currency.

**Example:** `fxnet(1000,400,0.01,2,100) = 395108`

## loanpayment

`loanpayment(principal,periodic_rate,periods[,beginning=0])`

principal is non-negative financed balance; periodic_rate is rate per payment period, greater than -1; periods is positive number of payments. beginning is optional: 0 means period end (default), 1 means period beginning. Returns a positive regular payment, with a zero-interest branch. Loan worksheets add fees, changes and balloons.

**Example:** `loanpayment(1200,0,12) = 100`

## brackettax

`brackettax(income,threshold_rate_matrix[,deduction=0,credit=0,refundable=0])`

income is non-negative gross taxable income. threshold_rate_matrix has two columns: lower bracket threshold and marginal fractional rate. Start at threshold 0, increase strictly and use rates from 0 to 1. deduction reduces taxable income; credit reduces computed tax; refundable is 0/1. Optional defaults are zero.

**Example:** `brackettax(150,[0,0.10;100,0.20]) = 20`

## grossup

`grossup(target,rate[,precision=2,contribution=0,fixed=0,allowance=0,credit=0,other_rate=0,refundable=0])`

target is required net money; rate is flat fractional tax. precision is monetary decimal places (default 2); contribution is contribution fraction; fixed is fixed deduction; allowance reduces taxable income; credit reduces tax; other_rate is an additional fractional deduction; refundable is 0/1. Optional deductions/credits default to zero. Returns the smallest gross monetary unit achieving at least target under transaction rounding.

**Example:** `grossup(80,0.20) = 100`

## grossupbrackets

`grossupbrackets(target,threshold_rate_matrix[,precision=2,contribution=0,fixed=0,allowance=0,credit=0,other_rate=0,refundable=0])`

target and optional arguments have the grossup meanings. threshold_rate_matrix supplies progressive marginal brackets as in brackettax, replacing the flat rate. Returns the smallest gross monetary unit achieving at least target.

**Example:** `grossupbrackets(80,[0,0.20]) = 100`

## npv

`npv(rate,flows): first flow at period 1`

rate is discount rate per equal cash-flow period, greater than -1; flows is a nonempty vector of signed money cash flows. The first flow is at period 1. An investment at time zero must be added separately or supplied to npv0.

**Example:** `npv(0.10,[110]) = 100`

## npv0

`npv0(rate,flows): first flow at period 0`

rate is discount rate per equal cash-flow period, greater than -1; flows is a nonempty vector. Its first value is at time zero, followed by periods 1, 2, and so on. Negative flows are outlays; positive flows are receipts.

**Example:** `npv0(0.10,[-100,110]) = 0`

## irr

`irr(flows[,minimum=-0.9999,maximum=100]): first flow at 0`

flows is a signed vector with its first value at time zero and later values in equal periods. Both cash-flow signs are required. minimum and maximum are fractional search bounds, default -0.9999 and 100, with -1 < minimum < maximum. Returns a fractional per-period rate only when one converged result is available; multiple roots or unsuccessful searches produce an error directing you to the worksheet. A returned rate is not proof of uniqueness.

**Example:** `irr([-100,110]) ≈ 0.10`

## datejd

`datejd(year,month,day)`

year is 1–9999, month 1–12, and day must form a valid calendar date. Returns an exact Julian-day integer for dated helper vectors. This avoids ambiguous regional date strings.

**Example:** `datejd(2026,1,1) = 2461042`

## xnpv

`xnpv(rate,flows,julian_dates[,basis=0])`

rate is annual effective discount rate, greater than -1. flows and julian_dates are equal-length vectors with an initial and at least one subsequent entry. The first date is the valuation date; dates must be ordered and no earlier than it. basis defaults to 0: 0 actual/365, 1 actual/360, 2 actual/actual, 3 European 30E/360.

**Example:** `xnpv(0.10,[-100,110],[datejd(2023,1,1),datejd(2024,1,1)]) ≈ 0`

## xirr

`xirr(flows,julian_dates[,basis=0,minimum=-0.9999,maximum=100])`

flows and julian_dates have the xnpv meanings, with both signs required. basis uses the same 0–3 codes, default 0; minimum and maximum default to -0.9999 and 100. Returns an annual effective fractional rate only when one converged result is available. The worksheet exposes roots, residuals and search limits.

**Example:** `xirr([-100,110],[datejd(2023,1,1),datejd(2024,1,1)]) ≈ 0.10`

## allocate

`allocate(amount,weights[,precision=2])`

amount is the positive or negative money amount to split and must be exactly representable at the selected precision; weights is a nonempty vector of non-negative weights with positive total; precision is monetary decimal places, default 2. Returns a vector of allocated money amounts using largest remainders, with input order breaking ties, so the displayed amounts sum to the original total. Increase precision if the original amount is not representable.

**Example:** `allocate(100,[1,1,1]) = [33.34,33.33,33.33]`

---

[User manual](../) · [Finance reference](./) · [Previous: Investments, savings and economics](07-investments-savings-and-economics.md) · [Next: Interpreting schedules and numerical searches](09-interpreting-schedules-and-numerical-searches.md)
