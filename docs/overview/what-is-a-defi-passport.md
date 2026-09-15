# What is a DeFi Passport?

An account that holds money with instructions attached.

A normal wallet holds a balance. A passport holds a balance *and* knows what every part of it is for. Six thousand USDC is payroll, and nothing may touch it. Two thousand is inventory for a grid. Two thousand more buys ALGO every Monday. The passport keeps those apart itself — the grid cannot reach payroll, even if a bigger trade would suit it.

That is the whole idea. Everything else is detail.

## Money with a job

At any moment, every token in a passport is in one of three states:

| State | What it means |
|---|---|
| **Available** | Not spoken for. Assign it to something, or withdraw it. |
| **Committed** | Assigned to a rule. That rule can spend it; nothing else can. |
| **Locked** | Deliberately fenced off. No strategy and no automation can reach it until you unlock it. |

This is why a total balance tells you so little on its own. A treasury showing 10,000 USDC might have 400 genuinely free. The passport tracks the difference and refuses any action that would spend money belonging to something else — including your own withdrawal.

## You stay the owner

Only the owner can fund a rule, change it, release capital, or withdraw. Automation executes what you already approved; it cannot invent a new destination for your money, and it cannot pay itself more than the allowance you granted.

If you want out, you take the capital back. Cancelling a strategy returns its money to available. Closing the passport sweeps everything to your wallet. There is no notice period and no counterparty whose permission you need.

The protocol can also ship new versions without moving you. Your account, your balances and your rules stay where they are — there is no migration to perform and no moment where you are asked to send funds to a new address. See [staying in control](staying-in-control.md).

## From one rule to a treasury

A single scheduled buy is a complete, useful passport. So is a treasury running six strategies with a bot tuning them.

Start with a [strategy](../../catalog/strategies/README.md) if you want one behavior. Start with a [use case](../../catalog/use-cases/README.md) if you recognize your own situation in it. Start with a [system](../../catalog/systems/README.md) if you want the finished shape of a treasury.

Next: [what a passport can do](capabilities.md) · [how automation works](how-automation-works.md) · [what it costs](costs.md)
