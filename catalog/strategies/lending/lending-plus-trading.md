# Lending plus trading

Idle capital earning, trading inventory working, neither depending on the other.

The mistake this avoids: funding a grid and assuming you can top it up from lending if it runs low. You often can't, at least not quickly — and a strategy built on that assumption fails precisely when markets are moving.

## How it works

A 10,000 USDC treasury:

| | Amount | Behavior |
|---|---|---|
| Operating reserve | 3,000 | Locked, untouchable |
| Trading inventory | 3,000 | A [grid](../trading/basic/grid.md) on ALGO/USDC |
| Lending | 4,000 | Earning, withdrawable on the protocol's terms |

The grid runs entirely on its own 3,000. If it exhausts its buy side, it waits — it does not reach into lending, and you shouldn't plan for it to.

If you decide to add to the grid after a large move, that's a deliberate sequence: withdraw from lending, confirm receipt, fund the grid. Days, not seconds.

## Adapting it

Keep a small liquid buffer outside both, so a top-up doesn't require a withdrawal at an awkward moment.

Route grid profits into lending so trading gains compound at the lending rate rather than sitting idle. See [profit recycling](../portfolio/profit-recycling.md).

Size the grid to what you'd accept losing, given it can't be reinforced quickly.

## What to watch for

**Lending is not a credit line for your grid.** This is the whole point. Withdrawals take time, and the moment you want capital most is the moment withdrawals are slowest.

**Both suffer in a crisis together.** A market crash hurts grid inventory and stresses lending markets at once. They're separate strategies, not uncorrelated ones.

**Fees on both sides.** The grid pays to trade, lending has its own costs. Each slice needs to be large enough to be worth running.

**Related**

- [Idle capital lending](idle-capital.md) · [grid](../trading/basic/grid.md)
- [Lending plus rebalancing](lending-plus-rebalancing.md)
- [Trading plus lending treasury](../../systems/trading-plus-lending.md)
