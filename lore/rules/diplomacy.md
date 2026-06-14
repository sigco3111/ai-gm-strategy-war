# Diplomacy Rules

> Genre-wide rules for diplomatic relations, alliances, and non-violent state interactions.

## [CHUNK: rule -- Diplomatic Relations]
# triggers: diplomacy, relation, attitude, friendly, hostile, neutral
# priority: 7
Every pair of `faction` entities has a `diplomatic_relations[<other_faction_id>]` integer in `[-100, +100]`. The scale:

| Range | Disposition |
|-------|-------------|
| +80 to +100 | Ally — fights together by treaty |
| +40 to +79 | Friendly — favors in trade and minor disputes |
| +10 to +39 | Cordial — open to negotiation, leans positive |
| -9 to +9 | Neutral — no strong feeling, default starting point |
| -10 to -39 | Cold — disfavors, refuses routine requests |
| -40 to -79 | Hostile — actively opposes in third-party conflicts |
| -80 to -100 | At war or feud — military engagement is justified |

Relations drift slowly over time (typically ±1 per season without active events) and shift dramatically with events (alliances, betrayals, wars, marriages, religious changes).

## [CHUNK: rule -- Alliance Types]
# triggers: alliance, treaty, defensive, offensive, dynastic, marriage
# priority: 6
An `alliance` is a binding agreement between two or more factions. Common types:

- **Defensive** — the ally joins the war if either party is attacked. Does not require joining offensive wars.
- **Offensive** — the ally actively joins planned wars against a named target. Stronger commitment, more brittle if the target is tough.
- **Dynastic** — a marriage between royal houses, often combined with defensive or offensive terms. Carries succession consequences (see `succession.Claim Fabrication`).
- **Non-aggression** — both parties agree not to attack each other for a fixed term. Cheaper than full alliance; no military commitment.
- **Vassalage** — one party becomes a subordinate of the other, owing tribute and military service in exchange for protection and recognition.

Alliances can be broken — but at severe cost to the betrayer's `legitimacy` and `diplomatic_relations` with all other parties.

## [CHUNK: rule -- Tribute & Trade]
# triggers: tribute, trade, tariff, embargo, commerce
# priority: 5
Non-war economic interactions:

- **Tribute** — a weaker faction pays the stronger a fixed seasonal amount of `gold` (and sometimes `food` or `iron`) in exchange for protection or non-aggression. Recorded as a recurring `update_resource` event.
- **Trade agreement** — both parties reduce tariffs and grant market access. Effects: +5 to +15 `economy` for both, gradually. May be one-sided (e.g. "tribute + preferential terms") for asymmetric relationships.
- **Embargo** — a hostile faction cuts off trade. Effects: -10 to -20 `economy` on the target; small `legitimacy` loss for the embargoing party among neutral observers (embargoes hurt commoners).
- **Caravan rights** — permission for merchants to traverse a faction's territory. Effects: small `gold` income to the transit faction; `economy` boost to the trading faction.

Trade is one of the strongest diplomatic tools short of war. A trade embargo is a slow siege.
