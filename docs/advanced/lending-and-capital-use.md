# Lending and borrowing

Most treasuries hold more cash than they need this month. Lending is what you do with the difference; borrowing is what you do when you need cash but don't want to sell.

## Earning on what's idle

Work out what you actually need liquid, then lend what's left.

A 10,000 USDC treasury spending 2,000 a month might keep three months — 6,000 — liquid and lend the other 4,000. The liquid portion pays the bills and funds trading. The lent portion earns until you need it.

Capital you've lent still counts toward what a rebalancing strategy sees, so lending part of a holding doesn't distort your target mix.

Start with [idle capital lending](../../catalog/strategies/lending/idle-capital.md), then [lending plus trading](../../catalog/strategies/lending/lending-plus-trading.md) or [capital recycling](../../catalog/strategies/lending/capital-recycling.md).

## Borrowing instead of selling

If you hold something you intend to keep, borrowing against it raises cash without ending the position. You pay interest rather than giving up the asset, and you repay on your own terms to release it.

Collateral posted against a loan is committed to that loan. It isn't available to your strategies and won't leave in a withdrawal until the loan is repaid.

See [borrowing](../../catalog/strategies/lending/borrowing.md).

## Deployed capital isn't spendable capital

This is the one thing to internalize. A treasury worth 10,000 with 4,000 lent out can't spend 10,000 tomorrow. Total value and available cash are different numbers, and plans that confuse them break at the worst moment.

Two habits follow from it:

**Keep near-term spending out of lending entirely.** Payroll due in three weeks does not belong in a lending position, however good the rate.

**Confirm money has actually arrived before you commit it.** Withdraw from lending, see the balance land, then fund the next thing. Multi-step reallocations can stop halfway, and a step funded from expected proceeds fails when the proceeds are late.

A worked version: of 1,000 USDC returning from lending, you plan 600 for trading and 400 for operations. Withdraw, confirm receipt, then fund each. Not the other way around.

## What you're taking on

Capital in a lending protocol follows that protocol's rules, not the passport's. Rates move, withdrawals can be constrained when utilization is high, and borrowing brings liquidation risk if your collateral falls far enough.

The passport tracks what you've deployed and enforces your own accounting around it. It does not insure the position.
