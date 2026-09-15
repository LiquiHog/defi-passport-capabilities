# Token sale diversification

Finishing a raise with everything in one asset, and fixing that without crashing it.

A sale closes and the treasury is concentrated — often in the project's own token, or in whatever the raise was denominated in. Every month of operating costs is now a bet on one price. Diversifying is obviously right and obviously delicate, because selling fast moves the price and tells everyone you're selling.

## The setup

A project holding 500,000 USDC-equivalent, spending about 25,000 a month:

| Purpose | Amount | Approach |
|---|---|---|
| Runway — 18 months | 450,000 | Convert to stable, gradually |
| Long-term holdings | 30,000 | [Rebalancing](../../strategies/portfolio/rebalancing.md) |
| Working capital | 20,000 | Available |

The runway is the priority. Everything else waits until the project can survive eighteen months regardless of what any price does.

## Converting without a scene

Use [scheduled buying](../../strategies/trading/basic/dca.md) in reverse — a fixed amount converted at a regular interval, with a price floor so a bad day doesn't force a bad sale.

Spreading 450,000 across six months of weekly conversions is roughly 17,000 a week. That's absorbable in most markets, whereas the same amount at once is an event.

Set the floor deliberately. Too tight and the conversion stalls when you most need it; too loose and it's not protecting you. If the whole runway depends on the conversion completing, favour completing it.

## Adapting it

Lend the converted runway so it earns while it waits. See [idle capital](../../strategies/lending/idle-capital.md).

Post part of it as an [OTC block](../markets/otc-trading.md) if you can find a counterparty — no market impact at all.

Keep a modest allocation in the original asset if conviction is genuine. Just make sure it's the surplus, not the runway.

## What to watch for

**Diversifying is not disloyalty.** Projects that hold everything in their own token and fail during a drawdown didn't fail from lack of belief. Runway in a stable asset is what lets you keep building.

**Announced selling is worse than steady selling.** A visible, regular conversion is priced in quickly. An unexpected large one is not.

**Runway first, always.** A treasury that diversifies into a trading strategy before securing operating costs has swapped one concentration for another.

**Related**

- [Scheduled buying](../../strategies/trading/basic/dca.md) · [OTC trading](../markets/otc-trading.md)
- [Protocol treasury](../treasury/protocol-treasury.md)
