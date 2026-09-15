# Multi-timescale

Different money, different horizons, one treasury.

The trade you'd make on a 2% wobble and the one you'd make on a 40% collapse are not the same trade, and they shouldn't compete for the same capital. Splitting by horizon means a busy short-term strategy can't spend the money you were saving for a real opportunity.

## How it works

From 10,000 USDC allocated to ALGO exposure:

| Horizon | Capital | Strategy |
|---|---|---|
| Days | 3,000 | A [grid](../basic/grid.md) working a tight range |
| Weeks | 3,000 | [Scheduled buying](../basic/dca.md), 250 USDC weekly |
| Months | 4,000 | [Nonlinear accumulation](nonlinear-accumulation.md), triggering only on deep drawdowns |

In a quiet month the grid does the work and the rest waits. In a crash the grid exhausts its buy side, the schedule keeps buying, and the deep rules finally spend the capital they were holding for exactly that.

No strategy can reach another's funding. The grid cannot spend the crash money, however attractive a level looks.

## Adapting it

Change the weighting to match your conviction. More in the short horizon if you believe in the range; more in the long one if you're waiting for a dislocation.

Add an exit horizon — a [take-profit ladder](../basic/take-profit.md) funded from acquired inventory, selling into strength over months.

Let a controller shift the balance between horizons as conditions change. See [external controllers](../../../../docs/advanced/external-controllers.md).

## What to watch for

**Three strategies cost three sets of fees.** Each needs to justify its own overhead. If the short-horizon slice is too small to cover its trading costs, fold it in.

**The long horizon may never trigger.** Capital reserved for a crash that doesn't come is capital that did nothing for a year. That's the deliberate cost of readiness.

**More strategies, more to watch.** Three interacting positions are harder to reason about than one. Be able to state what each is for and when you'd change it.

**Related**

- [Grid](../basic/grid.md) · [scheduled buying](../basic/dca.md) · [nonlinear accumulation](nonlinear-accumulation.md)
- [Core and satellite](../../portfolio/core-and-satellite.md)
