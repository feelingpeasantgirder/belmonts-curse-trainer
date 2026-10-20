# Offset table

| Build | HEART_COUNT   | WHIP_DAMAGE   | MOVEMENT_SPEED |
|-------|---------------|---------------|----------------|
| 1.4.2 | 0x0A17C4B0    | 0x0A17C520    | 0x0A17C534     |
| 1.3.9 | 0x0A16F1A0    | 0x0A16F210    | 0x0A16F224     |

Regenerate with:
```
python -m tools.scan_offsets --base 0x140000000 --offsets 0x... 0x...
```