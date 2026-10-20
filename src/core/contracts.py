"""Shared plugin contracts — every extension module implements these."""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class PluginContract(Protocol):
    name: str
    version: str

    def on_load(self, bus, settings) -> None: ...
    def tick(self) -> None: ...
    def on_unload(self) -> None: ...


@runtime_checkable
class MemoryReader(Protocol):
    def read_i32(self, address: int) -> int: ...
    def write_i32(self, address: int, value: int) -> None: ...
    def resolve_chain(self, base: int, offsets: list[int]) -> int: ...