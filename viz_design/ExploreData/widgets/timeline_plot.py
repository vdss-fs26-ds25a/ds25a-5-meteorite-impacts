import plotly.express as px
import plotly.graph_objects as go


def build_timeline_plot(df):
    if df.empty:
        return go.Figure()

    yearly_counts = df.groupby("year").size().reset_index(name="count")
    fig = px.bar(
        yearly_counts,
        x="year",
        y="count",
        color="count",
        color_continuous_scale="RdYlGn_r",
    )
    fig.update_layout(
        margin={"r": 10, "t": 10, "l": 10, "b": 10},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        coloraxis_showscale=False,
        xaxis=dict(title="YEAR", showgrid=False, tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
        yaxis=dict(
            title="FREQUENCY",
            showgrid=True,
            gridcolor="#222",
            tickfont=dict(color="#666"),
            titlefont=dict(color="#888", size=9),
        ),
    )
    return fig
