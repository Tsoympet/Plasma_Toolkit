
"""I/O helpers."""
import os, pandas as pd, matplotlib.pyplot as plt
def load_townsend_params(path):
    df = pd.read_csv(path)
    if "Gas" not in df.columns: raise ValueError("Missing 'Gas' column")
    return df.set_index("Gas")
def load_exp_csvs(dirpath, gases):
    out={}
    for g in gases:
        p=os.path.join(dirpath,f"exp_{g}.csv")
        out[g]=pd.read_csv(p) if os.path.exists(p) else None
    return out
def save_figure(fig, out_base):
    for ext in ("png","pdf"):
        fig.savefig(f"{out_base}.{ext}", dpi=300, bbox_inches="tight")
    plt.close(fig)
