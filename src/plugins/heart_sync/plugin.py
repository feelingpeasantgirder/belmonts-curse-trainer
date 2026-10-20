"""Infinite hearts + subweapon ammo sync."""
from __future__ import annotations

from src.core.contracts import PluginContract
from .offsets import HEART_COUNT, SUBWEAPON_AMMO


class HeartSyncPlugin(PluginContract):
    name = "heart_sync"
    version = "0.4.1"

    def __init__(self) -> None:
        self._bus = None
        self._enabled = False

    def on_load(self, bus, settings) -> None:
        self._bus = bus
        self._enabled = settings.hotkeys.get("toggle_infinite_hearts") == "F2"

    def tick(self) -> None:
        if not self._enabled or self._bus is None:
            return
        self._bus.write_i32(HEART_COUNT, 999)
        self._bus.write_i32(SUBWEAPON_AMMO, 99)

    def on_unload(self) -> None:
        self._enabled = False