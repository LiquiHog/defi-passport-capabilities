# Recurring payments

Set up a payment once and let it run. Salaries, grants, vesting, royalty splits.

Paying people repeatedly from a crypto treasury is usually a monthly chore: remember the date, check the address, sign the transaction, do it again. A funded payment rule does it on schedule, and the recipient can verify the funding exists rather than trusting that it does.

## How it works

You set four things:

| | |
|---|---|
| **Recipient** | An address, fixed |
| **Amount** | Per payment, in ALGO or any Algorand token |
| **Interval** | Weekly, monthly, whatever you choose |
| **Number of payments** | Optional. Twelve, twenty-four, or open-ended |

Then you fund it. The funded capital is committed to that rule — no strategy can spend it and it won't leave in a withdrawal.

A contributor on 1,300 USDC monthly for twelve months means funding 15,600. It pays out monthly and ends, without a reminder.

## Timing

Intervals are measured from the last actual payment. If one runs a day late, the next is a month from then. Missed dates don't stack up and fire together.

If the funding left is smaller than a full payment, the final one pays what remains rather than failing. A plan that ran slightly over still closes out cleanly.

## Adapting it

**Vesting.** A long schedule with a fixed count is a vesting contract — fund it, and the recipient can see the whole schedule.

**Grants.** Fund a milestone-based grant in tranches, each with its own end date.

**Royalty splits.** Several rules paying different recipients from the same incoming revenue. See [revenue splitting](revenue-splitting.md).

**Contributor payroll.** One rule per person, funded for the period governance approved. See [DAO operating reserve](../treasury/dao-treasury.md).

## What to watch for

**The recipient must hold the token.** On Algorand an account has to opt into an asset before it can receive it. Check before funding, not after a payment fails.

**Funding runs out silently.** When the money is gone, payments stop. Track the end date somewhere you'll actually see it.

**Amounts are fixed, not indexed.** A salary set in a token pays the same number of tokens regardless of what they're worth. Paying in a stable asset avoids surprising both sides.

**Changing a rule doesn't reset it.** Adjusting the amount keeps the count of payments already made. To start fresh, cancel and create a new one.

**Related**

- [Revenue splitting](revenue-splitting.md) · [DAO operating reserve](../treasury/dao-treasury.md)
- [NFT project treasury](../../systems/nft-project-treasury.md)
