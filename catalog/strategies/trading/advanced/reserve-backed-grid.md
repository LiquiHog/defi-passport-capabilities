# Reserve-backed grid

Run a grid, but keep capital back for the move you didn't plan for.

Committing your whole allocation to grid levels on day one means having no answer if the market goes somewhere your range doesn't cover. Holding part of it in reserve keeps that option open.

## How it works

You have 5,000 USDC for trading ALGO. Instead of spreading all of it across the grid:

- **3,000 USDC** funds the grid levels between $0.14 and $0.22
- **2,000 USDC** sits in reserve, committed to nothing

If price breaks below $0.14 and stalls there, the grid has spent its buy side and is waiting. Now you have a decision to make with real capital behind it: extend the range down, re-centre the grid, or leave it alone and wait.

The reserve is ordinary available capital. Nothing spends it automatically — that's the point.

## Adapting it

Automate the top-up. Route grid profits into the reserve so it refills from trading gains — see [profit recycling](../../portfolio/profit-recycling.md).

Let a controller manage it. A bot can watch conditions and decide when to deploy reserve capital into new levels. See [volatility-controlled grid](../../externally-managed/volatility-controlled-grid.md).

Set a rule for yourself in advance. "Deploy half the reserve if we hold below $0.12 for a week" is a decision made calmly, which beats one made during the drop.

## What to watch for

**Reserve capital earns nothing while it waits.** That's the premium you pay for flexibility. If the market stays in range all year, the full grid would have out-earned you.

**Reserves attract bad decisions.** Capital held back for a considered response is easy to spend on an emotional one. If you won't follow a pre-set rule, the reserve is just money you haven't deployed yet.

**Consider lending it.** An idle reserve can earn while it waits, as long as you can pull it out when you need it. See [idle capital](../../lending/idle-capital.md).

**Related**

- [Grid](../basic/grid.md) · [asymmetric grid](asymmetric-grid.md)
- [Market-making treasury](../../../systems/market-maker.md)
