# Gaming treasury

Keeping the reward pool, the studio's runway and the investment allocation from ever becoming the same pot.

A game with an in-economy has three obligations that look similar from a balance sheet and behave nothing alike. Player rewards are a promise to the community. Runway keeps the studio alive. Investment is what's genuinely spare. Mixing them is how a studio ends up funding payroll from the reward pool.

## The setup

A studio holding 500,000 USDC:

| Purpose | Amount | State |
|---|---|---|
| Studio runway — 12 months | 300,000 | **Locked** |
| Player reward pool | 120,000 | **Locked**, paid out on schedule |
| Investment allocation | 50,000 | [Rebalancing](../../strategies/portfolio/rebalancing.md) |
| Working capital | 30,000 | Available |

Both the runway and the reward pool are locked. That's deliberate: neither should be reachable by a decision made under pressure, and players can verify the pool actually exists.

## Paying rewards

Fund [recurring payments](../commerce/recurring-payments.md) for scheduled distributions — seasonal prize pools, staking rewards, tournament payouts. A funded, visible schedule is worth considerably more to a player community than an announcement, because it can be checked.

For variable rewards, fund each season from working capital once the amounts are known, and keep the locked pool as the guarantee that seasons will continue.

## Adapting it

Hold token inventory for in-game economies as a separate allocation again, so operational tokens aren't mixed with treasury holdings.

Run a small [market-making allocation](../markets/market-making.md) if your game token trades, sized as capital you'd accept losing.

Lend the reward pool between distributions, as long as withdrawal timing comfortably beats your payout dates. See [idle capital](../../strategies/lending/idle-capital.md).

## What to watch for

**Never fund runway from the reward pool.** It's the most tempting mistake available and it's the one that destroys player trust permanently. Locking it is what stops the conversation happening.

**Reward promises outlive good intentions.** A pool funded for eight seasons should be funded for eight seasons. Extending a season without extending the funding is a shortfall you'll discover late.

**Don't hold the treasury in your game token.** If the game struggles, the token falls, and you need the treasury most exactly then.

**Publish the structure.** Players who can verify a funded reward pool behave differently from players who are asked to trust one.

**Related**

- [Recurring payments](../commerce/recurring-payments.md) · [market making](../markets/market-making.md)
- [Reserve management](../../strategies/portfolio/reserve-management.md)
