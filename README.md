# DeFi Passport Capabilities

An on-chain account on Algorand that holds your ALGO and tokens — and runs your rules for them.

You fund a rule and set its conditions. The passport enforces those conditions on-chain every time it acts. Automation can execute your rules, but it can never move capital outside them. You can change a rule, pull the capital back, or close the account whenever you want.

## What a passport can do

- **Work a price range on its own** — buy low and sell high, over and over, from an inventory you cap up front. → [Grid](catalog/strategies/trading/basic/grid.md)
- **Buy on a schedule, with a floor** — a set amount every interval, and only if the price clears a minimum you choose. → [Scheduled buying](catalog/strategies/trading/basic/dca.md)
- **Earn on cash you aren't using** — lend the part of the treasury you don't need this quarter, keep the rest liquid. → [Idle capital](catalog/strategies/lending/idle-capital.md)
- **Raise cash without selling** — borrow against what you hold instead of closing the position. → [Borrowing](catalog/strategies/lending/borrowing.md)
- **Pay people automatically** — recipient, amount, interval, optional end date. Salaries, royalties, vesting, grants. → [Recurring payments](catalog/use-cases/commerce/recurring-payments.md)
- **Offer a trade another treasury can take** — post what you'll give and what you want. Settlement is all-or-nothing. → [Treasury-to-treasury exchange](catalog/strategies/counterparty/passport-swap.md)
- **Ring-fence your runway** — lock capital where no strategy and no automation can reach it until you release it. → [Staying in control](docs/overview/staying-in-control.md)
- **Take direction from a bot or an AI** — let software adjust your settings while the passport keeps enforcing your limits. → [External controllers](docs/advanced/external-controllers.md)
- **Send profits somewhere useful** — route a share of every gain to your wallet, into another strategy, or back into your running costs. → [Profit recycling](catalog/strategies/portfolio/profit-recycling.md)

## Start from what you want

| I want to… | Start here |
|---|---|
| Trade a range without watching it | [Grid](catalog/strategies/trading/basic/grid.md) → [asymmetric grid](catalog/strategies/trading/advanced/asymmetric-grid.md) |
| Build a position over months | [Scheduled buying](catalog/strategies/trading/basic/dca.md) → [selling into strength](catalog/strategies/trading/basic/take-profit.md) |
| Keep payroll safe from everything else | [Reserve management](catalog/strategies/portfolio/reserve-management.md) → [DAO treasury](catalog/use-cases/treasury/dao-treasury.md) |
| Earn on capital that's just sitting there | [Idle capital](catalog/strategies/lending/idle-capital.md) → [lending plus trading](catalog/strategies/lending/lending-plus-trading.md) |
| Handle money coming in from a project | [NFT sale proceeds](catalog/use-cases/commerce/nft/sale-proceeds.md) · [token sale](catalog/use-cases/commerce/token-sale-diversification.md) · [business revenue](catalog/use-cases/treasury/business-treasury.md) |
| Trade directly with another treasury | [Passport-to-passport exchange](catalog/strategies/counterparty/passport-swap.md) |
| Put a bot or an AI in charge of tuning | [Volatility-controlled grid](catalog/strategies/externally-managed/volatility-controlled-grid.md) → [AI-managed treasury](catalog/systems/autonomous-treasury.md) |

## Browse the library

- **[Strategies](catalog/strategies/README.md)** — single behaviors you can fund and run.
- **[Use cases](catalog/use-cases/README.md)** — what people actually use these for.
- **[Systems](catalog/systems/README.md)** — several strategies working as one treasury.
- **[Example plans](examples/README.md)** — real numbers you can adapt.

## How it fits together

A project might keep six months of payroll locked, run a small grid on a trading pair, buy into a long-term position every week, and lend whatever is left over. Each of those has its own money and its own rules. None of them can spend another one's capital.

A bot or an AI can sit on top and adjust the settings as conditions change. The passport still enforces the limits you set, so a bad signal can't spend money you didn't commit.

**New here?** Start with [what a passport is](docs/overview/what-is-a-defi-passport.md), then [how automation works](docs/overview/how-automation-works.md) and [what it costs](docs/overview/costs.md).

---

© 2026 LiquiHog. Licensed under [CC BY 4.0](LICENSE) — reuse and adapt with attribution.
