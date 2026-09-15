# Idle capital lending

Most treasuries hold more cash than they'll spend this quarter. Lending is what you do with the difference.

The hard part isn't the lending — it's working out honestly how much you can afford to have tied up.

## How it works

A 10,000 USDC treasury spending about 2,000 a month.

| | Amount | Why |
|---|---|---|
| Liquid runway | 6,000 | Three months of costs, available immediately |
| Lending | 4,000 | Not needed in the near term |

The 4,000 earns while it sits. The 6,000 pays bills and funds strategies. When you need the lent capital back, you withdraw it — and you wait for it to arrive before committing it to anything else.

Capital you've lent still counts toward what a [rebalancing](../portfolio/rebalancing.md) strategy sees, so lending part of a holding doesn't distort your target mix.

## Sizing the runway

Work it out in this order:

1. **Real monthly costs**, not optimistic ones.
2. **How many months** you'd want if revenue stopped entirely.
3. **Anything large and dated** — an audit, a payroll spike, a contract renewal.

What's left after those three is a candidate for lending. Not before.

## Adapting it

Ladder it. Lend in several pieces on different terms so capital becomes available in stages rather than all at once.

Run it alongside trading — see [lending plus trading](lending-plus-trading.md) and [lending plus rebalancing](lending-plus-rebalancing.md).

Borrow instead, if you need cash but don't want to sell what you hold. See [borrowing](borrowing.md).

## What to watch for

**Deployed is not spendable.** A treasury worth 10,000 with 4,000 lent cannot spend 10,000 tomorrow. Plans that confuse total value with available cash break at the worst possible moment.

**Withdrawals aren't always instant.** When a lending market is heavily utilized, getting capital out can take longer than you'd like — usually exactly when everyone else wants theirs too.

**Rates move, and they're not promises.** A good rate today is not a rate for the year.

**The lending protocol's rules apply, not the passport's.** Once capital is deposited there, its behavior belongs to that protocol.

**Confirm receipt before you commit it.** Withdraw, watch the balance land, then fund the next thing. Never the other way round.

**Related**

- [Borrowing](borrowing.md) · [capital recycling](capital-recycling.md)
- [Idle capital management](../../use-cases/treasury/idle-capital-management.md)
- [Lending and borrowing](../../../docs/advanced/lending-and-capital-use.md)
