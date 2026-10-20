from src.core.registry import PluginRegistry
from src.plugins.heart_sync import HeartSyncPlugin


def test_register_and_get():
    reg = PluginRegistry()
    p = HeartSyncPlugin()
    reg.register(p)
    assert reg.get("heart_sync") is p
    assert len(reg) == 1


def test_duplicate_rejected():
    reg = PluginRegistry()
    reg.register(HeartSyncPlugin())
    try:
        reg.register(HeartSyncPlugin())
    except ValueError:
        return
    raise AssertionError("expected ValueError on duplicate plugin")