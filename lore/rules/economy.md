# Economy Rules

> Genre-wide rules for resource production, treasury mechanics, and the food economy that keeps a realm alive.

## [CHUNK: rule -- Resource Production]
# triggers: production, yield, terrain, season, harvest
# priority: 7
A faction's `resources.{gold, food, iron}` change each turn (1 season) based on:

- **Province yields** — every `province` has `resource_yields.{gold, food, iron}` that contribute to the controlling faction's totals.
- **Terrain modifiers** — plains favor food, hills favor iron, mountains favor iron, coast favors trade (gold via fishing/ports).
- **Seasonal effects** — winter halves food production; spring/summer/autumn are full production. Iron and gold are less seasonal.
- **Stability multiplier** — when `stats.stability` is below 30, all production is halved (unrest disrupts work). When above 70, production is +20% (content population works harder).
- **Modifiers[]** — each entry in `faction.attributes.modifiers` can grant or subtract from a specific resource.

Per-season production is computed by a tool call (`update_resource` with `action="harvest"` or similar). The tool returns the new totals; the GM narrates.

## [CHUNK: rule -- Treasury Mechanics]
# triggers: treasury, gold, income, upkeep, deficit
# priority: 6
A faction's `resources.gold` is the treasury. Income sources:

- **Taxation** — gold proportional to population and `economy` stat. A `stats.economy` of 50 with a population of 1,000,000 yields ~50 gold per season.
- **Trade** — from trade agreements and merchant activity.
- **Tribute** — incoming tribute from vassals or client states.
- **War reparations** — one-time payments extracted after a successful war.

Upkeep expenses:

- **Military upkeep** — `military` stat × a constant (~5-10 gold per point per season). A `military` of 70 costs ~350-700 gold/season to maintain.
- **Court expenses** — flat ~50-100 gold/season for a monarchy.
- **Construction** — building fortress improvements, training new units, etc.
- **Tribute outflow** — outgoing tribute to a stronger neighbor or ally.

**Deficit** — if gold drops below 0, the faction suffers cascading consequences: mercenary desertions, court intrigue, vassal defection. The `economy` stat decays. The GM narrates the crisis and the player must find a solution (raise taxes, cut spending, take a loan, declare bankruptcy).

## [CHUNK: rule -- Food & Famine]
# triggers: food, famine, population, storage, harvest
# priority: 6
Food is the hard constraint. Without food, a realm dies.

- **Consumption** — each `province`'s population consumes food proportional to size. A province of 50,000 consumes ~5,000 food per season (a unit of food feeds ~10 people for a season).
- **Storage** — `faction.resources.food` carries over between seasons (no spoilage in this genre's abstraction; in a more realistic variant, food spoils above a storage cap).
- **Deficit** — if a province's food consumption exceeds its supply, the excess population dies or emigrates. `population` falls. `stability` falls. Famine events may fire (see `events`).
- **Surplus** — surplus food can be exported, fed to the military, or stockpiled. Faction-level food above 1.5× consumption is "secure" — it can sustain a year of bad harvest.
- **Plague** — a population under famine stress is more susceptible to plague. The `events` chunks can trigger this.

A player who ignores the food economy will watch their realm starve. The food balance is a forcing function — every other policy (war, expansion, building) ultimately serves or threatens it.
