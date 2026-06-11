# AI Game Master — Strategy / War (장르 플러그인)

> **장르 플러그인:** 중세~근대 시대의 턴제 그랜드 전략. 1개 국가의 통치자로서 내정·외교·전쟁을 벌이는 AI GM 시뮬레이션.
> **Genre plugin:** Turn-based grand strategy in the medieval-to-early-modern era. You rule one nation; the AI GM operates the rest.

[![Genre](https://img.shields.io/badge/genre-strategy%20%2F%20war-red)](#🎮-새-게임을-시작하세요)
[![Depends on](https://img.shields.io/badge/depends%20on-ai--gm-blue)](#요구사항)
[![Status](https://img.shields.io/badge/status-MVP%20planning-yellow)](#로드맵)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](#라이선스)

---

## 🇰🇷 한국어 소개

### 이게 뭔가요?

이 저장소는 [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) **장르 비종속 공통 엔진 위에 얹는 장르 플러그인**입니다. 공통 인프라(MCP 서버, 메모리, RAG, 검증)는 ai-gm에서 가져오고, 이 repo는 장르 콘텐츠만 담습니다:

- 그랜드 전략 장르의 JSON 스키마 (nations / characters / wars / provinces / units)
- 그랜드 전략 톤에 맞춘 GM 시스템 프롬프트
- **시작 가능한 샘플 시드** (예: 고구려 391)
- **사용자 정의 시드**를 만드는 도구와 가이드
- 샘플 lore (세력 / 지역 / 경제 / 법률 / 문화)

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

- Genre-specific JSON schemas (nations, characters, wars, provinces, units)
- GM system prompt tuned for grand-strategy tone
- **Sample seeds** you can play right away (e.g. Goguryeo 391)
- **Tools & guides for crafting your own seed**
- Sample lore (factions, regions, economy, law, culture)

The player rules **one nation**. The AI GM operates **all other nations, characters, and world events**. 1 turn = 1 season, infinite progression.

### Dependency

**You must first install [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) core.** This repo alone cannot run.

```
ai-gm (core engine) ← ai-gm-strategy-war (this repo, genre 1)
                  ← ai-gm-fantasy-rpg (genre 2, planned)
                  ← ai-gm-sci-fi-explore (genre 3, planned)
```

---

## 🎮 새 게임을 시작하세요 / Start a New Game

> **시작할 때 미리 정해진 설정은 없습니다. 게임 시작 시 GM이 당신에게 물어보고, 당신이 결정합니다.**
>
> **Nothing is preset. When you start, the GM will ask you and you'll decide.**

GM이 먼저 던지는 질문은 단 하나 — **"어떤 게임을 플레이하시겠어요?"**

The GM opens with a single question — **"What kind of game do you want to play?"**

### 4가지 결정 사항 / Four Decisions

| # | 결정 / Decision | 옵션 (예시) / Options (examples) |
|---|---------|------|
| 1 | **시대** / **Era** | 고대(BC) → 중세(500~1500) → 르네상스(1500~1700) → 산업혁명(1700~1900) → 2차대전(1900~1945) → 근현대(1945~) |
| 2 | **톤** / **Tone** | 사실주의 / 저마법 / 신화·전설 / 디스토피아 / 코미디 / 다크 |
| 3 | **맵 규모** / **Map scale** | 소규모 (1국가 깊이, 10~30 지역) / 중규모 (5~10국, 50~150 지역) / 대규모 (20+국, 200+ 지역) |
| 4 | **당신의 국가** / **Your nation** | GM이 생성한 후보 중 선택 — 또는 직접 설계 |

**모르겠으면?** GM이 "추천 시나리오"를 제시하거나, 샘플 시드를 추천해줍니다.

**Don't know?** The GM will offer a "recommended scenario" or point you to a sample seed.

### 샘플 시드 (바로 시작 가능) / Sample Seeds (play immediately)

미리 만들어진 시드 중 골라도 됩니다 — 결정 4가지를 한 번에 단축:

| 시드 / Seed | 시대 / Era | 톤 / Tone | 규모 / Scale | 플레이어 국가 / Player nation |
|------|------|------|------|------|
| **고구려 391** (Goguryeo 391) | 4세기 후반 (삼국 시대 전기) | 사실주의 / 영토 확장 | 중규모 | 고구려 (광개토대왕 즉위 직후) |
| _(더 많은 샘플 시드 추가 예정)_ | | | | |

샘플 시드는 **그냥 시작점**입니다 — 본게임에 들어서면 톤·규칙·세력은 GM이 자유롭게 변주할 수 있어요.

Sample seeds are just **starting points** — once the game begins, the GM may freely riff on tone, rules, and factions.

### 직접 시드 만들기 (고급) / Craft Your Own Seed (advanced)

`lore/seeds/`에 직접 YAML/JSON을 작성해 완전히 새로운 세계를 던져줄 수도 있습니다. `seed_template.json`을 참고하세요.

You can also drop your own YAML/JSON into `lore/seeds/` to hand the GM a fully custom world. See `seed_template.json` for the schema.

---

## 🌰 샘플 시드 미리보기: 고구려 391 / Sample Seed Preview: Goguryeo 391

> **이건 *하나의 예시*일 뿐입니다. 위 "새 게임을 시작하세요" 섹션의 옵션으로 당신이 무엇이든 정할 수 있어요.**
>
> **This is *one* example. The "Start a New Game" section above lets you pick anything you want.**

391년, 고구려. **태왕(광개토대왕)** 이 즉위한 지 얼마 되지 않아 동방의 패권을 향한 질풍노도의 시기가 펼쳐집니다. 한반도에서 백제·신라·가야, 만주에서 후燕·선비, 바다 건너 왜국까지 — 오합지졸의 영토가 이제 제국의 서막을 올립니다.

The year 391. **Gwanggaeto the Great** has just ascended the throne of **Goguryeo** — and an era of storm and conquest begins. On the peninsula: Baekje, Silla, Gaya. In Manchuria: Former Yan and the Xianbei. Across the sea: Wa (Japan). What was once a small kingdom now stands at the threshold of empire.

**당신의 자리 / Your seat:** 고구려 왕좌 — 광개토대왕 시점. 

**Your seat:** the throne of Goguryeo — playing as Gwanggaeto the Great.

**시작 조건 / Starting conditions:**
- 왕조 / Dynasty: 고구려, 고국원왕 계승
- 군사 / Military: 30,000 중앙군 + 부족별 민병 50,000 (추가 징집 가능)
- 동맹 / Allies: 없음 (즉위 초기, 외교 재편 단계)
- 진행 중 위협 / Active threats: 전연의 만주 잔여 세력, 백제의 북진 압력, 동부여 내부 갈등
- 진행 중 기회 / Active opportunities: 신라와의 동맹 가능성, 왜국과의 해상 교류, 남하 정책

전체 시드 파일은 `lore/seeds/goguryeo-391/`에서 확인 (Phase 1 추가).

Full seed files in `lore/seeds/goguryeo-391/` (Phase 1).

---

## 🧱 장르 엔티티 / Genre-Specific Entities

> **이 스키마는 "플레이 가능한 모든 시나리오"의 공통 부분집합입니다.** 시드마다 일부 필드가 추가/오버라이드될 수 있습니다.
>
> **This schema is the common subset of all playable scenarios.** Individual seeds may add or override fields.

```json
{
  "nations": {
    "<nation_id>": {
      "ruler": "<character_id>",
      "government": "monarchy|republic|theocracy|tribe|empire|...",
      "stats": {"economy": 0-100, "military": 0-100, "stability": 0-100, "legitimacy": 0-100},
      "resources": {"gold": 0, "food": 0, "iron": 0, "mana": 0, "...": "..."},
      "modifiers": ["...", "..."]
    }
  },
  "characters": {
    "<character_id>": {
      "name": "...",
      "age": 0,
      "traits": ["...", "..."],
      "location": "<region_id>",
      "loyalty": 0-100
    }
  },
  "active_wars": [
    {
      "aggressor": "<nation_id>",
      "defender": "<nation_id>",
      "war_score": -100..+100,
      "objectives": ["...", "..."]
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
├── lore/                       # 정적 세계관 + 청크 (Git 추적)
│   ├── rules/                  # [CHUNK: rules] (장르 공통, 핀 고정)
│   │   ├── succession.md
│   │   ├── warfare.md
│   │   ├── diplomacy.md
│   │   └── economy.md
│   ├── seeds/                  # 시작 가능한 시드 모음 (각 시드 = 디렉토리)
│   │   ├── goguryeo-391/       # [CHUNK: seed]
│   │   │   ├── seed.json       # 시드 정의
│   │   │   ├── factions/
│   │   │   ├── characters/
│   │   │   ├── regions/
│   │   │   └── overview.md
│   │   └── _template/          # 새 시드 작성용 템플릿
│   └── _shared/                # 시드 간 공유되는 청크 (예: 공통 룰)
│
├── schemas/                    # 장르 스키마 (Phase 1)
├── system_prompt.md            # GM 행동 규약
├── seed_template.json          # 새 시드 작성 가이드
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
#    → GM이 "어떤 게임을 플레이하시겠어요?" 라고 물어봄
#    → The GM will ask "What kind of game do you want to play?"
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
| **0. 계획** | 아키텍처, README, 시드 시스템 설계 | ✅ 진행 중 |
| **1. 시드 시스템** | `seed_template.json` + `lore/seeds/goguryeo-391/` (샘플 1개) | 🔜 다음 |
| **2. 스키마** | 장르별 JSON 스키마 (ai-gm 코어에 등록) | 🔜 다음 |
| **3. 샘플 시드 2~3** | 시드 옵션 확장 (예: 제국崩壊 476, 산업혁명 영국 등) | ⏳ |
| **4. 시드 빌더 도구** | `start_game` MCP 도구 + 대화형 설정 UI | ⏳ |
| **5. 샘플 플레이** | 50턴 진행 가능한 샘플 | ⏳ |
| **6. NPC 자율성** | AI가 다른 국가 내부 결정을 운영 | ⏳ |

---

## 🎨 톤 & 영감 / Tone & Inspiration

저마법(low-fantasy) 정치 전략이 **기본 톤**이지만, 시드에서 다른 톤을 지정하면 GM이 그대로 따릅니다.

저마법 그랜드 전략 — Crusader Kings 3 + Europa Universalis 4 + 약간의 Hearts of Iron 4. 인물 중심 계승, 외교, 무역, 시대 진행.

**플레이어 권리가 최우선입니다.** GM은 플레이어 입력 없이 플롯을 진행하지 않습니다. 세계는 *반응*하지 *추진*하지 않습니다.

**Low-fantasy grand strategy is the *default* tone** — but if you pick a different tone in the seed, the GM follows your lead.

Low-fantasy grand strategy — Crusader Kings 3 + Europa Universalis 4 + a touch of Hearts of Iron 4. Character-driven succession, diplomacy, trade, era progression.

**Player agency is paramount.** The GM does not advance the plot without player input. The world *reacts*; it does not *push*.

---

## 📚 함께 보기 / See Also

- [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) — 공통 엔진 / shared engine
- [ai-gm-architecture.md](https://gist.github.com/sigco3111/) — 풀 디자인 문서 (한글) / full design doc (Korean)

## 📄 라이선스 / License

Apache 2.0 — see [LICENSE](LICENSE).
