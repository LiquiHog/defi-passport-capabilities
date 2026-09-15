# Grid plus rebalancing

Trading gains that feed a portfolio instead of just piling up.

A [grid](../basic/grid.md) generates profit in whatever asset it trades. Left alone, that accumulates in the trading strategy and keeps trading. Pointing it at a [rebalancing](../../portfolio/rebalancing.md) strategy turns short-term trading into long-term portfolio growth.

## How it works

Two strategies, each with its own money:

- A grid trades ALGO/USDC with 3,000 USDC of inventory
- A rebalancing strategy holds a 60/40 ALGO/USDC target with 7,000 USDC

The grid's profit destination is set to the rebalancing strategy. Every time a round trip closes, a share of the gain moves across and increases what the portfolio has to work with. The portfolio then rebalances on its own schedule, at its own thresholds.

Your day-to-day trading compounds into the thing you're actually building.

## Adapting it

Send a percentage rather than everything, so the grid retains some gains and grows its own inventory too.

Reverse the flow for a treasury that would rather harvest than compound: route profits to your wallet and keep the portfolio at a fixed size.

Let a controller adjust both — grid spacing and portfolio targets — from one view of the market. See [dynamic rebalancing](../../externally-managed/dynamic-rebalancing.md).

## What to watch for

**Assets have to match.** Profit routing tops up a strategy holding the same asset. Nothing is converted for you, so a grid earning USDC can only feed a strategy that holds USDC.

**Routing adds funding, not action.** The rebalancing strategy doesn't run because money arrived. It runs when its own conditions are met, now with more behind it.

**Two strategies on correlated assets.** A downturn in ALGO hits the grid's inventory and the portfolio's allocation together.

**Related**

- [Grid](../basic/grid.md) · [rebalancing](../../portfolio/rebalancing.md) · [profit recycling](../../portfolio/profit-recycling.md)
- [Reserve plus rebalancer](../../../systems/reserve-plus-rebalancer.md)
