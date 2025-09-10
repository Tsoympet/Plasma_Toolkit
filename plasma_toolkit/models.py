
"""Core discharge models."""
import numpy as np, math
def paschen_voltage(pd, A, B, gamma=0.01):
    """Compute Paschen breakdown voltage (V)."""
    pd = np.asarray(pd, dtype=float)
    denom = np.log(A*pd) - np.log(np.log(1+1.0/gamma))
    return (B*pd)/denom
def AB_from_min(pd_min, Vmin, gamma=0.01):
    """Back-calc (A,B) from Paschen minimum."""
    A = math.e * math.log(1.0+1.0/gamma) / pd_min
    B = Vmin / pd_min
    return A, B
def meek_raether_streamer(pd, A_t, B_t, Ncrit=20.0):
    """Streamer inception (V) via Meek–Raether."""
    pd = np.asarray(pd, dtype=float)
    num = B_t * pd
    denom = np.log((A_t * pd) / Ncrit)
    return np.where(denom > 0, num/denom, np.nan)
