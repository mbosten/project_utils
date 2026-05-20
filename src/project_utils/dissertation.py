from __future__ import annotations


import matplotlib as mpl
import matplotlib.pyplot as plt

CYBER_AI_PALETTE = [
    "#00E5FF",  # electric cyan
    "#7C4DFF",  # neural violet
    "#00C853",  # signal green
    "#FFB300",  # anomaly amber
    "#FF5252",  # alert coral
    "#2979FF",  # deep blue
    "#D500F9",  # magenta
    "#263238",  # graphite
]

MARKERS = ["o", "x", "^", "s", "D", "v", "P", "*"]
LINESTYLES = ["-", "--", "-.", ":", (0, (5, 1)), (0, (3, 1, 1, 1)), (0, (1, 1)), "-"]
BAR_HATCHES = ["", "///", "\\\\\\", "xx", "--", "++", "..", "**"]

LINESTYLE_CYCLE = (
    mpl.cycler(color=CYBER_AI_PALETTE)
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
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.6,
        "lines.linewidth": 1.8,
        "lines.markersize": 5,
        "figure.figsize": (5.2, 3.4),
        "axes.prop_cycle": LINESTYLE_CYCLE,
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
        "figure.figsize": (5.2, 3.4),
        "axes.prop_cycle": LINESTYLE_CYCLE,
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
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.frameon": False,
        "lines.linewidth": 1.9,
        "figure.figsize": (5.2, 3.4),
        "axes.prop_cycle": LINESTYLE_CYCLE,
    },
}


def use_theme(name="dissertation"):
    if name not in THEMES:
        raise ValueError(f"Unknown theme: {name}. Choose from {list(THEMES)}")

    mpl.rcParams.update(mpl.rcParamsDefault)
    mpl.rcParams.update(THEMES[name])


def polish_axes(ax, title=None, xlabel=None, ylabel=None):
    if title:
        ax.set_title(title, pad=8)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    for line in ax.get_lines():
        line.set_markevery(18)
        line.set_markeredgewidth(1.2)

    ax.legend(frameon=False)
    return ax


def apply_bar_hatches(bars):
    for bar, hatch in zip(bars, BAR_HATCHES):
        bar.set_hatch(hatch)
        bar.set_edgecolor("black")
        bar.set_linewidth(0.8)


__all__ = ["use_theme", "polish_axes", "apply_bar_hatches"]