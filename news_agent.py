"""Compatibility wrapper for the actual script used by the daily workflow."""

from __future__ import annotations

from pathlib import Path
import runpy

if __name__ == "__main__":
    script = Path(__file__).with_name("news_Version2.agent")
    runpy.run_path(str(script), run_name="__main__")