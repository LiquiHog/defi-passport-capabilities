# AI-managed treasury

A model allocating across several strategies, inside limits it cannot exceed.

The appeal is obvious: software that watches conditions continuously and reallocates faster and less emotionally than a committee. The risk is equally obvious. This system is mostly about the second part.

## The allocation

A 100,000 USDC treasury with about 6,000 a month in costs:

| Purpose | Amount | Who controls it |
|---|---|---|
| Operating reserve — 12 months | 72,000 | **Locked.** The model cannot reach this. |
| Managed allocation | 20,000 | The model, within bounds |
| Manual reserve | 6,000 | You |
| Running costs | ~2,000 in ALGO | Fees, minimum balance |

The model manages 20% of the treasury. That number is the design. Everything else follows from deciding what a wrong model is allowed to cost you.

## What the model may do

Within the managed allocation, it can shift between a [grid](../strategies/trading/basic/grid.md), a [rebalancing](../strategies/portfolio/rebalancing.md) strategy and [lending](../strategies/lending/idle-capital.md), and resize each within limits.

| Guardrail | Value |
|---|---|
| Maximum in any one strategy | 10,000 |
| Maximum single-asset exposure | 60% of the managed allocation |
| Minimum interval between changes | 24 hours |
| Automation allowance | Bounded, and expires unless renewed |

It cannot withdraw, cannot reach locked capital, and cannot pay itself. Every trade still has to clear its worst-acceptable price.

## Reviewing it

**Weekly:** what changed and why. You should be able to follow the reasoning even if you'd have decided differently.

**Monthly:** did the managed allocation beat simply holding? If not consistently, the complexity isn't paying for itself.

**Whenever it does something you don't understand:** tighten the bounds. Confusion is a signal, not a thing to sit with.

## What to watch for

**Fluent is not correct.** A model will explain a bad decision persuasively. Judge it on what the treasury did, not the quality of the write-up.

**Stopping it doesn't stop the rules.** Its last settings stay in force and keep executing. Standing down means releasing funding or cancelling strategies.

**It only knows what you tell it.** An obligation you didn't mention isn't part of its reasoning.

**Start smaller than this.** 20% is where you might end up after a few quarters of watching. Begin with a [satellite](../strategies/portfolio/core-and-satellite.md) you'd accept losing entirely.

**Related**

- [AI-managed allocation](../strategies/externally-managed/ai-strategy-manager.md) · [AI strategy planner](../strategies/externally-managed/strategy-compiler.md)
- [Risk controller](../strategies/externally-managed/risk-controller.md)
- [Staying in control](../../docs/overview/staying-in-control.md)
