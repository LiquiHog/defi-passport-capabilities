# Example plans

Concrete numbers you can adapt, rather than percentages you have to interpret.

- **[Treasury allocation](treasury-allocation.md)** — a 10,000 USDC treasury divided across a locked reserve, a portfolio, trading inventory and lending.
- **[Grid plan](basic-grid.example.json)** — a worked grid allocation in JSON.

Every amount here is illustrative. Adapt the assets and the sizes to your own costs, and leave room for transaction fees and minimum balance — see [costs](../docs/overview/costs.md).

Maintainers can run `python examples/check_docs.py` from the repository root to check links, folder structure and JSON syntax. It checks the writing holds together; it doesn't check whether a plan is a good one.
