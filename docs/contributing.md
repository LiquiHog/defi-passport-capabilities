# Contributing

The goal of every page is that a reader finishes it knowing something they can actually do.

## Where things go

| | |
|---|---|
| `catalog/strategies/` | One behavior, funded and running |
| `catalog/use-cases/` | A person or project in a situation |
| `catalog/systems/` | Several strategies working as one treasury |
| `docs/` | How the underlying capabilities work |
| `examples/` | Concrete plans with real numbers |

One idea per file, named descriptively. Create a folder only when it groups several genuinely related pages, and give it a `README.md` that says what's inside.

## How to write

**Outcome first.** Open with what the reader gets, then how it works. "Buy low and sell high, repeatedly, from an inventory you cap up front" — not "trade a pair through repeating legs at fixed quantities".

**Real numbers.** Actual tickers and actual amounts. 1,000 USDC buying ALGO at $0.15, not "1,000 quote units with an output condition".

**No hedging.** Avoid "supported", "eligible" and "compatible" as qualifiers. They make capabilities sound provisional and tell the reader nothing. If something works, say so; if it has a limit, name the limit.

**Explain jargon or drop it.** Say "levels" not "cells", "sides" not "legs". Expand anything unavoidable on first use. Infrastructure names — keepers, routers — belong in the guides, not in a recipe.

**Risks get their own section.** Collect them at the end under a clear heading rather than scattering them through the explanation where they undercut it. Be specific: "a sustained trend leaves you holding a falling asset" is useful; "market conditions may affect performance" is not.

**Be honest about the hard parts.** A page that makes something sound effortless is less trustworthy than one that names the two decisions you have to get right.

See the [writing prompts](../assets/templates/README.md) for the three page shapes.

## Keeping it accurate

Describe behavior the contract actually has. Don't generalize a capability from one strategy type to another — cooldowns, price feeds and expiry don't apply uniformly, and saying they do will mislead someone into funding something that won't work.

When you're unsure whether a capability exists, ask rather than hedging the language. A hedged sentence and a wrong sentence are equally unhelpful; a question gets it right.

## Before you submit

Run the checker from the repository root:

```
python examples/check_docs.py
```

It validates local links, folder structure and JSON syntax. It does not check whether your prose is any good or your economics make sense — read the page back as someone encountering the idea for the first time.
