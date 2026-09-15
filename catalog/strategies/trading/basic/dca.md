# Scheduled buying

Buy a fixed amount on a fixed schedule, and stop trying to time it.

Also called dollar-cost averaging. Instead of deciding when to deploy 1,000 USDC, you deploy 100 of it every week for ten weeks. Some purchases land well and some don't; you get the average rather than the outcome of one decision made on one day.

## How it works

Commit 1,000 USDC to buying ALGO, 100 USDC at a time, once a week.

Every week the rule checks two things: has the interval elapsed, and can it buy at a price you'd accept? If both are true it buys. If the price has spiked past your limit, it waits — a schedule is not a reason to accept a bad fill.

The rule tracks what's left of the 1,000 and when it last ran, so it never spends more than you committed.

## Timing is measured from execution

If a purchase runs two days late, the next one is a week from *then*, not from the original date. Missed weeks don't accumulate and fire all at once. Over a long schedule this drifts relative to the calendar, which is usually what you want.

## Adapting it

Set your price limit loosely if you care more about the schedule running than about any individual fill. Set it tightly if you'd rather skip weeks than overpay.

Add a [take-profit ladder](take-profit.md) once you've built a position and want a plan for selling parts of it.

Run it alongside a [grid](grid.md) — the grid works the range while the schedule keeps accumulating regardless. See [grid plus scheduled buying](../composed/grid-plus-dca.md).

Drop the schedule entirely and buy purely on price with [conditional accumulation](accumulation.md).

## What to watch for

**Buying steadily into a long decline still loses money.** Averaging in softens a bad entry; it doesn't rescue a bad asset. The schedule is a discipline for timing, not a substitute for the decision to own the thing.

**A tight price limit can stall the whole plan.** If the market spends two months above your limit, nothing gets bought. Decide which you actually care about — deploying the capital, or the price you deploy it at.

**This only buys.** Building a position and exiting it are separate strategies with separate funding.

**More frequent means more fees.** Daily purchases pay roughly seven times the transaction costs of weekly ones for the same capital.

**Related**

- [Conditional accumulation](accumulation.md) · [take-profit ladder](take-profit.md)
- [Grid plus scheduled buying](../composed/grid-plus-dca.md)
- [Nonlinear accumulation](../advanced/nonlinear-accumulation.md)
