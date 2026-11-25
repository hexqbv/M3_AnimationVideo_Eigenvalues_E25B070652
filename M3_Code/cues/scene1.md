# Cue Sheet — Scene 0 & Scene 1

## Scene 0 — Silent Title Card (`scene0_title.py`, `Scene0Title`)
- **Audio:** Silent (`4.00s` total)

| Scene Time | Visual Beat |
|---|---|
| `0.00s – 4.00s` | Dark background; Title: **"Eigenvalues & Eigenvectors"**, Subtitle: **"M3 Internal Assessment"**, Name & ID: **"Sagar Mangla, E25B070652"**; fade out by `4.00s`. |

---

## Scene 1 — Hook & Context (`scene1_hook.py`, `Scene1Hook`)
- **Audio file:** `audio/scene1.wav` (`time_offset=0.5s`)
- **Total audio duration:** `29.50s` (`29.504000s` via `ffprobe`) → **Target scene duration:** `30.00s`
- **Colors:** Orange for `(1, 0)`, Teal for `(1, 1)`, Purple for `(1, -1)`

| Audio Cue | Scene Clock (`+0.5s`) | Visual Beat | Narration Cue |
|---|---|---|---|
| `0.40s` | `0.90s` | 2-D coordinate grid appears & Matrix **A = [[2,1],[1,2]]** badge shown | *"Every matrix is secretly a function that transforms space."* (`0.40s – 4.10s`) |
| `4.48s` | `4.98s` | Dashed reference lines & vectors drawn: **orange** `(1, 0)`, **teal** `(1, 1)`, **purple** `(1, -1)` | *"It stretches, squishes, or rotates vectors. Take this matrix A."* (`4.48s – 8.26s`) |
| `8.80s` | `9.30s` | Apply A to **orange** arrow `(1, 0)` → transforms toward `(2, 1)` | *"Apply it to the orange arrow and watch."* (`8.80s – 10.78s`) |
| `11.08s` | `11.58s` | Label *"direction changed / Rotated!"* on orange arrow | *"The arrow changes direction entirely."* (`11.08s – 13.04s`) |
| `13.82s` | `14.32s` | Focus on **teal** arrow `(1, 1)` | *"But apply it to the teal arrow."* (`13.82s – 15.20s`) |
| `15.54s` | `16.04s` | **Teal** arrow stretches ×3 to `(3, 3)` along its line; **purple** `(1, -1)` stays on its line; label *"Stays on line! (×3)"* | *"Something remarkable happens. The vector doesn't rotate at all. It simply scales up by a factor of three."* (`15.54s – 21.24s`) |
| `21.82s` | `22.32s` | Hook card: *"Which vectors only get stretched? — Eigenvectors"* | *"Vectors like this, that survive a transformation with their direction intact are called eigenvectors."* (`21.82s – 26.58s`) |
| `27.12s` | `27.62s` | Hold & fade out to `30.00s` | *"Let's find out why they exist."* (`27.12s – 29.48s`) |
