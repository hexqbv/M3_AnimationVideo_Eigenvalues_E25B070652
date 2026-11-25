# Cue Sheet — Scene 3: Visual Intuition
- **Audio file:** `audio/scene3.wav` (`time_offset=0.5s`)
- **Total audio duration:** `67.43s` (`67.434688s` via `ffprobe`) → **Target scene duration:** `67.93s`
- **Colors:** Teal for `(1, 1)` (`y = x`), Purple for `(1, -1)` (`y = -x`), Orange for test/generic vector `(2, 0)`

| Audio Cue | Scene Clock (`+0.5s`) | Visual Beat | Narration Cue |
|---|---|---|---|
| `1.23s` | `1.73s` | Grid, Matrix **A = [[2,1],[1,2]]** badge, and Unit Square appear | *"Let's see these eigenvectors in action on the grid."* (`1.23s – 4.07s`) |
| `4.59s` | `5.09s` | **Teal** vector **v₁ = (1, 1)** drawn on line `y = x` | *"First, the teal vector pointing at 45 degrees: (1, 1)."* (`4.59s – 8.41s`) |
| `8.83s` | `9.33s` | `ApplyMatrix(A)` deforms grid and unit square | *"When we apply our matrix A, the whole grid deforms, but watch this vector."* (`8.83s – 13.49s`) |
| `13.99s` | `14.49s` | **Teal** vector stretches to `(3, 3)` along `y = x` | *"It stays pointing in exactly the same direction, stretching to (3, 3)."* (`13.99s – 17.93s`) |
| `18.53s` | `19.03s` | Label *"stretched by 3 (λ = 3)"* | *"Its eigenvalue is 3. The transformation tripled it."* (`18.53s – 21.83s`) |
| `22.23s` | `22.73s` | **Purple** vector **v₂ = (1, -1)** drawn on line `y = -x` | *"Now the purple vector: (1, –1)."* (`22.23s – 24.49s`) |
| `24.85s` | `25.35s` | **Purple** vector maps to `(1, -1)` unchanged | *"Under the same transformation, it maps to (1, –1) exactly."* (`24.85s – 28.93s`) |
| `29.53s` | `30.03s` | Label *"stretched by 1 (λ = 1)"* | *"Its eigenvalue is 1. The transformation left it completely unchanged."* (`29.53s – 34.27s`) |
| `34.75s` | `35.25s` | Both eigenvectors (`y = x` teal, `y = -x` purple) highlighted perpendicular — natural axes | *"Notice that these two vectors are perpendicular. They define the natural axes of this particular transformation..."* (`34.75s – 44.39s`) |
| `44.99s` | `45.49s` | **Orange** vector **w = (2, 0)** drawn & decomposed: `(2,0) = 1·(1,1) + 1·(1,-1)` | *"Here is the payoff. Take any vector, say (2, 0). Decompose it into our two eigenvectors, one part of each."* (`44.99s – 53.27s`) |
| `53.99s` | `54.49s` | Each component scales by its eigenvalue: `3·(1,1)` & `1·(1,-1)` | *"Apply A and each part just scales by its own eigenvalue."* (`53.99s – 57.37s`) |
| `57.37s` | `57.87s` | Sum shown: `(3,3) + (1,-1) = (4, 2)` | *"Add the results. You get the correct answer immediately without any matrix multiplication."* (`57.37s – 62.59s`) |
| `63.39s` | `63.89s` | Geometric Insight card; hold & fade out to `67.93s` | *"Eigenvectors are a coordinate system tuned to the transformation."* (`63.39s – 66.15s`) |
