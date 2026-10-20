# Writing a Belmont's Curse Trainer plugin

Every plugin is a package under `src/plugins/<name>/` exporting a class
that satisfies `src.core.contracts.PluginContract`:

```python
class MyPlugin(PluginContract):
    name = "my_plugin"
    version = "0.1.0"
    def on_load(self, bus, settings): ...
    def tick(self): ...
    def on_unload(self): ...
```

The loader auto-discovers any subdirectory with an `__init__.py`. Keep
offsets in a sibling `offsets.py` and bump the version whenever the game
build changes.