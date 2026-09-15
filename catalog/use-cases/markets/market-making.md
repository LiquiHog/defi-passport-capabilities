# Bounded market-making inventory

Give your token a market people can trade in, without hiring anyone or handing over inventory.

A thin market hurts a project in ways that compound: buyers move the price against themselves, sellers get poor fills, and both conclude the token isn't worth holding. Running two-sided liquidity from your own treasury fixes that, and the important word is *bounded*.

## The setup

A project with 100,000 USDC and 2,000,000 of its own token:

| Purpose | Amount | State |
|---|---|---|
| Operating reserve | 40,000 USDC | **Locked**, in a different asset |
| Active liquidity | 30,000 USDC + 1,200,000 tokens | [Grid](../../strategies/trading/basic/grid.md) |
| Replenishment reserve | 25,000 USDC + 800,000 tokens | Available, uncommitted |
| Buffer and running costs | 5,000 USDC + ALGO | |

Only 30% of the USDC is exposed at any moment. The active grid is what you'd accept losing in a bad run.

## Shaping it

**Weight the buy side.** Most projects are happier accumulating their token cheaply than selling it cheaply. See [asymmetric grid](../../strategies/trading/advanced/asymmetric-grid.md).

**Start wider than feels right.** Tight spacing looks better and costs more. Widen until the gaps clearly exceed trading costs, then tighten only if volume justifies it.

**Hold capital back.** The replenishment reserve is what lets you respond to a move outside your range instead of watching it. See [reserve-backed grid](../../strategies/trading/advanced/reserve-backed-grid.md).

## Adapting it

Let a bot adjust spacing with volatility — see [volatility-controlled grid](../../strategies/externally-managed/volatility-controlled-grid.md).

Handle large trades separately through [OTC](otc-trading.md) rather than letting them walk through your grid.

## What to watch for

**You are the exit liquidity in a sell-off.** Your buy levels absorb selling all the way down, and you end up holding tokens bought higher with less USDC. This is the main risk and it's structural, not avoidable.

**Liquidity is not price support.** A grid makes trading smoother. It cannot hold a price, and treasuries that try to defend one run out.

**Keep the reserve in a different asset.** An operating reserve in your own token fails at exactly the moment you need it.

**Related**

- [Market-making treasury](../../systems/market-maker.md) · [grid](../../strategies/trading/basic/grid.md)
- [OTC trading](otc-trading.md)
