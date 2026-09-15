# Profit recycling

Decide where gains go before you have them.

Profit that lands back in the strategy that made it just keeps trading. Sometimes that's what you want. Often you'd rather it grew the portfolio, refilled a reserve, or covered the cost of running everything. Deciding once, in advance, means it happens without you.

## Where profits can go

| Destination | Good for |
|---|---|
| **Your wallet** | Taking gains off the table |
| **Another strategy** | Compounding — a grid's gains growing your portfolio allocation |
| **Running costs** | Automation that pays for itself out of what it earns |

You choose either a percentage of each gain or a fixed amount, so you can take a steady slice or skim only what exceeds a threshold.

## How it works

A grid trading ALGO/USDC with 3,000 USDC of inventory, earning roughly 40 USDC a week.

Point 50% of profits at your [rebalancing](rebalancing.md) strategy and leave the rest in the grid. Each week about 20 USDC moves across and grows the portfolio; about 20 stays and slowly increases the grid's own inventory.

Trading gains become portfolio growth without you moving anything.

## Adapting it

Point profits at running costs so a busy strategy funds its own automation — useful for anything that trades often. See [costs](../../../docs/overview/costs.md).

Route into a reserve instead, and the reserve grows from trading rather than from new deposits. See [reserve-backed grid](../trading/advanced/reserve-backed-grid.md).

Take everything to your wallet for a treasury that wants income rather than compounding.

## What to watch for

**Assets have to match.** Profits top up a strategy holding the same asset. Nothing is converted for you — USDC profits can only feed a strategy that holds USDC.

**It adds funding, it doesn't trigger anything.** The destination strategy runs on its own conditions, now with more to work with.

**Sending everything away starves the source.** A grid that never keeps any gains stays exactly the same size forever. If you want it to grow, leave it a share.

**Related**

- [Rebalancing](rebalancing.md) · [core and satellite](core-and-satellite.md)
- [Grid plus rebalancing](../trading/composed/grid-plus-rebalancing.md)
- [Protocol profit allocation](../../use-cases/treasury/profit-management.md)
