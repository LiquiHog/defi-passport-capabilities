# AI strategy planner

Describe what you want in plain language; get a set of funded rules back.

Most people know what they want their treasury to do. Turning that into specific strategies with specific amounts is the part that stalls. A planner does that translation — and because it produces ordinary passport rules, you can read the result before anything is funded.

## How it works

You describe the objective:

> "We have 50,000 USDC from a token sale. We need 18 months of runway at 2,000 a month, want some ALGO exposure built up gradually, and we'd like the rest earning something."

The planner proposes:

| Allocation | Amount | Strategy |
|---|---|---|
| Operating reserve | 36,000 | Locked, 18 months at 2,000 |
| ALGO accumulation | 8,000 | [Scheduled buying](../trading/basic/dca.md), 350 weekly |
| Earning | 6,000 | [Idle capital lending](../lending/idle-capital.md) |

You read it, adjust it, and fund it. The plan is a proposal until you do.

## Adapting it

Ask for alternatives — conservative, balanced and aggressive versions of the same objective — and compare them.

Have it explain its reasoning per allocation. A plan you can't follow is one you shouldn't fund.

Let it revise as things change. A plan built for 18 months of runway needs revisiting when revenue starts.

Keep it as a planner. Generating a plan you approve is a much smaller trust decision than [ongoing management](ai-strategy-manager.md).

## What to watch for

**Review before funding.** The plan is the model's opinion. It doesn't know about the audit you're paying for next month unless you said so.

**Plausible isn't correct.** A well-presented plan can still be badly sized. Check the arithmetic — particularly the runway.

**Tell it your obligations.** Anything you leave out isn't in the plan.

**A plan is a starting point.** Treasuries change. Revisit it rather than treating a first draft as permanent.

**Related**

- [AI-managed allocation](ai-strategy-manager.md)
- [AI-managed treasury](../../systems/autonomous-treasury.md)
- [Example capital plans](../../../examples/README.md)
