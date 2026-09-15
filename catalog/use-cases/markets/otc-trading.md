# OTC trading

Moving size without telling the market you're moving it.

A public order for 500,000 USDC of a mid-cap token does two things before it fills: it walks through the book, getting worse as it goes, and it announces your intention to everyone watching. For real size, agreeing a price directly with a counterparty is simply better.

## How it works

You hold 2,000,000 of a token and want roughly 100,000 USDC for it.

Rather than selling into the market, you agree terms with a counterparty — a fund, another treasury, a market maker — and settle directly. One price, no slippage, no spectators.

Fund only what you're offering. Settlement moves both sides together or neither. Nobody can take your tokens and fail to pay.

## Two shapes

**Negotiated block.** You've agreed terms with a specific counterparty. All-or-nothing, with an expiry, because the size is the point of the deal. See [passport-to-passport exchange](../../strategies/counterparty/passport-swap.md).

**Standing offer.** You post what you'll accept and let whoever wants it take the other side. Partial fills allowed, so it works down over time as counterparties appear.

## Adapting it

Split a large block across several counterparties at slightly different prices rather than depending on one.

Combine with a public route — some size through [scheduled selling](../../strategies/trading/basic/dca.md), the rest OTC.

Always set an expiry. Terms agreed on Monday shouldn't be executable on Friday.

## What to watch for

**Pricing is on you.** There's no book to anchor against. Check fair value independently before agreeing, because atomic settlement executes a bad price as faithfully as a good one.

**Expect a discount for size.** A counterparty taking a large block carries the risk of moving it. That discount is the cost of not moving the market yourself — compare it honestly against the slippage you'd have paid.

**Counterparties can walk.** Until settlement runs, no exchange has happened and you still hold everything. But your capital stays funded to the offer, and therefore unavailable for anything else, while you wait.

**Related**

- [Passport-to-passport exchange](../../strategies/counterparty/passport-swap.md) · [limit trading](../../strategies/trading/basic/limit-trading.md)
- [Token sale diversification](../commerce/token-sale-diversification.md)
