# Market-making treasury

Provide two-sided liquidity in your own token, with capital held back for when it's needed.

A token project wants a market people can actually trade in without paying for an external market maker or handing inventory to a third party. This runs it from a treasury you control.

## The allocation

A project with 100,000 USDC and 2,000,000 of its own token:

| Purpose | Amount | State |
|---|---|---|
| Operating reserve | 40,000 USDC | **Locked** |
| Active grid inventory | 30,000 USDC + 1,200,000 tokens | [Grid](../strategies/trading/basic/grid.md) across the working range |
| Replenishment reserve | 25,000 USDC + 800,000 tokens | Available, deliberately uncommitted |
| Buffer and running costs | 5,000 USDC + ALGO | Fees, minimum balance, flexibility |

Only 30% of the USDC is in the market at any time. The replenishment reserve is what lets you respond to a move you didn't plan for — see [reserve-backed grid](../strategies/trading/advanced/reserve-backed-grid.md).

## Shaping the grid

Two-sided, and usually asymmetric. Most projects are happier buying their token at low prices than selling it cheaply, so buy levels get more weight — see [asymmetric grid](../strategies/trading/advanced/asymmetric-grid.md).

Spacing is a real decision. Too tight and you churn fees against your own liquidity; too wide and the market looks thin. Start wider than feels right and tighten once you've seen real volume.

## Running it

**When price breaks the range**, decide rather than react: extend the grid, re-centre it, or leave it and wait. The replenishment reserve is what makes any of those possible.

**When inventory skews**, you're accumulating one side. Holding more of your own token after a fall is normal for a project; holding less after a rise is too. Watch the trend, not the snapshot.

**Let a bot handle spacing** if volatility varies a lot. See [volatility-controlled grid](../strategies/externally-managed/volatility-controlled-grid.md).

## What to watch for

**You are the exit liquidity in a sustained sell-off.** Your buy levels absorb selling pressure all the way down, leaving you holding tokens bought at higher prices with less USDC. Size the active grid at what you'd accept losing.

**Providing liquidity is not price support.** A grid makes trading smoother. It cannot hold a price, and trying to spend a treasury defending one is how treasuries end.

**Your own token isn't diversification.** The operating reserve should be in something else entirely, or a bad quarter takes both at once.

**Related**

- [Grid](../strategies/trading/basic/grid.md) · [asymmetric grid](../strategies/trading/advanced/asymmetric-grid.md)
- [Bounded market-making inventory](../use-cases/markets/market-making.md)
