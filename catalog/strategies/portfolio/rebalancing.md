# Rebalancing

Decide what you want to hold, and hold it — even as prices try to change it for you.

You choose 60% ALGO and 40% USDC. ALGO doubles, and now you're at 75/25 whether you meant to be or not. Rebalancing sells some ALGO to get back to 60/40, which means selling strength and buying weakness automatically, without having to feel good about it at the time.

## How it works

A 10,000 USDC treasury targeting 60/40:

| | Target | After ALGO rises 50% |
|---|---|---|
| ALGO | 6,000 | 9,000 (69%) |
| USDC | 4,000 | 4,000 (31%) |

You set a band — say 5% — so the strategy acts when the mix drifts past 65/35 rather than on every small move. Here it sells about 1,200 USDC worth of ALGO, returning to 60/40 and banking part of the gain.

The same thing works in reverse. If ALGO falls, it buys, because the target says so.

## What you set

| | |
|---|---|
| **Target mix** | The allocation you actually want |
| **Band** | How far it may drift before acting |
| **Cooldown** | A minimum gap between rebalances |
| **Worst-acceptable price** | Every trade still has to clear it |

Band and cooldown exist to stop a volatile market from rebalancing you into a fee bill.

## Adapting it

Add a third asset and the same logic holds across all of them.

Keep operating cash outside the strategy entirely — rebalancing should manage your investment allocation, not your payroll. See [reserve management](reserve-management.md).

Let a controller move the target as conditions change, rather than holding one fixed mix forever. See [trend-aware allocation](../externally-managed/trend-aware-allocation.md) and [dynamic rebalancing](../externally-managed/dynamic-rebalancing.md).

Lend the stable portion while it waits — capital in lending still counts toward the mix. See [lending plus rebalancing](../lending/lending-plus-rebalancing.md).

## What to watch for

**It underperforms in a strong trend.** Rebalancing trims winners. If ALGO runs for a year, you'll have sold into it the whole way and done worse than holding. That's the trade you made for not riding it back down.

**Tight bands are expensive.** Rebalancing on a 1% drift in a choppy market means constant trading and constant fees for very little correction.

**It doesn't pick assets.** Holding 60% of something falling to zero rebalances you diligently into a loss. The target mix is a decision you make, not one the strategy makes for you.

**Related**

- [Reserve management](reserve-management.md) · [core and satellite](core-and-satellite.md)
- [Grid plus rebalancing](../trading/composed/grid-plus-rebalancing.md)
- [Reserve plus rebalancer](../../systems/reserve-plus-rebalancer.md)
