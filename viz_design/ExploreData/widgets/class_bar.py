import plotly.express as px
import plotly.graph_objects as go


def build_class_bar(df):
    if df.empty:
        return go.Figure()

    top_classes = df["recclass"].value_counts().nlargest(10).reset_index(name="count")
    top_classes.columns = ["class", "count"]
    fig = px.bar(
        top_classes,
        x="class",
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
        xaxis=dict(
            title="METEORITE CLASS",
            showgrid=False,
            tickfont=dict(color="#666"),
            titlefont=dict(color="#888", size=9),
        ),
        yaxis=dict(title="COUNT", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
    )
    return fig
