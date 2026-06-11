# AI Game Master — Strategy / War

> **장르 플러그인:** 중세~르네상스 시대의 턴제 그랜드 전략 게임. 1개 국가의 통치자로서 내정·외교·전쟁을 벌이는 AI GM 시뮬레이션.

[![Genre](https://img.shields.io/badge/genre-grand%20strategy-red)](#)
[![Depends on](https://img.shields.io/badge/depends%20on-ai--gm--core-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP%20planning-yellow)](#roadmap)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](#license)

---

## 🎮 What is this?

This is a **genre plugin** for [ai-gm-core](https://github.com/sigco3111/ai-gm-core). It bundles:

- A default world seed (Aldoria Kingdom, year 1487)
- Genre-specific JSON schemas (nations, characters, wars, provinces, units)
- GM system prompt tuned for grand-strategy tone
- Sample lore: factions, regions, economy, law, culture
- A playable starter campaign

The player rules **one nation**. The AI GM operates **all other nations, characters, and world events**. Every 1 turn = 1 season (Spring/Summer/Autumn/Winter), and the world keeps moving forward indefinitely.

---

## 🌍 World Seed: Aldoria (1487)

The default seed drops you into the throne room of **Queen Elisabet** of the **Kingdom of Aldoria** — a 200-year-old constitutional monarchy in the northern continent. Six rival kingdoms, two merchant republics, and the Holy Order of Light share the map.

**Starting conditions:**
- Treasury: 12,400 gold (modest)
- Military: 35,000 standing, 80,000 leviable
- Stability: 65/100 (peasant unrest in the south)
- One active border skirmish with the Khanate of Volgar
- Two marriage proposals on the table

You can override the seed via the MCP tool `start_game({era, tone, scale, ...})` — the GM will guide you through character/nation creation.

---

## 🏗️ Architecture (inherited from Core)

This plugin plugs into the shared ai-gm-core engine. The 3-tier memory, MCP tools, and state validation are all provided by the core. This repo only adds:

- `lore/` — world bible (chunks classified as faction / character / location / rules / economy / culture)
- `system_prompt.md` — GM ruleset for grand strategy (tone, diplomacy protocols, war resolution)
- `seed_template.json` — schema for player-chosen seeds
- `games/` (gitignored) — your actual playthrough data

See [ai-gm-core README](https://github.com/sigco3111/ai-gm-core) for the engine.

---

## 🧱 Genre-Specific Entities

```json
{
  "nations": {
    "kingdom-of-aldoria": {
      "ruler": "queen-elisabet",
      "government": "constitutional_monarchy",
      "stats": {"economy": 72, "military": 58, "stability": 65, "legitimacy": 80},
      "resources": {"gold": 12400, "food": 8500, "iron": 1200, "mana": 300},
      "modifiers": ["trade-boom", "plague-threat"]
    }
  },
  "characters": {
    "queen-elisabet": {
      "name": "Elisabet",
      "age": 34,
      "traits": ["paranoid", "charismatic"],
      "location": "capital-aldoria",
      "loyalty": 95
    }
  },
  "active_wars": [
    {
      "aggressor": "khanate-of-volgar",
      "defender": "kingdom-of-aldoria",
      "war_score": -8,
      "objectives": ["repel_invasion", "secure_north_pass"]
    }
  ]
}
```

Full schema in `schemas/` (planned for Phase 1).

---

## 🗂️ Repository Structure

```
ai-gm-strategy-war/
├── lore/                       # Static world bible
│   ├── overview.md             # [CHUNK: world_overview]
│   ├── factions/               # [CHUNK: faction]
│   │   ├── kingdom-of-aldoria.md
│   │   ├── khanate-of-volgar.md
│   │   ├── republic-of-mareth.md
│   │   └── ...
│   ├── characters/             # [CHUNK: character]
│   │   ├── queen-elisabet.md
│   │   ├── prince-aldric.md
│   │   └── ...
│   ├── regions/                # [CHUNK: location]
│   ├── rules/                  # [CHUNK: rules] (pinned by default)
│   │   ├── succession.md
│   │   ├── warfare.md
│   │   ├── diplomacy.md
│   │   └── economy.md
│   ├── culture.md              # [CHUNK: culture]
│   └── religion.md             # [CHUNK: culture]
│
├── system_prompt.md            # GM behavior ruleset
├── seed_template.json          # Player-chosen game seed
├── games/                      # (gitignored) actual playthroughs
│   └── .gitkeep
├── examples/                   # Sample transcripts
│   └── turn-001-founding.jsonl
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start (target)

```bash
# 1. Clone core + this plugin
git clone https://github.com/sigco3111/ai-gm-core.git
git clone https://github.com/sigco3111/ai-gm-strategy-war.git

# 2. Install core
cd ai-gm-core && pip install -e ".[dev]" && cd ..

# 3. Register MCP server with your agent
# (OpenCode / Claude Code / Hermes config — see ai-gm-core docs)

# 4. Open your agent and say:
#    "Start a new game of ai-gm-strategy-war"
#    The GM will walk you through era/tone/nation selection.
```

---

## 🎲 Gameplay Loop (per turn)

1. **Player input** — free-form natural language (e.g. "I send 5,000 troops to reinforce the North Pass" or "I propose a marriage alliance with Mareth")
2. **GM consults context** — Tier 1 (recent turns) + Tier 2 (active wars, modifiers) + Tier 3 (relevant lore via RAG)
3. **GM calls MCP tools** — `update_resource`, `move_unit`, `declare_war`, `advance_turn`, etc.
4. **GM narrates** — outcome based on tool results, never on invented numbers
5. **Turn ends** — transcript persisted, optional auto-summarization triggered

**No silent fixes.** If a tool fails, the GM tells the player honestly and waits for input.

---

## 🗺️ Roadmap

| Phase | Scope | Status |
|-------|-------|--------|
| **0. Planning** | Architecture, README, seed design | ✅ In progress |
| **1. World bible** | 6 factions, 12 characters, 20 regions, rules | 🔜 Next |
| **2. Schemas** | Genre-specific JSON schema for core | 🔜 Next |
| **3. Sample run** | 50-turn playable sample | ⏳ |
| **4. Event system** | GM generates crises, wars, succession events | ⏳ |
| **5. NPC autonomy** | AI runs other nations' internal decisions | ⏳ |

---

## 🎨 Tone & Inspiration

This is *not* a magic-and-dragons fantasy RPG. It's a **low-fantasy political strategy** game closer to:

- **Crusader Kings 3** — character-driven, succession, intrigue
- **Europa Universalis 4** — diplomacy, trade, era progression
- **Hearts of Iron 4** — industrial-era warfare (later expansion)

Magic exists but is subtle — court astrologers, battlefield rumors, the occasional prophetic dream. No fireballs, no chosen ones.

**Player agency is paramount.** The GM does not advance the plot without player input. The world reacts; it does not push.

---

## 📚 See Also

- [ai-gm-core](https://github.com/sigco3111/ai-gm-core) — shared engine
- [ai-gm-architecture.md](https://gist.github.com/sigco3111/) — full design doc (Korean)

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).
