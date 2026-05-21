from __future__ import annotations

import colorsys
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio


DARK_CYBER_AI_PALETTE = [
    "#00E5FF",  # electric cyan
    "#7C4DFF",  # neural violet
    "#00C853",  # signal green
    "#FFB300",  # anomaly amber
    "#FF5252",  # alert coral
    "#2979FF",  # deep blue
    "#D500F9",  # magenta
    "#263238",  # graphite
]

def darken_hex(hex_color, factor=0.72, saturation_factor=0.9):
    """
    Create a darker/more print-friendly version of a color.
    factor < 1 darkens.
    """

    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255

    h, l, s = colorsys.rgb_to_hls(r, g, b)

    l *= factor
    s *= saturation_factor

    r, g, b = colorsys.hls_to_rgb(h, l, s)

    return "#{:02X}{:02X}{:02X}".format(
        int(r * 255),
        int(g * 255),
        int(b * 255),
    )


LIGHT_CYBER_AI_PALETTE = [
    "#009FC2",  # refined cyan-blue
    "#6A42E8",  # brighter neural violet
    "#00A15B",  # brighter emerald green
    darken_hex("#FFB300", factor=0.82),
    darken_hex("#FF5252", factor=0.82),
    darken_hex("#2979FF", factor=0.82),
    darken_hex("#D500F9", factor=0.82),
    darken_hex("#263238", factor=0.90),
]

MARKERS = ["o", "x", "^", "s", "D", "v", "P", "*"]
LINESTYLES = ["-", "--", "-.", ":", (0, (5, 1)), (0, (3, 1, 1, 1)), (0, (1, 1)), "-"]
BAR_HATCHES = ["", "///", "\\\\\\", "xx", "--", "++", "..", "**"]

LIGHT_PROP_CYCLE = (
    mpl.cycler(color=LIGHT_CYBER_AI_PALETTE)
    + mpl.cycler(marker=MARKERS)
    + mpl.cycler(linestyle=LINESTYLES)
)

DARK_PROP_CYCLE = (
    mpl.cycler(color=DARK_CYBER_AI_PALETTE)
    + mpl.cycler(marker=MARKERS)
    + mpl.cycler(linestyle=LINESTYLES)
)

THEMES = {
    "dissertation": {
        "font.family": "serif",
        "font.serif": ["STIX Two Text", "Times New Roman", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "axes.titlesize": 20,
        "axes.labelsize": 17,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12,
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.6,
        "lines.linewidth": 1.8,
        "lines.markersize": 5,
        "figure.figsize": (10, 6),
        "axes.prop_cycle": LIGHT_PROP_CYCLE,
    },

    "cyber_dark": {
        "font.family": "sans-serif",
        "font.sans-serif": ["Aptos", "Arial", "DejaVu Sans"],
        "figure.facecolor": "#101418",
        "axes.facecolor": "#151B22",
        "savefig.facecolor": "#101418",
        "text.color": "#EAECEF",
        "axes.labelcolor": "#EAECEF",
        "xtick.color": "#D0D7DE",
        "ytick.color": "#D0D7DE",
        "axes.edgecolor": "#8B949E",
        "axes.grid": True,
        "grid.color": "#30363D",
        "grid.alpha": 0.7,
        "lines.linewidth": 2.0,
        "figure.figsize": (10, 6),
        "axes.prop_cycle": DARK_PROP_CYCLE,
    },

    "topology_minimal": {
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "figure.dpi": 120,
        "savefig.dpi": 300,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "axes.linewidth": 0.9,
        "axes.titlesize": 20,
        "axes.labelsize": 17,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.frameon": False,
        "lines.linewidth": 1.9,
        "figure.figsize": (10, 6),
        "axes.prop_cycle": LIGHT_PROP_CYCLE,
    },
}


def use_theme(name="dissertation", plotly=False):
    """
    Apply a predefined Matplotlib theme by updating global rcParams.

    The selected theme affects all figures created afterward and should
    therefore be applied before creating figures or subplots.

    Example
    -------
    >>> use_theme("dissertation")
    >>> fig, ax = plt.subplots()
    """
    if name not in THEMES:
        raise ValueError(f"Unknown theme: {name}. Choose from {list(THEMES)}")

    mpl.rcParams.update(mpl.rcParamsDefault)
    mpl.rcParams.update(THEMES[name])


    if plotly:
        register_plotly_theme(name, set_as_default=True)


def polish_axes(
    ax,
    title=None,
    xlabel=None,
    ylabel=None,
    legend=True,
):
    """
    Apply consistent styling, labels, and legend formatting to an axes object.

    Also adjusts line marker visibility for improved readability.

    Example
    -------
    >>> fig, ax = plt.subplots()
    >>> ax.plot(x, y, label="Signal")
    >>> polish_axes(ax, title="Example", xlabel="Time", ylabel="Value")
    """

    if title:
        ax.set_title(title, pad=8)

    if xlabel:
        ax.set_xlabel(xlabel)

    if ylabel:
        ax.set_ylabel(ylabel)

    for line in ax.get_lines():
        line.set_markevery(18)
        line.set_markeredgewidth(1.2)

    if legend:
        ax.legend(frameon=False)

    return ax


def apply_bar_hatches(bars):
    """
    Apply hatch patterns and edge styling to bar plot elements.

    Useful for improving distinction in print and grayscale figures.

    Example
    -------
    >>> bars = ax.bar(labels, values)
    >>> apply_bar_hatches(bars)
    """
    for bar, hatch in zip(bars, BAR_HATCHES):
        bar.set_hatch(hatch)
        bar.set_edgecolor("black")
        bar.set_linewidth(0.8)


def _plotly_font_family():
    family = mpl.rcParams.get("font.family", "serif")

    if isinstance(family, list):
        family = family[0]

    if family == "serif":
        serif_fonts = mpl.rcParams.get("font.serif", [])
        return serif_fonts[0] if serif_fonts else "Times New Roman"

    if family == "sans-serif":
        sans_fonts = mpl.rcParams.get("font.sans-serif", [])
        return sans_fonts[0] if sans_fonts else "Arial"

    return family


def register_plotly_theme(name="dissertation", set_as_default=True):
    """
    Register a Plotly template based on the currently active Matplotlib theme.
    Call this after use_theme(...).
    """

    colors = mpl.rcParams["axes.prop_cycle"].by_key()["color"]

    template_name = f"{name}_plotly"

    pio.templates[template_name] = go.layout.Template(
        layout=go.Layout(
            font=dict(
                family=_plotly_font_family(),
                size=mpl.rcParams.get("font.size", 12),
                color=mpl.rcParams.get("text.color", "black"),
            ),
            title=dict(
                font=dict(
                    family=_plotly_font_family(),
                    size=mpl.rcParams.get("axes.titlesize", 20),
                    color=mpl.rcParams.get("text.color", "black"),
                )
            ),
            paper_bgcolor=mpl.rcParams.get("figure.facecolor", "white"),
            plot_bgcolor=mpl.rcParams.get("axes.facecolor", "white"),
            colorway=colors,
        )
    )

    if set_as_default:
        pio.templates.default = template_name

    return template_name

__all__ = ["use_theme", "THEMES", "polish_axes", "apply_bar_hatches"]