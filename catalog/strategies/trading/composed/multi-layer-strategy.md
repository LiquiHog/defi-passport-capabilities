# Layered grids

Several grids at different price regions, so a bigger move still finds you trading.

A single [grid](../basic/grid.md) covers one range. Price leaves that range and the grid stops working. Layering grids over different regions keeps something active across a much wider move, without stretching one grid so thin that its levels stop being worth trading.

## How it works

ALGO at $0.18. Three grids, each with its own capital:

| Layer | Range | Capital | Spacing |
|---|---|---|---|
| Tight | $0.17–$0.19 | 1,000 USDC | $0.005 |
| Medium | $0.14–$0.22 | 2,000 USDC | $0.02 |
| Wide | $0.08–$0.28 | 2,000 USDC | $0.05 |

Normal conditions keep the tight layer busy with small frequent gains. A larger move quiets it and activates the medium layer. A major dislocation reaches the wide layer, which has been holding capital for exactly that.

## Adapting it

Weight by expectation — more capital in the tight layer if you expect range-bound conditions, more in the wide one if you expect volatility.

Give layers different profit destinations. The tight layer's frequent small gains might fund running costs while the wide layer compounds.

Let a controller activate and deactivate layers by market regime. See [volatility-controlled grid](../../externally-managed/volatility-controlled-grid.md).

## What to watch for

**Overlapping layers trade against each other.** At $0.18 both the tight and medium grids may want to act. Overlap isn't fatal, but understand you're doubling up in that region rather than diversifying.

**Three grids, three sets of fees.** The tight layer trades most and pays most. Make sure its gaps clearly exceed its costs.

**A trend still hurts all of them**, in sequence, as price works down through each range.

**Wide layers wait a long time.** Capital in the $0.08–$0.28 grid may sit untouched for a year.

**Related**

- [Grid](../basic/grid.md) · [asymmetric grid](../advanced/asymmetric-grid.md)
- [Multi-timescale](../advanced/multi-timescale.md)
