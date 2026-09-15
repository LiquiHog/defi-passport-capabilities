# Passport-to-passport settlement

Two treasuries, one agreed trade, and no way for either side to be left short.

When two organizations trade with each other, the usual awkwardness is who moves first. Escrow adds a third party, staged transfers add risk, and doing it on trust works until it doesn't. Settling both sides in one transaction removes the question.

## How it works

Treasury A and Treasury B agree: 100,000 of A's token for 50,000 of B's USDC.

Each funds only what it's offering. At settlement, both sides move together — or nothing moves. There is no state in which one side has paid and the other hasn't.

## What the guarantee covers

The **exchange** is atomic. Once settlement runs it completes fully or does nothing at all.

The **negotiation** isn't part of it. Agreeing a price, deciding the counterparty is good for it, and funding your side all happen beforehand in the ordinary way.

This matters because the guarantee removes exactly one risk — settlement risk — and leaves the others in place. That one risk happens to be the one that makes treasuries reluctant to trade directly.

## Adapting it

Set an expiry so a stale agreement can't be executed after the market moves.

Use partial fills for a standing offer; keep it all-or-nothing for a negotiated block.

Settle in stages for very large deals — several agreed exchanges over weeks, each atomic, so neither side carries the whole exposure at once.

## What to watch for

**Check the price independently.** Atomic settlement is indifferent to whether the terms were fair.

**Confirm assets carefully.** Token IDs, decimals and amounts should be verified by both sides before funding. A settlement that executes the wrong asset executed correctly.

**Your counterparty may never fund.** The trade doesn't happen and you keep your assets, but your capital was committed and unavailable while you waited. Expiries limit that.

**Related**

- [Passport-to-passport exchange](../../strategies/counterparty/passport-swap.md) · [OTC trading](otc-trading.md)
- [Trading directly with another treasury](../../../docs/advanced/passport-to-passport.md)
