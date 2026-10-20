"""Standalone offset scanner — run against a live game process."""
from __future__ import annotations

import argparse

from src.core.memory_bus import MemoryBus
from src.utils.pointer_scan import scan_chain


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", type=lambda x: int(x, 0), required=True)
    ap.add_argument("--offsets", nargs="+", type=lambda x: int(x, 0), required=True)
    args = ap.parse_args()
    bus = MemoryBus("CastlevaniaBelmontsCurse.exe")
    bus.attach()
    for addr in scan_chain(bus, args.base, args.offsets):
        print(f"0x{addr:08X}")


if __name__ == "__main__":
    main()