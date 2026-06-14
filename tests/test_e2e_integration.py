"""End-to-end tests: load the goguryeo-391 seed into ai-gm core and exercise the full tool chain.

These tests require ai-gm to be installed (`pip install -e ../ai-gm` from this repo).
"""
import json
from pathlib import Path

import pytest

from tests.conftest import PLUGIN_ROOT


# ---------- S3 scenario: end-to-end start_game from the seed ----------

def test_e2e_start_game_from_seed_creates_state_file(tmp_games_dir, seed_payload):
    """S3: calling start_game_logic with the seed payload returns ok:true and persists state.json."""
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic

    store = StateStore(tmp_games_dir)
    result = start_game_logic(payload=seed_payload, store=store)

    assert result["ok"] is True, f"start_game failed: {result.get('error')}"
    assert result["game_id"] == "goguryeo-391"

    # State file must exist on disk
    state_file = tmp_games_dir / "goguryeo-391" / "state.json"
    assert state_file.exists(), f"state.json not written to {state_file}"
    on_disk = json.loads(state_file.read_text())
    assert on_disk["game_id"] == "goguryeo-391"
    assert len(on_disk["entities"]) == 18


# ---------- S4 scenario: first turn advances the state ----------

def test_e2e_advance_first_turn_succeeds(tmp_games_dir, seed_payload):
    """S4: a valid first-turn event (actor=character_gwanggaeto, action=custom) advances turn 0→1."""
    from ai_gm.state.store import StateStore
    from ai_gm.tools.start_game import start_game_logic
    from ai_gm.tools.advance_turn import advance_turn_logic

    store = StateStore(tmp_games_dir)
    start_result = start_game_logic(payload=seed_payload, store=store)
    assert start_result["ok"] is True

    # Construct a valid first-turn event
    event = {
        "event_id": "ev-e2e-001",
        "turn": 0,
        "actor_id": "character_gwanggaeto",
        "action": "custom",
        "payload": {"note": "First turn end — player inspects the southern border."},
        "reason": "E2E test: simulate the end-of-turn-0 event.",
    }
    result = advance_turn_logic("goguryeo-391", event, store)
    assert result["ok"] is True, f"advance_turn failed: {result.get('error')}"
    assert result["turn"] == 1

    # Audit entry should have been appended (Phase 3 T2.1)
    audit_file = tmp_games_dir / "goguryeo-391" / "audit.jsonl"
    if audit_file.exists():
        lines = audit_file.read_text().strip().splitlines()
        assert len(lines) >= 1, "Audit log should have at least one entry after advance_turn"


# ---------- S5 scenario: read_lore finds the Gungnae chunk ----------

def test_e2e_read_lore_finds_gungnae_chunk(tmp_games_dir, tmp_path):
    """S5: write a per-game lore/world.md containing the Gungnae chunk; read_lore returns it."""
    from ai_gm.lore.chunker import chunk_file
    from ai_gm.tools.read_lore import read_lore_logic

    # Set up: write the gungnae.md content to a per-game world.md (the path read_lore looks for)
    game_id = "gungnae-chunk-test"
    game_dir = tmp_games_dir / game_id
    game_dir.mkdir(parents=True, exist_ok=True)
    lore_dir = game_dir / "lore"
    lore_dir.mkdir(exist_ok=True)
    gungnae_src = PLUGIN_ROOT / "lore" / "seeds" / "goguryeo-391" / "regions" / "gungnae.md"
    lore_dir.joinpath("world.md").write_text(gungnae_src.read_text(encoding="utf-8"), encoding="utf-8")

    # Verify the chunk parses
    chunks = chunk_file(lore_dir / "world.md")
    assert len(chunks) >= 1
    gungnae_chunks = [c for c in chunks if c.name == "Gungnae Seong"]
    assert len(gungnae_chunks) == 1, f"Expected 1 Gungnae Seong chunk, found {len(gungnae_chunks)}"
    assert gungnae_chunks[0].type == "location"

    # Verify read_lore returns the chunk
    result = read_lore_logic(game_id=game_id, chunk_name="Gungnae Seong")
    assert result["ok"] is True, f"read_lore failed: {result.get('error')}"
    assert "Gungnae" in result.get("chunk", {}).get("content", "")
