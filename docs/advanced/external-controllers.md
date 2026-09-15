# Letting software run your strategy

A passport enforces rules; it doesn't form opinions. It won't read volatility, spot a trend, or decide that now is a bad time to be buying.

So put something on top that does. A bot or an AI watches the market, decides what should change, and updates your settings. The passport keeps enforcing your limits the whole time — which means a bad signal costs you a bad trade, not your treasury.

## The division of labor

| Outside the passport | Inside the passport |
|---|---|
| Reading the market | Holding the capital |
| Deciding what should change | Enforcing what may be spent |
| Proposing new settings | Checking every trade's price before accepting it |
| Choosing when to step back | Refusing anything outside its funding |

The controller never holds your money. It proposes changes that you have authorized it to make, and the passport is the thing that says yes or no.

## The loop

1. Read current balances, funding and rule state.
2. Analyze whatever your strategy cares about.
3. Decide what should change — sizes, prices, allocation, funding.
4. Submit the change.
5. Watch what actually executed, and start again.

Step 5 matters more than it looks. Changing a setting doesn't reset a rule's history: a grid keeps the inventory it's already holding, and a payment plan keeps the count of what it's already paid. Read real state before deciding, not the state you assumed after your last update.

## What this unlocks

- **[Volatility-controlled grid](../../catalog/strategies/externally-managed/volatility-controlled-grid.md)** — widen the grid when the market gets choppy, tighten it when things calm down.
- **[Trend-aware allocation](../../catalog/strategies/externally-managed/trend-aware-allocation.md)** — shift the target mix as the trend changes.
- **[Risk controller](../../catalog/strategies/externally-managed/risk-controller.md)** — cut exposure when your limits are breached, restore it when they aren't.
- **[Strategy compiler](../../catalog/strategies/externally-managed/strategy-compiler.md)** — turn a plain-language objective into funded rules.
- **[AI-managed treasury](../../catalog/systems/autonomous-treasury.md)** — all of it, across a whole treasury.

## Keeping it safe

**Bound it before you automate it.** Lock the capital the controller must never reach. Fund each strategy with what you'd accept losing. Then let it run.

**Stopping the bot doesn't stop the rules.** If the controller goes quiet, the last settings it wrote stay in force and keep executing. Standing down is an action — release the funding or cancel the strategy.

**Give it one job.** A controller that tunes grid width is easy to reason about. One that may retune anything is hard to audit when it does something strange.

**A model can be confidently wrong.** The guardrails are the point. Keep them tight enough that a wrong call is a bad trade rather than a bad quarter.

See [staying in control](../overview/staying-in-control.md) for the limits available to you.
