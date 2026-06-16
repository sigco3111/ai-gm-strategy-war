"""Tests for the three-kingdoms-208 seed.

Mirrors the goguryeo-391 test pattern but isolated to a new file so
existing tests are not modified. Validates seed shape, entity counts,
lore file coverage, chunk regex, and an end-to-end start_game_with_seed.
"""
import json
import re
from pathlib import Path

import pytest


SEED_ID = "three-kingdoms-208"
SEED_DIR = Path(__file__).resolve().parent.parent / "lore" / "seeds" / SEED_ID


@pytest.fixture(scope="module")
def seed_payload() -> dict:
    raw = json.loads((SEED_DIR / "seed.json").read_text(encoding="utf-8"))
    return raw


def test_seed_json_loads_and_shape(seed_payload):
    assert seed_payload["game_id"] == SEED_ID
    assert seed_payload["schema_version"] == 1
    assert seed_payload["turn"] == 0
    assert seed_payload["created_at"].endswith("Z")
    assert isinstance(seed_payload["event_log"], list)


def test_entity_counts(seed_payload):
    factions = [e for e in seed_payload["entities"] if e["type"] == "faction"]
    characters = [e for e in seed_payload["entities"] if e["type"] == "character"]
    provinces = [e for e in seed_payload["entities"] if e["type"] == "province"]
    assert len(factions) == 7, f"expected 7 factions, got {len(factions)}"
    assert len(characters) == 5, f"expected 5 characters, got {len(characters)}"
    assert len(provinces) == 6, f"expected 6 provinces, got {len(provinces)}"


def test_lore_files_exist_per_entity(seed_payload):
    for entity in seed_payload["entities"]:
        eid = entity["id"]
        if entity["type"] == "faction":
            assert (SEED_DIR / "factions" / f"{eid}.md").exists(), f"missing {eid}.md"
        elif entity["type"] == "character":
            assert (SEED_DIR / "characters" / f"{eid}.md").exists(), f"missing {eid}.md"
        elif entity["type"] == "province":
            assert (SEED_DIR / "regions" / f"{eid}.md").exists(), f"missing {eid}.md"
    # overview.md
    assert (SEED_DIR / "overview.md").exists(), "missing overview.md"


def test_chunk_regex_matches_all_files():
    pattern = re.compile(
        r"^##\s*\[CHUNK:\s*([a-zA-Z0-9_]+)\s*(?:--|—|-)\s*([^\]]+?)\s*\]\s*$",
        re.MULTILINE,
    )
    md_files = sorted(list((SEED_DIR / "factions").glob("*.md")))
    md_files += sorted(list((SEED_DIR / "characters").glob("*.md")))
    md_files += sorted(list((SEED_DIR / "regions").glob("*.md")))
    md_files.append(SEED_DIR / "overview.md")
    assert len(md_files) == 19, f"expected 19 md files, found {len(md_files)}"
    for path in md_files:
        content = path.read_text(encoding="utf-8")
        assert pattern.search(content), f"{path.name}: no valid H2 [CHUNK: ...] header"


def test_each_chunk_has_triggers_and_priority():
    trigger_re = re.compile(r"^#\s*triggers:", re.MULTILINE)
    priority_re = re.compile(r"^#\s*priority:\s*\d+", re.MULTILINE | re.IGNORECASE)
    md_files = list((SEED_DIR / "factions").glob("*.md"))
    md_files += list((SEED_DIR / "characters").glob("*.md"))
    md_files += list((SEED_DIR / "regions").glob("*.md"))
    md_files.append(SEED_DIR / "overview.md")
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        assert trigger_re.search(text), f"{path.name}: missing '# triggers:' line"
        assert priority_re.search(text), f"{path.name}: missing '# priority:' line"


def test_start_game_with_seed_smoke(tmp_games_dir, seed_payload):
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic

    store = StateStore(tmp_games_dir)
    result = start_game_logic(payload=seed_payload, store=store)
    assert result["ok"] is True, f"start_game failed: {result.get('error')}"
    assert result["game_id"] == SEED_ID
    state_file = tmp_games_dir / SEED_ID / "state.json"
    assert state_file.exists()
    on_disk = json.loads(state_file.read_text())
    assert len(on_disk["entities"]) == 18
