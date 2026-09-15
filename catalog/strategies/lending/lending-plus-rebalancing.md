# Lending plus rebalancing

Hold your target mix, and earn on the stable half while it waits.

A 60/40 portfolio keeps 40% in a stablecoin doing nothing between rebalances. Lending that portion earns a return without changing the allocation — capital in lending still counts toward what the rebalancing strategy sees.

## How it works

A 10,000 USDC treasury targeting 60% ALGO, 40% USDC:

| | Amount | Where it sits |
|---|---|---|
| ALGO | 6,000 | Held in the passport |
| USDC, liquid | 1,500 | Available for the next rebalance |
| USDC, lent | 2,500 | Earning |

The mix is still 60/40. The rebalancing strategy sees the full USDC position, including the lent portion, so lending doesn't pull your allocation out of shape.

Keeping 1,500 liquid means an ordinary rebalance happens immediately. Only an unusually large one needs a withdrawal first.

## Adapting it

Size the liquid buffer from your band. Wide bands mean rare, larger rebalances; tight bands mean frequent, smaller ones that need more cash on hand.

Widen the band deliberately to trade less and keep more capital lent.

Let a controller manage the split between liquid and lent as volatility changes. See [dynamic rebalancing](../externally-managed/dynamic-rebalancing.md).

## What to watch for

**A big move can outrun your buffer.** If ALGO drops sharply and the rebalance needs 3,000 USDC when you have 1,500 liquid, you're withdrawing from lending before you can act — and the price you rebalance at is whatever it is by then.

**Withdrawals are slowest when markets are worst.** The rebalance you most want to make is the one most likely to be delayed.

**Lending yield is not portfolio performance.** Keep them separate in your accounting or you'll flatter a rebalancing strategy that isn't earning its keep.

**Related**

- [Rebalancing](../portfolio/rebalancing.md) · [idle capital lending](idle-capital.md)
- [Lending plus trading](lending-plus-trading.md)
