# Reserve management

Give every part of the treasury a job, so none of them can spend another's money.

This is the foundation everything else sits on. Most treasury accidents aren't bad trades — they're a strategy quietly consuming capital that was meant for payroll.

## How it works

A 10,000 USDC treasury:

| Purpose | Amount | State |
|---|---|---|
| Six months of operating costs | 4,000 | **Locked** — nothing can reach it |
| Investment allocation | 3,000 | Committed to [rebalancing](rebalancing.md) |
| Trading inventory | 2,000 | Committed to a [grid](../trading/basic/grid.md) |
| Unassigned | 1,000 | Available |

Locking the operating reserve is the important part. It isn't a note in a spreadsheet — no strategy can spend it, no automation can reach it, and it won't leave in a withdrawal until you unlock it.

The grid cannot borrow from investment. Investment cannot dip into operations. Each one runs out of its own money and stops.

## Adapting it

Lend the reserve while it waits, if you can accept the withdrawal time. See [idle capital](../lending/idle-capital.md).

Pay out of the reserve on a schedule with [recurring payments](../../use-cases/commerce/recurring-payments.md) — approved amounts to approved recipients, without unlocking the whole thing.

Grow the reserve from trading gains by pointing a strategy's profits at it. See [profit recycling](profit-recycling.md).

## What to watch for

**Size the reserve honestly.** Work from real monthly costs, not optimistic ones. A four-month reserve that's really two months is worse than no plan, because it feels safe.

**Keep ALGO for running costs separate again.** Transaction fees and minimum balance come out of ALGO, not your USDC reserve. See [costs](../../../docs/overview/costs.md).

**Review it when things change.** Headcount, revenue and burn all move. A reserve sized last year may be wrong now.

**Locked means locked.** That's the feature. If you think you might need it next month, it belongs in available capital, not behind a lock you'll resent.

**Related**

- [Rebalancing](rebalancing.md) · [core and satellite](core-and-satellite.md)
- [DAO operating reserve](../../use-cases/treasury/dao-treasury.md) · [staying in control](../../../docs/overview/staying-in-control.md)
