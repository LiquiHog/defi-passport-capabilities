# Swapping on demand

Trade straight from the passport, without setting up a strategy at all.

Not everything needs a rule. Sometimes you just want to convert 5,000 USDC into ALGO today, because you decided to. This is that — a direct swap you initiate, priced and checked the same way an automated trade would be.

## How it works

You choose what you're spending, what you want, and the least you'll accept in return. The swap executes, or it doesn't happen.

Two things are enforced:

**It can only spend uncommitted capital.** Money funding a grid, backing an order, or sitting behind a lock is untouchable here. If the treasury holds 10,000 USDC and 9,000 is committed to strategies, a swap can spend 1,000. The passport works out the difference and refuses anything beyond it.

**Your minimum is binding.** If the market can't return at least what you asked for, the whole thing reverts and you still have your original asset. There's no partial fill and no "close enough".

## When to use it

**Converting revenue on arrival.** Payment lands in a volatile token you didn't choose to hold; swap it to something stable the same day.

**Rebalancing by hand.** You want a one-off adjustment, not a standing [rebalancing](../../portfolio/rebalancing.md) rule.

**Setting up a strategy.** A [grid](grid.md) needs inventory on both sides. If you hold only USDC, swap for the base asset first, then fund the grid.

**Acting on a decision.** You've concluded something and want to act now. A strategy is for behavior you want repeated; this is for a decision you've already made.

## What to watch for

**This is you timing the market.** The point of most strategies in this catalog is removing that. A one-off swap puts it back. That's fine when you've genuinely decided something — less fine as a habit.

**Set the minimum deliberately.** Too tight and the swap keeps failing; too loose and you've removed your own protection. It should reflect what you'd actually accept, not a formality.

**Committed capital is genuinely unavailable.** Discovering mid-swap that most of the treasury is spoken for is normal — that's the accounting working. Release funding from a strategy first if you want to use it.

**Large swaps move the price.** For real size, [OTC](../../../use-cases/markets/otc-trading.md) or a [scheduled conversion](dca.md) will cost you less than one large trade.

**Related**

- [Scheduled buying](dca.md) — the same conversion, spread over time
- [OTC trading](../../../use-cases/markets/otc-trading.md) — for size
- [What a passport can do](../../../../docs/overview/capabilities.md)
