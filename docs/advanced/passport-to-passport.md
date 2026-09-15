# Trading directly with another treasury

Two treasuries that want to trade with each other don't need a market to meet in. One posts terms, the other takes them, and both sides move in a single transaction that either completes entirely or does nothing.

## Why bother

A DAO wants 200,000 of a partner's token and is happy to pay 100,000 USDC. Routing that through a public market means moving the price against yourself on the way in, paying spread to people who aren't party to the deal, and announcing your size to everyone watching.

Agreeing the price directly avoids all of that. The trade clears at the number the two of you settled on.

## How settlement works

```text
Agree the terms between you
          ↓
Each side funds what it's offering
          ↓
Settle in one transaction
          ↓
Both sides receive, or neither does
```

The guarantee is worth being precise about: it covers the **exchange**. When settlement runs, either both sides receive what they agreed or nothing moves at all. Nobody can take your side of the trade and leave.

It does not cover the negotiation. Agreeing terms, deciding you trust the counterparty, and funding your side all happen before that point, in the ordinary way.

## Shaping the offer

**Set an expiry.** Terms agreed on Monday shouldn't still be executable on Friday after the market has moved. An offer with a deadline stops being your problem when it passes.

**Decide about partial fills.** All-or-nothing suits a negotiated deal where the size is the point. Allowing pieces suits a standing offer you're happy to have taken gradually.

**Only fund what you're offering.** The rest of your treasury is not exposed to the trade. A counterparty sees a funded offer, not your balance sheet.

## A worked example

Treasury A offers 100,000 X for Treasury B's 200,000 Y.

Each funds its own side. Neither can spend the other's, and neither can be drained beyond what it committed. At settlement, the passport checks the assets and amounts on both sides match what was agreed. If anything is off — wrong asset, short amount, expired offer — nothing happens and both sides keep what they had.

Operating reserves, payroll and unrelated strategies play no part. They can't be touched by a trade they weren't funded into.

Explore [passport-to-passport exchange](../../catalog/strategies/counterparty/passport-swap.md) and [OTC treasury trades](../../catalog/use-cases/markets/otc-trading.md).
