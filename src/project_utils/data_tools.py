from __future__ import annotations

import pandas as pd


def dfskimmer(df):
    """
    Provides a cursory glance at the dataframe descriptive statistics.
    Most output columns speak for themselves.

    unique: The number of unique values
    top:    The mode of the variable (most common value)
    freq:   Frequency of the mode

    returns a Pandas DataFrame.
    """

    n_rows = len(df)

    meta = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "missing": df.isna().sum(),
        "complete": df.count(),
        "unique": df.nunique(),
    })

    # Numeric statistics in bulk
    numeric = df.select_dtypes(include="number")

    if not numeric.empty:
        numeric_stats = pd.DataFrame({
            "mean": numeric.mean(),
            "std": numeric.std(),
            "skew": numeric.skew(),
            "kurtosis": numeric.kurt(),
            "min": numeric.min(),
            "p25": numeric.quantile(0.25),
            "median": numeric.median(),
            "p75": numeric.quantile(0.75),
            "p99": numeric.quantile(0.99),
            "max": numeric.max(),
        })
    else:
        numeric_stats = pd.DataFrame()

    rows = []
    
    for col in df.columns:
        s = df[col]

        # One value_counts call instead of mode() + value_counts()
        vc = s.value_counts(dropna=True)

        if len(vc):
            top = vc.index[0]
            freq = vc.iloc[0]
        else:
            top = None
            freq = None

        row = {
            "column": col,
            **meta.loc[col].to_dict(),
            "top": top,
            "freq": freq,
        }

        if col in numeric_stats.index:
            row.update(numeric_stats.loc[col].to_dict())

        rows.append(row)

    return pd.DataFrame(rows)


__all__ = ["dfskimmer"]