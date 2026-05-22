import plotly.graph_objects as go


def build_meteorite_classes_barchart_plot(df):
    fig = go.Figure()

    if df.empty or "recclass" not in df.columns:
        fig.update_layout(
            template=None,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#c5c5c5"),
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            annotations=[
                dict(
                    text="No data available",
                    showarrow=False,
                    font=dict(size=16, color="#8d8d8d"),
                )
            ],
            margin=dict(l=30, r=20, t=20, b=40),
            height=500,
        )
        return fig

    classes = (
        df["recclass"]
        .dropna()
        .astype(str)
        .str.strip()
        .loc[lambda s: s != ""]
        .value_counts()
        .head(5)
        .sort_values(ascending=True)
    )

    fig.add_trace(
        go.Bar(
            x=classes.values,
            y=classes.index,
            orientation="h",
            text=classes.values,
            textposition="outside",
            marker=dict(
                color=["#335d96", "#3f6cae", "#4e7dc0", "#6394df", "#7aa6f0"],
                line=dict(color="rgba(255,255,255,0.18)", width=1),
            ),
            hovertemplate="Class: %{y}<br>Impacts: %{x}<extra></extra>",
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c5c5c5"),
        margin=dict(l=90, r=40, t=20, b=50),
        xaxis=dict(
            title="Number of Meteorites",
            gridcolor="#2e2e2e",
            zeroline=False,
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
        ),
        yaxis=dict(
            title="Meteorite Class",
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
        ),
        height=500,
    )

    return fig
