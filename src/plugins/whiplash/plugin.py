"""Whip damage multiplier + Belmont movement tweaks."""
from __future__ import annotations

from src.core.contracts import PluginContract
from .offsets import WHIP_DAMAGE, MOVEMENT_SPEED


class WhiplashPlugin(PluginContract):
    name = "whiplash"
    version = "0.3.0"

    def __init__(self) -> None:
        self._bus = None
        self._multiplier = 3

    def on_load(self, bus, settings) -> None:
        self._bus = bus

    def set_multiplier(self, mult: int) -> None:
        self._multiplier = max(1, min(mult, 10))

    def tick(self) -> None:
        if self._bus is None:
            return
        base = self._bus.read_i32(WHIP_DAMAGE)
        if base and base < 1000:
            self._bus.write_i32(WHIP_DAMAGE, base * self._multiplier)
        self._bus.write_i32(MOVEMENT_SPEED, 180)

    def on_unload(self) -> None:
        self._bus = None