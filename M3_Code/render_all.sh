#!/usr/bin/env bash
# render_all.sh — Render all 7 scenes at 1080p30 (high quality) and concatenate.
# Usage: bash render_all.sh
# Requires: manim, ffmpeg, LaTeX (see README.md for install steps)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Rendering Scene 0: Title Card ==="
manim -qh scene0_title.py Scene0Title

echo "=== Rendering Scene 1: Hook ==="
manim -qh scene1_hook.py Scene1Hook

echo "=== Rendering Scene 2: Concept (Av = λv) ==="
manim -qh scene2_concept.py Scene2Concept

echo "=== Rendering Scene 3: Geometric Intuition ==="
manim -qh scene3_intuition.py Scene3Intuition

echo "=== Rendering Scene 4: Worked Example ==="
manim -qh scene4_example.py Scene4Example

echo "=== Rendering Scene 5: Verification & Interpretation ==="
manim -qh scene5_interpretation.py Scene5Interpretation

echo "=== Rendering Scene 6: Summary & Credits ==="
manim -qh scene6_summary.py Scene6Summary

echo "=== Concatenating scenes into final video ==="
cat > /tmp/concat_list.txt <<EOF
file '${SCRIPT_DIR}/media/videos/scene0_title/1080p30/Scene0Title.mp4'
file '${SCRIPT_DIR}/media/videos/scene1_hook/1080p30/Scene1Hook.mp4'
file '${SCRIPT_DIR}/media/videos/scene2_concept/1080p30/Scene2Concept.mp4'
file '${SCRIPT_DIR}/media/videos/scene3_intuition/1080p30/Scene3Intuition.mp4'
file '${SCRIPT_DIR}/media/videos/scene4_example/1080p30/Scene4Example.mp4'
file '${SCRIPT_DIR}/media/videos/scene5_interpretation/1080p30/Scene5Interpretation.mp4'
file '${SCRIPT_DIR}/media/videos/scene6_summary/1080p30/Scene6Summary.mp4'
EOF

ffmpeg -y -f concat -safe 0 -i /tmp/concat_list.txt -c copy \
    "M3_AnimationVideo_Eigenvalues_E25B070652_Video.mp4"

echo ""
echo "=== Done! Output: M3_AnimationVideo_Eigenvalues_E25B070652_Video.mp4 ==="
python3 -c "
import subprocess, json
r = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','json',
                   'M3_AnimationVideo_Eigenvalues_E25B070652_Video.mp4'],
                  capture_output=True, text=True)
d = float(json.loads(r.stdout)['format']['duration'])
print(f'Total duration: {d:.1f}s  ({d/60:.1f} min)')
"
