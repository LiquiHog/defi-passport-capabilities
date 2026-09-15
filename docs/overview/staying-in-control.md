# Staying in control

Automation is only comfortable if you can bound it and undo it. Here is what a passport gives you.

## You are the owner

Funding a rule, changing it, releasing capital, and withdrawing are owner-only actions. Automation executes rules you already approved. It cannot create a new destination for your money, redirect a payment, or withdraw to itself.

## Lock what must not move

You can lock an amount of any token. Locked capital is invisible to every strategy and to automation, and it won't leave in a withdrawal either. It stays locked until you release it — nothing expires it and nobody else can touch it.

This is the simplest way to protect a runway. Lock six months of payroll and the rest of the treasury can trade, lend and rebalance without any chance of reaching it.

## Cap what automation may spend

Two separate limits, both yours:

- **An allowance with an expiry.** You grant the automation service an amount it may draw for transaction costs, and a date after which that permission lapses. It renews only if you renew it.
- **A per-strategy ceiling.** Each strategy carries its own cap on what it may consume, so one busy strategy can't drain the budget the others rely on.

The protocol also enforces a hard upper bound per action, independently of what you set.

## Take the capital back

| You want to | What happens |
|---|---|
| Pause a rule | Release its funding. The rule stays configured, with nothing to spend. |
| Stop a strategy | Cancel it. Every rule's funding returns to available and any capital it held is released. |
| Take money out | Withdraw. The passport checks that the amount isn't committed elsewhere first. |
| Leave entirely | Close the passport. Every token and the remaining ALGO go back to your wallet. |

Closing requires no notice and no counterparty's permission. Settle or close any open lending position first, since that capital sits outside the passport until it returns.

## Upgrades don't move your money

The protocol can ship new versions, and a passport can follow them in place — it picks up the current components and continues. Your account, your balances and your rules stay where they are. There's no migration to perform and no window where you're asked to move funds to a new address.

Version changes are owner-authorized and gated: a passport only moves to a version the protocol has actually published.

## What you're still trusting

Being straight about this is worth more than a reassurance:

- **The contract itself.** Your rules are only as good as the code enforcing them.
- **The venues trades route through.** A trade needs someone on the other side, at a price you'll accept.
- **Lending protocols**, for anything you deposit or borrow against. That capital follows their rules, not the passport's.
- **Price feeds**, where a strategy uses one.
- **Availability.** If nothing submits your transactions, rules wait. They don't fail or lose capital — they just don't run.

Next: [what it costs](costs.md) · [how automation works](how-automation-works.md)
