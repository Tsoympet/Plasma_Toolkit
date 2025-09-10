
"""Light validators."""
import numpy as np, pandas as pd, os
REQUIRED_COLS=["pd_Torr_cm","Vb_V"]
def validate_dataframe(df):
    if df is None: return ["DataFrame is None"]
    errs=[]; 
    for c in REQUIRED_COLS:
        if c not in df.columns: errs.append(f"Missing column {c}")
    if errs: return errs
    if df[REQUIRED_COLS].isna().any().any(): errs.append("NaNs in required columns")
    for c in REQUIRED_COLS:
        if not np.issubdtype(df[c].dtype, np.number):
            try: pd.to_numeric(df[c])
            except Exception: errs.append(f"Non-numeric in {c}")
    if (df["pd_Torr_cm"]<=0).any() or (df["Vb_V"]<=0).any(): errs.append("Non-positive values")
    return errs
def validate_path(path): return os.path.exists(path) and os.path.isfile(path)
