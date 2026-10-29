## Algebra / Calculus and Steps

Open **Algebra / Calculus** for guided equations, systems, derivatives, integrals, limits, sums, products and expression transformations. Select an operation first, then complete its labelled expression, variable and bound fields. Argument help explains function order if you choose to insert an equivalent function into Calculate.

A useful first equation is `x^2=4`, solved for x. For differentiation, use expression `x^3` and variable x; the derivative is `3*x^2`. For a definite integral, specify `x^2`, variable x, and bounds 0 and 1 to obtain `1/3`. These are different input forms; do not place bounds in an unrelated text field.

**Transform selection** acts on selected structured input; **Ctrl+Shift+T** opens it. Check the selected part before applying a transformation.

**Steps** explains supported families of exact arithmetic, algebra, calculus and small rational-matrix operations. Expand a step to read its rule, explanation and conditions. More actions offers copying, expanding/collapsing all, and PDF or PNG export. Use PDF for a derivation too tall for the PNG limit.

A valid result does not guarantee an available derivation. Steps is bounded rather than a universal proof engine. It covers, among other cases, rational arithmetic, specified polynomial and elementary calculus forms, rational RREF up to 6 × 6, and determinant/inverse explanations for rational 2 × 2 matrices. Read exclusions and domain conditions instead of treating a simplified expression as proof that an excluded input became valid.

## Matrix and vectors

Open **Matrix**, set the dimensions and fill the expression cells. For a first determinant, enter a 2 × 2 A grid with rows `1, 2` and `3, 4`, choose determinant and calculate; the answer is −2. For a binary operation, fill B as well and check its dimensions.

Entry supports 1–32 rows and columns. Multiplication requires A's column count to match B's row count; addition and subtraction require equal dimensions. Determinant and inverse require a square matrix, and a singular matrix has no inverse. Clear affected nonempty cells before reducing dimensions so values are not silently discarded.

Use named storage and CSV to retain matrices. Inspecting or inserting a workbench result is separate from confirming a calculation. Numerical LU supports up to 32 × 32, eigen analysis up to 8 × 8, minors/cofactors up to 8 × 8 and characteristic polynomials up to 6 × 6. Numerical decompositions have finite precision and convergence limits; they are not arbitrary-precision proofs of near-singular behaviour.

## Data / Statistics

Open **Data / Statistics**, enter X values, and supply paired Y values when the selected analysis needs them. A blank frequency means one observation; an integer frequency repeats that observation. Start with X values `1`, `2`, `3` and `4`: the mean is 2.5 and the median is 2.5.

Choose sample or population conventions deliberately. Sample variance divides by N−1 and needs at least two observations; population variance divides by N. Quantiles use interpolated type-7 positions in the frequency-expanded data. Zero-frequency rows stay in the grid but do not contribute to calculations.

Fits include linear, quadratic, cubic, polynomial degree 1–8, exponential, logarithmic and power models. Exponential needs positive Y; logarithmic needs positive X; power needs both positive. Check fit status and residuals before interpreting predictions. Scatter and residual plots belong to this workbench.

The data grid accepts up to 10,000 rows, with total frequency up to 10,000,000. Cells must resolve to finite dimensionless real values. This analysis uses a bounded double-precision kernel: increasing general calculator digits does not make statistics arbitrary precision. Rescale extreme data if the tool reports a magnitude or rank limit.

## Finance

Open **Finance** from **Data & tools**, or use **Toolbox → Statistics → Finance worksheets**. Choose a category and worksheet, complete its fields, then select **Calculate**. **Load example** deliberately fills the selected worksheet with a supplied example; startup does not populate a financial scenario for you.

The 29 worksheets cover loans and schedules, overpayments, refinancing, tax and invoices, pricing, depreciation, allocation, cash flow, inventory, savings, NPV/IRR and dated variants, growth, inflation and currency fees. Numeric fields accept expressions, including register references. Dates use `YYYY-MM-DD`.

Rates are fractions: **`0.05` and `5%` mean five percent; `5` means five hundred percent.** Check whether the selected rate is nominal annual, effective annual or periodic, and select beginning/end payment timing explicitly. Use consistent money units. Monetary precision supports 0–8 decimal places.

**Display** rounding preserves internal precision and rounds presented amounts. **Transaction** rounding rounds each booked movement or schedule period, half away from zero. Read the summary and detailed schedule together; final adjustments and residual balances may matter. **Copy summary** and **Copy table CSV** preserve the displayed results. Editing an input invalidates the old output until you calculate again.

These are generic mathematical worksheets. You supply tax rates, brackets, deductibility, fee rules and accounting assumptions. A modeled borrowing cost is not a jurisdiction-certified APR/THM. A simulation horizon or a failed root search does not establish that a goal is impossible or that an IRR is unique.

For every worksheet's inputs, conventions, examples and limitations, open the [Finance reference](finance/).

---

[Previous: Plot a curve and read a table](07-graphs-tables.md) · [Manual contents](./) · [Next: Customize your working method](09-input-workflows.md)
