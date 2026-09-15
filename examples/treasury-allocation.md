# Treasury allocation example

A 10,000 USDC treasury with roughly 1,300 a month in costs, divided so every part has a job.

| Allocation | Amount | State | Purpose |
|---|---:|---|---|
| Operating reserve | 4,000 | **Locked** | Three months of costs, out of reach |
| Portfolio | 2,000 | Committed | [Rebalancing](../catalog/strategies/portfolio/rebalancing.md), 60/40 ALGO/USDC |
| Trading inventory | 2,000 | Committed | [Grid](../catalog/strategies/trading/basic/grid.md) on ALGO/USDC |
| Lending | 1,000 | Deployed | [Idle capital](../catalog/strategies/lending/idle-capital.md) |
| Buffer | 1,000 | Available | Unexpected costs, top-ups |
| **Total** | **10,000** | | |

Keep ALGO separately for transaction fees and minimum balance — see [costs](../docs/overview/costs.md).

## How to set it up

1. **Lock the operating reserve first.** Before anything else is decided.
2. **Fund each strategy** with its own assets. The grid gets its 2,000; the portfolio gets its own.
3. **Choose where profits go** for each — your wallet, another strategy, or running costs.
4. **Deploy the lending allocation** last, with capital you're confident you won't need quickly.

## What this treasury can and can't do

**Available to spend right now:** 1,000. Not 10,000, and not 6,000.

**Available within days:** the 1,000 buffer plus the 1,000 in lending, once withdrawn and confirmed.

**Not available:** the locked reserve until you unlock it, and capital committed to strategies until you release it.

The grid cannot borrow from lending. The portfolio cannot dip into the reserve. Each runs out of its own money and stops — which is the entire point.

## Adjusting it

Rising costs mean a bigger reserve first, funded by reducing the trading or lending allocation. Falling costs free capital up, but confirm the trend before committing it.

Strategy profits can top up the buffer automatically rather than needing a decision each time. See [profit recycling](../catalog/strategies/portfolio/profit-recycling.md).

## Related

- [Reserve plus rebalancer](../catalog/systems/reserve-plus-rebalancer.md) — this shape, explained as a complete system
- [Trading plus lending](../catalog/systems/trading-plus-lending.md) — the larger version
- [Active versus idle capital](../catalog/use-cases/treasury/idle-capital-management.md) — sizing the reserve honestly
