import pandas as pd


def simple_hybrid_sample(
    df,
    n,
    seed=42,
    middle_quantiles=(0.20, 0.80),
    smallest_mass_floor_g=1.0,
):
    """Simple deterministic hybrid sampler.

    Mixes: 20% biggest by mass, 20% smallest by mass (with a minimum mass
    floor), and 60% random points from the middle mass quantile band.
    """
    if n <= 0 or df.empty:
        return df.iloc[0:0]
    if len(df) <= n:
        return df.copy()

    work = df.copy()
    work["__mass_g__"] = pd.to_numeric(work["mass_g"], errors="coerce")
    valid = work.dropna(subset=["__mass_g__"]).copy()

    if valid.empty:
        return df.sample(n=min(n, len(df)), random_state=seed)

    n_biggest = int(round(n * 0.20))
    n_smallest = int(round(n * 0.20))
    n_middle = n - n_biggest - n_smallest

    selected_idx = []

    biggest = valid.nlargest(min(n_biggest, len(valid)), "__mass_g__")
    selected_idx.extend(biggest.index.tolist())

    remaining = valid.drop(index=selected_idx, errors="ignore")
    smallest_pool = remaining[remaining["__mass_g__"] >= smallest_mass_floor_g]
    if smallest_pool.empty:
        smallest_pool = remaining

    smallest = smallest_pool.nsmallest(min(n_smallest, len(smallest_pool)), "__mass_g__")
    selected_idx.extend(smallest.index.tolist())

    remaining = valid.drop(index=selected_idx, errors="ignore")
    if n_middle > 0 and not remaining.empty:
        q_low = float(valid["__mass_g__"].quantile(middle_quantiles[0]))
        q_high = float(valid["__mass_g__"].quantile(middle_quantiles[1]))
        middle_pool = remaining[
            (remaining["__mass_g__"] >= q_low) & (remaining["__mass_g__"] <= q_high)
        ]

        take_middle = min(n_middle, len(middle_pool))
        if take_middle > 0:
            middle = middle_pool.sample(n=take_middle, random_state=seed)
            selected_idx.extend(middle.index.tolist())

    remaining = valid.drop(index=selected_idx, errors="ignore")
    if len(selected_idx) < n and not remaining.empty:
        shortfall = n - len(selected_idx)
        fill = remaining.sample(n=min(shortfall, len(remaining)), random_state=seed + 1)
        selected_idx.extend(fill.index.tolist())

    if len(selected_idx) < n:
        shortfall = n - len(selected_idx)
        pool = df.drop(index=selected_idx, errors="ignore")
        if not pool.empty:
            fill = pool.sample(n=min(shortfall, len(pool)), random_state=seed + 2)
            selected_idx.extend(fill.index.tolist())

    out = df.loc[selected_idx].copy()
    if len(out) > n:
        out = out.sample(n=n, random_state=seed + 3)

    return out.sample(frac=1, random_state=seed + 4)


def limit_points(df, limit, sampling_mode="hybrid", seed=42):
    if df.empty or len(df) <= limit:
        return df

    if sampling_mode == "random":
        return df.sample(limit)

    if sampling_mode == "top_mass":
        return df.nlargest(limit, "mass_g")

    return simple_hybrid_sample(df, n=limit, seed=seed)
