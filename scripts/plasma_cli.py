
#!/usr/bin/env python3
import argparse, os, numpy as np
from plasma_toolkit import (paschen_voltage, meek_raether_streamer, AB_from_min,
    gamma_band_vals, ncrit_band_vals, load_townsend_params, load_exp_csvs, save_figure)
from plasma_toolkit.plots import plot_multigas_overlays, plot_air_paschen_vs_streamer, plot_multigas_streamer

def main():
    ap = argparse.ArgumentParser(description="Plasma Toolkit CLI")
    ap.add_argument("--data-dir", default="data"); ap.add_argument("--fig-dir", default="figures")
    ap.add_argument("--ncrit", type=float, default=20.0)
    ap.add_argument("--ncrit-min", type=float, default=18.0); ap.add_argument("--ncrit-max", type=float, default=22.0)
    ap.add_argument("--gamma-min", type=float, default=0.005); ap.add_argument("--gamma-max", type=float, default=0.02)
    ap.add_argument("--gamma-steps", type=int, default=20)
    args = ap.parse_args(); os.makedirs(args.fig_dir, exist_ok=True)
    gases=["Air","Argon","Helium","Nitrogen","CO2"]
    town = load_townsend_params(os.path.join(args.data_dir, "townsend_params_generic.csv"))
    exp_map = load_exp_csvs(args.data_dir, gases)
    KPA_TO_TORR = 7.500616827; A_air_p = 112.5 / KPA_TO_TORR; B_air_p = 2737.5 / KPA_TO_TORR
    minima = {"Argon":(0.912,137.0),"Helium":(0.30,189.0),"Nitrogen":(1.0,265.0),"CO2":(0.5,540.0)}
    pd_vals = np.logspace(-2,2,600); curves={"Air": paschen_voltage(pd_vals, A_air_p, B_air_p, 0.01)}
    for g,(pdmin,Vmin) in minima.items(): A,B=AB_from_min(pdmin,Vmin,0.01); curves[g]=paschen_voltage(pd_vals,A,B,0.01)
    fig = plot_multigas_overlays(pd_vals, curves, exp_map); save_figure(fig, os.path.join(args.fig_dir, "paschen_multigas_exp_overlay"))
    A_air_t=float(town.loc["Air","A_cm^-1_Torr^-1"]); B_air_t=float(town.loc["Air","B_V_cm_Torr"])
    V_str = meek_raether_streamer(pd_vals, A_air_t, B_air_t, args.ncrit)
    band = ncrit_band_vals(pd_vals, A_air_t, B_air_t, args.ncrit_min, args.ncrit_max) if args.ncrit_max>args.ncrit_min else None
    fig = plot_air_paschen_vs_streamer(pd_vals, curves["Air"], V_str, exp_map.get("Air"), band, args.ncrit); save_figure(fig, os.path.join(args.fig_dir, "air_paschen_vs_streamer_generic"))
    streamers={}; bands={}
    for g in ["Argon","Helium","Nitrogen","CO2"]:
        if g in town.index:
            A_t=float(town.loc[g,"A_cm^-1_Torr^-1"]); B_t=float(town.loc[g,"B_V_cm_Torr"])
            streamers[g]=meek_raether_streamer(pd_vals,A_t,B_t,args.ncrit)
            if args.ncrit_max>args.ncrit_min: bands[g]=ncrit_band_vals(pd_vals,A_t,B_t,args.ncrit_min,args.ncrit_max)
    fig = plot_multigas_streamer(pd_vals, curves, streamers, bands, args.ncrit); save_figure(fig, os.path.join(args.fig_dir, "multigas_paschen_vs_streamer_generic"))
    # Gamma band (Air)
    lo,hi = gamma_band_vals(pd_vals, A_air_p, B_air_p, args.gamma_min, args.gamma_max, args.gamma_steps)
    import matplotlib.pyplot as plt
    fig=plt.figure(); ax=fig.add_subplot(111); ax.fill_between(pd_vals,lo,hi,alpha=0.2,label=f"γ-band [{args.gamma_min},{args.gamma_max}]")
    g_c=(args.gamma_min*args.gamma_max)**0.5; Vc=paschen_voltage(pd_vals,A_air_p,B_air_p,g_c)
    ax.loglog(pd_vals,Vc,label=f"Air — Paschen (γ≈{g_c:.4f})")
    if exp_map.get("Air") is not None and len(exp_map["Air"]): ax.scatter(exp_map["Air"]["pd_Torr_cm"],exp_map["Air"]["Vb_V"],s=18,label="Air — exp")
    ax.set_xlabel("p·d (Torr·cm)"); ax.set_ylabel("Breakdown V (V)"); ax.set_title("Air — Paschen γ-band"); ax.legend(); 
    save_figure(fig, os.path.join(args.fig_dir, "air_paschen_gamma_band"))
if __name__ == "__main__": main()
