# Grid

Buy low and sell high, over and over, from an inventory you cap up front.

Prices rarely move in a straight line. A grid turns that back-and-forth into realized gains: it holds buy levels below the current price and sell levels above it, and every time one fills it flips to face the other way. You never pick a direction, and you never watch a chart.

## How it works

ALGO is around $0.18. You set aside 1,000 USDC and 2,000 ALGO for the grid, and nothing else in the treasury is involved.

You place levels every $0.01 between $0.14 and $0.22. Each level commits a slice of that inventory. When price falls to $0.17, that level spends USDC and buys ALGO. Now filled, it turns into a sell at $0.18. When price comes back up, it sells and flips back to a buy.

Each completed round trip captures the gap between the two prices, minus fees. A choppy month might produce fifty of them.

## What you set

| | |
|---|---|
| **Range** | The prices you're willing to trade between |
| **Spacing** | Tighter levels fill more often, for smaller gains each |
| **Size per level** | How much inventory each one commits |
| **Worst-acceptable price** | Every fill must clear it, or the trade doesn't happen |
| **Where profits go** | Your wallet, another strategy, or running costs |

Keep both sides funded. A level that just sold needs USDC before it can buy again, and a level that just bought needs the ALGO it acquired to sell. Running costs stay separate from trading inventory.

## Adapting it

Make the levels uneven if you have a view — bigger size where you'd genuinely like to own more. See [asymmetric grid](../advanced/asymmetric-grid.md).

Hold capital back rather than committing it all at launch, so you can add to the grid deliberately after a move. See [reserve-backed grid](../advanced/reserve-backed-grid.md).

Run several grids over different price regions to cover a wider move. See [layered grids](../composed/multi-layer-strategy.md).

Let a bot widen the spacing when the market gets volatile and tighten it when things settle. See [volatility-controlled grid](../../externally-managed/volatility-controlled-grid.md).

## What to watch for

**A trend is what hurts a grid.** In a sustained fall you keep buying all the way down and end up holding an asset worth less than you paid. In a sustained rise you sell your inventory early and watch it continue without you. Grids earn in ranges and lose ground in trends — pick pairs and ranges accordingly.

**Fees set a floor on your spacing.** If the gap between two levels doesn't clearly exceed the cost of trading it, you're paying to churn. Tighter is not automatically better.

**Running out of one side stalls it.** A grid that has bought its way through every level has no USDC left to buy with and sits waiting for a recovery. That's the strategy working as designed, but it can be a long wait.

**Each level stands alone.** A grid level doesn't wait for a cooldown and doesn't consult a price feed. If you want that behavior, use [conditional accumulation](accumulation.md) or an [externally managed](../../externally-managed/volatility-controlled-grid.md) variant.

**Related**

- [Asymmetric grid](../advanced/asymmetric-grid.md) · [reserve-backed grid](../advanced/reserve-backed-grid.md)
- [Grid plus rebalancing](../composed/grid-plus-rebalancing.md) · [grid plus scheduled buying](../composed/grid-plus-dca.md)
- [Market-making treasury](../../../systems/market-maker.md)
