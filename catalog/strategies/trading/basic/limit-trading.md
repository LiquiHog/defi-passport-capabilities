# Limit trading

A standing offer: this much of mine, for at least that much of yours.

Useful when you know what you'd accept but not when someone will accept it. The inventory is committed, the terms are fixed, and the order waits.

## How it works

You offer 1,000 of your token and want at least 5,000 USDC for it.

The order commits that inventory — no other strategy can spend it while the offer stands. It fills when someone or something can meet your terms, and if nobody can, nothing happens. You are never filled at a worse price than you set.

## Fill policy and expiry

**All-or-nothing or in pieces.** All-or-nothing suits a negotiated block where the size is the point. Allowing partial fills suits a standing offer you're happy to have taken gradually — set a sensible minimum so you aren't filled twelve tokens at a time.

**Expiry.** An offer priced on Monday shouldn't still be live on Friday after the market has moved. Give it a deadline and it stops being your problem when it passes.

Together these cover the familiar cases: good-till-date, fill-or-kill, and a resting offer that works down over days.

## Adapting it

Set several orders at different prices to build a [take-profit ladder](take-profit.md).

Point the order at a specific counterparty rather than the open market when you've agreed terms directly — see [passport-to-passport exchange](../../counterparty/passport-swap.md) and [OTC trading](../../../use-cases/markets/otc-trading.md).

## What to watch for

**It may simply never fill.** A price nobody will pay is an order that expires. Committed inventory does nothing in the meantime.

**Partial fills leave a remainder.** After 960 of 1,000 sells, you hold an awkward 40. Setting a minimum fill size keeps the leftovers manageable.

**Depth limits large orders.** An offer far bigger than the market normally trades will fill slowly, in pieces, or not at all. For real size, consider [OTC](../../../use-cases/markets/otc-trading.md) instead of a public route.

**Related**

- [Take-profit ladder](take-profit.md)
- [Passport-to-passport exchange](../../counterparty/passport-swap.md) · [OTC trading](../../../use-cases/markets/otc-trading.md)
