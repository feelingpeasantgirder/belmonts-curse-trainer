"""In-game overlay: hearts, HP, current whip tier."""
from __future__ import annotations

from rich.console import Console

from src.core.contracts import PluginContract
from src.plugins.heart_sync.offsets import HEART_COUNT

console = Console()


class OverlayWidget(PluginContract):
    name = "overlay"
    version = "0.2.2"

    def __init__(self) -> None:
        self._bus = None
        self._frames = 0

    def on_load(self, bus, settings) -> None:
        self._bus = bus
        self._enabled = settings.overlay_enabled

    def tick(self) -> None:
        self._frames += 1
        if self._frames % 60 != 0 or self._bus is None or not self._enabled:
            return
        hearts = self._bus.read_i32(HEART_COUNT)
        console.print(f"[dim]overlay[/] hearts={hearts}")

    def on_unload(self) -> None:
        self._enabled = False