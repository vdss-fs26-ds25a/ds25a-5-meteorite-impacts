import numpy as np
import plotly.graph_objects as go
from scipy.ndimage import gaussian_filter

from viz_design.ExploreData.formatting import decade_ticks, format_mass


def _build_smoothed_geo_heat(df, n_lat=140, n_lon=280, sigma=1.35):
    lat = df["reclat"].to_numpy(dtype=float)
    lon = df["reclong"].to_numpy(dtype=float)

    valid = np.isfinite(lat) & np.isfinite(lon)
    lat = np.clip(lat[valid], -90.0, 90.0)
    lon = ((lon[valid] + 180.0) % 360.0) - 180.0

    if lat.size == 0:
        return None, None, None

    lat_edges = np.linspace(-90.0, 90.0, n_lat + 1)
    lon_edges = np.linspace(-180.0, 180.0, n_lon + 1)

    density, _, _ = np.histogram2d(lat, lon, bins=[lat_edges, lon_edges])
    smoothed = gaussian_filter(density, sigma=(sigma, sigma), mode=("nearest", "wrap"))

    positive = smoothed[smoothed > 0]
    if positive.size == 0:
        return None, None, None

    low = float(np.percentile(positive, 2.5))
    high = float(np.percentile(positive, 99.5))
    if high <= low:
        low = float(np.min(positive))
        high = float(np.max(positive))

    norm = np.clip((smoothed - low) / max(high - low, 1e-9), 0.0, 1.0)
    lat_centers = (lat_edges[:-1] + lat_edges[1:]) / 2.0
    lon_centers = (lon_edges[:-1] + lon_edges[1:]) / 2.0

    lon_grid, lat_grid = np.meshgrid(lon_centers, lat_centers)
    heat = np.power(norm, 0.65).ravel()
    lon_flat = lon_grid.ravel()
    lat_flat = lat_grid.ravel()

    mask = heat >= 0.025
    if not np.any(mask):
        return None, None, None

    lon_sel = lon_flat[mask]
    lat_sel = lat_flat[mask]
    heat_sel = heat[mask]

    # Keep payload responsive in Shiny while preserving strongest density cells.
    if heat_sel.size > 9000:
        idx = np.argpartition(heat_sel, -9000)[-9000:]
        lon_sel = lon_sel[idx]
        lat_sel = lat_sel[idx]
        heat_sel = heat_sel[idx]

    return lon_sel, lat_sel, heat_sel


def build_globe_plot(df, mass_log, show_impacts=True, show_heatmap=False):
    fig = go.Figure()

    fig.update_geos(
        resolution=110,
        projection_type="orthographic",
        showland=True,
        landcolor="#252525",
        showocean=True,
        oceancolor="#191919",
        showcountries=True,
        countrycolor="#333333",
        showlakes=True,
        lakecolor="#0d0d0d",
        showrivers=True,
        rivercolor="#0d0d0d",
        bgcolor="rgba(0,0,0,0)",
        showcoastlines=True,
        coastlinecolor="#444444",
        showframe=False,
        projection_scale=1.0,
        center=dict(lat=0, lon=0),
        projection_rotation=dict(lon=0, lat=0, roll=0),
    )

    if show_heatmap and not df.empty:
        lon_heat, lat_heat, heat = _build_smoothed_geo_heat(df)
        if heat is not None:
            fig.add_trace(
                go.Scattergeo(
                    lon=lon_heat,
                    lat=lat_heat,
                    mode="markers",
                    hoverinfo="skip",
                    marker=dict(
                        symbol="hexagon",
                        size=3.0 + (heat * 7.5),
                        opacity=0.2 + (heat * 0.7),
                        color=heat,
                        cmin=0,
                        cmax=1,
                        colorscale="Hot",
                        showscale=False,
                        line=dict(width=0),
                    ),
                )
            )

    if show_impacts and not df.empty:
        tickvals, ticktext = decade_ticks(mass_log[0], mass_log[1])
        hover_texts = []

        for _, row in df.iterrows():
            fall_type = "Fallen" if row["fall"] == "Fell" else ("Found" if row["fall"] == "Found" else "")
            year_label = f"Year {fall_type}" if fall_type else "Year"
            text = (
                f"<b>{row['name']}</b><br>"
                f"Class: {row['recclass']}<br>"
                f"Mass: {format_mass(row['mass_g'])}<br>"
                f"{year_label}: {row['year']}<br>"
                f"Coord: {row['reclat']:.2f}, {row['reclong']:.2f}"
            )
            hover_texts.append(text)

        fig.add_trace(
            go.Scattergeo(
                lon=df["reclong"],
                lat=df["reclat"],
                text=hover_texts,
                hoverinfo="text",
                mode="markers",
                marker=dict(
                    size=5 + (df["log_mass"] * 1.5),
                    opacity=0.8,
                    color=df["log_mass"],
                    cmin=mass_log[0],
                    cmax=mass_log[1],
                    colorscale="RdYlGn",
                    reversescale=True,
                    showscale=True,
                    colorbar=dict(
                        title="MASS (g/kg/t)",
                        titleside="right",
                        thickness=15,
                        len=0.8,
                        x=0.95,
                        y=0.5,
                        tickvals=tickvals,
                        ticktext=ticktext,
                        tickfont=dict(color="#888", size=10),
                        titlefont=dict(color="#888", size=10),
                    ),
                    line=dict(width=0.5, color="rgba(255,255,255,0.2)"),
                ),
            )
        )

    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        scene=dict(dragmode="orbit"),
        geo=dict(domain=dict(x=[0, 1], y=[0, 1])),
        height=600,
    )

    return fig
