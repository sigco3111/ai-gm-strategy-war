# Installation — ai-gm-strategy-war (장르 플러그인)

> **For LLM agents: Use `curl`, NOT WebFetch.** WebFetch summarizes content and loses critical details like env var names, file paths, MCP config snippets, and verification commands. Always use:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/sigco3111/ai-gm-strategy-war/main/INSTALL.md
> ```

The strategy-war plugin is a **content library** for the `ai-gm` core engine. It cannot run standalone; it requires the `ai-gm` core (with the `start_game_with_seed` MCP tool) to be installed. This doc covers the full setup.

---

## Editions

| Edition | What | Run | Lands on disk |
|---------|------|-----|----------------|
| **Core only** | `ai-gm` MCP server, no plugin | (see Step 2) | `ai-gm/` with 220 pytest passing |
| **Core + this plugin** | (recommended) | see below | both repos, `AI_GM_PLUGINS_DIR` set |
| **Core + multiple plugins** | core + 2+ plugins | see below | `AI_GM_PLUGINS_DIR` colon-separated |

Most users want **Core + at least one plugin**. The plugin alone is a content library, not a runnable server.

## For Humans

**Recommended: let an LLM agent install this for you.** Setup involves choosing an MCP client, cloning repos, setting env vars, and wiring up the MCP server. LLM agents can read this full guide and walk every step correctly.

### One-liner (LLM-agent install)

Paste this prompt into Claude Code, AmpCode, Cursor, or any LLM agent session:

```
Install and configure ai-gm-strategy-war by following the instructions at:
https://raw.githubusercontent.com/sigco3111/ai-gm-strategy-war/main/INSTALL.md
```

### Manual quick install (for the brave)

```bash
# 1. Install ai-gm core
git clone https://github.com/sigco3111/ai-gm.git
cd ai-gm && pip install -e ".[dev]" && cd ..

# 2. Clone this plugin
git clone https://github.com/sigco3111/ai-gm-strategy-war.git

# 3. Set plugin env var
export AI_GM_PLUGINS_DIR="$(pwd)/ai-gm-strategy-war"

# 4. Verify
cd ai-gm-strategy-war && PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
# Expect: 14 passed in ~0.4s
```

---

## For LLM Agents

> **CRITICAL: Use `curl` to fetch this file, NOT WebFetch.** WebFetch summarizes content and may drop the env var names, file paths, MCP config snippets, and verification commands that this guide depends on. Always use:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/sigco3111/ai-gm-strategy-war/main/INSTALL.md
> ```

If you are an LLM agent helping a user install `ai-gm-strategy-war`, walk them through the following steps **in order**. Ask the user any question whose answer you cannot infer.

### Step 0: Ask user which MCP client

The plugin requires an MCP-aware client. Ask which they want:

> "Which MCP client do you want to use? Pick one:
> 1. **OpenCode** — terminal AI coding agent (https://opencode.ai)
> 2. **Claude Code** — Anthropic's CLI for Claude
> 3. **Other** — specify the client name"

The user may also have multiple clients; if they do, repeat Step 5 for each one. If they don't know which, **OpenCode** is the recommended default.

### Step 1: Check prerequisites

The plugin needs Python 3.11+ and git. Run these checks:

```bash
python3 --version
# Expect: Python 3.11.x or higher (3.13 recommended)

git --version
# Expect: git version 2.x or higher
```

If either is missing or too old, install via the OS package manager before continuing.

| OS | Command |
|----|---------|
| macOS | `brew install python@3.13 git` (or use Xcode CLT for git) |
| Ubuntu/Debian | `sudo apt install python3.13 git` |
| Fedora/RHEL | `sudo dnf install python3.13 git` |
| Windows | `winget install Python.Python.3.13 Git.Git` |

### Step 2: Install ai-gm core (required dependency)

The core provides the MCP server, validation harness, memory pipeline, and the `start_game_with_seed` tool. Install it first.

```bash
# Choose a parent directory (the plugin will go alongside)
cd /path/to/your/projects  # or any directory

# Clone + install
git clone https://github.com/sigco3111/ai-gm.git
cd ai-gm
pip install -e ".[dev]"
cd ..
```

Verify the core's test suite passes:

```bash
cd ai-gm && python -m pytest -q
# Expect: 220 passed in ~15s
```

If the core's tests don't pass, the install is broken. **Stop and debug before continuing.** Common issues:
- `pip install -e ".[dev]"` failed silently — check pip output for errors
- `ModuleNotFoundError: No module named 'ai_gm'` — re-run pip install in the same venv
- Tests pass on a fresh venv but fail in your shell — make sure you're in the venv

The plugin is locked to ai-gm v0.4+ (which includes the `start_game_with_seed` tool). If you have an older ai-gm, the plugin's tests will fail with ImportError.

### Step 3: Install the strategy-war plugin

The plugin is a sibling directory. It ships the goguryeo-391 sample seed, 4 lore rule files, the GM contract, and 14 integration tests.

```bash
cd /path/to/your/projects  # same parent as ai-gm
git clone https://github.com/sigco3111/ai-gm-strategy-war.git
cd ai-gm-strategy-war
```

Verify the plugin's tests pass against the core:

```bash
PYTHONPATH="../ai-gm/src" python -m pytest tests/ -v
# Expect: 14 passed in ~0.4s
```

The 6 unit tests verify the seed validates against the core's state schema, all entity IDs match `^[a-z0-9_-]+$`, cross-references resolve, and stats are in range. The 5 lore tests verify the markdown chunks parse correctly. The 3 e2e tests verify the seed actually loads via `start_game_with_seed`, that `advance_turn` advances the state, and that `read_lore` returns a chunk.

If 14/14 pass, the plugin and core are correctly wired. If tests fail with `ModuleNotFoundError`, your `PYTHONPATH` is wrong — set it to the core's `src/` directory (the absolute path, not relative).

### Step 4: Set environment variables

The ai-gm core reads `AI_GM_PLUGINS_DIR` (colon-separated) to discover plugins. Multiple plugins are supported by separating paths with `:` (colon, no whitespace).

```bash
# Single plugin
export AI_GM_PLUGINS_DIR="/absolute/path/to/ai-gm-strategy-war"

# Multiple plugins
export AI_GM_PLUGINS_DIR="/path/to/ai-gm-strategy-war:/path/to/ai-gm-fantasy-rpg:/path/to/ai-gm-sci-fi-explore"
```

**Persist this in the user's shell profile** so future sessions inherit it:

| Shell | File | Command |
|-------|------|----------|
| zsh (macOS default) | `~/.zshrc` | `echo 'export AI_GM_PLUGINS_DIR="..."' >> ~/.zshrc` |
| bash (Linux default) | `~/.bashrc` | `echo 'export AI_GM_PLUGINS_DIR="..."' >> ~/.bashrc` |
| fish | `~/.config/fish/config.fish` | `set -gx AI_GM_PLUGINS_DIR "..."` |

Reload the profile: `source ~/.zshrc` (or the appropriate file).

You may also want to set `AI_GM_GAMES_DIR` to keep runtime games out of your project directory:

```bash
export AI_GM_GAMES_DIR="$HOME/.ai-gm-games"
mkdir -p "$AI_GM_GAMES_DIR"
```

### Step 5: Configure the MCP client

Pick the section that matches the user's answer from Step 0.

#### 5.1 OpenCode (recommended default)

File: `~/.config/opencode/mcp.json`

```json
{
  "mcpServers": {
    "ai-gm": {
      "command": "python",
      "args": ["-m", "ai_gm"],
      "cwd": "/absolute/path/to/ai-gm",
      "env": {
        "AI_GM_PLUGINS_DIR": "/absolute/path/to/ai-gm-strategy-war",
        "AI_GM_GAMES_DIR": "/absolute/path/to/your/games/dir"
      }
    }
  }
}
```

If the user is on Windows, replace `python` with the full path to the Python executable (e.g., `C:\\Python313\\python.exe`) and use double-backslashes in JSON paths.

#### 5.2 Claude Code

File: `~/.claude/mcp.json`

```json
{
  "mcpServers": {
    "ai-gm": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "ai_gm"],
      "cwd": "/absolute/path/to/ai-gm",
      "env": {
        "AI_GM_PLUGINS_DIR": "/absolute/path/to/ai-gm-strategy-war"
      }
    }
  }
}
```

#### 5.3 Other MCP clients

For any other stdio-based MCP client, the connection requires:
- **Command**: `python`
- **Args**: `["-m", "ai_gm"]`
- **CWD**: absolute path to the `ai-gm` repo (the one with `src/ai_gm/`)
- **Env**: `AI_GM_PLUGINS_DIR` set to the absolute plugin path

The server speaks JSON-RPC 2.0 over stdio. See [MCP spec](https://modelcontextprotocol.io/) for client integration.

### Step 6: Verify end-to-end with manual_qa

The ai-gm core ships a manual_qa script that exercises the full MCP server. It will start the server as a subprocess, send JSON-RPC requests, and verify all responses.

```bash
cd /absolute/path/to/ai-gm
python scripts/manual_qa.py 2>&1 | tee /tmp/manual_qa_phase4.log
# Expect: "ALL CHECKS PASSED (Phase 3 + Phase 4)"
# The script exits 0 on success
```

The script performs **13 round-trips**:
- 5 demo-001 round-trips (start_game, read_state, advance_turn, duplicate start_game error, etc.)
- 1 structured-error path (GAME_EXISTS)
- 4 Phase 2+3 tools (read_lore, search_history, end_session, read_state_history)
- **3 Phase 4 plugin round-trips** (`start_game_with_seed("goguryeo-391")` → `read_lore("Gungnae Seong")` → `advance_turn`)

If the script exits 0, the full stack works: core + plugin + MCP server + JSON-RPC. If it exits non-zero, scroll up in the log for the FATAL line.

### Step 7: First game prompt

Once verification passes, tell the user to send this to their LLM agent:

> "Start a new game of ai-gm-strategy-war with the goguryeo-391 seed"

The agent will call `start_game_with_seed("goguryeo-391")`, which returns:
- The state with 18 entities
- 23 lore chunks indexed
- A `_meta` block with the seed's metadata

The agent then enters the standard gameplay loop: `read_state` → narrate → `advance_turn` → repeat. The plugin's `system_prompt.md` tells the GM the 4 opening questions, the no-silent-fixes rule, and the pacing (1 turn = 1 season).

---

## Troubleshooting

### "Seed not found" error from `start_game_with_seed`

Causes (in order of likelihood):
1. `AI_GM_PLUGINS_DIR` is not set or doesn't point to the plugin
2. The plugin path is wrong (use absolute path, not `~`)
3. The seed directory structure is wrong — must be `<plugin>/lore/seeds/<seed_id>/seed.json`
4. The `seed.json`'s top-level `game_id` doesn't match the directory name

Debug:
```bash
echo "AI_GM_PLUGINS_DIR=$AI_GM_PLUGINS_DIR"
ls "$AI_GM_PLUGINS_DIR/lore/seeds/goguryeo-391/seed.json"
python3 -c "import json; d = json.load(open('$AI_GM_PLUGINS_DIR/lore/seeds/goguryeo-391/seed.json')); print('game_id =', d['game_id'])"
# Expect: game_id = goguryeo-391
```

### Tests fail in the plugin with `ModuleNotFoundError`

The 14 plugin tests require `PYTHONPATH` to point at the core's `src/` directory. Use the absolute path:
```bash
PYTHONPATH="/absolute/path/to/ai-gm/src" python -m pytest tests/ -v
```

### `manual_qa.py` exits non-zero

The script logs `FATAL: <message>` for the first failed check. Common causes:
- `AI_GM_PLUGINS_DIR` not exported when running the script — set it before running
- The strategy-war plugin isn't at the expected path — check `ls /path/to/ai-gm-strategy-war/`
- ai-gm core is older than v0.4 (missing `start_game_with_seed`) — re-pull and re-install

### MCP server doesn't start in the client

Try running the server manually to see stderr:
```bash
cd /path/to/ai-gm && python -m ai_gm
```

If it imports and waits silently on stdin, the server works — the issue is in the client's mcp.json config. Check:
- Absolute paths (not `~`)
- JSON syntax is valid (use `python -c "import json; json.load(open('mcp.json'))"`)
- The Python interpreter matches the one in the venv where you installed ai-gm

### "Validation failed" on the seed

Run the validation standalone:
```bash
PYTHONPATH="/path/to/ai-gm/src" python3 -c "
import json
from ai_gm.state.validation import validate_and_parse
with open('lore/seeds/goguryeo-391/seed.json') as f:
    raw = json.load(f)
state = validate_and_parse('state', {k: v for k, v in raw.items() if not k.startswith('_')})
print(f'OK: {len(state.entities)} entities')
"
```

If this fails, the seed has been corrupted (e.g., a Korean character in an `id` field, missing required key, or out-of-range stat). The plugin's own tests should have caught this — run them first.

### "I want a different sample seed"

Currently this plugin ships only the `goguryeo-391` seed. To use a different historical moment, create your own:

1. Copy `lore/seeds/_template/` to `lore/seeds/<your-seed-id>/`
2. Edit `seed.json` (use the goguryeo-391 seed as a template for the entity structure)
3. Add lore markdown files in `factions/`, `characters/`, `regions/` subdirectories
4. Run `PYTHONPATH=../ai-gm/src python -m pytest tests/ -v` — 14/14 must pass before committing

The `seed_id` format: lowercase letters, digits, `-`, `_` only. No spaces, no Korean, no dots.

---

## After install

- [README.md](README.md) — usage instructions, gameplay loop, roadmap
- [system_prompt.md](system_prompt.md) — the GM's behavior contract
- [schemas/README.md](schemas/README.md) — Option A schema mapping (rich → flat)
- [examples/turn-001-founding.jsonl](examples/turn-001-founding.jsonl) — sample first turn
- [tests/](tests/) — the 14-test integration suite
- The ai-gm core docs — `https://github.com/sigco3111/ai-gm`

## License

Apache 2.0 — see [LICENSE](LICENSE).
