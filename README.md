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

The README's rich nested `nations{}` / `characters{}` / `active_wars[]` shape is the **author-facing** representation. The runtime contract is the **flat `entities[]`** shape defined by `ai-gm`'s `schemas/state.json` (see [schemas/README.md](schemas/README.md) for the full Option-A mapping).

**Quick mapping:**
- Each "nation" → a `faction` entity with `attributes.{government, ruler_id, stats, resources, modifiers, diplomatic_relations}`
- Each "character" → a `character` entity with `attributes.{age, traits, location_id, loyalty}`
- Each "war" → encoded as a per-target integer in `faction.attributes.diplomatic_relations[<other_faction_id>]` (-100..+100, war_score)

> Full schema lives in [schemas/README.md](schemas/README.md). The runtime contract lives in [`sigco3111/ai-gm/schemas/state.json`](https://github.com/sigco3111/ai-gm/blob/main/schemas/state.json).

---

## 🗂️ 저장소 구조 / Repository Structure

```
ai-gm-strategy-war/
├── lore/                                  # 장르 콘텐츠 (Git 추적)
│   ├── rules/                             # [CHUNK: rules] (장르 공통, 핀 고정)
│   │   ├── succession.md                  # 3 chunks: succession types, claims, civil war
│   │   ├── warfare.md                     # 3 chunks: war declaration, battle, siege
│   │   ├── diplomacy.md                   # 3 chunks: relations, alliances, trade
│   │   └── economy.md                     # 3 chunks: production, treasury, food/famine
│   ├── seeds/                             # 시작 가능한 시드
│   │   ├── goguryeo-391/                  # 샘플 시드 1 (고구려 391, 광개토대왕 즉위)
│   │   │   ├── seed.json                  # state-shape 페이로드 (18 entities, validates)
│   │   │   ├── overview.md                # 1-page narrative intro
│   │   │   ├── factions/                  # 4 markdown files (goguryeo, baekje, yan, neighbors)
│   │   │   ├── characters/                # 3 markdown files (gwanggaeto, advisors, rivals)
│   │   │   └── regions/                   # 3 markdown files (gungnae, korean_peninsula, manchuria)
│   │   └── _template/                     # 새 시드 작성용 스켈레톤
│   │       ├── seed.template.json
│   │       └── overview.template.md
│   └── _shared/                           # 시드 간 공유 청크 (예: 공통 룰)
│
├── schemas/                               # Genre-Specific Schema Reference
│   └── README.md                          # Option A: rich → flat entity 매핑 문서
│
├── system_prompt.md                       # GM 행동 규약 (10 sections, 119 LOC)
├── seed_template.json                     # 새 시드 작성을 위한 정형 계약
├── games/                                 # (gitignored) 실제 진행 게임 디렉토리
│   └── .gitkeep
├── examples/                              # 샘플 트랜스크립트
│   └── turn-001-founding.jsonl            # 12-line JSONL (user→GM→tool_call→tool_result 시퀀스)
│
├── tests/                                 # 14 pytest (TDD)
│   ├── conftest.py                        # tmp_games_dir fixture
│   ├── test_seed_validates.py             # 6 tests: state schema, ID pattern, cross-refs, stats
│   ├── test_lore_chunks.py                # 5 tests: chunking, required fields, no dupes
│   └── test_e2e_integration.py            # 3 tests: start_game, advance_turn, read_lore end-to-end
│
├── LICENSE
└── README.md
```

---

## 🚀 사용법 (with ai-gm core) / Usage (with ai-gm core)

### 0. 사전 요구사항 / Prerequisites

- **Python 3.11+** (3.13 권장 / recommended)
- **ai-gm 코어 v0.4+** (`start_game_with_seed` 도구 포함) — [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm)
- **이 플러그인** — `ai-gm-strategy-war` (이 repo)
- (선택 / optional) **MCP 클라이언트** — OpenCode, Claude Code, Hermes 중 하나

### 1. 설치 / Installation

```bash
# 1.1. 클론 / Clone both repos side by side
git clone https://github.com/sigco3111/ai-gm.git
git clone https://github.com/sigco3111/ai-gm-strategy-war.git
cd ai-gm-strategy-war

# 1.2. ai-gm 코어 설치 (editable 모드, dev 의존성 포함) / Install core
cd ../ai-gm
pip install -e ".[dev]"
cd ../ai-gm-strategy-war

# 1.3. 의존성 확인 / Verify dependencies
python -c "from ai_gm.state.validation import validate_and_parse; print('ai-gm OK')"
python -m pytest tests/ -v   # 14/14 should pass
```

> **왜 14 테스트인가?** 이 플러그인은 콘텐츠 라이브러리입니다. ai-gm 코어가 진실의 출처(source of truth)이고, 우리는 그 위에 얹는 콘텐츠가 코어의 계약을 위반하지 않는지 검증합니다. 14 테스트가 정확히 그 검증(시드 검증 + 청크 검증 + end-to-end 시드 부팅 검증)을 합니다.

### 2. 환경 변수 설정 / Environment variables

ai-gm 코어가 `AI_GM_PLUGINS_DIR`을 읽어 이 플러그인을 찾습니다. (선택) 임시 게임 디렉토리도 분리할 수 있습니다.

```bash
# 2.1. 플러그인 위치 노출 / Expose plugin location (colon-separated for multiple plugins)
export AI_GM_PLUGINS_DIR="$(pwd)"

# 2.2. (선택) 실제 진행 게임을 별도 디렉토리에 보관 / Keep runtime games in a separate dir
export AI_GM_GAMES_DIR="$HOME/.ai-gm-games"
mkdir -p "$AI_GM_GAMES_DIR"
```

> **여러 플러그인 동시 사용** — 공백 없는 콜론(`:`)으로 구분:
> ```bash
> export AI_GM_PLUGINS_DIR="/path/to/ai-gm-strategy-war:/path/to/ai-gm-fantasy-rpg"
> ```

### 3. MCP 서버 기동 / Start the MCP server

```bash
# 3.1. ai-gm 코어 디렉토리에서 (플러그인 환경변수 상속)
cd ../ai-gm
python -m ai_gm
# 이제 FastMCP 서버가 stdin/stdout JSON-RPC로 대기 중
```

서버는 8개 도구를 노출합니다:

| 도구 | 용도 | 이 플러그인과의 관련 |
|------|------|----------------|
| `start_game` | state-shape 페이로드로 게임 시작 | (레거시) 직접 페이로드 주입 |
| **`start_game_with_seed`** | **시드 ID로 게임 시작** | **← 이 플러그인의 권장 진입점** |
| `read_state` | 현재 게임 상태 조회 | 매 턴 사용 |
| `advance_turn` | 이벤트로 상태 변경 + 턴 진행 | 매 턴 사용 |
| `end_session` | Tier 1 → Tier 2 → Tier 3 압축 | 챕터 종료 시 |
| `read_lore` | 청크 단위로 세계관 조회 | `lore/seeds/goguryeo-391/**/*.md`의 청크 |
| `search_history` | Tier 3 RAG 검색 | 과거 유사 사건 |
| `read_state_history` | 상태 변경 audit 로그 조회 | (Phase 3) |

### 4. 게임 시작 / Start a game (MCP JSON-RPC 예시)

#### 4.1. 시드 ID로 시작 (권장) — `start_game_with_seed`

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "start_game_with_seed",
    "arguments": {
      "seed_id": "goguryeo-391"
    }
  }
}
```

**응답:**
```json
{
  "ok": true,
  "game_id": "goguryeo-391",
  "state": { "game_id": "goguryeo-391", "turn": 0, "entities": [ ... 18 entities ... ] },
  "seed_meta": {
    "seed_name": "Goguryeo 391",
    "era": "Late 4th century CE (Three Kingdoms prelude)",
    "tone": "realistic",
    "player_nation_id": "faction_goguryeo"
  },
  "lore_files_indexed": 6,
  "lore_chunks_indexed": 23,
  "world_md_path": "/.../goguryeo-391/lore/world.md"
}
```

**동작:**
1. 코어가 `AI_GM_PLUGINS_DIR`을 스캔
2. `<plugin>/lore/seeds/goguryeo-391/seed.json`을 찾음
3. `_meta`, `_about`, `_notes` 키 제거 (코어 스키마가 모르는 키)
4. `validate_and_parse("state", payload)`로 검증 → 18 entities
5. `store.create("goguryeo-391", state)`로 디스크에 저장
6. Tier 1 (verbatim buffer) + Tier 3 디렉토리 초기화
7. `<plugin>/lore/rules/*.md` + `<plugin>/lore/seeds/goguryeo-391/**.md`를 `<game_dir>/lore/world.md`로 결합
8. 23 청크가 `read_lore`/`search_history`로 즉시 조회 가능

#### 4.2. 직접 페이로드로 시작 (레거시) — `start_game`

코어 1.x와의 호환성. `seed.json`을 직접 읽어 `_meta` 키를 직접 제거한 후:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "start_game",
    "arguments": {
      "payload": { /* the seed.json content with _meta stripped */ }
    }
  }
}
```

> **권장하지 않는 이유**: 시드 ID 한 개로 충분한 작업을 100+ 라인의 페이로드 + `_meta` 수동 제거로 확장. `start_game_with_seed`를 쓰세요.

### 5. 첫 턴 플레이 / Play the first turn

`start_game_with_seed`가 성공한 후, `read_state`로 현재 상태를 읽고, `advance_turn`으로 첫 이벤트를 제출:

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "read_state",
    "arguments": { "game_id": "goguryeo-391" }
  }
}
```

```json
{
  "jsonrpc": "2.0",
  "id": 5,
  "method": "tools/call",
  "params": {
    "name": "advance_turn",
    "arguments": {
      "game_id": "goguryeo-391",
      "event": {
        "event_id": "ev-founding-001",
        "turn": 0,
        "actor_id": "character_gwanggaeto",
        "action": "diplomacy",
        "payload": {
          "target_faction_id": "faction_silla",
          "treaty_type": "defensive",
          "gifts": ["10_gold", "5_iron"]
        },
        "reason": "Founding action: open diplomatic channel with Silla."
      }
    }
  }
}
```

GM은 도구 결과를 받아 서술로 풀어냅니다. **임의 숫자 금지** — `treasury`, `casualties`, `diplomacy_reputation` 같은 값은 모두 도구 호출 결과에서 와야 합니다.

### 6. OpenCode / Claude Code / Hermes에서 사용 / Using with AI agents

#### OpenCode
```json
// ~/.config/opencode/mcp.json
{
  "mcpServers": {
    "ai-gm": {
      "command": "python",
      "args": ["-m", "ai_gm"],
      "cwd": "/path/to/ai-gm",
      "env": {
        "AI_GM_PLUGINS_DIR": "/path/to/ai-gm-strategy-war",
        "AI_GM_GAMES_DIR": "/path/to/your/games/dir"
      }
    }
  }
}
```

#### Claude Code
```json
// ~/.claude/mcp.json
{
  "mcpServers": {
    "ai-gm": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "ai_gm"],
      "cwd": "/path/to/ai-gm",
      "env": {
        "AI_GM_PLUGINS_DIR": "/path/to/ai-gm-strategy-war"
      }
    }
  }
}
```

에이전트 시작 시 이렇게 말하세요:
> "Start a new game of ai-gm-strategy-war with the goguryeo-391 seed"

에이전트는 코어의 `start_game_with_seed`를 호출하여 게임을 부팅하고, 이후 `read_state` → `advance_turn` 사이클을 돌립니다.

### 7. 수동 QA (개발자용) / Manual QA (for developers)

```bash
# ai-gm 코어의 수동 QA 스크립트 — 이 플러그인도 자동으로 exercise함
cd ../ai-gm
python scripts/manual_qa.py 2>&1 | tee /tmp/manual_qa_phase4.log
```

이 스크립트는 **13 round-trips**를 수행합니다:
- 5개 (Phase 1) demo-001 round-trips
- 1개 구조화된 오류 (GAME_EXISTS)
- 4개 (Phase 2+3) 도구: read_lore, search_history, end_session, read_state_history
- **3개 (Phase 4) 플러그인 round-trips**: `start_game_with_seed("goguryeo-391")` → `read_lore("Gungnae Seong")` → `advance_turn`

`ALL CHECKS PASSED (Phase 3 + Phase 4)`가 보이면 정상.

### 8. 자신만의 시드 작성 / Author your own seed

`lore/seeds/_template/`을 복사해 시드 디렉토리 하나를 만들고, 4가지를 채우면 됩니다:

```
lore/seeds/<your-seed-id>/
├── seed.json              # state-shape JSON (schema_version=1, entities)
├── overview.md            # 자유 형식 (chunk 헤더 없어도 됨)
├── factions/              # [CHUNK: faction -- <name>] 형식
├── characters/             # [CHUNK: character -- <name>] 형식
└── regions/               # [CHUNK: location -- <name>] 형식
```

**필수 검증 (run this before committing):**
```bash
cd ../ai-gm-strategy-war
PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
# 14/14 pass = good to commit
```

**종족(magic systems), 경제 자원, 전쟁 등**을 추가하려면 `lore/rules/`에 새 청크 파일을 추가하세요. `seed_id` 형식:
- ASCII 소문자 + 숫자 + `-` + `_` 만
- 한국어 이름은 반드시 `name` 필드에 (id에 한국어 금지)
- 예: `goguryeo-391`, `baekje-396`, `rome-476`, `industrial-england-1850`

### 9. 디버깅 팁 / Debugging tips

- **시드를 못 찾을 때** — `AI_GM_PLUGINS_DIR`이 올바른지 확인, `<plugin>/lore/seeds/<seed_id>/seed.json`이 존재하는지 확인, `seed.json`의 `game_id`가 디렉토리 이름과 일치하는지 확인
- **검증 실패** — pytest의 `test_seed_validates.py`로 정확한 위반 사항을 찾을 수 있음
- **lore 청크가 안 보일 때** — `seed.json`의 `game_id`와 요청한 `seed_id`가 일치하는지 확인 (대소문자 구분)
- **청크 포맷 오류** — `## [CHUNK: TYPE -- NAME]` H2 헤더, TYPE은 `character|location|faction|event|rule|item|misc` 중 하나

### 10. 통합 테스트 / Running the integration tests

```bash
cd ../ai-gm-strategy-war
PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
```

**예상 출력:**
```
tests/test_seed_validates.py::test_seed_json_validates_against_state_schema PASSED
tests/test_seed_validates.py::test_seed_template_json_validates PASSED
tests/test_seed_validates.py::test_seed_entity_ids_match_strict_pattern PASSED
tests/test_seed_validates.py::test_seed_cross_references_resolve PASSED
tests/test_seed_validates.py::test_seed_stats_in_range PASSED
tests/test_seed_validates.py::test_seed_has_three_entity_types PASSED
tests/test_lore_chunks.py::test_all_rules_md_files_chunk PASSED
tests/test_lore_chunks.py::test_all_seed_md_files_chunk PASSED
tests/test_lore_chunks.py::test_all_chunks_have_required_fields PASSED
tests/test_lore_chunks.py::test_no_duplicate_chunk_names_within_file PASSED
tests/test_lore_chunks.py::test_lore_chunk_count_is_substantial PASSED
tests/test_e2e_integration.py::test_e2e_start_game_from_seed_creates_state_file PASSED
tests/test_e2e_integration.py::test_e2e_advance_first_turn_succeeds PASSED
tests/test_e2e_integration.py::test_e2e_read_lore_finds_gungnae_chunk PASSED
14 passed in 0.35s
```

14개 모두 통과하면 이 플러그인은 ai-gm 코어와의 계약을 100% 지킵니다.

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
| **0. 계획** | 아키텍처, README, 시드 시스템 설계 | ✅ 완료 |
| **1. 시드 시스템** | `seed_template.json` + `lore/seeds/goguryeo-391/` (샘플 1개) + 14 tests | ✅ 완료 (10 커밋) |
| **2. 스키마** | 장르별 JSON 스키마 — 코어의 `start_game_with_seed`로 통합됨 | ✅ 완료 (ai-gm 코어 Phase 4) |
| **3. 샘플 시드 2~3** | 시드 옵션 확장 (예: 제국崩壊 476, 산업혁명 영국 등) | ⏳ 다음 |
| **4. 시드 빌더 도구** | `start_game_with_seed`는 ✅ 완료. 대화형 설정 UI는 ⏳ | ⏳ 부분 |
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

### 의존성 / Dependencies
- [`sigco3111/ai-gm`](https://github.com/sigco3111/ai-gm) — **공통 엔진** (이 플러그인이 의존). v0.4+는 `start_game_with_seed` 도구 포함.

### 형제 플러그인 / Sibling plugins
- [`sigco3111/ai-gm-fantasy-rpg`](https://github.com/sigco3111/ai-gm-fantasy-rpg) — 판타지 RPG (드래곤 시대 1024)
- [`sigco3111/ai-gm-sci-fi-explore`](https://github.com/sigco3111/ai-gm-sci-fi-explore) — SF 탐험 (인류 진출기 2247)
- [`sigco3111/ai-gm-mystery-detective`](https://github.com/sigco3111/ai-gm-mystery-detective) — 미스터리/탐정 (하버튼 저택 1923)

### 디자인 참조 / Design references
- [ai-gm-architecture.md](https://gist.github.com/sigco3111/) — 풀 디자인 문서 (한글) / full design doc (Korean)

## 📄 라이선스 / License

Apache 2.0 — see [LICENSE](LICENSE).
