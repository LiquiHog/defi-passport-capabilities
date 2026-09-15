# Protocol treasury

Fund development for years, and put the rest to work without risking any of it.

A protocol with a large treasury faces the opposite problem to a startup. There's plenty of money, which makes it easy to leave it idle for years — or to deploy it badly in search of a return nobody asked for.

## The setup

A 2,000,000 USDC treasury with about 60,000 a month in costs:

| Purpose | Amount | State |
|---|---|---|
| Development runway — 24 months | 1,440,000 | **Locked** |
| Long-term holdings | 300,000 | [Rebalancing](../../strategies/portfolio/rebalancing.md), 50/50 |
| Earning | 200,000 | [Idle capital lending](../../strategies/lending/idle-capital.md) |
| Working capital | 60,000 | Available for grants and one-offs |

Two years of runway locked first. That's what lets the protocol keep building through a bad market instead of making funding decisions under pressure.

## How money moves

Protocol revenue arrives as available capital. The order is the same every time: top up the runway to 24 months, then fund working capital, then allocate genuine surplus.

Strategy profits can be routed automatically rather than handled each time — see [profit allocation](profit-management.md).

## Adapting it

Pay contributor teams with [recurring payments](../commerce/recurring-payments.md) from the locked runway.

Run a [market-making allocation](../../systems/market-maker.md) in your own token, sized as capital you'd accept losing.

Let a controller manage the earning allocation within bounds, keeping the runway untouchable. See [AI-managed treasury](../../systems/autonomous-treasury.md).

## What to watch for

**Don't hold the treasury in your own token.** If the protocol struggles, the token falls at exactly the moment the treasury is needed. Runway in a stable asset is what makes it runway.

**Twenty-four months goes quickly.** Check quarterly. Headcount grows and costs rise, so a runway sized last year is shorter than it looks.

**Large treasuries attract bad ideas.** Every proposal to deploy capital for yield is a proposal to take a risk the protocol may not need to take. The runway isn't underperforming — it's doing its job.

**Related**

- [Profit allocation](profit-management.md) · [idle capital management](idle-capital-management.md)
- [Trading plus lending](../../systems/trading-plus-lending.md)
