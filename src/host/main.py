"""Belmont's Curse Trainer — plugin host entrypoint."""
from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from rich.console import Console

from src.core.registry import PluginRegistry
from src.core.loader import PluginLoader
from src.core.memory_bus import MemoryBus
from src.config.paths import PLUGIN_DIR, CONFIG_FILE
from src.config.settings import load_settings

log = logging.getLogger("belmont.host")
console = Console()


class TrainerHost:
    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run
        self.settings = load_settings(CONFIG_FILE)
        self.bus = MemoryBus(process_name=self.settings.process_name, dry_run=dry_run)
        self.registry = PluginRegistry()
        self.loader = PluginLoader(PLUGIN_DIR, self.registry)

    async def boot(self) -> None:
        console.print(f"[bold red]Belmont's Curse Trainer[/] v{self._version()}")
        if not self.dry_run:
            self.bus.attach()
        self.loader.discover()
        self.loader.load_all(self.bus, self.settings)
        console.print(f"loaded [green]{len(self.registry)}[/] plugins")
        await self._serve()

    async def _serve(self) -> None:
        while True:
            await asyncio.sleep(0.5)
            for name, plugin in self.registry.items():
                try:
                    plugin.tick()
                except Exception as exc:  # noqa: BLE001
                    log.warning("plugin %s tick failed: %s", name, exc)

    @staticmethod
    def _version() -> str:
        from src import __version__
        return __version__


def cli() -> None:
    p = argparse.ArgumentParser(prog="belmonts-curse-trainer")
    p.add_argument("--dry-run", action="store_true", help="boot without attaching to the game")
    p.add_argument("--version", action="store_true")
    args = p.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(message)s")
    if args.version:
        print(TrainerHost._version())
        return
    asyncio.run(TrainerHost(dry_run=args.dry_run).boot())


if __name__ == "__main__":
    cli()