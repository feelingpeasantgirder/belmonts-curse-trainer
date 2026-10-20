"""Discovers and loads plugin packages from a directory."""
from __future__ import annotations

import importlib
import inspect
import logging
from pathlib import Path

from src.core.contracts import PluginContract
from src.core.registry import PluginRegistry

log = logging.getLogger("belmont.loader")


class PluginLoader:
    def __init__(self, plugin_dir: Path, registry: PluginRegistry) -> None:
        self.plugin_dir = plugin_dir
        self.registry = registry
        self._discovered: list[str] = []

    def discover(self) -> list[str]:
        self._discovered = [
            p.name for p in self.plugin_dir.iterdir()
            if p.is_dir() and (p / "__init__.py").exists() and not p.name.startswith("_")
        ]
        log.info("discovered %d plugin packages", len(self._discovered))
        return self._discovered

    def load_all(self, bus, settings) -> None:
        for pkg in self._discovered:
            mod = importlib.import_module(f"src.plugins.{pkg}")
            for _, obj in inspect.getmembers(mod, inspect.isclass):
                if obj is not PluginContract and issubclass(obj, PluginContract) \
                        and obj.__module__.startswith("src.plugins"):
                    instance = obj()
                    instance.on_load(bus, settings)
                    self.registry.register(instance)