"""Shared pytest fixtures for strategy-war plugin tests."""
import json
from pathlib import Path

import pytest


PLUGIN_ROOT = Path(__file__).resolve().parent.parent
SEED_PATH = PLUGIN_ROOT / "lore" / "seeds" / "goguryeo-391" / "seed.json"
TEMPLATE_PATH = PLUGIN_ROOT / "seed_template.json"


@pytest.fixture
def plugin_root() -> Path:
    """The strategy-war plugin's repo root."""
    return PLUGIN_ROOT


@pytest.fixture
def seed_payload() -> dict:
    """The goguryeo-391 seed.json, parsed and _meta-stripped (the runtime payload)."""
    raw = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    return {k: v for k, v in raw.items() if not k.startswith("_")}


@pytest.fixture
def template_payload() -> dict:
    """The seed_template.json, parsed and _meta-stripped (the author template)."""
    raw = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
    return {k: v for k, v in raw.items() if not k.startswith("_")}


@pytest.fixture
def tmp_games_dir(tmp_path, monkeypatch):
    """Redirect ai-gm core's GAMES_DIR to a tmp dir for the test."""
    from ai_gm import paths
    games = tmp_path / "games"
    games.mkdir()
    monkeypatch.setattr(paths, "GAMES_DIR", games)
    return games
