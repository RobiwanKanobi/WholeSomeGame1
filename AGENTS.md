# AGENTS.md

## Game pitch owner brief

You are responsible for shaping and refining the game's pitch. Treat the current concept below as the default direction unless the user explicitly asks to pivot.

### Core concept

- **Working title:** `Post & Parcel`
- **Format:** 2D wholesome game
- **Primary platform:** Steam only for now
- **Tone:** Cozy, optimistic, neighborly, and emotionally warm
- **Non-goals:** Do not introduce grim themes, edgy humor, horror, gritty survival, or combat-first design

### Pitch

`Post & Parcel` is a wholesome 2D cozy adventure about becoming the new postal carrier in a quiet mountain town where letters still matter. Players sort mail, read delivery clues, and walk or bike scenic routes to hand-deliver parcels, reconnect neighbors, and slowly uncover the personal stories that bind the community together.

The emotional hook is simple: every delivery is a small act of care. The game should feel like a gentle mix of exploration, light logistics puzzles, and heartfelt community building, with progress driven by trust, routine, and seasonal change instead of danger or conflict.

### Creative pillars

1. **Wholesome community care:** The player helps people stay connected through kind, everyday actions.
2. **Readable 2D exploration:** The world should be appealing, easy to parse, and designed around charming routes, landmarks, and discoverable shortcuts.
3. **Gentle puzzle solving:** Route planning, package traits, and delivery clues should create satisfying decisions without punishing failure.
4. **Steam-friendly commercial clarity:** The concept should be easy to understand from a capsule, short trailer, and store description.

### Audience and positioning

- Target players who enjoy cozy and heartfelt games, especially fans of exploration, light puzzle solving, and community-driven progression.
- Keep the pitch commercially legible for Steam tags such as `Cozy`, `Exploration`, `Puzzle`, `Adventure`, and `Wholesome`.
- When expanding the concept, prioritize features that strengthen wishlisting appeal on Steam rather than mobile or web-first ideas.

### Instructions for future agents

- When asked to write or refine a pitch, keep it concise, vivid, and commercially clear.
- Preserve the 2D format and wholesome tone unless the user says otherwise.
- Treat Steam as the only planned release platform for now.
- Favor features that support a strong store page pitch: a memorable fantasy, a clear core loop, and emotionally resonant differentiators.
- If proposing alternatives, stay within the same cozy, non-violent, wholesome design space.

## Cursor Cloud specific instructions

This is a **Godot 4.6 game project** written in GDScript. There are no package managers, Docker containers, databases, or backend services.

### Engine

- Requires **Godot Engine 4.6.1** (`/usr/local/bin/godot`). The update script installs it automatically from GitHub releases.

### Project structure

| Path | Purpose |
|---|---|
| `project.godot` | Godot project config; main scene is `scenes/main.tscn` |
| `scenes/` | All game scenes (`.tscn` files) |
| `scripts/` | All GDScript source files (`.gd` files) |
| `addons/gdai-mcp-plugin-godot/` | GDAI MCP editor plugin (optional; binary not included — gracefully no-ops) |
| `Builds/` | Optional export output directory (git-ignored) |
| `export_presets.cfg` | Export presets; current product goal is Steam-only release |

### Starting a new game from this template

1. Clone this repo and rename `project.godot` `config/name` to your game name.
2. Set `run/main_scene` in `project.godot` to your actual entry scene.
3. Replace `scenes/main.tscn` and `scripts/main.gd` with your game's scenes and scripts.
4. Treat Steam as the only release target for now unless the user explicitly asks for another platform.

### Running the game

- **Native (with display):** `godot --path /workspace` opens the editor; press F5 / Play to run.
- **Headless import:** `godot --headless --import` imports all resources without a display.
- **Web export (optional template path, not current release target):** `godot --headless --export-release "Web"` builds to `Builds/`. Serve with COOP/COEP headers:
  ```
  python3 -c "
  from http.server import HTTPServer, SimpleHTTPRequestHandler
  class H(SimpleHTTPRequestHandler):
      def end_headers(self):
          self.send_header('Cross-Origin-Opener-Policy','same-origin')
          self.send_header('Cross-Origin-Embedder-Policy','require-corp')
          super().end_headers()
  HTTPServer(('0.0.0.0',8080),H).serve_forever()
  "
  ```
  Then open `http://localhost:8080/index.html` in Chrome.

### Linting / validation

- GDScript syntax check: `godot --headless --check-only --script <file.gd>`
- Validate all scripts: `for f in scripts/*.gd; do godot --headless --check-only --script "$f"; done`

### Gotchas

- Export templates must be installed at `~/.local/share/godot/export_templates/4.6.1.stable/` before web export will work. The update script handles this.
- The GDAI MCP plugin prints a warning about missing binaries on every editor/export run — this is harmless.
- The web export requires COOP/COEP headers; a plain `python3 -m http.server` will not work.
- `Builds/` is git-ignored.
