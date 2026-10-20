"""Helper to walk a base+offset chain and dump candidate pointers."""
from __future__ import annotations


def scan_chain(bus, base: int, offsets: list[int]) -> list[int]:
    chain = [base]
    cur = base
    for off in offsets:
        cur = bus.read_i32(cur + off)
        chain.append(cur)
    return chain