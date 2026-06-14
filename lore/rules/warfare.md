# Warfare Rules

> Genre-wide rules for declaring war, resolving battles, and sieging provinces. Pinned context.

## [CHUNK: rule -- War Declaration]
# triggers: war, declaration, casus belli, declare_war, diplomacy
# priority: 7
A war is *declared* through a structured diplomatic event, not by simply marching troops across a border. A valid declaration requires:

- **Casus belli** — a public justification (claim, treaty violation, religious offense, defensive response). Unjustified wars incur a `legitimacy` penalty with neutral third parties.
- **Notice** — the aggressor announces intent through formal channels (envoy, herald, public proclamation). Surprise attacks without notice carry severe reputation costs.
- **Target** — the defender must be a known faction. A side effect of `declare_war` is to set the aggressor's `diplomatic_relations[<defender_id>]` to a hostile value (typically ≤ -80).

The cost of declaring war is diplomatic, not material. The aggressor loses ~10-20 `legitimacy` with each neutral party per the war's perceived justness.

## [CHUNK: rule -- Battle Resolution]
# triggers: battle, combat, attack, defense, resolution, dice
# priority: 8
**No invented numbers.** Every battle is resolved by a tool call (`update_resource`, `advance_turn` with `action="attack"`) that the ai-gm core validates. The GM does NOT make up dice rolls, troop counts, or casualty figures in prose.

The general shape of a battle resolution:

1. **Composition** — the attacker and defender each have a force composition (infantry, cavalry, ranged) drawn from their `province` garrisons and `unit` formations.
2. **Modifiers** — terrain, general traits, supply state, fortification level, weather.
3. **Outcome** — the tool returns a structured result with casualties on each side, a winner, and a `morale` delta. The GM narrates the result; the tool produced the numbers.

If a tool fails (e.g. insufficient gold for mercenary hire), the GM tells the player honestly and waits for a new input. The "no silent fixes" rule applies here as everywhere.

## [CHUNK: rule -- Siege & Occupation]
# triggers: siege, occupation, garrison, fortress, capture
# priority: 6
A `province` may be besieged by a hostile force. The siege lasts until the garrison's `food` and `iron` (or equivalent supply) are exhausted, OR a relief force breaks the siege, OR the garrison surrenders.

- **Fortress level** — a province with a strong fortress (e.g. an `attributes.fortress` integer ≥ 5) can hold out for many seasons against a numerically superior foe.
- **Attrition** — a besieging force suffers attrition from disease, desertion, and supply shortages. The longer the siege, the worse the attrition.
- **Surrender** — the garrison may surrender if the besieger offers acceptable terms, if supplies are exhausted, or if a relief force fails to arrive after a "reasonable" timeout (typically 4-8 seasons for a well-fortified province).
- **Occupation** — after surrender, the province's `controller_id` is updated. Occupation carries ongoing costs (garrison, pacification) until the population accepts the new ruler or rises in rebellion.
