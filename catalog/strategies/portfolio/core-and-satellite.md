# Core and satellite

Most of the treasury boring on purpose, a small part free to be interesting.

Trying to run one strategy that is both safe and ambitious produces something that's neither. Splitting the decision lets the majority of your capital stay conservative while a defined slice takes real risk — and caps what that risk can cost you.

## How it works

A 10,000 USDC treasury:

| | Amount | What it does |
|---|---|---|
| **Core** | 8,000 | A conservative [60/40 allocation](rebalancing.md), rebalanced on wide bands |
| **Satellite A** | 1,000 | A [grid](../trading/basic/grid.md) on a volatile pair |
| **Satellite B** | 1,000 | [Accumulation](../trading/basic/accumulation.md) in a smaller asset |

Each satellite can lose everything without threatening the treasury. That's what makes it acceptable to try things. If a satellite works, it proves itself with real money and you can decide to size it up.

The core cannot be drawn on to rescue a satellite, which is the whole point — the losing position can't quietly become the big one.

## Adapting it

Feed winners back to the core. Route satellite profits into the core allocation so successes compound somewhere safe. See [profit recycling](profit-recycling.md).

Give satellites a review date. Three or six months, then decide: grow it, keep it, or shut it down.

Use a satellite as a testbed for an [externally managed strategy](../externally-managed/README.md) before letting software near anything larger.

## What to watch for

**Satellites are supposed to fail sometimes.** If none of yours ever lose money, they aren't taking enough risk to be worth the complexity.

**Don't rescue a loser.** Adding core capital to a failing satellite converts a capped loss into an uncapped one. The cap was the feature.

**Too many satellites is just a portfolio.** Two or three you can actually explain beat eight you can't.

**Related**

- [Rebalancing](rebalancing.md) · [reserve management](reserve-management.md)
- [Multi-timescale](../trading/advanced/multi-timescale.md)
