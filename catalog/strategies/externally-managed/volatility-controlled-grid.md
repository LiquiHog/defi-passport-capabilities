# Volatility-controlled grid

A grid that widens when the market gets rough and tightens when it calms down.

A fixed [grid](../trading/basic/grid.md) has one spacing, chosen once. In a quiet market that spacing is too wide and it barely trades; in a volatile one it's too tight and it churns through fees. A bot watching volatility can keep adjusting it — while the passport keeps enforcing your limits.

## How it works

**The bot decides.** It measures volatility however you like — recent ranges, realized volatility, whatever your model uses — and works out what the spacing should be.

**The passport enforces.** It receives updated settings and applies them. It never calculates volatility, never forms a view, and never spends beyond the inventory you funded.

| Market | Bot does | Result |
|---|---|---|
| Quiet | Tightens spacing to $0.005 | More fills, smaller gains each |
| Normal | Holds at $0.01 | Baseline |
| Volatile | Widens to $0.03 | Fewer fills, larger gains, less churn |
| Extreme | Widens further, or reduces active inventory | Less exposure while things are wild |

## Adapting it

Give it bounds. Minimum and maximum spacing, and a ceiling on active inventory, mean a miscalibrated model can only do so much.

Adjust size as well as spacing — pulling inventory back in extreme conditions is often more useful than widening.

Let it manage several [layered grids](../trading/composed/multi-layer-strategy.md), activating and deactivating layers by regime.

## What to watch for

**Volatility is measured looking backwards.** By the time your model sees a volatile market, the move has already happened. Adaptive grids react; they don't anticipate.

**Stopping the bot doesn't stop the grid.** Whatever settings it wrote last stay in force and keep trading. Standing down means releasing the funding or cancelling the strategy, not just turning off the controller.

**Retuning has a cost.** Changing settings constantly means transaction fees and a grid that never settles into a range. Give the controller a minimum interval.

**It's still a grid.** A sustained trend hurts it, and clever spacing doesn't change that.

**Related**

- [Grid](../trading/basic/grid.md) · [layered grids](../trading/composed/multi-layer-strategy.md)
- [Letting software run your strategy](../../../docs/advanced/external-controllers.md)
