# Capital recycling

Moving money between lending, reserves and strategies as your needs change — without losing track of where it is.

Treasuries aren't static. Revenue arrives, a strategy closes, a lending position matures. Each of those is capital arriving that needs a next job. Recycling is just doing that deliberately rather than letting balances drift.

## How it works

1,000 USDC comes back from a lending position. You've decided it should become 600 trading and 400 operating.

The order matters:

1. **Withdraw** from lending.
2. **Confirm** the 1,000 has actually landed and is available.
3. **Fund** the trading strategy with 600.
4. **Fund** operations with 400.

Each step uses capital that's genuinely there. If step 1 returns 950 instead of 1,000, you find out before you've promised 1,000 to something else.

## Adapting it

Automate the routing with [profit recycling](../portfolio/profit-recycling.md) — gains move to a chosen destination as they're realized, no manual step.

Set triggers instead of a schedule. "When the reserve drops below 5,000, top it up from lending" beats a monthly review you'll forget.

Let a controller manage the whole loop, within limits you set. See [external controllers](../../../docs/advanced/external-controllers.md).

## What to watch for

**Never fund from expected proceeds.** A multi-step move can stop halfway. If step 3 assumes money that step 1 hasn't delivered, you've built a plan that fails quietly.

**Every move costs fees.** Capital shuffled weekly between four destinations spends real money on transactions. Recycle when there's a reason, not on a calendar.

**Watch for gaps.** Capital in transit isn't earning and isn't working. Long unwinding chains leave money doing nothing for days.

**Related**

- [Idle capital lending](idle-capital.md) · [profit recycling](../portfolio/profit-recycling.md)
- [Lending and borrowing](../../../docs/advanced/lending-and-capital-use.md)
