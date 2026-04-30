import plotly.graph_objects as go


def build_heatmap_2d(df):
    if df.empty:
        return go.Figure()

    fig = go.Figure(
        go.Densitymapbox(
            lat=df["reclat"],
            lon=df["reclong"],
            z=df["log_mass"],
            radius=15,
        )
    )
    fig.update_layout(
        mapbox=dict(style="carto-darkmatter", center=dict(lat=20, lon=0), zoom=1.2),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig
