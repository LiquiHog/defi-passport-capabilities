# Borrowing against what you hold

Raise cash without selling the position.

A treasury holding ALGO it intends to keep for years still has bills this month. Selling covers the bills and ends the position — and if the price runs afterwards, you bought those bills expensively. Borrowing against the holding leaves it intact.

## How it works

Your passport deposits a holding into a lending protocol as collateral and borrows a different asset against it. You get spendable cash, the original position stays yours, and you repay on your own schedule to release the collateral.

Collateral securing a loan is committed to that loan. While it's posted, it isn't available to your trading strategies and it won't leave in a withdrawal — the passport accounts for it as spoken for, the same way it treats capital funding a rule.

## A concrete case

A project holds 50,000 ALGO it doesn't want to sell and needs 20,000 USDC for six months of contractor payments.

Post the ALGO as collateral and borrow 20,000 USDC against it — comfortably under what the collateral supports, rather than the maximum available. Fund a [recurring payment](../../use-cases/commerce/recurring-payments.md) to pay contractors monthly from the borrowed USDC. When revenue arrives, repay the loan and the ALGO is released.

The project kept its ALGO exposure through the whole period and paid interest instead of giving up the position.

## Borrowing deliberately

Borrow well below the maximum. The gap between what you borrowed and what your collateral supports is the room you have before a price move becomes your problem — borrowing the maximum leaves none.

Have the repayment planned before you borrow. Revenue you expect, a lending position maturing, a vesting schedule. Borrowing against a hope is how treasuries get liquidated.

Interest accrues the whole time. A loan held for a year against an asset that went sideways cost you real money for nothing.

## What to watch for

**Liquidation is the real risk.** If your collateral falls far enough in value, the protocol sells it to repay the loan — at a moment you didn't choose and probably wouldn't have chosen. Borrowing against a volatile asset to hold another volatile asset compounds this.

**Rates move.** Borrowing costs are set by the lending market and can rise while you hold the loan.

**The collateral is committed.** It cannot back a strategy or be withdrawn until the loan is repaid, so don't post capital another part of your plan is relying on.

**The lending protocol's rules apply, not the passport's.** Once capital is deposited there, its behavior — rates, liquidation thresholds, availability — belongs to that protocol.

**Related**

- [Idle capital lending](idle-capital.md) — the other direction: earn on cash you aren't using
- [Capital recycling](capital-recycling.md)
- [Lending and capital use](../../../docs/advanced/lending-and-capital-use.md)
