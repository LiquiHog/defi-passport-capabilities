# Strategies

A strategy is one behavior with its own money. Fund it, set its conditions, and it runs on its own.

## [Trading](trading/README.md)

Grids, scheduled buying, take-profit ladders and orders. From a single rule to layered, multi-horizon setups.

## [Portfolio](portfolio/README.md)

| | |
|---|---|
| [Rebalancing](portfolio/rebalancing.md) | Hold a target mix as prices move it around |
| [Reserve management](portfolio/reserve-management.md) | Keep operating, investment and trading capital genuinely separate |
| [Core and satellite](portfolio/core-and-satellite.md) | Most capital conservative, a small slice adventurous |
| [Profit recycling](portfolio/profit-recycling.md) | Send gains where they compound instead of letting them sit |

## [Lending](lending/README.md)

| | |
|---|---|
| [Idle capital](lending/idle-capital.md) | Earn on cash you don't need this quarter |
| [Borrowing](lending/borrowing.md) | Raise cash without selling the position |
| [Lending plus trading](lending/lending-plus-trading.md) | A lending allocation alongside live trading inventory |
| [Lending plus rebalancing](lending/lending-plus-rebalancing.md) | Earn on the surplus while the liquid portion holds its mix |
| [Capital recycling](lending/capital-recycling.md) | Move capital between lending, reserves and strategies as needs change |

## [Counterparty](counterparty/README.md)

| | |
|---|---|
| [Passport-to-passport exchange](counterparty/passport-swap.md) | Trade directly with another treasury, all-or-nothing |

## [Externally managed](externally-managed/README.md)

Strategies a bot or an AI tunes for you, while the passport keeps enforcing your limits.

| | |
|---|---|
| [Volatility-controlled grid](externally-managed/volatility-controlled-grid.md) | Widen when choppy, tighten when calm |
| [Trend-aware allocation](externally-managed/trend-aware-allocation.md) | Shift the target mix as the trend changes |
| [Dynamic rebalancing](externally-managed/dynamic-rebalancing.md) | Rebalance on analysis rather than a fixed schedule |
| [Risk controller](externally-managed/risk-controller.md) | Cut exposure when limits are breached |
| [AI-managed allocation](externally-managed/ai-strategy-manager.md) | Hand treasury allocation to a model, inside guardrails |
| [AI strategy planner](externally-managed/strategy-compiler.md) | Turn a plain-language objective into funded rules |
