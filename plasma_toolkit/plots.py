
"""Plot helpers."""
import matplotlib.pyplot as plt
def plot_multigas_overlays(pd_vals, curves, exp_map):
    fig=plt.figure(); ax=fig.add_subplot(111)
    for g,V in curves.items():
        ax.loglog(pd_vals,V,label=f"{g} — Paschen (context)")
        df=exp_map.get(g)
        if df is not None and len(df): ax.scatter(df["pd_Torr_cm"],df["Vb_V"],s=18,label=f"{g} — exp")
    ax.set_xlabel("p·d (Torr·cm)"); ax.set_ylabel("Breakdown V (V)"); ax.set_title("Paschen — Multi-Gas with Experimental Overlays"); ax.legend(ncol=2); return fig
def plot_air_paschen_vs_streamer(pd_vals, Vp, Vs, exp_df=None, band=None, ncrit=20):
    fig=plt.figure(); ax=fig.add_subplot(111)
    if band is not None: lo,hi=band; ax.fill_between(pd_vals,lo,hi,alpha=0.2,label="Streamer band")
    ax.loglog(pd_vals,Vp,label="Air — Paschen"); ax.loglog(pd_vals,Vs,label=f"Air — Streamer (Ncrit={ncrit})")
    if exp_df is not None and len(exp_df): ax.scatter(exp_df["pd_Torr_cm"],exp_df["Vb_V"],s=18,label="Air — exp")
    ax.set_xlabel("p·d (Torr·cm)"); ax.set_ylabel("Threshold V (V)"); ax.set_title("Air — Paschen vs Streamer"); ax.legend(); return fig
def plot_multigas_streamer(pd_vals, curves, streamers, bands=None, ncrit=20):
    fig=plt.figure(); ax=fig.add_subplot(111)
    for g in curves:
        ax.loglog(pd_vals,curves[g],label=f"{g} — Paschen")
        if bands and g in bands: ax.fill_between(pd_vals,bands[g][0],bands[g][1],alpha=0.08)
        ax.loglog(pd_vals,streamers[g],linestyle="--",label=f"{g} — Streamer (Ncrit={ncrit})")
    ax.set_xlabel("p·d (Torr·cm)"); ax.set_ylabel("Threshold V (V)"); ax.set_title("Multi-Gas — Paschen vs Streamer"); ax.legend(ncol=2); return fig
