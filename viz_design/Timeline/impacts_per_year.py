import pandas as pd
import plotly.graph_objects as go


def build_impacts_per_year_plot(df):
    fig = go.Figure()

    if df.empty or any(col not in df.columns for col in ("year", "fall")):
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

    chart_df = df[["year", "fall"]].copy()
    chart_df = chart_df[chart_df["fall"].isin(["Found", "Fell"])]
    chart_df["year"] = pd.to_numeric(chart_df["year"], errors="coerce")
    chart_df = chart_df.dropna(subset=["year"])
    chart_df["year"] = chart_df["year"].astype(int)

    if chart_df.empty:
        return fig

    counts = chart_df.groupby(["year", "fall"]).size().unstack(fill_value=0)
    years = list(range(int(chart_df["year"].min()), int(chart_df["year"].max()) + 1))
    counts = counts.reindex(years, fill_value=0)

    found = counts["Found"] if "Found" in counts else pd.Series(0, index=years)
    fallen = counts["Fell"] if "Fell" in counts else pd.Series(0, index=years)

    fig.add_trace(
        go.Scatter(
            x=years,
            y=found,
            mode="lines",
            name="Found",
            line=dict(color="#ff4d4f", width=2.4),
            hovertemplate="Year: %{x}<br>Found: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=years,
            y=fallen,
            mode="lines",
            name="Fallen",
            line=dict(color="#4da3ff", width=2.4),
            hovertemplate="Year: %{x}<br>Fallen: %{y}<extra></extra>",
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c5c5c5"),
        margin=dict(l=60, r=24, t=20, b=60),
        xaxis=dict(
            title="Year",
            gridcolor="#2e2e2e",
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
        ),
        yaxis=dict(
            title="Number of Meteorites",
            gridcolor="#2e2e2e",
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
            rangemode="tozero",
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="#c5c5c5"),
        ),
        height=500,
    )

    return fig
