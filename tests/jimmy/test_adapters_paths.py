"""Adapter workspace paths point at the real nested folders."""

from __future__ import annotations

from jimmy.adapters.ecc import EccAdapter
from jimmy.adapters.munder import MunderAdapter
from jimmy.adapters.openclaw import OpenClawAdapter
from jimmy.paths import repo_root, worker_root


def test_worker_roots_exist():
    assert (worker_root("openclaw") / "openclaw.mjs").exists() or (
        worker_root("openclaw") / "package.json"
    ).exists()
    assert (worker_root("munder") / "package.json").exists()
    assert (worker_root("ecc") / "scripts" / "ecc.js").exists()
    assert repo_root().name


def test_adapter_status_reports_real_workspaces():
    for cls in (OpenClawAdapter, MunderAdapter, EccAdapter):
        st = cls().get_status()
        assert st.workspace
        assert st.agent_id
        assert st.capabilities
