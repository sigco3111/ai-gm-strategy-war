# AI Game Master — Strategy / War (장르 플러그인)

> **장르 플러그인:** 중세~르네상스 시대의 턴제 그랜드 전략. 1개 국가의 통치자로서 내정·외교·전쟁을 벌이는 AI GM 시뮬레이션.
> **Genre plugin:** Turn-based grand strategy in the medieval-to-Renaissance era. You rule one nation; the AI GM operates the rest.

[![Genre](https://img.shields.io/badge/genre-strategy%20%2F%20war-red)](#장르-소개)
[![Depends on](https://img.shields.io/badge/depends%20on-ai--gm-blue)](#요구사항)
[![Status](https://img.shields.io/badge/status-MVP%20planning-yellow)](#로드맵)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](#라이선스)

---

## 🇰🇷 한국어 소개

### 이게 뭔가요?

이 저장소는 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) **장르 비종속 공통 엔진 위에 얹는 장르 플러그인**입니다. 공통 인프라(MCP 서버, 메모리, RAG, 검증)는 ai-gm에서 가져오고, 이 repo는 장르 콘텐츠만 담습니다:

- 기본 세계관 시드 — **알도리아 왕국, 1487년**
- 장르별 JSON 스키마 (nations / characters / wars / provinces / units)
- 그랜드 전략 톤에 맞춘 GM 시스템 프롬프트
- 샘플 lore (세력 / 지역 / 경제 / 법률 / 문화)
- 시작 가능한 캠페인 1개

플레이어는 **1개 국가**의 통치자. AI GM이 **다른 모든 국가·인물·세계 사건**을 운영합니다. 1턴 = 1계절, 무한 진행.

### 의존성

**반드시 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) 코어를 먼저 설치**하세요. 이 저장소만으로는 동작하지 않습니다.

```
ai-gm (공통 엔진) ← ai-gm-strategy-war (이 repo, 장르 1)
                  ← ai-gm-fantasy-rpg (장르 2, 예정)
                  ← ai-gm-sci-fi-explore (장르 3, 예정)
```

---

## 🇺🇸 English

### What is this?

This is a **genre plugin** for the [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) genre-agnostic engine. The core engine (MCP server, memory, RAG, validation) lives in `ai-gm`. This repo adds only genre-specific content:

- Default world seed — **Kingdom of Aldoria, year 1487**
- Genre-specific JSON schemas (nations, characters, wars, provinces, units)
- GM system prompt tuned for grand-strategy tone
- Sample lore (factions, regions, economy, law, culture)
- One playable starter campaign

The player rules **one nation**. The AI GM operates **all other nations, characters, and world events**. 1 turn = 1 season, infinite progression.

### Dependency

**You must first install [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) core.** This repo alone cannot run.

```
ai-gm (core engine) ← ai-gm-strategy-war (this repo, genre 1)
                  ← ai-gm-fantasy-rpg (genre 2, planned)
                  ← ai-gm-sci-fi-explore (genre 3, planned)
```

---

## 🌍 기본 시드: 알도리아 (1487) / Default Seed: Aldoria (1487)

기본 시드는 **엘리사벳 여왕**의 알도리아 왕국 옥좌에서 시작합니다. 북부 대륙의 200년 된 입헌군주국. 여섯 개의 라이벌 왕국, 두 개의 상인 공화국, 빛의 성기사단이 지도를 나눕니다.

The default seed drops you into the throne room of **Queen Elisabet** of the **Kingdom of Aldoria** — a 200-year-old constitutional monarchy in the northern continent. Six rival kingdoms, two merchant republics, and the Holy Order of Light share the map.

**시작 조건 / Starting conditions:**
- 국고 / Treasury: 12,400 골드 (보통) / 12,400 gold (modest)
- 군사 / Military: 상비 35,000명 + 징집 가능 80,000명 / 35,000 standing, 80,000 leviable
- 안정도 / Stability: 65/100 (남부 농민 폭동 위협) / 65/100 (peasant unrest in the south)
- 진행 중 국경 분쟁 1건 / One active border skirmish with the Khanate of Volgar
- 진행 중 혼인 제안 2건 / Two marriage proposals on the table

`start_game({era, tone, scale, ...})` MCP 도구로 시드를 덮어쓸 수 있습니다 — GM이 시대·톤·국가 선택을 안내합니다.

Override the seed via the MCP tool `start_game({era, tone, scale, ...})` — the GM will guide you through character/nation creation.

---

## 🧱 장르 엔티티 / Genre-Specific Entities

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

전체 스키마는 Phase 1에서 `schemas/`에 들어갑니다.

Full schema lives in `schemas/` (Phase 1).

---

## 🗂️ 저장소 구조 / Repository Structure

```
ai-gm-strategy-war/
├── lore/                       # 정적 세계관 (Git 추적)
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
│   ├── rules/                  # [CHUNK: rules] (기본 핀 고정)
│   │   ├── succession.md
│   │   ├── warfare.md
│   │   ├── diplomacy.md
│   │   └── economy.md
│   ├── culture.md              # [CHUNK: culture]
│   └── religion.md             # [CHUNK: culture]
│
├── schemas/                    # 장르 스키마 (Phase 1)
├── system_prompt.md            # GM 행동 규약
├── seed_template.json          # 플레이어 시드 템플릿
├── games/                      # (gitignored) 실제 진행 게임
│   └── .gitkeep
├── examples/                   # 샘플 트랜스크립트
│   └── turn-001-founding.jsonl
├── LICENSE
└── README.md
```

---

## 🚀 빠른 시작 / Quick Start (목표)

```bash
# 1. 코어 + 이 플러그인 클론 / Clone core + this plugin
git clone https://github.com/sigco3111/ai-gm.git
git clone https://github.com/sigco3111/ai-gm-strategy-war.git

# 2. 코어 설치 / Install core
cd ai-gm && pip install -e ".[dev]" && cd ..

# 3. MCP 서버를 에이전트에 등록 / Register MCP server
#    (OpenCode / Claude Code / Hermes 설정 — ai-gm/docs/ 참조)

# 4. 에이전트에게 / Tell your agent:
#    "Start a new game of ai-gm-strategy-war"
#    → GM이 시대·톤·국가 선택 안내 / GM walks you through setup
```

---

## 🎲 게임플레이 루프 / Gameplay Loop (per turn)

1. **플레이어 입력** — 자유 자연어 (예: "북쪽 고개에 5,000명 증원 보내" / "마레스와 혼인 동맹 제안")
2. **GM 컨텍스트 조회** — Tier 1 (최근 턴) + Tier 2 (활성 전쟁, 수정값) + Tier 3 (관련 lore RAG)
3. **GM 도구 호출** — `update_resource`, `move_unit`, `declare_war`, `advance_turn` 등
4. **GM 서술** — 도구 결과를 바탕으로 묘사, **절대 임의 숫자 ❌**
5. **턴 종료** — 트랜스크립트 저장, 필요 시 자동 요약 트리거

**No silent fixes.** 도구 실패 시 GM은 플레이어에게 정직하게 알리고 대기.

**No silent fixes.** If a tool fails, the GM tells the player honestly and waits for input.

---

## 🗺️ 로드맵 / Roadmap

| Phase | 범위 / Scope | 상태 / Status |
|-------|-------------|------------|
| **0. 계획** | 아키텍처, README, 시드 설계 | ✅ 진행 중 |
| **1. 세계관** | 6개 세력, 12명 인물, 20개 지역, 룰셋 | 🔜 다음 |
| **2. 스키마** | 장르별 JSON 스키마 (ai-gm 코어에 등록) | 🔜 다음 |
| **3. 샘플 플레이** | 50턴 진행 가능한 샘플 | ⏳ |
| **4. 이벤트 시스템** | GM이 위기·전쟁·계승 사건 자동 생성 | ⏳ |
| **5. NPC 자율성** | AI가 다른 국가 내부 결정을 운영 | ⏳ |

---

## 🎨 톤 & 영감 / Tone & Inspiration

저마법(low-fantasy) 정치 전략. 마법은 있지만 미묘합니다 — 궁정 점성술사, 전장 소문, 가끔 예언적 꿈. 파이어볼 ❌, 선택받은 자 ❌.

저마법 그랜드 전략 — Crusader Kings 3 + Europa Universalis 4 + 약간의 Hearts of Iron 4. 인물 중심 계승, 외교, 무역, 시대 진행.

**플레이어 권리가 최우선입니다.** GM은 플레이어 입력 없이 플롯을 진행하지 않습니다. 세계는 *반응*하지 *추진*하지 않습니다.

**No fireballs, no chosen ones.** Magic exists but is subtle — court astrologers, battlefield rumors, the occasional prophetic dream.

Low-fantasy grand strategy — Crusader Kings 3 + Europa Universalis 4 + a touch of Hearts of Iron 4. Character-driven succession, diplomacy, trade, era progression.

**Player agency is paramount.** The GM does not advance the plot without player input. The world *reacts*; it does not *push*.

---

## 📚 함께 보기 / See Also

- [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) — 공통 엔진 / shared engine
- [ai-gm-architecture.md](https://gist.github.com/sigco3111/) — 풀 디자인 문서 (한글) / full design doc (Korean)

## 📄 라이선스 / License

Apache 2.0 — see [LICENSE](LICENSE).
