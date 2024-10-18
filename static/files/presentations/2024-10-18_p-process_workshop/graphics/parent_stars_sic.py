from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# dark mode for matplotlib
plt.style.use("dark_background")

# Host stars
hosts = ["AGB", "CCSN", "Nova"]
abu_agb = 0.884 + 0.039 + 0.014 + 0.048 / 2
abu_ccsn = 0.013 + 0.048 / 2 + 0.001 + 0.0002 + 0.0007 / 2
abu_nova = 0.0007 / 2
abu_hosts = np.array([abu_agb, abu_ccsn, abu_nova])

np.testing.assert_almost_equal(abu_hosts.sum(), 1, decimal=4)

# make a bar plot of the abundances
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(4, 3)

ax.bar(hosts, abu_hosts)
# show y axis logarithmically
ax.set_yscale("log")
ax.set_ylabel("SiC relative abundance")

fig.tight_layout()

# label the bars with the abundances in percent
for i, abu in enumerate(abu_hosts):
    ax.text(i, abu, f"{round(abu*100, 2):.2f}%", ha="center", va="bottom")
ax.set_ylim(top=3)

# save the figure:
outname = Path(__file__).with_suffix(".svg")
fig.savefig(outname, transparent=True)
