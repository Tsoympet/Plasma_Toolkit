
"""Uncertainty band utilities for gamma and Ncrit."""
import numpy as np
from .models import meek_raether_streamer
def gamma_band_vals(pd_axis, A_p, B_p, gmin, gmax, steps=20):
    gs = np.linspace(gmin, gmax, steps); M=[]
    for g in gs:
        denom = np.log(A_p*pd_axis) - np.log(np.log(1+1.0/g))
        V = (B_p * pd_axis)/denom; M.append(V)
    import numpy as _np
    M = _np.vstack(M); return _np.nanmin(M,axis=0), _np.nanmax(M,axis=0)
def ncrit_band_vals(pd_axis, A_t, B_t, nmin, nmax, steps=25):
    import numpy as _np
    Ns = _np.linspace(nmin, nmax, steps)
    M = [_np.asarray(meek_raether_streamer(pd_axis, A_t, B_t, N)) for N in Ns]
    M = _np.vstack(M); return _np.nanmin(M,axis=0), _np.nanmax(M,axis=0)
