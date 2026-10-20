"""Global hotkey listener — F1/F2/F3/F8 by default."""
from __future__ import annotations

import logging

log = logging.getLogger("belmont.hotkeys")

VK_MAP = {
    "F1": 0x70, "F2": 0x71, "F3": 0x72, "F4": 0x73,
    "F5": 0x74, "F6": 0x75, "F7": 0x76, "F8": 0x77,
}


def resolve_vk(key: str) -> int:
    if key not in VK_MAP:
        raise KeyError(f"unsupported hotkey: {key}")
    return VK_MAP[key]