from __future__ import annotations

from typing import Iterator

from src.core.contracts import PluginContract


class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: dict[str, PluginContract] = {}

    def register(self, plugin: PluginContract) -> None:
        if plugin.name in self._plugins:
            raise ValueError(f"duplicate plugin: {plugin.name}")
        self._plugins[plugin.name] = plugin

    def get(self, name: str) -> PluginContract:
        return self._plugins[name]

    def items(self) -> Iterator[tuple[str, PluginContract]]:
        return iter(self._plugins.items())

    def __len__(self) -> int:
        return len(self._plugins)