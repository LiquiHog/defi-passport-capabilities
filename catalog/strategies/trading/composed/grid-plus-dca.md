# Grid plus scheduled buying

Work the range and build a long-term position at the same time, with separate money for each.

A [grid](../basic/grid.md) trades a range and ends roughly where it started, holding gains rather than a growing position. [Scheduled buying](../basic/dca.md) accumulates but ignores the range entirely. Running both means neither has to be the whole plan.

## How it works

From 5,000 USDC:

- **3,000** funds a grid on ALGO/USDC between $0.14 and $0.22
- **2,000** buys 100 USDC of ALGO every week and holds it

The grid trades its inventory back and forth, capturing gaps. The schedule quietly accumulates ALGO that the grid can never sell, because that inventory belongs to a different strategy.

After six months you have realized trading gains and a position you actually still hold.

## Adapting it

Route grid profits into the accumulation budget so trading gains fund the long-term position. See [profit recycling](../../portfolio/profit-recycling.md).

Add a [take-profit ladder](../basic/take-profit.md) against the accumulated position once it's worth exiting in stages.

Shift the weighting toward whichever you believe in more — the range or the trend.

## What to watch for

**The grid can be losing while the position gains, and vice versa.** Judge them separately. Netting them together hides which one is actually working.

**Both are exposed to the same asset.** This isn't diversification. A collapse in ALGO hurts both at once.

**Two strategies, two sets of fees.** Each slice needs to be big enough to be worth running.

**Related**

- [Grid](../basic/grid.md) · [scheduled buying](../basic/dca.md)
- [Multi-timescale](../advanced/multi-timescale.md)
