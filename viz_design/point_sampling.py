import numpy as np
import pandas as pd


def _allocate_quotas(counts, target_n, min_per_group=5):
    if target_n <= 0 or counts.empty:
        return pd.Series(0, index=counts.index, dtype=int)

    counts = counts.astype(int)
    groups = len(counts)

    if target_n < groups:
        top_groups = counts.sort_values(ascending=False).head(target_n).index
        out = pd.Series(0, index=counts.index, dtype=int)
        out.loc[top_groups] = 1
        return out

    per_group_floor = min_per_group if target_n >= min_per_group * groups else 1
    quotas = counts.clip(upper=per_group_floor).astype(int)

    remaining = target_n - int(quotas.sum())
    if remaining <= 0:
        return quotas

    capacity = (counts - quotas).clip(lower=0).astype(int)
    active = capacity[capacity > 0]
    if active.empty:
        return quotas

    weights = np.sqrt(counts.loc[active.index].astype(float))
    raw = weights / weights.sum() * remaining
    extra = np.floor(raw).astype(int)
    extra = np.minimum(extra, active.values)
    extra_series = pd.Series(extra, index=active.index, dtype=int)
    quotas.loc[extra_series.index] += extra_series

    leftover = remaining - int(extra_series.sum())
    if leftover > 0:
        capacity = (counts - quotas).clip(lower=0).astype(int)
        active = capacity[capacity > 0]
        if not active.empty:
            weights = np.sqrt(counts.loc[active.index].astype(float))
            raw = weights / weights.sum() * leftover
            frac = (raw - np.floor(raw)).sort_values(ascending=False)
            for idx in frac.index:
                if leftover <= 0:
                    break
                if quotas.loc[idx] < counts.loc[idx]:
                    quotas.loc[idx] += 1
                    leftover -= 1

            if leftover > 0:
                for idx in active.sort_values(ascending=False).index:
                    if leftover <= 0:
                        break
                    if quotas.loc[idx] < counts.loc[idx]:
                        quotas.loc[idx] += 1
                        leftover -= 1

    return quotas


def _geo_balanced_sample(group_df, n, rng, cell_col="geo_id", per_cell_cap=5):
    if n <= 0 or group_df.empty:
        return group_df.iloc[0:0]
    if len(group_df) <= n:
        return group_df

    cell_counts = group_df[cell_col].value_counts()
    cell_quotas = _allocate_quotas(cell_counts, n, min_per_group=1)
    cell_quotas = np.minimum(cell_quotas, per_cell_cap)
    selected_idx = []

    for cell, q in cell_quotas.items():
        if q <= 0:
            continue
        candidates = group_df[group_df[cell_col] == cell]
        if len(candidates) <= q:
            selected_idx.extend(candidates.index.tolist())
        else:
            chosen = rng.choice(candidates.index.to_numpy(), size=q, replace=False)
            selected_idx.extend(chosen.tolist())

    if len(selected_idx) >= n:
        if len(selected_idx) > n:
            chosen = rng.choice(np.array(selected_idx), size=n, replace=False)
            selected_idx = chosen.tolist()
        return group_df.loc[selected_idx]

    shortfall = n - len(selected_idx)
    remaining_df = group_df.drop(index=selected_idx, errors="ignore")
    if shortfall > 0 and not remaining_df.empty:
        if len(remaining_df) <= shortfall:
            selected_idx.extend(remaining_df.index.tolist())
        else:
            chosen = rng.choice(remaining_df.index.to_numpy(), size=shortfall, replace=False)
            selected_idx.extend(chosen.tolist())

    return group_df.loc[selected_idx]


def representative_sample(df, n, seed=42):
    if n <= 0 or df.empty:
        return df.iloc[0:0]
    if len(df) <= n:
        return df.copy()

    work = df.copy()
    work["mass_bin"] = pd.cut(
        work["log_mass"],
        bins=np.arange(-2, 9, 1),
        right=False,
        include_lowest=True,
        labels=False,
    )
    work["year_bin"] = pd.cut(
        work["year"],
        bins=[800, 1900, 1950, 1980, 1990, 2000, 2005, 2010, 2026],
        right=False,
        include_lowest=True,
        labels=False,
    )
    work = work.dropna(subset=["mass_bin", "year_bin"]).copy()
    if work.empty:
        return df.sample(n=min(n, len(df)), random_state=seed)

    work["mass_bin"] = work["mass_bin"].astype(int)
    work["year_bin"] = work["year_bin"].astype(int)
    work["lat_cell"] = np.floor((work["reclat"] + 90) / 8).astype(int)
    work["lon_cell"] = np.floor((work["reclong"] + 180) / 8).astype(int)
    work["geo_id"] = work["lat_cell"].astype(str) + "_" + work["lon_cell"].astype(str)

    strata_counts = work.groupby(["mass_bin", "year_bin"], observed=True).size()
    strata_quotas = _allocate_quotas(strata_counts, n, min_per_group=5)

    rng = np.random.default_rng(seed)
    selected_idx = []
    for key, q in strata_quotas.items():
        if q <= 0:
            continue
        strata_df = work[(work["mass_bin"] == key[0]) & (work["year_bin"] == key[1])]
        strata_df = strata_df.drop(index=selected_idx, errors="ignore")
        if strata_df.empty:
            continue
        sampled = _geo_balanced_sample(strata_df, min(q, len(strata_df)), rng)
        selected_idx.extend(sampled.index.tolist())

    if len(selected_idx) > n:
        selected_idx = rng.choice(np.array(selected_idx), size=n, replace=False).tolist()

    if len(selected_idx) < n:
        shortfall = n - len(selected_idx)
        remaining = df.drop(index=selected_idx, errors="ignore")
        if not remaining.empty:
            add = remaining.sample(n=min(shortfall, len(remaining)), random_state=seed)
            selected_idx.extend(add.index.tolist())

    out = df.loc[selected_idx].copy()
    if len(out) > n:
        out = out.sample(n=n, random_state=seed)
    return out


def anchor_sample(df, n):
    if n <= 0 or df.empty:
        return df.iloc[0:0]
    if len(df) <= n:
        return df.copy()

    n_top_mass = int(round(n * 0.40))
    n_recent = int(round(n * 0.30))
    n_rare = int(round(n * 0.20))
    n_fell = n - n_top_mass - n_recent - n_rare

    selected_idx = []

    top_mass = df.nlargest(n_top_mass, "mass_g")
    selected_idx.extend(top_mass.index.tolist())

    recent = df.sort_values(["year", "mass_g"], ascending=[False, False]).head(n_recent)
    for idx in recent.index:
        if idx not in selected_idx:
            selected_idx.append(idx)

    class_counts = df["recclass"].value_counts()
    rare_df = df[df["recclass"].map(class_counts) <= 5].copy()
    if not rare_df.empty:
        rare_df = rare_df.sort_values("mass_g", ascending=False).drop_duplicates("recclass")
        for idx in rare_df.head(n_rare).index:
            if idx not in selected_idx:
                selected_idx.append(idx)

    fell_df = df[df["fall"] == "Fell"]
    if not fell_df.empty:
        fell_top = fell_df.nlargest(n_fell, "mass_g")
        for idx in fell_top.index:
            if idx not in selected_idx:
                selected_idx.append(idx)

    if len(selected_idx) < n:
        remainder = df.drop(index=selected_idx, errors="ignore").nlargest(
            n - len(selected_idx), "mass_g"
        )
        selected_idx.extend(remainder.index.tolist())

    if len(selected_idx) > n:
        selected_idx = selected_idx[:n]

    return df.loc[selected_idx].copy()


def limit_points(df, limit, sampling_mode="hybrid", seed=42):
    if df.empty or len(df) <= limit:
        return df

    if sampling_mode == "random":
        return df.sample(limit, random_state=seed)

    if sampling_mode == "top_mass":
        return df.nlargest(limit, "mass_g")

    anchor_n = int(round(limit * 0.15))
    anchor_n = max(5, anchor_n)
    anchor_n = min(anchor_n, limit)
    anchors = anchor_sample(df, n=min(anchor_n, len(df)))

    remaining_df = df.drop(index=anchors.index, errors="ignore")
    repr_n = limit - len(anchors)
    repr_sample = representative_sample(remaining_df, n=max(0, repr_n), seed=seed)

    combined = pd.concat([anchors, repr_sample], axis=0)
    if len(combined) < limit:
        missing = limit - len(combined)
        pool = df.drop(index=combined.index, errors="ignore")
        if not pool.empty:
            fill = pool.sample(n=min(missing, len(pool)), random_state=seed)
            combined = pd.concat([combined, fill], axis=0)

    if len(combined) > limit:
        combined = combined.head(limit)

    return combined.sample(frac=1, random_state=seed)
