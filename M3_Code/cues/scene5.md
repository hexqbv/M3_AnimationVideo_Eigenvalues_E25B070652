# Cue Sheet — Scene 5: Interpretation
- **Audio file:** `audio/scene5.wav` (`time_offset=0.5s`)
- **Total audio duration:** `47.30s` (`47.296000s` via `ffprobe`) → **Target scene duration:** `47.80s`

| Audio Cue | Scene Clock (`+0.5s`) | Visual Beat | Narration Cue |
|---|---|---|---|
| `1.04s` | `1.54s` | Header & coordinate plane appear | *"Let's verify our answers by substituting back."* (`1.04s – 3.66s`) |
| `3.94s` | `4.44s` | **Verification 1 — Sub-cue A:** Vector `(1, 1)` & **top row = 3** (`2·1 + 1·1 = 3`) | *"Matrix A times the vector (1, 1): top row gives 2×1 + 1×1 = 3."* (`3.94s – 9.82s`) |
| `10.28s` | `10.78s` | **Verification 1 — Sub-cue B:** **bottom row = 3** (`1·1 + 2·1 = 3`) | *"Bottom row gives 1×1 + 2×1 = 3."* (`10.28s – 13.32s`) |
| `13.74s` | `14.24s` | **Verification 1 — Sub-cue C:** Result `(3, 3) = 3·(1, 1) ✓` + Flash | *"Result (3, 3), which is exactly 3 times (1, 1). Confirmed."* (`13.74s – 17.64s`) |
| `18.06s` | `18.56s` | **Verification 2:** Vector `(1, -1)` & `A(1, -1) = (1, -1) = 1·(1, -1) ✓` | *"Second check. A times (1, –1) gives (2 – 1, 1 – 2) equals (1, –1). That's 1 times (1, –1). Also confirmed."* (`18.06s – 28.10s`) |
| `28.62s` | `29.12s` | Clear verification; show Unit Square (`Area = 1`) on grid | *"Now notice something deeper."* (`28.62s – 29.74s`) |
| `30.12s` | `30.62s` | Start unit-square-to-parallelogram deformation under A | *"The determinant of A is 2 times 2 minus 1 times 1..."* (`30.12s – 33.42s`) |
| `33.00s` | `33.50s` | Show **Area = 3** label & `det(A) = 2·2 - 1·1 = 3`; at `33.86s` (`34.36s` scene) show `= λ₁·λ₂ = 1·3 = 3 ✓` | *"...which is 3. And the product of our eigenvalues is 1 times 3, also 3. This is not a coincidence — the determinant always equals the product of all eigenvalues."* (`33.86s – 42.40s`) |
| `43.32s` | `43.82s` | Highlight **"Area ×3"** (callout/indicate on area = 3); hold & fade out to `47.80s` | *"Geometrically it means the matrix scales areas by exactly a factor of 3."* (`43.32s – 46.84s`) |
