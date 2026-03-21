import plotly.express as px
import plotly.graph_objects as go

from formatting import decade_ticks


def build_mass_hist(df):
    if df.empty:
        return go.Figure()

    fig = px.histogram(df, x="log_mass", nbins=50, color_discrete_sequence=["#555"])
    tickvals, ticktext = decade_ticks(df["log_mass"].min(), df["log_mass"].max())
    fig.update_layout(
        margin={"r": 10, "t": 10, "l": 10, "b": 10},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            title="MASS (g/kg/t)",
            tickvals=tickvals,
            ticktext=ticktext,
            showgrid=False,
            tickfont=dict(color="#666"),
            titlefont=dict(color="#888", size=9),
        ),
        yaxis=dict(title="COUNT", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
    )
    return fig
