# Cue Sheet — Scene 4: Worked Example (Audio Order)
- **Audio file:** `audio/scene4.wav` (`time_offset=0.5s`)
- **Total audio duration:** `90.84s` (`90.837313s` via `ffprobe`) → **Target scene duration:** `91.34s`

| Audio Cue | Scene Clock (`+0.5s`) | Visual Beat | Narration Cue |
|---|---|---|---|
| `0.66s` | `1.16s` | Header + Step 1 badge + **Av = λv** → **(A – λI)v = 0** | *"Now let's find eigenvalues algebraically step by step, we start from Av = λv and rearrange: (A – λI)v = 0."* (`0.66s – 10.70s`) |
| `11.04s` | `11.54s` | Non-zero **v** exists only if **det(A – λI) = 0** | *"We want non-zero solutions which require the matrix A minus lambda I to be singular, that is its determinant must be 0."* (`11.04s – 18.22s`) |
| `18.64s` | `19.14s` | Build **det([[2–λ, 1], [1, 2–λ]]) = 0** | *"This is the characteristic equation. For our matrix A, subtract lambda from each diagonal entry..."* (`18.64s – 28.76s`) |
| `29.24s` | `29.74s` | **(2 – λ)² – (1)(1) = 0** | *"Its determinant is (2 minus lambda) squared minus 1 times 1."* (`29.24s – 33.06s`) |
| `33.78s` | `34.28s` | **4 – 4λ + λ² – 1 = 0** | *"Expand the bracket: 4 minus 4 lambda plus lambda squared, then subtract 1."* (`33.78s – 38.24s`) |
| `38.80s` | `39.30s` | **λ² – 4λ + 3 = 0** | *"That gives us lambda squared minus 4 lambda plus 3."* (`38.80s – 42.54s`) |
| `43.24s` | `43.74s` | Factorisation: **(λ – 1)(λ – 3) = 0** | *"We now factor this quadratic... (lambda minus 1) times (lambda minus 3) equals 0."* (`43.24s – 56.10s`) |
| `56.42s` | `56.92s` | Boxed eigenvalues: **λ₁ = 1, λ₂ = 3** | *"The two eigenvalues are lambda equals 1 and lambda equals 3."* (`56.42s – 59.90s`) |
| `60.30s` | `60.80s` | Step 2 heading (`λ₂ = 3`) + **(A – 3I)v = 0** → `[[-1, 1], [1, -1]] v = 0` | *"For lambda equals 3, plug into A minus 3I to get the matrix with negative 1s and 1s."* (`60.30s – 66.02s`) |
| `66.68s` | `67.18s` | Row 1: **–v₁ + v₂ = 0 → v₂ = v₁** | *"First row says minus v1 plus v2 equals 0. So v2 equals v1."* (`66.68s – 71.02s`) |
| `71.52s` | `72.02s` | Choose **v₁ = 1 → v = (1, 1)ᵀ** | *"Choosing v1 equals 1 gives eigenvector (1, 1)."* (`71.52s – 75.06s`) |
| `75.56s` | `76.06s` | Step 3 heading (`λ₁ = 1`) + **(A – I)v = 0** → `[[1, 1], [1, 1]] v = 0` | *"For lambda equals 1, A minus I has all entries equal to 1."* (`75.56s – 79.40s`) |
| `79.40s` | `79.90s` | Row 1: **v₁ + v₂ = 0 → v₂ = –v₁** | *"The row equation says v1 plus v2 equals 0. So v2 equals negative v1."* (`79.40s – 84.90s`) |
| `85.28s` | `85.78s` | Choose **v₁ = 1 → v = (1, –1)ᵀ** + summary cards; hold to `91.34s` | *"Choosing v1 equals 1 gives eigenvector (1, minus 1)."* (`85.28s – 89.86s`) |
