from pathlib import Path
import pandas as pd
import requests

# Base directory = wherever data.py lives
BASE_DIR = Path(__file__).parent

def download_data():
    url = "https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.csv"

    raw_dir = BASE_DIR / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(raw_dir / "Meteorite_Landings.csv", "wb") as f:
        f.write(response.content)


def generate_cleaned_file() -> str:
    source_path = BASE_DIR / "raw" / "Meteorite_Landings.csv"
    cleaned_path = BASE_DIR / "processed" / "Meteorite_Landings_cleaned.csv"

    cleaned_path.parent.mkdir(parents=True, exist_ok=True)  # ← always creates next to the script

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


if __name__ == "__main__":
    download_data()
    generate_cleaned_file()