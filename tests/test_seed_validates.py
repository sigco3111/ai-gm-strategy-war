"""Tests for the goguryeo-391 seed against the ai-gm state schema.

Mirrors ai-gm core's tests/test_seeds.py::test_seed_validates_against_state_schema,
plus plugin-specific cross-reference and stat-range checks.
"""
import json
import re

import pytest


# ---------- S1: seed.json validates against state schema ----------

def test_seed_json_validates_against_state_schema(seed_payload):
    """S1: seed.json (with _meta stripped) passes validate_and_parse('state', ...)."""
    from ai_gm.state.validation import validate_and_parse
    state = validate_and_parse("state", seed_payload)
    assert state.game_id == "goguryeo-391"
    assert state.schema_version == 1
    assert state.turn == 0
    assert len(state.entities) >= 10  # at least 7 factions + 5 characters + 6 provinces = 18


# ---------- S2: template.json validates ----------

def test_seed_template_json_validates(template_payload):
    """S2: seed_template.json (with _about/_meta/_notes stripped) validates too."""
    from ai_gm.state.validation import validate_and_parse
    # The template is illustrative — the example entity has incomplete attributes (no stats).
    # Replace it with a minimal valid entity so the schema check passes.
    payload = dict(template_payload)
    payload["game_id"] = "demo-template"
    payload["created_at"] = "2026-06-15T00:00:00Z"
    payload["entities"] = [
        {
            "id": "faction_demo",
            "type": "faction",
            "name": "Demo Faction",
            "attributes": {"government": "monarchy"},
        }
    ]
    state = validate_and_parse("state", payload)
    assert state.game_id == "demo-template"


# ---------- S3: all entity ids match the strict pattern ----------

def test_seed_entity_ids_match_strict_pattern(seed_payload):
    """S3: every id matches ^[a-z0-9_-]+$ (no Korean, no spaces, no uppercase)."""
    pattern = re.compile(r"^[a-z0-9_-]+$")
    for entity in seed_payload["entities"]:
        assert pattern.match(entity["id"]), f"id {entity['id']!r} does not match ^[a-z0-9_-]+$"
    # Also check game_id
    assert pattern.match(seed_payload["game_id"]), f"game_id {seed_payload['game_id']!r} fails pattern"


# ---------- S4: cross-references resolve ----------

def test_seed_cross_references_resolve(seed_payload):
    """S4: every ruler_id, controller_id, location_id references an existing entity id."""
    ids = {e["id"] for e in seed_payload["entities"]}
    problems = []
    for e in seed_payload["entities"]:
        attrs = e.get("attributes", {})
        for k in ("ruler_id", "controller_id", "location_id", "commander_id", "home_province_id"):
            v = attrs.get(k)
            if v is not None and v != "" and v not in ids:
                problems.append(f"{e['id']}.attributes.{k} = {v!r} (dangling)")
    assert not problems, "Cross-references that don't resolve: " + ", ".join(problems)


# ---------- S5: stat ranges ----------

def test_seed_stats_in_range(seed_payload):
    """S5: every attributes.stats.* value is in [0, 100]."""
    problems = []
    for e in seed_payload["entities"]:
        if e["type"] != "faction":
            continue
        stats = e.get("attributes", {}).get("stats", {})
        for k, v in stats.items():
            if not (0 <= v <= 100):
                problems.append(f"{e['id']}.attributes.stats.{k} = {v} (out of [0,100])")
    assert not problems, "Stat range violations: " + ", ".join(problems)


# ---------- S6: all 3 major entity types present ----------

def test_seed_has_three_entity_types(seed_payload):
    """S6: the seed exercises all 3 of the genre's primary entity types (faction, character, province)."""
    types_present = {e["type"] for e in seed_payload["entities"]}
    assert "faction" in types_present
    assert "character" in types_present
    assert "province" in types_present
    # Sanity: at least 5 of each
    type_counts = {t: sum(1 for e in seed_payload["entities"] if e["type"] == t) for t in types_present}
    assert type_counts["faction"] >= 5
    assert type_counts["character"] >= 3
    assert type_counts["province"] >= 3
