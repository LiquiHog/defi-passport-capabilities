# How automation works

You set up a rule and fund it. After that, something has to submit the transaction when the moment arrives — you don't have to be online, and you don't have to watch a chart.

## Who presses the button

An automation service watches for rules that are ready and submits them.

It is not trusted with your money. It can only trigger rules you already funded and approved, every condition is re-checked on-chain at the moment of execution, and the transaction simply fails if those conditions aren't met. The service cannot send your funds anywhere your own rule doesn't already point, and it cannot pay itself more than the allowance you granted.

Submitting transactions costs ALGO, so you keep a small ALGO balance for running costs and grant an allowance the service can draw on. That allowance has a ceiling and an expiry date. See [costs](costs.md).

## What makes a rule ready

| Rule | Waits for |
|---|---|
| Grid | Price to reach the next level, with that level's side funded |
| Scheduled buying | The interval to elapse, and the price to clear your minimum |
| Order | Its price to be met, and its expiry date not to have passed |
| Recurring payment | The interval to elapse, with funding and payments still remaining |
| Rebalancing | Your mix to drift past the band you set, after any cooldown |

Timing runs from the last actual execution, not from a calendar. If a payment runs a day late, the next one is measured from when it actually ran. Missed dates don't pile up and fire all at once.

## Why a rule might not have fired

Worth checking in this order:

1. **The condition isn't met yet.** The price hasn't reached your level, or the interval hasn't elapsed.
2. **The side isn't funded.** A grid level that just sold needs its buy side funded before it can buy again.
3. **The price moved through your minimum.** Every trade has a worst-acceptable price. If the market can't fill you at that price or better, the trade doesn't happen — by design.
4. **Running costs ran out**, or the automation allowance expired.
5. **The order expired**, or the payment hit its final scheduled run.

A rule that can't execute isn't lost. It sits and waits, and your capital is still yours.

## Getting a fair price

Every trade carries a worst-acceptable price, expressed as a percentage away from the expected one. The passport checks the actual result before it accepts the trade. If you'd receive less than you agreed to, the whole thing reverts.

Some strategies can additionally check a price feed before acting, and where both a feed and the passport's own figure are available, it uses whichever is more conservative.

## Changing your mind

You can refund a rule, change its settings, release its capital, or cancel it outright at any time. Capital released from a rule becomes available again — still inside the passport, ready for something else. Withdrawing moves it out entirely.

Changing a setting doesn't reset history. A grid keeps the levels it's already holding; a payment plan keeps the count of what it's already paid. If you want a clean slate, cancel and start again.

A bot or an AI can make these same changes on your behalf, within limits you set — see [external controllers](../advanced/external-controllers.md).
