"""
validators.py — Validation utilities for Plasma Toolkit

Checks input DataFrames for required columns, numeric types,
and valid ranges.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED_COLS = ["pd_Torr_cm", "Vb_V"]


def validate_dataframe(df: pd.DataFrame) -> list[str]:
    """
    Validate that the input DataFrame has the correct structure.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with Paschen / breakdown data. Must include columns
        "pd_Torr_cm" and "Vb_V".

    Returns
    -------
    list[str]
        A list of error messages. Empty if valid.
    """
    errors: list[str] = []

    # Check required columns
    for col in REQUIRED_COLS:
        if col not in df.columns:
            errors.append(f"Missing required column: {col}")

    # Check numeric types
    for col in REQUIRED_COLS:
        if col in df.columns:
            if not np.issubdtype(df[col].dtype, np.number):
                try:
                    pd.to_numeric(df[col])
                except Exception:
                    errors.append(f"Non-numeric values in column '{col}'")

    # Check positive values
    if (
        "pd_Torr_cm" in df.columns
        and "Vb_V" in df.columns
        and ((df["pd_Torr_cm"] <= 0).any() or (df["Vb_V"] <= 0).any())
    ):
        errors.append("Non-positive values found in pd_Torr_cm or Vb_V")

    return errors
