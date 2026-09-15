# Trend-aware allocation

A target mix that shifts with the market instead of staying fixed forever.

Plain [rebalancing](../portfolio/rebalancing.md) holds one allocation through everything, which means buying a falling asset all the way down. A controller that reads the trend can move the target itself — more risk when conditions support it, less when they don't.

## How it works

**The bot decides** what the allocation should be, from whatever signals it uses.

**The passport enforces** the resulting target, and keeps your operating reserve entirely out of reach.

| Bot's read | Target mix |
|---|---|
| Strong uptrend | 75% ALGO / 25% USDC |
| Neutral | 60% / 40% |
| Weakening | 40% / 60% |
| Strong downtrend | 20% / 80% |

Only the investment allocation moves. Locked operating capital isn't part of this and can't be reached by it.

## Adapting it

Bound the range. Allowing 20–75% means even a badly wrong model can't put everything into one asset.

Add a cooldown so the target can't be rewritten daily on noisy signals.

Combine with [core and satellite](../portfolio/core-and-satellite.md) — let the controller manage a satellite before trusting it with the core.

## What to watch for

**Trend signals lag.** They identify a trend once it's underway, which means buying after a rise and selling after a fall. In choppy markets that's a reliable way to be wrong in both directions.

**Whipsaws are expensive.** A signal that flips weekly means constant rebalancing and constant fees, with no net position change to show for it.

**Bound it or it will find the edges.** A model with no limits will eventually propose 100% of something. The bounds are what makes this safe to run.

**Stopping the bot freezes the last target.** If it read "strong uptrend" before going quiet, you're sitting at 75% ALGO indefinitely. Standing down is an action.

**Related**

- [Rebalancing](../portfolio/rebalancing.md) · [dynamic rebalancing](dynamic-rebalancing.md)
- [Risk controller](risk-controller.md)
