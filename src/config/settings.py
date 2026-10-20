from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Settings:
    process_name: str = "CastlevaniaBelmontsCurse.exe"
    game_build: str = "1.4.2"
    overlay_enabled: bool = True
    hotkeys: dict[str, str] = field(default_factory=dict)


def load_settings(path: Path) -> Settings:
    if not path.exists():
        return Settings()
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return Settings(**data)