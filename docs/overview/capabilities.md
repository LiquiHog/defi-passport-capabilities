# What a passport can do

Every row here is something you can fund today and let run.

## Trading

| | |
|---|---|
| **Work a price range** | Buy low and sell high across a range, repeatedly, from a capped inventory. Each level flips side after it fills. → [Grid](../../catalog/strategies/trading/basic/grid.md) |
| **Buy on a schedule** | A set amount every interval, and only if the price clears a minimum you set. → [Scheduled buying](../../catalog/strategies/trading/basic/dca.md) |
| **Sell into strength** | Standing sell orders at prices you choose, filled as the market reaches them. → [Take-profit](../../catalog/strategies/trading/basic/take-profit.md) |
| **Set a deadline** | Orders can expire on a date, and can be all-or-nothing or fill in pieces. → [Limit trading](../../catalog/strategies/trading/basic/limit-trading.md) |
| **Swap on demand** | Trade directly from the passport whenever you want, without setting up a strategy. → [Swapping on demand](../../catalog/strategies/trading/basic/swap.md) |

## Treasury

| | |
|---|---|
| **Hold a target mix** | Drift back to your intended allocation as prices move. → [Rebalancing](../../catalog/strategies/portfolio/rebalancing.md) |
| **Protect the runway** | Lock capital so no strategy and no automation can spend it. → [Reserve management](../../catalog/strategies/portfolio/reserve-management.md) |
| **Earn on idle cash** | Lend what you don't need this quarter; keep the rest liquid. → [Idle capital](../../catalog/strategies/lending/idle-capital.md) |
| **Borrow without selling** | Raise cash against your holdings instead of closing the position. → [Borrowing](../../catalog/strategies/lending/borrowing.md) |
| **Send profits somewhere** | Route a share of each gain to your wallet, another strategy, or your running costs. → [Profit recycling](../../catalog/strategies/portfolio/profit-recycling.md) |

## Payments and counterparties

| | |
|---|---|
| **Pay on a schedule** | Recipient, amount, interval, optional end date. ALGO or any Algorand token. → [Recurring payments](../../catalog/use-cases/commerce/recurring-payments.md) |
| **Split revenue** | Send fixed shares of incoming money to several recipients. → [Revenue splitting](../../catalog/use-cases/commerce/revenue-splitting.md) |
| **Trade with another treasury** | Post terms another passport can take. Both sides settle together or not at all. → [Passport-to-passport](../../catalog/strategies/counterparty/passport-swap.md) |
| **Deal over the counter** | Let a counterparty take the other side of a standing offer. → [OTC trading](../../catalog/use-cases/markets/otc-trading.md) |

## Automation and control

| | |
|---|---|
| **Run several strategies at once** | Each with its own money, its own rules, and no access to the others. → [Composition](strategies-and-composition.md) |
| **Hand tuning to software** | A bot or an AI adjusts settings; the passport still enforces your limits. → [External controllers](../advanced/external-controllers.md) |
| **Cap what automation may spend** | A time-limited allowance and a hard per-action ceiling. → [Staying in control](staying-in-control.md) |
| **Leave whenever** | Cancel a strategy, or close the passport and take everything back. → [Staying in control](staying-in-control.md) |
| **Keep working through upgrades** | The protocol ships new versions; your account, balances and rules stay where they are. → [Staying in control](staying-in-control.md#upgrades-dont-move-your-money) |

Different rules wait for different things before they act — see [how automation works](how-automation-works.md). For what this costs to run, see [costs](costs.md).
