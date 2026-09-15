# Dynamic rebalancing

Rebalance when it's worth doing, not when the calendar says so.

Fixed [rebalancing](../portfolio/rebalancing.md) uses one band forever. But a 5% drift means something different in a calm market than a wild one, and rebalancing through high volatility often just pays fees to be undone tomorrow. A controller can decide when a rebalance is actually worth making.

## How it works

The target mix stays the same — 60/40. What changes is when the strategy acts on it.

| Conditions | Controller does |
|---|---|
| Calm | Narrows the band to 3% — cheap to correct, worth doing |
| Normal | Holds at 5% |
| Volatile | Widens to 12% — avoid rebalancing into noise |
| Extreme | Pauses entirely |

Your allocation doesn't change. Only the threshold for acting on it does.

## Adapting it

Add a minimum trade size so small corrections never happen, whatever the band says.

Let it adjust the target as well as the band, and you have [trend-aware allocation](trend-aware-allocation.md) instead.

Combine with lending — a wider band means less frequent trading, so more capital can stay lent. See [lending plus rebalancing](../lending/lending-plus-rebalancing.md).

## What to watch for

**Pausing in extreme conditions cuts both ways.** It avoids rebalancing into chaos. It also means not buying the dip that a fixed strategy would have bought. Decide which you actually want.

**Complexity needs to earn its keep.** If the adaptive version doesn't clearly beat a fixed 5% band after fees, the fixed band is better because you can reason about it.

**A drifting portfolio is an unmanaged one.** Widening the band during volatility lets your allocation wander furthest exactly when it matters most.

**Related**

- [Rebalancing](../portfolio/rebalancing.md) · [trend-aware allocation](trend-aware-allocation.md)
- [Lending plus rebalancing](../lending/lending-plus-rebalancing.md)
