# Succession Rules

> Genre-wide rules for throne succession, inheritance, and the politics of who rules next. Pinned context — every game of strategy-war includes these chunks unless a seed explicitly overrides them.

## [CHUNK: rule -- Succession Types]
# triggers: succession, inheritance, heir, throne, claim
# priority: 7
A realm's succession type determines who inherits the throne when the current ruler dies. The five common types in this genre:

- **Primogeniture** — the eldest legitimate child inherits, regardless of gender if a succession law permits it. Stable, but produces weak heirs if the eldest is incompetent.
- **Gavelkind** — the realm is divided among all legitimate children. Frequent fragmentation, civil war, and small weak kingdoms.
- **Elective** — the realm's great nobles (or a council) elect the next ruler from among the late king's relatives. High court intrigue; a weak king can be deposed.
- **Tanistry** — a variant of elective: the electors choose from a single dynasty but not necessarily the late king's children. Common among tribal peoples.
- **Claim-based** — anyone with a blood claim may press it. The realm fragments, wars of succession follow, the strongest claimant wins.

A `faction.attributes.government` of `monarchy` typically pairs with one of the above; `tribe` typically pairs with `tanistry`; `republic` elects magistrates instead of kings.

## [CHUNK: rule -- Claim Fabrication]
# triggers: claim, fabrication, marriage, alliance, press claim
# priority: 6
A weak claim can be strengthened, and a strong claim can be manufactured:

- **Blood claim** — descent from a prior legitimate ruler. Stronger for closer generations.
- **Marriage claim** — marrying into a royal line grants a claim on that realm. Claims are often inherited by descendants.
- **Conquest claim** — holding a realm by force for a generation is itself a (weak) claim; it strengthens with each subsequent generation of unchallenged rule.
- **Fabrication** — genealogies can be forged, witnesses bribed, records altered. The GM may accept a fabrication if the player invests resources and time, but other courts will dispute it.

A claim is *pressed* through diplomacy (marriage, alliance), through war (casus belli), or through election (in elective realms). Pressing a weak claim without military backing is a recipe for humiliation.

## [CHUNK: rule -- Civil War Triggers]
# triggers: civil war, rebellion, pretender, faction split, unrest
# priority: 6
A realm slides toward civil war when:

- The heir's `loyalty` to the realm (as opposed to a faction) drops below ~30, AND a rival claimant with a strong claim exists.
- A powerful vassal's `legitimacy` toward the crown drops below ~25.
- A succession type produces multiple legitimate heirs of roughly equal status AND no clear primogeniture.
- A pretender backed by a foreign power (a strong claim, foreign troops) makes their move.

Once civil war erupts, the realm splits into 2+ factions, each headed by a claimant. The war is resolved like any other war (see warfare rules), but with the extra stakes of dynastic legitimacy.
