"""Thin wrapper over pymem with a dry-run backend for tests."""
from __future__ import annotations

import logging
import struct

log = logging.getLogger("belmont.bus")


class MemoryBus:
    def __init__(self, process_name: str, dry_run: bool = False) -> None:
        self.process_name = process_name
        self.dry_run = dry_run
        self._pm = None
        self._base = 0

    def attach(self) -> None:
        if self.dry_run:
            log.info("dry-run: skipping attach to %s", self.process_name)
            return
        import pymem  # local import so dry-run works without the dep
        self._pm = pymem.Pymem(self.process_name)
        self._base = self._pm.base_address
        log.info("attached to %s @ 0x%x", self.process_name, self._base)

    def read_i32(self, address: int) -> int:
        if self.dry_run or self._pm is None:
            return 0
        return struct.unpack("<i", self._pm.read_bytes(address, 4))[0]

    def write_i32(self, address: int, value: int) -> None:
        if self.dry_run or self._pm is None:
            log.debug("dry-run write 0x%x = %d", address, value)
            return
        self._pm.write_int(address, value)

    def resolve_chain(self, base: int, offsets: list[int]) -> int:
        addr = self.read_i32(base)
        for off in offsets[:-1]:
            addr = self.read_i32(addr + off)
        return addr + offsets[-1]