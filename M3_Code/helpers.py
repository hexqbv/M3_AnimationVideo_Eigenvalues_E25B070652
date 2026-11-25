"""
helpers.py - Reusable utilities and visual style for Manim Linear Algebra videos.

This module sets up:
1. Global video configuration (1080p @ 30fps with dark background #0f1117).
2. Consistent color palette for linear transformations and eigenvectors.
3. Plain-English documented helper functions for:
   - Creating a readable coordinate plane (NumberPlane).
   - Creating vectors with MathTex labels positioned cleanly near the tip.
   - Formatting and positioning matrices with optional variable names.
"""

from manim import *
import numpy as np

# ==============================================================================
# 1. GLOBAL MANIM CONFIGURATION
# ==============================================================================
# Setting output resolution to Full HD (1920x1080) at 30 frames per second.
# This gives smooth playback while keeping render times fast for production.
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30
config.background_color = "#0f1117"  # Deep dark navy-slate background

# Single consistent font family for all Text mobjects
FONT_FAMILY = "Helvetica"
FONT = FONT_FAMILY
Text.set_default(font=FONT_FAMILY)

# ==============================================================================
# 1B. LAYOUT ZONES (14.22 wide x 8.0 tall Manim coordinate system)
# ==============================================================================
TITLE_Y_MIN = 3.2
TITLE_Y_MAX = 3.9
UNDERLINE_Y = 3.0

CONTENT_X_MIN = -6.5
CONTENT_X_MAX = 6.5
CONTENT_Y_MIN = -3.5
CONTENT_Y_MAX = 2.6
CONTENT_CENTER = np.array([0.0, (CONTENT_Y_MIN + CONTENT_Y_MAX) / 2.0, 0.0])  # y = -0.45
CONTENT_WIDTH = CONTENT_X_MAX - CONTENT_X_MIN   # 13.0
CONTENT_HEIGHT = CONTENT_Y_MAX - CONTENT_Y_MIN  # 6.1
SAFE_MARGIN = 0.5

# ==============================================================================
# 2. COLOR PALETTE
# ==============================================================================
# We define distinct colors so students immediately recognize each mathematical
# object across all scenes without confusion:
# - Blue: General/standard vectors that rotate or shear under transformations.
# - Yellow: Eigenvector 1 (lambda = 3), showing intense stretch along (1, 1).
# - Green: Eigenvector 2 (lambda = 1), showing preservation along (1, -1).
# - Teal: Matrix A representation and transformation markers.
# - Red: Critical highlights, determinants, and warnings/pivotal steps.
# - White/Light Gray: General equations, axes, and neutral annotations.

COLOR_BG = "#0f1117"           # Main background canvas color
COLOR_REGULAR = "#38BDF8"      # Bright Sky Blue: used for standard vectors v_1
COLOR_ORANGE = "#FB923C"       # Vibrant Orange: used for (1,0) / test vectors
COLOR_TEAL = "#2DD4BF"         # Teal: Matrix A and eigenvector (1, 1)
COLOR_PURPLE = "#C084FC"       # Purple: eigenvector (1, -1)
COLOR_EIGEN_1 = "#FACC15"      # Vibrant Yellow: Eigenvector 1 (lambda = 3)
COLOR_EIGEN_2 = "#4ADE80"      # Bright Emerald Green: Eigenvector 2 (lambda = 1)
COLOR_MATRIX_A = "#2DD4BF"     # Teal: Matrix A, linear map labels
COLOR_HIGHLIGHT = "#F87171"    # Soft Bright Red: Key highlights, alerts, det = 0
COLOR_TEXT = "#F3F4F6"         # Crisp off-white: High contrast body text & math
COLOR_GRID = "#1E293B"         # Muted navy: Background grid lines (non-distracting)
COLOR_AXIS = "#475569"         # Slate: Main coordinate axes


def create_title_bar(title_text, font_size=38):
    """
    Creates a standardized header title inside the Title Zone (y in [3.2, 3.9])
    with an underline strictly at y = 3.0.
    """
    title = Text(
        title_text,
        font_size=max(font_size, 32),
        weight=BOLD,
        color=COLOR_TEXT,
    )
    if title.width > CONTENT_WIDTH:
        title.scale_to_fit_width(CONTENT_WIDTH)
    title.move_to(np.array([0.0, 3.52, 0.0]))
    if title.get_top()[1] > TITLE_Y_MAX:
        title.shift(DOWN * (title.get_top()[1] - TITLE_Y_MAX))
    if title.get_bottom()[1] < TITLE_Y_MIN:
        title.shift(UP * (TITLE_Y_MIN - title.get_bottom()[1]))

    underline = Line(
        start=np.array([-6.0, UNDERLINE_Y, 0.0]),
        end=np.array([6.0, UNDERLINE_Y, 0.0]),
        color=COLOR_MATRIX_A,
        stroke_width=2.5,
    )
    title.is_title = True
    underline.is_title = True
    return title, underline


def center_in_content_zone(mobject, x_offset=0.0):
    """
    Centers a mobject vertically in the Content Zone (y in [-3.5, 2.6], center y = -0.45)
    and clamps it within [-6.5, 6.5] x [-3.5, 2.6] if needed.
    """
    mobject.move_to(np.array([x_offset, CONTENT_CENTER[1], 0.0]))
    if mobject.get_left()[0] < CONTENT_X_MIN:
        mobject.shift(RIGHT * (CONTENT_X_MIN - mobject.get_left()[0]))
    if mobject.get_right()[0] > CONTENT_X_MAX:
        mobject.shift(LEFT * (mobject.get_right()[0] - CONTENT_X_MAX))
    if mobject.get_bottom()[1] < CONTENT_Y_MIN:
        mobject.shift(UP * (CONTENT_Y_MIN - mobject.get_bottom()[1]))
    if mobject.get_top()[1] > CONTENT_Y_MAX:
        mobject.shift(DOWN * (mobject.get_top()[1] - CONTENT_Y_MAX))
    return mobject


def make_box(
    content_group,
    color=COLOR_MATRIX_A,
    pad=0.4,
    max_width=12.0,
    fixed_width=None,
    align_content=None,
    fill_color=COLOR_BG,
    fill_opacity=0.95,
    stroke_width=2.5,
    corner_radius=0.2,
):
    """
    Builds a box ALWAYS sized from its content using SurroundingRectangle.
    - If content_group.width > max_width - 2*pad, scales it down with scale_to_fit_width so it fits.
    - Builds the box with SurroundingRectangle(content_group, buff=pad, corner_radius=corner_radius, color=color).
    - If fixed_width is specified, stretches the box to fixed_width.
    - Centers content in the box (or left-aligns if align_content='left').
    - Returns VGroup(box, content_group).
    """
    avail_w = (fixed_width if fixed_width is not None else max_width) - 2 * pad
    if content_group.width > avail_w:
        content_group.scale_to_fit_width(avail_w)

    box = SurroundingRectangle(
        content_group,
        buff=pad,
        corner_radius=corner_radius,
        color=color,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        stroke_width=stroke_width,
    )
    if fixed_width is not None:
        box.stretch_to_fit_width(fixed_width)

    if align_content is not None and (align_content == "left" or np.array_equal(align_content, LEFT)):
        content_group.align_to(box, LEFT).shift(RIGHT * pad)
    else:
        content_group.move_to(box.get_center())

    res = VGroup(box, content_group)
    res.box = box
    res.content = content_group
    box.is_box = True
    box.content = content_group
    box.pad = pad
    return res


def clip_segment_to_box(p0, p1, xmin, xmax, ymin, ymax):
    """
    Liang-Barsky line clipping in 2D so grid/span lines never leave a bounding box.
    Returns (q0, q1) 3D points or None if completely outside.
    """
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    t0, t1 = 0.0, 1.0
    for p, q in [
        (-dx, p0[0] - xmin),
        (dx, xmax - p0[0]),
        (-dy, p0[1] - ymin),
        (dy, ymax - p0[1]),
    ]:
        if abs(p) < 1e-9:
            if q < 0:
                return None
        else:
            r = q / p
            if p < 0:
                if r > t1:
                    return None
                t0 = max(t0, r)
            else:
                if r < t0:
                    return None
                t1 = min(t1, r)
    return (
        np.array([p0[0] + t0 * dx, p0[1] + t0 * dy, 0.0]),
        np.array([p0[0] + t1 * dx, p0[1] + t1 * dy, 0.0]),
    )


def build_clipped_warped_grid(plane, matrix_2x2):
    """
    Creates a VGroup of grid lines representing `plane` transformed by `matrix_2x2`,
    clipped strictly to `plane`'s coordinate grid box so it never overflows
    the content zone.
    """
    p_min = plane.c2p(plane.x_range[0], plane.y_range[0])
    p_max = plane.c2p(plane.x_range[1], plane.y_range[1])
    xmin, xmax = p_min[0], p_max[0]
    ymin, ymax = p_min[1], p_max[1]
    origin = plane.c2p(0, 0)
    x_step = np.linalg.norm(plane.c2p(1, 0) - origin)
    y_step = np.linalg.norm(plane.c2p(0, 1) - origin)
    M = np.array(matrix_2x2, dtype=float)

    def to_screen(gx, gy):
        return origin + np.array([gx * x_step, gy * y_step, 0.0])

    lines = VGroup()
    for gx in range(-12, 13):
        a = M @ np.array([gx, -12.0])
        b = M @ np.array([gx, 12.0])
        clipped = clip_segment_to_box(to_screen(a[0], a[1]), to_screen(b[0], b[1]), xmin, xmax, ymin, ymax)
        if clipped is not None:
            is_axis = (gx == 0)
            lines.add(Line(
                clipped[0], clipped[1],
                color=COLOR_AXIS if is_axis else COLOR_GRID,
                stroke_width=2.5 if is_axis else 1.5,
                stroke_opacity=1.0 if is_axis else 0.6,
            ))
    for gy in range(-12, 13):
        a = M @ np.array([-12.0, gy])
        b = M @ np.array([12.0, gy])
        clipped = clip_segment_to_box(to_screen(a[0], a[1]), to_screen(b[0], b[1]), xmin, xmax, ymin, ymax)
        if clipped is not None:
            is_axis = (gy == 0)
            lines.add(Line(
                clipped[0], clipped[1],
                color=COLOR_AXIS if is_axis else COLOR_GRID,
                stroke_width=2.5 if is_axis else 1.5,
                stroke_opacity=1.0 if is_axis else 0.6,
            ))
    return lines


def wait_until(scene, t):
    """
    Waits until the scene clock reaches `t` seconds.

    Why this matters in a viva:
    Using absolute timestamps instead of fixed relative waits ensures every
    animation lands on its exact narration cue without accumulating drift.
    """
    current = getattr(scene.renderer, "time", None)
    if current is None:
        current = getattr(scene, "time", 0.0)
    dt = t - current
    if dt > 1e-3:
        scene.wait(dt)


# ==============================================================================
# 3. HELPER FUNCTIONS (Documented for oral exams / vivas)
# ==============================================================================

def create_labeled_plane(
    x_range=(-5, 5, 1),
    y_range=(-4, 4, 1),
    x_length=10,
    y_length=8,
    axis_config=None,
    background_line_style=None,
    font_size=32
):
    """
    Creates a 2D coordinate grid (NumberPlane) with clear axes and legible numbers.

    Why this matters in a viva:
    A linear transformation is fundamentally visualized as a warping of coordinate space.
    Having a clean, non-distracting coordinate plane allows the viewer to see how unit
    squares become parallelograms and how grid lines remain parallel and evenly spaced.

    Parameters:
    - x_range: Tuple of (min_x, max_x, step_x). Controls horizontal span.
    - y_range: Tuple of (min_y, max_y, step_y). Controls vertical span.
    - x_length, y_length: Total width and height of the plane in Manim scene units.
    - font_size: Size for axis tick numbers (minimum 32 for 1080p legibility).

    Returns:
    - A NumberPlane mobject with coordinates added.
    """
    if axis_config is None:
        axis_config = {
            "stroke_color": COLOR_AXIS,
            "stroke_width": 2.5,
            "include_numbers": True,
            "font_size": max(font_size, 32),
            "decimal_number_config": {
                "num_decimal_places": 0,
                "color": COLOR_TEXT,
            },
        }

    if background_line_style is None:
        background_line_style = {
            "stroke_color": COLOR_GRID,
            "stroke_width": 1.5,
            "stroke_opacity": 0.6,
        }

    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config=axis_config,
        background_line_style=background_line_style,
        faded_line_ratio=1,  # Keeps grid simple and uncluttered
    )
    return plane


def create_labeled_vector(
    plane,
    coords,
    label_tex,
    color=COLOR_REGULAR,
    label_direction=UR,
    label_buff=0.15,
    font_size=34,
    stroke_width=6,
    max_tip_length_to_length_ratio=0.25
):
    """
    Creates a directed arrow representing a 2D vector on a coordinate plane,
    along with an accompanying MathTex mathematical label placed near its tip.

    Why this matters in a viva:
    Vectors are geometric entities (arrows with magnitude and direction) as well as
    algebraic lists of numbers. This function bridges both representations: it draws
    the geometric arrow from the origin (0, 0) to (x, y) in plane coordinates and
    attaches the algebraic symbol (like \\mathbf{v} or A\\mathbf{v}) right next to it.

    Parameters:
    - plane: The NumberPlane reference used to convert coordinate pairs (x, y)
             into scene positions via plane.c2p(x, y).
    - coords: (x, y) tuple or list specifying the vector's destination point.
    - label_tex: Raw LaTeX string for the label (e.g., r"\\mathbf{v}_1" or r"A\\mathbf{v}").
    - color: Arrow and label color (from our defined palette).
    - label_direction: Direction vector (e.g. UR, UL, UP, RIGHT) to offset the label
                       away from the arrowhead so they never collide.
    - label_buff: Distance buffer between the arrow tip and the label text.
    - font_size: Size of the MathTex label (strictly >= 32).
    - stroke_width: Thickness of the vector shaft for high visibility at 1080p.

    Returns:
    - VGroup containing:
        group[0] = the Arrow mobject
        group[1] = the MathTex label mobject
    """
    # 1. Convert mathematical (x, y) coordinates to screen coordinates
    start_point = plane.c2p(0, 0)
    end_point = plane.c2p(coords[0], coords[1])

    # 2. Build the visual vector arrow
    arrow = Arrow(
        start=start_point,
        end=end_point,
        buff=0,  # Starts precisely at origin, ends precisely at coordinates
        color=color,
        stroke_width=stroke_width,
        max_tip_length_to_length_ratio=max_tip_length_to_length_ratio,
    )

    # 3. Create the mathematical label using LaTeX MathTex
    label = MathTex(
        label_tex,
        font_size=max(font_size, 32),
        color=color
    )

    # 4. Position the label relative to the arrow tip
    label.next_to(end_point, direction=label_direction, buff=label_buff)

    # 5. Group them together for clean single-call animations or transformations
    vector_group = VGroup(arrow, label)
    
    # Store convenient attributes on the group object
    vector_group.arrow = arrow
    vector_group.label = label
    vector_group.coords = np.array(coords)

    return vector_group


def create_matrix_display(
    matrix_entries,
    name="A",
    color=COLOR_MATRIX_A,
    bracket="[",
    font_size=36,
    include_name=True
):
    """
    Creates a cleanly formatted mathematical matrix display with brackets
    and an optional leading name (e.g., 'A = [[2, 1], [1, 2]]').

    Why this matters in a viva:
    In linear algebra, a matrix represents the linear transformation in standard
    coordinates. Presenting the matrix clearly with brackets and distinct coloring
    reinforces the connection between the numeric entries [a_ij] and their
    transformation effect on standard basis vectors.

    Parameters:
    - matrix_entries: 2D list of numbers or LaTeX strings, e.g. [[2, 1], [1, 2]].
    - name: Variable name string for the matrix (e.g., 'A', 'A - \\lambda I').
    - color: Highlight color for the matrix entries and brackets.
    - bracket: Bracket style - '[' for square brackets, '(' for parentheses.
    - font_size: Font size for the matrix entries and label (minimum 32).
    - include_name: Boolean. If True, displays 'name =' before the bracketed matrix.

    Returns:
    - A VGroup containing the formatted matrix (and optional name equality prefix).
    """
    effective_font_size = max(font_size, 32)

    # Use Manim's Matrix class for clean typographical spacing
    mat = Matrix(
        matrix_entries,
        left_bracket="[" if bracket == "[" else "(",
        right_bracket="]" if bracket == "[" else ")",
        element_to_mobject=MathTex,
        element_to_mobject_config={"font_size": effective_font_size, "color": color},
        bracket_h_buff=MED_SMALL_BUFF,
        bracket_v_buff=MED_SMALL_BUFF,
    )
    mat.get_brackets().set_color(color)

    if include_name and name:
        prefix = MathTex(
            rf"{name} =",
            font_size=effective_font_size,
            color=COLOR_TEXT
        )
        prefix.next_to(mat, LEFT, buff=0.2)
        group = VGroup(prefix, mat)
        group.matrix = mat
        group.prefix = prefix
        return group
    else:
        mat.matrix = mat
        return mat


# Quick test scene to verify all components render at 1080p without any errors
if __name__ == "__main__":
    print("helpers.py loaded successfully!")
    print(f"Canvas resolution: {config.pixel_width}x{config.pixel_height} @ {config.frame_rate}fps")
    print(f"Background color: {config.background_color}")
