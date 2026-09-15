# Passport-to-passport exchange

Two treasuries, one agreed trade, settled all-or-nothing.

When you've already agreed terms with someone, going through a public market is worse in every direction: you move the price against yourself, pay spread to people who aren't part of the deal, and show your size to everyone watching. Trading directly avoids all of it.

## How it works

Treasury A holds a token Treasury B wants. B holds USDC that A wants. They agree on 100,000 tokens for 50,000 USDC.

Each side funds only what it's offering. A commits 100,000 tokens; B commits 50,000 USDC. Neither can touch the other's treasury, and neither is exposed beyond what it committed.

Settlement happens in a single transaction. Both sides receive what they agreed, or nothing moves at all. Nobody can take one side of the trade and walk away.

## What the guarantee covers

The **exchange** is atomic. Once settlement runs, it either completes fully or does nothing.

The **negotiation** isn't. Agreeing the price, deciding you trust the counterparty, and funding your side happen beforehand, in the ordinary way. The passport enforces the terms you configured; it doesn't tell you whether they were good terms.

## Adapting it

Set an expiry. Terms agreed on Monday shouldn't still be executable on Friday after the market has moved.

Allow partial fills for a standing offer you're happy to have taken gradually. Keep it all-or-nothing when the size is the point of the deal.

Post it openly instead of to a named counterparty, and let whoever wants it take the other side. See [OTC trading](../../use-cases/markets/otc-trading.md).

## What to watch for

**Pricing is on you.** There's no market quote to anchor against, so check the fair value yourself before agreeing. An atomic settlement executes a bad price just as reliably as a good one.

**Your counterparty might not fund their side.** The trade simply doesn't happen — you keep your assets — but you've had capital committed and unavailable in the meantime.

**Set an expiry.** An offer with no deadline is one you're still exposed to weeks later.

**Related**

- [Limit trading](../trading/basic/limit-trading.md)
- [OTC trading](../../use-cases/markets/otc-trading.md) · [passport-to-passport settlement](../../use-cases/markets/p2p-settlement.md)
- [Trading directly with another treasury](../../../docs/advanced/passport-to-passport.md)
