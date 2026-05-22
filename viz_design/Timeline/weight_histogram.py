import numpy as np
import plotly.graph_objects as go


def build_weight_histogram_plot(df):
    fig = go.Figure()

    if df.empty or "mass_g" not in df:
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

    masses = df["mass_g"].to_numpy(dtype=float)
    masses = masses[np.isfinite(masses) & (masses > 0)]
    log_masses = np.log10(masses)

    fig.add_trace(
        go.Histogram(
            x=log_masses,
            nbinsx=42,
            marker=dict(
                color="#7aa6f0",
                line=dict(color="rgba(17,17,17,0.9)", width=1),
            ),
            opacity=0.9,
            hovertemplate="log10(Mass g): %{x:.2f}<br>Impacts: %{y}<extra></extra>",
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c5c5c5"),
        bargap=0.02,
        margin=dict(l=60, r=24, t=20, b=60),
        xaxis=dict(
            title="log10(Mass in grams)",
            gridcolor="#2e2e2e",
            zeroline=False,
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
        ),
        yaxis=dict(
            title="Number of Meteorites",
            gridcolor="#2e2e2e",
            zeroline=False,
            tickfont=dict(color="#a9a9a9"),
            title_font=dict(color="#bcbcbc"),
        ),
        height=500,
    )
    return fig
