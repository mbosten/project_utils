import matplotlib as mpl
import matplotlib.pyplot as plt

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
        "axes.prop_cycle": mpl.cycler(color=[
            "#1B365D", "#7A5195", "#2A9D8F", "#E76F51",
            "#6C757D", "#B08968", "#4D908E"
        ]),
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
        "axes.prop_cycle": mpl.cycler(color=[
            "#58A6FF", "#3FB950", "#F778BA", "#D29922",
            "#A371F7", "#FF7B72", "#79C0FF"
        ]),
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
        "axes.prop_cycle": mpl.cycler(color=[
            "#264653", "#2A9D8F", "#E9C46A", "#F4A261",
            "#E76F51", "#8AB17D", "#577590"
        ]),
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
    ax.legend(frameon=False)
    return ax


__all__ = ["use_theme", "polish_axes"]