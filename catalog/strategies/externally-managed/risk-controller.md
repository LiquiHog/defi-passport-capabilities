# Risk controller

Software whose only job is to make the treasury smaller when things go wrong.

Most controllers try to earn more. This one tries to lose less. It watches exposure against limits you set and pulls funding back when they're breached — no view on direction, no prediction, just a rule that acts faster than you would at 3am.

## How it works

You define the limits. The controller enforces them.

| Limit | Controller does |
|---|---|
| Single asset above 40% of treasury | Reduce that strategy's funding |
| Drawdown past 15% from the high | Cut active trading inventory by half |
| Volatility above your threshold | Pause new positions |
| Conditions normalize | Restore funding, in stages |

It only changes funding and settings. It can't move money out of the passport, and it can't touch locked capital.

## Adapting it

Restore gradually. Cutting fast and restoring slowly is usually right — the reverse gets you back into a falling market early.

Run it over several strategies so one controller enforces treasury-wide limits rather than per-strategy ones.

Pair it with an earning controller, with the risk controller holding veto. See [AI-managed allocation](ai-strategy-manager.md).

## What to watch for

**It will sometimes sell the bottom.** A drawdown limit that fires at 15% locks in that loss if the market recovers the next day. That's the cost of a rule that also protects you when it doesn't recover.

**Limits are only useful set in advance.** A limit you'd override in the moment isn't a limit. Set thresholds you'd genuinely accept being enforced against you.

**Restoring needs a rule too.** Controllers that cut but never restore leave a treasury permanently defensive, earning nothing, long after conditions normalized.

**A quiet controller protects nothing.** If it stops running, limits stop being enforced — and you may not notice until they're breached.

**Related**

- [Trend-aware allocation](trend-aware-allocation.md) · [AI-managed allocation](ai-strategy-manager.md)
- [Staying in control](../../../docs/overview/staying-in-control.md)
