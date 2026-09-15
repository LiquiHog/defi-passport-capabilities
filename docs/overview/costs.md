# What it costs to run

Four things consume ALGO or take a cut. None of them are hidden, and you can see all of them before you fund anything.

## Network fees

Every action is an Algorand transaction, so every action costs a network fee. Algorand's fees are small and fixed rather than auction-based, but a strategy that fires often pays more of them than one that fires monthly. Keep this in mind when setting a tight interval or a dense grid: more executions means more fees, and each fill has to be worth the cost of making it.

## Running costs

The automation service pays the network fee up front and draws from an allowance you granted to cover it.

You control both the size of that allowance and the date it expires, and each strategy carries its own ceiling so one busy strategy can't consume what the others need. The protocol enforces an upper bound per action as well.

Setting an allowance is not the same as depositing ALGO. The passport needs a real ALGO balance to draw from — an allowance only sets how much of it may be used.

## Trading fee

Trades carry a protocol fee, taken as a percentage of what the trade returns. It comes out of the proceeds, so the amount you receive is already net of it. Your worst-acceptable price is checked against that net figure, which means a trade that would only clear after the fee is not a trade the passport will accept.

Strategies that lend pay a fifth of the standard rate.

## Minimum balance

Algorand requires every account to hold a small amount of ALGO in reserve, and that requirement grows as an account holds more tokens and more rules. It isn't a fee — it's yours, and you get it back when you close things down — but it isn't spendable while it's held.

In practice: a passport's ALGO balance is never entirely available, and opting into another token or adding another strategy raises the floor slightly.

## Planning for it

A treasury running a handful of strategies should hold ALGO for the minimum balance and running costs, kept clear of trading inventory. The exact amount depends on how often your rules fire; the point is to treat it as its own line rather than discovering it when a strategy stops.

See [staying in control](staying-in-control.md) for how to bound what automation may spend.
