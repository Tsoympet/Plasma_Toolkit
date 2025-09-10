
import json, os, numpy as np
def paschen_voltage(pd, A, B, gamma=0.01):
    pd = np.asarray(pd, dtype=float)
    denom = np.log(A*pd) - np.log(np.log(1+1.0/gamma))
    return (B*pd)/denom
def meek_raether_streamer(pd, A_t, B_t, Ncrit=20.0):
    pd = np.asarray(pd, dtype=float); num = B_t*pd; denom = np.log((A_t*pd)/Ncrit)
    return np.where(denom>0, num/denom, np.nan)
def approx_equal(a,b,abs_tol,rel_tol):
    a=np.asarray(a,float); b=np.asarray(b,float); 
    if a.shape!=b.shape: return False
    diff=np.abs(a-b); return np.all((diff<=abs_tol)|(diff<=rel_tol*np.maximum(np.abs(a),np.abs(b))))
def test_regression_golden():
    base=os.path.dirname(__file__)+"/.."
    gpath=os.path.join(base,"data","golden_regression.json")
    with open(gpath,"r",encoding="utf-8") as f: g=json.load(f)
    A=g["paschen"]["A"]; B=g["paschen"]["B"]; gamma=g["paschen"]["gamma"]; pd=np.array(g["paschen"]["pd"],float)
    V_exp=np.array(g["paschen"]["V"],float); V=paschen_voltage(pd,A,B,gamma)
    assert approx_equal(V,V_exp,g["tolerances"]["abs_V"],g["tolerances"]["rel_V"])
    A=g["streamer"]["A"]; B=g["streamer"]["B"]; N=g["streamer"]["Ncrit"]; pd=np.array(g["streamer"]["pd"],float)
    V_exp=np.array(g["streamer"]["V"],float); V=meek_raether_streamer(pd,A,B,N)
    m=np.isfinite(V)&np.isfinite(V_exp); assert m.any(); 
    assert approx_equal(V[m],V_exp[m],g["tolerances"]["abs_V"],g["tolerances"]["rel_V"])
