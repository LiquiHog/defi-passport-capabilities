# Asymmetric grid

A grid that reflects a view, instead of treating every price as equally interesting.

A plain [grid](../basic/grid.md) spreads inventory evenly. But you rarely feel evenly about every price. If you'd happily own a lot more ALGO at $0.14 and only reluctantly at $0.20, the grid should say so.

## How it works

Same structure as a normal grid, with uneven levels.

| Price | Buy size | Reasoning |
|---|---|---|
| $0.20 | 100 USDC | Near current price, small commitment |
| $0.18 | 200 USDC | Getting interesting |
| $0.16 | 400 USDC | Genuinely good value |
| $0.14 | 800 USDC | Would like to own a lot here |

The sell side can be shaped the same way — release inventory slowly into early strength, more freely higher up.

## Adapting it

Skew the spacing as well as the size. Wide gaps near the current price and tighter ones at the extremes concentrate your activity where you actually want it.

Shape only one side. An accumulating treasury might use heavy buys and light sells; one raising cash might do the reverse.

Let a bot reshape the weighting as conditions change — see [volatility-controlled grid](../../externally-managed/volatility-controlled-grid.md).

## What to watch for

**Your heaviest levels are your deepest drawdowns.** Weighting 800 USDC at $0.14 means your largest purchase happens in the worst conditions. That's intentional, but be honest that it's how it will feel.

**It's still a grid.** A sustained trend hurts it the same way, and the skew doesn't rescue that — it just changes where the damage lands.

**Complexity should earn its keep.** Four thoughtfully weighted levels beat twelve arbitrary ones. If you can't explain why a level is sized the way it is, it's noise.

**Related**

- [Grid](../basic/grid.md) · [reserve-backed grid](reserve-backed-grid.md)
- [Nonlinear accumulation](nonlinear-accumulation.md)
