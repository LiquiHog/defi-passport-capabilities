# Revenue splitting

Income arrives, and everyone's share reaches them without anyone doing arithmetic.

Four collaborators agreed on 40/30/20/10. Every time money comes in, someone has to work out four numbers, send four transactions, and be trusted to have done it right. Funding four payment rules removes both the chore and the trust question.

## How it works

12,000 USDC of revenue to divide four ways:

| Recipient | Share | Amount |
|---|---|---|
| Lead | 40% | 4,800 |
| Developer | 30% | 3,600 |
| Artist | 20% | 2,400 |
| Community fund | 10% | 1,200 |

Fund four [payment rules](recurring-payments.md), one per recipient. Each is committed to that recipient and can't be spent on anything else. Everyone can verify their share is funded before it arrives.

## Recurring versus per-batch

**Per batch.** Revenue is irregular, so you fund the split each time income arrives. More work, but shares always match actual revenue.

**Recurring.** Income is predictable enough to commit to a monthly figure. Less work, but you're promising an amount rather than a share.

Most projects start per-batch and move to recurring once revenue is steady.

## Adapting it

Take costs off the top first — fund operations, then split the remainder. Splitting gross revenue and paying costs afterwards is how collaborations end in argument.

Route strategy profits into a split automatically, so investment gains are shared the same way. See [profit allocation](../treasury/profit-management.md).

Fund a reserve as one of the "recipients", so the project accumulates alongside the people.

## What to watch for

**Everyone must hold the token.** A recipient who hasn't opted into the asset can't receive it. Check all of them before funding.

**Percentages need rounding rules.** Three ways into 10,000 doesn't divide evenly. Decide in advance who absorbs the remainder.

**Splits change; funded rules don't.** If someone leaves, the existing funded rules keep paying as configured until you change them.

**Agree gross or net in writing.** By far the most common dispute is whether the split applies before or after costs.

**Related**

- [Recurring payments](recurring-payments.md) · [creator revenue](../economies/creator-revenue.md)
- [Royalty revenue](nft/royalty-revenue.md)
