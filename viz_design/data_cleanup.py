from pathlib import Path

import pandas as pd


def generate_cleaned_file(
    source_file: str = "Meteorite_Landings.csv",
    cleaned_file: str = "Meteorite_Landings_cleaned.csv",
) -> str:
    source_path = Path(source_file)
    cleaned_path = Path(cleaned_file)

    df = pd.read_csv(source_path)
    df.columns = df.columns.str.strip()

    for col in ["year", "mass (g)", "reclat", "reclong"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.rename(columns={"mass (g)": "mass_g"})
    df = df.dropna(subset=["year", "mass_g", "reclat", "reclong"])
    df = df[(df["year"] >= 800) & (df["year"] <= 2025)]
    df = df[(df["reclat"] != 0) | (df["reclong"] != 0)]
    df = df[(df["reclat"].between(-90, 90)) & (df["reclong"].between(-180, 180))]
    df = df[df["mass_g"] > 0]
    df["year"] = df["year"].astype(int)

    df.to_csv(cleaned_path, index=False)
    return str(cleaned_path)
