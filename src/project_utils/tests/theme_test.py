import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from project_utils import THEMES, polish_axes, apply_bar_hatches

themes = ["dissertation", "cyber_dark", "topology_minimal"]

x = np.linspace(0, 10, 200)

models = ["Raw", "PCA", "UMAP", "TopoAE", "Graph NN"]
scores = [0.42, 0.57, 0.63, 0.74, 0.69]
sizes = np.ones(8)

# Minimal outer figure only
fig = plt.figure(figsize=(16, 9), dpi=160, constrained_layout=True)
fig.patch.set_facecolor("white")

gs = fig.add_gridspec(3, 3)

axes = np.empty((3, 3), dtype=object)

for row, theme in enumerate(themes):

    with mpl.rc_context(THEMES[theme]):

        # Create axes INSIDE themed context
        for col in range(3):
            axes[row, col] = fig.add_subplot(gs[row, col])

        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

        # ---- Line plot ----
        ax = axes[row, 0]

        ax.plot(x, np.sin(x), label="Embedding quality")
        ax.plot(x, np.cos(x) * 0.7, label="Topology signal")
        ax.scatter(
            x[::20],
            np.sin(x[::20]) + 0.15,
            color=colors[2],
            marker="^",
            label="Dataset samples",
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
            {"edgecolor": "#EAECEF", "linewidth": 1.0}
            if theme == "cyber_dark"
            else {"linewidth": 0}
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

plt.show()

