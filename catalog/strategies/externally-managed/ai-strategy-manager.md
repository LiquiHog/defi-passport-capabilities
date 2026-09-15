# AI-managed allocation

Hand the thinking to a model, keep the limits on-chain.

A language model can weigh things a fixed rule can't — market conditions, your treasury's obligations, how last quarter went. What it shouldn't have is unbounded access to your money. This splits those: the model proposes, the passport enforces.

## How it works

**The model decides.** It reads balances, positions and whatever context you give it, and proposes changes: shift the allocation, resize a strategy, pause something.

**The passport enforces.** It applies changes within the bounds you set. Locked capital stays locked. Funding limits hold. Every trade still has to clear its worst-acceptable price.

A model that decides to put everything into one asset finds it simply can't.

## What makes this safe

| Guardrail | Why |
|---|---|
| Lock the operating reserve | The model can never reach payroll |
| Cap each strategy's funding | A bad call costs one strategy, not the treasury |
| Bound allocation ranges | No single asset can dominate |
| Keep an [automation allowance with an expiry](../../../docs/overview/staying-in-control.md) | Permission lapses unless renewed |
| Log every change | You can reconstruct what it did and why |

## Adapting it

Give it one job first — sizing a single strategy — before letting it manage allocation.

Run it over a [satellite](../portfolio/core-and-satellite.md) with capital you'd accept losing, until it's earned more.

Put a [risk controller](risk-controller.md) alongside it with veto power over exposure.

Require approval for large changes, so it acts freely within a band and asks beyond it.

## What to watch for

**A model can be confidently wrong.** It will produce a fluent, plausible rationale for a bad decision. The guardrails are the actual protection — not the quality of the reasoning.

**Explanations aren't evidence.** Judge it on what the treasury did, not on how good the write-up was.

**Its context is limited.** It knows what you tell it. Obligations you didn't mention aren't part of its reasoning.

**Stopping it leaves its last settings running.** Standing down means releasing funding, not just switching off the model.

**Related**

- [AI strategy planner](strategy-compiler.md) · [risk controller](risk-controller.md)
- [AI-managed treasury](../../systems/autonomous-treasury.md)
- [Letting software run your strategy](../../../docs/advanced/external-controllers.md)
