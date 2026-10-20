# Security Policy

## Supported builds

| Game build | Trainer branch |
|------------|----------------|
| 1.4.x      | `main`         |
| 1.3.x      | `legacy/1.3`   |

## Scope

The trainer attaches to the `CastlevaniaBelmontsCurse.exe` process and
reads/writes process memory via `pymem`. It does **not** phone home, does
**not** include a remote loader, and does **not** ship prebuilt binaries.

## Reporting a vulnerability

Open a private security advisory on GitHub or email
`security@belmonts-curse-trainer.dev`. Please include:

- Trainer version (`python -m src.host.main --version`)
- Game build number
- Repro steps
- Whether the issue involves arbitrary code execution or only a
  memory-write out-of-bounds.

Do **not** file public issues for exploit-class bugs until a fix lands.

## Anti-cheat note

This trainer is for **single-player offline use only**. Do not use it in
any online leaderboard context. The maintainers take no responsibility
for bans, corrupted saves, or game instability.