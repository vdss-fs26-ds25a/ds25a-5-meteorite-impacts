import pandas as pd

from point_sampling import limit_points


def filter_and_sample(
    df,
    years,
    mass_log,
    fall_types,
    limit,
    sampling_mode,
    seed=42,
):
    if df.empty:
        return pd.DataFrame()

    fall_mask = (
        df["fall"].isin(fall_types)
        if fall_types
        else pd.Series(True, index=df.index)
    )

    mask = (
        (df["year"] >= years[0])
        & (df["year"] <= years[1])
        & (df["log_mass"] >= mass_log[0])
        & (df["log_mass"] <= mass_log[1])
        & fall_mask
    )

    df_filtered = df[mask].copy()
    return limit_points(df_filtered, limit=limit, sampling_mode=sampling_mode, seed=seed)
