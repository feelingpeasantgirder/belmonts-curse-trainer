from src.core.memory_bus import MemoryBus


def test_dry_run_read_write_noop():
    bus = MemoryBus("CastlevaniaBelmontsCurse.exe", dry_run=True)
    bus.attach()
    bus.write_i32(0x1000, 42)
    assert bus.read_i32(0x1000) == 0