import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datacentre 1 data
df = pd.read_csv("data/datacentre_1.csv", index_col=0, parse_dates=True)

sns.set(style="ticks", context="notebook", font_scale=1.1)

# Select two arbitrary columns to plot
column1 = df.columns[0] 
column2 = df.columns[1]

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True)

sns.lineplot(
    data=df, x=df.index, y=column1, ax=axes[0], 
    color="#1f77b4", linewidth=2 
)
axes[0].set_title("Requests Over Time (Channel 1)", fontsize=14, pad=20)
axes[0].set_ylabel("Requests", fontsize=12)
axes[0].set_xlabel("")  # Remove x-label for the top plot
axes[0].tick_params(axis="x", rotation=45)  # Rotate x-axis labels for clarity

sns.lineplot(
    data=df, x=df.index, y=column2, ax=axes[1], 
    color="#ff7f0e", linewidth=2  
)
axes[1].set_title("Requests Over Time (Channel 2)", fontsize=14, pad=20)
axes[1].set_ylabel("Requests", fontsize=12)
axes[1].set_xlabel("Time", fontsize=12)
axes[1].tick_params(axis="x", rotation=45)  


for ax in axes:
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter("%Y-%m-%d %H:%M"))  # Format datetime
    ax.grid(True, linestyle="--", alpha=0.6)  # Add a clean grid


plt.tight_layout()
plt.savefig("./example_datacentre1.png", dpi=300, bbox_inches="tight")
plt.close()