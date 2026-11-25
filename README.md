# Eigenvalues & Eigenvectors — M3 Internal Assessment
**Author:** Sagar Mangla · E25B070652

---

## Learning Objective

> By the end of the video, the viewer will be able to **explain what an eigenvector is geometrically** and **find eigenvalues and eigenvectors of a 2×2 matrix**.

---

## Example Matrix

The video walks through one worked example end-to-end:

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

**Characteristic equation:** det(A − λI) = 0 → λ² − 4λ + 3 = 0 → **λ₁ = 1, λ₂ = 3**

| Eigenvalue | Equation | Eigenvector |
|---|---|---|
| λ₁ = 1 | (A − I)v = 0 | v₁ = (1, −1) (purple) |
| λ₂ = 3 | (A − 3I)v = 0 | v₂ = (1, 1) (teal) |

---

## How to Render

### 1. Prerequisites

**macOS (Homebrew):**
```bash
brew install ffmpeg
```

**LaTeX (required by Manim for math rendering):**
```bash
# Option A — TeX Live minimal (recommended, ~1 GB)
brew install --cask mactex-no-gui

# Option B — full MacTeX (~5 GB)
brew install --cask mactex
```

**Python 3.11+:**
```bash
brew install python@3.11
```

### 2. Install Manim CE and Dependencies

```bash
# From the M3_Code/ directory
cd M3_Code
pip install -r requirements.txt
```

### 3. Render All Scenes

```bash
# From the M3_Code/ directory
bash render_all.sh
```

This renders all 7 scenes at **1080p30** (`-qh`) and concatenates them into a single file:
```
M3_AnimationVideo_Eigenvalues_E25B070652_Video.mp4
```

### 4. Run the Layout Checker (optional)

```bash
python check_layout.py
```
Verifies every scene against the content-zone bounds, text-in-box padding (≥ 0.3 u), and frame margin (≥ 0.5 u) rules. Should report **Total layout issues: 0**.

---

## File List

```
M3_AnimationVideo_Eigenvalues_E25B070652/
├── M3_AnimationVideo_Eigenvalues_E25B070652_Video.mp4   # Final assembled video
├── storyboard.pdf                                        # Approved storyboard
├── README.md                                             # This file
└── M3_Code/
    ├── scene0_title.py          # 4 s silent title card
    ├── scene1_hook.py           # Scene 1: Matrices Transform Space (~30 s)
    ├── scene2_concept.py        # Scene 2: The Central Concept: Av = λv (~36 s)
    ├── scene3_intuition.py      # Scene 3: Geometric Intuition (~68 s)
    ├── scene4_example.py        # Scene 4: Worked Example (~91 s)
    ├── scene5_interpretation.py # Scene 5: Verification & Area Scaling (~48 s)
    ├── scene6_summary.py        # Scene 6: Summary & Credits (~35 s)
    ├── helpers.py               # Shared layout constants, make_box(), wait_until(), etc.
    ├── check_layout.py          # Automated layout verification tool
    ├── render_all.sh            # One-shot render + concat script
    ├── requirements.txt         # Pip dependencies (manim 0.22.1 + direct deps)
    ├── audio/
    │   ├── scene1.wav           # Narration for Scene 1
    │   ├── scene2.wav           # Narration for Scene 2
    │   ├── scene3.wav           # Narration for Scene 3
    │   ├── scene4.wav           # Narration for Scene 4
    │   ├── scene5.wav           # Narration for Scene 5
    │   └── scene6.wav           # Narration for Scene 6
    └── cues/
        ├── scene1.md            # Audio-to-visual beat cue sheet
        ├── scene2.md
        ├── scene3.md
        ├── scene4.md
        ├── scene5.md
        └── scene6.md
```

---

## References

- Strang, G. *Introduction to Linear Algebra*, 5th ed. Wellesley-Cambridge Press, 2016.
- 3Blue1Brown. *Essence of Linear Algebra* (YouTube series). Inspiration only; no content reproduced.

---

## AI Disclosure

> Antigravity (Gemini) was used to help draft the storyboard and write/debug Manim code.
> All mathematics was verified by me. Narration recorded by me.
> Final assembly and audio levelling were done in Premiere Pro.
