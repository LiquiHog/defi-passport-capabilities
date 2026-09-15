# Nonlinear accumulation

Buy harder the further price falls.

A flat schedule buys the same amount whatever the price. But a 40% drawdown is a better opportunity than a 5% one, and your buying can say so. This is several [conditional accumulation](../basic/accumulation.md) rules, each funded separately, forming a deliberate curve.

## How it works

ALGO is at $0.20. Rather than one rule, you fund four:

| Trigger | Commitment |
|---|---|
| Below $0.18 | 200 USDC |
| Below $0.15 | 400 USDC |
| Below $0.12 | 800 USDC |
| Below $0.09 | 1,600 USDC |

A mild dip spends 200. A severe one eventually spends all 3,000, with most of it deployed at the lowest prices. Each rule holds its own capital, so the deep-drawdown money cannot be spent early by a shallower rule.

## Adapting it

Change the curve's steepness. Doubling at each step is aggressive; adding 50% is gentler and leaves more capital unspent in a moderate decline.

Cap the total. The curve is a shape, not a commitment to infinite capital — the deepest rule should hold an amount you'd accept losing entirely.

Combine with [scheduled buying](../basic/dca.md) so you're accumulating steadily as well as opportunistically.

## What to watch for

**The deepest rules trigger in the worst moments.** Your largest purchase happens when the asset is down 55% and the news is bad. If you'd override that in the moment, this strategy isn't for you.

**Deep rules may never fire.** In a market that drifts sideways, most of your capital sits committed and idle for a long time.

**There's no bottom guarantee.** Buying more at lower prices doesn't make the price stop falling. This shapes your average entry; it doesn't protect you.

**Related**

- [Conditional accumulation](../basic/accumulation.md) · [scheduled buying](../basic/dca.md)
- [Asymmetric grid](asymmetric-grid.md)
