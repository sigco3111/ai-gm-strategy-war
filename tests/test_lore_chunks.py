"""Tests for all lore markdown files in the strategy-war plugin.

Mirrors ai-gm core's tests/test_lore.py.
"""
from pathlib import Path

import pytest

from tests.conftest import PLUGIN_ROOT


def _all_md_files() -> list[Path]:
    """Discover every .md file under lore/ in the plugin."""
    return sorted((PLUGIN_ROOT / "lore").rglob("*.md"))


# ---------- S1: every rules .md produces valid chunks ----------

def test_all_rules_md_files_chunk():
    """S1: every lore/rules/*.md parses to ≥1 valid LoreChunk."""
    from ai_gm.lore.chunker import chunk_file
    rules_dir = PLUGIN_ROOT / "lore" / "rules"
    md_files = sorted(rules_dir.glob("*.md"))
    assert len(md_files) == 4, f"Expected 4 rule files (succession, warfare, diplomacy, economy), found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) >= 1, f"{path.name} produced 0 chunks"
        for c in chunks:
            assert c.type == "rule", f"{path.name} chunk '{c.name}' has type {c.type}, expected 'rule'"
            assert 1 <= c.priority <= 10, f"{path.name} chunk '{c.name}' has priority {c.priority}"


# ---------- S2: every seed .md produces valid chunks (where applicable) ----------

def test_all_seed_md_files_chunk():
    """S2: every lore/seeds/goguryeo-391/**/*.md parses to ≥1 valid LoreChunk (overview.md is exempt)."""
    from ai_gm.lore.chunker import chunk_file
    seed_dir = PLUGIN_ROOT / "lore" / "seeds" / "goguryeo-391"
    md_files = [p for p in sorted(seed_dir.rglob("*.md")) if p.name != "overview.md"]
    assert len(md_files) >= 5, f"Expected ≥5 seed .md files, found {len(md_files)}"
    for path in md_files:
        chunks = chunk_file(path)
        assert len(chunks) >= 1, f"{path.relative_to(PLUGIN_ROOT)} produced 0 chunks"
        for c in chunks:
            valid_types = {"character", "location", "faction", "event", "rule", "item", "misc"}
            assert c.type in valid_types, f"{path.name} chunk '{c.name}' has invalid type {c.type}"


# ---------- S3: every chunk has all required fields ----------

def test_all_chunks_have_required_fields():
    """S3: every chunk in every .md has type, name, content, triggers, priority all present and valid."""
    from ai_gm.lore.chunker import chunk_file
    for path in _all_md_files():
        if path.name == "overview.md":  # overview is free prose, not chunked
            continue
        for c in chunk_file(path):
            assert c.type, f"{path.name}: chunk missing type"
            assert c.name, f"{path.name}: chunk missing name"
            assert c.content, f"{path.name}: chunk '{c.name}' has empty content"
            assert isinstance(c.triggers, list), f"{path.name}: chunk '{c.name}' triggers not a list"
            assert 1 <= c.priority <= 10, f"{path.name}: chunk '{c.name}' priority {c.priority} out of range"


# ---------- S4: chunk names unique per file ----------

def test_no_duplicate_chunk_names_within_file():
    """S4: within any one .md file, no two chunks share the same name."""
    from ai_gm.lore.chunker import chunk_file
    for path in _all_md_files():
        if path.name == "overview.md":
            continue
        names = [c.name for c in chunk_file(path)]
        duplicates = {n for n in names if names.count(n) > 1}
        assert not duplicates, f"{path.relative_to(PLUGIN_ROOT)} has duplicate chunk names: {duplicates}"


# ---------- S5: chunk count is plausible ----------

def test_lore_chunk_count_is_substantial():
    """S5: the plugin has a substantial amount of lore (≥30 chunks across all files)."""
    from ai_gm.lore.chunker import chunk_file
    total = 0
    for path in _all_md_files():
        if path.name == "overview.md":
            continue
        total += len(chunk_file(path))
    assert total >= 30, f"Plugin has only {total} chunks; expected ≥30"
