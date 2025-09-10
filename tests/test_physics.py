
import numpy as np
from plasma_toolkit import paschen_voltage, meek_raether_streamer
def test_paschen_minimum_exists():
    A,B = 15.0, 365.0; pd = np.logspace(-3,3,800); V = paschen_voltage(pd,A,B,0.01)
    idx = np.nanargmin(V); assert 5 < idx < (len(V)-5); assert np.isfinite(V[idx]) and V[idx] > 0
def test_streamer_monotonic_with_ncrit():
    pd = np.logspace(-2,2,200); A_t,B_t=15.0,365.0
    V18 = meek_raether_streamer(pd,A_t,B_t,18.0); V22 = meek_raether_streamer(pd,A_t,B_t,22.0)
    m = np.isfinite(V18) & np.isfinite(V22); assert np.nanmedian(V22[m]) > np.nanmedian(V18[m])
