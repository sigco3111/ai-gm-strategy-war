# Genre Schema Reference — Strategy / War

> **Why does this file exist?** The plugin's `README.md` §"장르 엔티티" describes a rich *nested* schema (`nations{}`, `characters{}`, `active_wars[]`). The ai-gm core's runtime contract is a *flat* array of entities (`entities[]`). This file documents the **Option A mapping** that bridges the two, so a new-seed author can think in the rich shape and still produce a `seed.json` that the core will accept.

---

## 1. Why flat?

The ai-gm core loads and saves `state.json` as a single flat `entities[]` array — every entity has the same shape (`id`, `type`, `name`, `attributes`) regardless of whether it's a faction, a character, or a province. The "no silent fixes" rule, the two-layer `validate_and_parse` harness, the `read_state` / `advance_turn` tools — they all assume this flat shape.

The plugin's README shows a richer *author-facing* shape (nested `nations{}`, `characters{}`, `active_wars[]`) because that's how a human naturally thinks about the world. But the *runtime contract* is flat.

**Option A** (this plugin's choice) means: each "nation" in the rich schema becomes a core `faction` entity, with the rich schema's `stats` / `resources` / `modifiers` fields living inside `attributes`. Each "character" becomes a core `character` entity. Each "war" lives as a derived structure inside `faction.attributes.diplomatic_relations` (a per-target integer in `[-100, +100]` representing war-score / disposition).

**Why not a transformation layer (Option B)?** It would require a Phase-4 `start_game` tool that translates the rich schema on every load. Option A keeps the runtime contract simple at the cost of mild verbosity in `seed.json`. We chose simplicity for Phase 1.

---

## 2. Mapping Table

| README rich schema | Core runtime entity |
|--------------------|---------------------|
| `nations.<id>.government` | `Entity(type="faction").attributes.government` |
| `nations.<id>.ruler` (a character id) | `Entity(type="faction").attributes.ruler_id` |
| `nations.<id>.stats.{economy, military, stability, legitimacy}` | `Entity(type="faction").attributes.stats.{economy, military, stability, legitimacy}` (each 0–100) |
| `nations.<id>.resources.{gold, food, iron}` | `Entity(type="faction").attributes.resources.{gold, food, iron}` (non-negative integers) |
| `nations.<id>.modifiers` (list of strings) | `Entity(type="faction").attributes.modifiers[]` |
| `nations.<id>.diplomatic_relations[<other_nation>]` | `Entity(type="faction").attributes.diplomatic_relations{<other_faction_id>: int}` (-100..+100) |
| `characters.<id>.name` | `Entity(type="character").name` |
| `characters.<id>.age` | `Entity(type="character").attributes.age` |
| `characters.<id>.traits` | `Entity(type="character").attributes.traits[]` |
| `characters.<id>.location` (a region id) | `Entity(type="character").attributes.location_id` |
| `characters.<id>.loyalty` | `Entity(type="character").attributes.loyalty` (0–100) |
| (no direct equivalent) | `Entity(type="province", id, name, attributes{population, controller_id, terrain, resource_yields})` |
| (no direct equivalent) | `Entity(type="unit", id, name, attributes{size, commander_id, location_id, home_province_id})` |
| `active_wars[]` array | derived from `faction.attributes.diplomatic_relations` (NOT a top-level entity); `war_score` lives as the integer value keyed by opponent id |

**Entities to use sparingly (Phase 1 doesn't require them):**
- `unit` — a military formation. Often expressed as a `faction.attributes.modifiers` entry or a `province.attributes.garrison` instead.
- `resource` — a single resource node (e.g. a specific mine). Can be folded into the parent `province`'s `resource_yields`.

---

## 3. ID Rules

Every `id` field — `game_id`, entity `id`, and any cross-reference (`ruler_id`, `controller_id`, `location_id`) — must match the strict pattern:

```
^[a-z0-9_-]+$
```

That is: lowercase letters, digits, hyphen, underscore only. No Korean, no spaces, no dots, no uppercase.

**Korean names belong in the `name` field.** Example: a faction representing Goguryeo should have:

```json
{
  "id": "faction_goguryeo",
  "type": "faction",
  "name": "고구려 (Goguryeo)"
}
```

The core's `Entity` model has `id: pattern=r"^[a-z0-9_-]+$"` enforced by Pydantic. A `seed.json` with a Korean id will fail validation. This is a hard rule.

---

## 4. Reserved Attribute Keys

These keys have *semantic meaning* — the loader and (eventually) the `start_game` MCP tool will read them, and the GM will use them to make decisions:

| Key | On entity type | Read by |
|-----|----------------|---------|
| `ruler_id` | `faction` | The GM to identify the current sovereign (e.g. for succession events) |
| `controller_id` | `province` | The GM to identify which faction owns a territory |
| `location_id` | `character`, `unit` | The GM to place a character on the map |
| `commander_id` | `unit` | The GM to identify who leads a military formation |
| `home_province_id` | `unit` | The GM to identify a unit's recruitment / supply origin |
| `government` | `faction` | The GM to apply the matching `succession` rule chunk |
| `stats.{economy, military, stability, legitimacy}` | `faction` | The GM to apply `warfare` / `economy` rule chunks |
| `resources.{gold, food, iron}` | `faction` | The GM to apply `economy` rule chunks |
| `diplomatic_relations{<faction_id>: int}` | `faction` | The GM to apply `diplomacy` rule chunks |
| `loyalty` | `character` | The GM to decide if a character defects, rebels, or remains loyal |
| `terrain` | `province` | The GM to apply movement cost / defensive bonuses |
| `traits[]` | `character` | The GM to flavor dialogue and decisions |

**Cross-reference validation**: every `ruler_id` / `controller_id` / `location_id` / `commander_id` / `home_province_id` MUST point to an existing entity id within the same `seed.json`. The core's `State` model does NOT enforce this (it stores ids as strings); the plugin's own `test_seed_validates.py::test_seed_cross_references_resolve` is the source of truth.

---

## 5. The `_meta` Field

`seed.json` files in this plugin carry a top-level `_meta` object:

```json
{
  "_meta": {
    "seed_name": "Goguryeo 391",
    "era": "Late 4th century CE",
    "tone": "realistic",
    "scale": "medium",
    "player_nation_id": "faction_goguryeo",
    "lore_overview": "overview.md",
    "game_start_date": "391 CE, Spring"
  },
  "game_id": "...",
  ...
}
```

The `_meta` field is **not** part of the ai-gm core's `state.json` contract — it is plugin metadata. **It must be stripped before passing to `start_game`.** The `seed_template.json` carries it as a hint to authors; the Phase-4 `start_game` tool (or a simple `del payload["_meta"]` before the call) will strip it.

The `seed_template.json` also carries `_about` (this README in JSON form) and `_notes` (authoring tips). Strip all three (`_about`, `_meta`, `_notes`) before validation.

---

## 6. What Lives Where

| File | Purpose | Validated by |
|------|---------|--------------|
| `seed.json` | The state payload. Strips `_meta`/`_about`/`_notes` → flat `state` for the core. | `validate_and_parse("state", ...)` |
| `*.md` under `lore/` | Genre world lore. Each `## [CHUNK: TYPE -- NAME]` becomes a `LoreChunk`. | `chunk_file(path)` from `ai_gm.lore.chunker` |
| `system_prompt.md` | The GM's behavior contract. Read once at session start. | (read by GM, not validated) |
| `_template/*` | Empty skeletons for new-seed authors. Not loaded by the engine. | (parity check vs `seed_template.json`) |
| `schemas/README.md` | This file. Not loaded by the engine. | (doc) |

---

## 7. The "No Silent Fixes" Invariant (carried over from ai-gm core)

If a `seed.json` violates any of the rules above, the engine MUST reject it. Specifically:

- The core's `start_game_logic` calls `validate_and_parse("state", payload)`. If any entity id fails the pattern, if `schema_version != 1`, if any required field is missing, the call returns `{"ok": false, "error": {"code": "schema_violation", "message": "..."}}`. The error must be surfaced to the player — never silently coerced.

- The plugin's `test_seed_validates.py` enforces the cross-reference and stat-range checks. If a check fails, the test fails loudly; the seed cannot ship.

A new-seed author who hits a validation error should fix the seed, not work around the validator.
