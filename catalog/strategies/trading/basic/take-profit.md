# Take-profit ladder

Sell a position in stages, at prices you decided in advance.

Selling everything at once means being right about one moment. A ladder spreads the exit across several prices, so a partial gain is locked in early and the rest stays exposed if the move continues.

## How it works

You hold 2,000 ALGO bought around $0.14. You split it into four sell orders:

| Size | Target |
|---|---|
| 500 ALGO | $0.18 |
| 500 ALGO | $0.22 |
| 500 ALGO | $0.26 |
| 500 ALGO | $0.30 |

Each order sits until the market reaches its price. If ALGO runs to $0.23, the first two have sold and the rest are still waiting. You've realized gains on half the position without having had to call the top.

Each order commits its own ALGO, so no other strategy can spend inventory that's already promised to a sell.

## Adapting it

Weight the ladder. Sell more early if you mainly want your capital back, or more at the top if you're willing to hold for a bigger move.

Pair it with [scheduled buying](dca.md) — one strategy builds the position, the other exits it, each with its own funding.

Run it alongside a [grid](grid.md) so small repeated trades and larger planned exits coexist without competing for the same inventory. See [grid plus take-profit](../composed/grid-plus-take-profit.md).

## What to watch for

**The top rungs may never fill.** That's the trade-off you accepted. Set the highest target at a price you'd be genuinely happy to sell at, not an aspirational one.

**A ladder doesn't chase.** If price reaches $0.29, reverses, and collapses, your $0.30 order simply never fills. Targets don't follow a rising market unless something updates them — see [external controllers](../../../../docs/advanced/external-controllers.md).

**Selling early caps your upside.** Realizing gains at $0.18 feels good until the asset reaches $0.50. This is the cost of not having to be right about timing.

**Set targets against your actual entry.** The passport enforces the prices you give it; working out which prices leave you ahead after fees is your decision, made before you configure it.

**Related**

- [Scheduled buying](dca.md) · [limit trading](limit-trading.md)
- [Grid plus take-profit](../composed/grid-plus-take-profit.md)
