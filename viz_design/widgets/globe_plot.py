import plotly.graph_objects as go

from formatting import decade_ticks, format_mass


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
        df_bin = df.copy()
        df_bin["lat_bin"] = df_bin["reclat"].round(0)
        df_bin["lon_bin"] = df_bin["reclong"].round(0)
        density = df_bin.groupby(["lat_bin", "lon_bin"]).size().reset_index(name="count")

        fig.add_trace(
            go.Scattergeo(
                lon=density["lon_bin"],
                lat=density["lat_bin"],
                mode="markers",
                hoverinfo="skip",
                marker=dict(
                    size=10,
                    opacity=0.6,
                    color=density["count"],
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
