# Conditional accumulation

Buy only at prices you'd actually choose, however long that takes.

[Scheduled buying](dca.md) trades on a clock. This trades on a price. The capital sits ready and does nothing until the market comes to you — which might be next week or might be never.

## How it works

Set aside 500 USDC to buy ALGO, in slices of up to 100 USDC, and require each slice to fill at $0.15 or better.

Nothing happens while ALGO trades at $0.18. The capital stays committed to the rule, doing nothing. If price drops to $0.15, a slice buys. The rest keeps waiting.

The rule tracks remaining capital, what it has acquired, and when it last filled.

## Adapting it

Use several rules with different prices and different sizes, so you buy more the further the market falls. That turns a flat limit into a deliberate curve — see [nonlinear accumulation](../advanced/nonlinear-accumulation.md).

Add a timing interval alongside the price condition when you want both: no more than one purchase a week, and only under $0.15.

Some strategies can check a price feed before acting, which strengthens the guarantee that you're buying at the level you meant.

## What to watch for

**Waiting is a position too.** Capital committed to a rule that never triggers earns nothing and isn't available for anything else. If the market spends a year above your price, that's a year of doing nothing with that money.

**Getting filled means the market fell.** You'll be buying while things look bad — that's the entire design. If you're going to override it then, don't set it up.

**Averaging down has a floor.** Each fill increases your exposure to an asset that is, by construction, declining. Decide your total commitment up front and let the rule respect it.

**Related**

- [Scheduled buying](dca.md) · [nonlinear accumulation](../advanced/nonlinear-accumulation.md)
- [Take-profit ladder](take-profit.md)
