from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_FILE = ROOT / "config" / "trainer.yaml"
PLUGIN_DIR = ROOT / "src" / "plugins"
CAPTURE_DIR = ROOT / "captures"