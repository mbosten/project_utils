import numpy as np
import matplotlib.pyplot as plt

from project_utils import use_theme, polish_axes, apply_bar_hatches

themes = ["dissertation", "cyber_dark", "topology_minimal"]

x = np.linspace(0, 10, 200)

models = ["Raw", "PCA", "UMAP", "TopoAE", "Graph NN"]
scores = [0.42, 0.57, 0.63, 0.74, 0.69]

sizes = np.ones(8)

fig, axes = plt.subplots(
    nrows=3,
    ncols=3,
    figsize=(16, 9),
    dpi=160,
    constrained_layout=True,
)

for row, theme in enumerate(themes):
    use_theme(theme)

    prop_cycle = plt.rcParams["axes.prop_cycle"]
    colors = prop_cycle.by_key()["color"]


    # Apply theme colors/backgrounds to row axes
    for ax in axes[row]:
        ax.set_facecolor(plt.rcParams["axes.facecolor"])
        ax.set_prop_cycle(prop_cycle)

    # ---- Line plot ----
    ax = axes[row, 0]

    ax.plot(x, np.sin(x), label="Embedding quality")
    ax.plot(x, np.cos(x) * 0.7, label="Topology signal")
    ax.scatter(
        x[::20],
        np.sin(x[::20]) + 0.15,
        label="Dataset samples",
        color=colors[2],
        marker="^",
    )

    polish_axes(
        ax,
        title=f"{theme}: Line chart",
        xlabel="Filtration / scale",
        ylabel="Normalized score",
    )

    # ---- Bar plot ----
    ax = axes[row, 1]

    bars = ax.bar(models, scores, color=colors[:len(models)])
    apply_bar_hatches(bars)

    ax.set_title(f"{theme}: Bar chart")
    ax.set_xlabel("Representation")
    ax.set_ylabel("Quality estimate")
    ax.tick_params(axis="x", rotation=20)

    # ---- Pie chart ----
    ax = axes[row, 2]
    
    wedgeprops = (
        {
            "edgecolor": "#EAECEF",
            "linewidth": 1.0,
        }
        if theme == "cyber_dark"
        else {
            "linewidth": 0,
        }
    )

    ax.pie(
        sizes,
        colors=colors[:len(sizes)],
        startangle=90,
        counterclock=False,
        wedgeprops=wedgeprops,
    )

    ax.set_title(f"{theme}: Pie chart")
    ax.set_aspect("equal")

# Match full figure background to a neutral presentation canvas
fig.patch.set_facecolor("white")

fig.savefig(
    "theme_showcase.png",
    dpi=300,
    bbox_inches="tight",
)

fig.savefig(
    "theme_showcase.pdf",
    bbox_inches="tight",
)

plt.show()