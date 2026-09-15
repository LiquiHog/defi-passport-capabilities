# DAO operating reserve

Contributors get paid on schedule. The reserve stays where governance put it.

A DAO's treasury has a structural problem: the money is collectively owned, decisions are slow, and contributors need paying whether or not a vote passed this week. Passing a proposal for every payroll run is exhausting and fragile.

## The setup

Governance approves a budget once. The passport enforces it afterwards.

| Purpose | Amount | State |
|---|---|---|
| Long-term reserve | 400,000 USDC | **Locked** |
| Approved contributor payments | 96,000 USDC | Funded [recurring payments](../commerce/recurring-payments.md), 12 months |
| Working capital | 30,000 USDC | Available for approved spending |
| Running costs | ALGO | Fees and minimum balance |

Six contributors on 1,300 a month each, funded for twelve months. Each has their own payment rule: recipient, amount, monthly interval, twelve payments and then it ends.

## What this changes

**Contributors can verify they'll be paid.** The funding exists on-chain and the schedule is visible. That's a materially different proposition from trusting a multisig to remember.

**Payroll doesn't need a vote.** Governance approved twelve months. The twelve months run.

**The reserve is genuinely separate.** Locked capital can't be reached by a payment rule, a strategy, or anyone's mistake.

**Ending is deliberate.** Payments stop after twelve, or when you stop them. Nobody gets paid indefinitely because a rule was forgotten.

## Adapting it

Renew before expiry so a governance delay doesn't mean a missed month.

Add [revenue splitting](../commerce/revenue-splitting.md) for protocol income that should be divided automatically.

Lend the reserve so it earns while it waits, accepting that withdrawals take time. See [idle capital](../../strategies/lending/idle-capital.md).

Fund a small [investment allocation](../../strategies/portfolio/rebalancing.md) from surplus, clearly separated from anything operational.

## What to watch for

**Contributors need to hold the token you're paying.** A recipient who hasn't opted into the asset can't receive it. Check before funding, not after a payment fails.

**Locked means locked.** If governance may need the reserve at short notice, don't lock it — the friction is the feature, and resenting it means it's in the wrong place.

**Payments end quietly.** Twelve months passes faster than it sounds. Put the renewal date somewhere you'll see it.

**Related**

- [Recurring payments](../commerce/recurring-payments.md) · [reserve management](../../strategies/portfolio/reserve-management.md)
- [Reserve plus rebalancer](../../systems/reserve-plus-rebalancer.md)
