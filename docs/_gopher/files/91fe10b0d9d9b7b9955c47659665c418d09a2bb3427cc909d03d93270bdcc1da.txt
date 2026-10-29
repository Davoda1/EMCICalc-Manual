Open **Graph / Table**, or press **Ctrl+G**. A new graph starts empty.

1. Select **Add curve**.
2. Choose an explicit curve and enter `sin(x)` in **Expression**.
3. Set the series **Angle** to RAD.
4. Use **Range** to choose a view, for example x from −6.3 to 6.3 and y from −1.5 to 1.5.
5. Select **Plot**. Add `cos(x)` as another series if you want to compare them.
6. Use the **Plot**, **Series**, **Range** and **Table** tabs to switch tasks.

The workspace supports up to 20 configured series: explicit, polar, parametric, implicit equality, inequality regions and `z=f(x,y)` surfaces. Parametric curves need the corresponding component expressions and parameter interval. Set the relevant fields for the chosen type; a second component is not needed for an ordinary y=f(x) curve.

Drag a two-dimensional canvas to pan and use the mouse wheel to zoom. In 3D, dragging rotates the sampled surface. **View** provides zoom, rotation, reset, fit and export actions. **Reset view** changes the viewing range; **Series → Manage curves → Clear all curves** removes the series. Changing a formula invalidates its old plotted output until you plot again.

Tables accept a range and step, up to 10,000 requested inputs. Polar and parametric tables use their parameter; implicit and surface tables use the documented y=0 slice. **Export CSV** preserves returned row status as well as numbers. **Export PNG** captures the current 2D or 3D view; **Export SVG** is for 2D.

Plots are numerical samples. Invalid points appear as gaps. Roots, intersections, extrema and inflections are numerical candidates, not symbolic proofs. Zoom around suspected poles and check the function's domain. Sampling has time and evaluation budgets; use fewer enabled series, a narrower range or a lower sampling quality if a request reaches its limit.

---

[Previous: Convert units and currencies](06-conversions.md) · [Manual contents](./) · [Next: Use the mathematical workbenches](08-workbenches.md)
