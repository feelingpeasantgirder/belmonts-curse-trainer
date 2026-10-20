# Contributing to Belmont's Curse Trainer

Thanks for wanting to help whip Dracula's minions into shape. This is a
community-maintained trainer for *Castlevania: Belmont's Curse* targeting
Windows 10/11 (Steam build). Contributions of new offsets, plugins, and
overlay widgets are welcome.

## Ground rules

1. **Offsets rot.** Every game patch invalidates pointer chains. If you
   submit an offset update, include the game build number and a short
   memory-scan trace in the PR description.
2. **Plugins live in `src/plugins/`.** Each plugin is a self-contained
   Python package implementing `contracts.PluginContract`. Do not import
   the host directly — go through the registry.
3. **No hardcoded absolute paths.** Use `config/paths.py`.
4. **Tests are mandatory** for anything touching the memory bus or the
   save-state patcher. `pytest tests/` must pass with the mock backend.

## Workflow

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest tests/
python -m src.host.main --dry-run
```

## Style

- Black formatting, 100 col limit.
- Type hints on public functions.
- Keep the trainer safe: never write to memory unless the process
  handle was obtained through `MemoryBus.attach()`.

## Reporting cheat signatures

If you find a new godmode/heart/whiplash flag, drop it in
`src/plugins/heart_sync/offsets.py` alongside a comment with the build id.