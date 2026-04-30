import numpy as np
import pandas as pd


def format_mass(value_g):
    if pd.isna(value_g):
        return "NA"
    if value_g >= 1_000_000:
        value = value_g / 1_000_000
        unit = "t"
    elif value_g >= 1_000:
        value = value_g / 1_000
        unit = "kg"
    else:
        value = value_g
        unit = "g"

    if value >= 100:
        text = f"{value:,.0f}"
    elif value >= 10:
        text = f"{value:,.1f}".rstrip("0").rstrip(".")
    else:
        text = f"{value:,.2f}".rstrip("0").rstrip(".")
    return f"{text} {unit}"


def decade_ticks(min_log, max_log):
    start = int(np.floor(min_log))
    end = int(np.ceil(max_log))
    tickvals = list(range(start, end + 1))
    ticktext = [format_mass(10 ** exponent) for exponent in tickvals]
    return tickvals, ticktext
