import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from shiny import App, render, ui, reactive
from shinywidgets import output_widget, render_widget

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

# Load and clean data
def load_data():
    try:
        df = pd.read_csv("Meteorite_Landings.csv")
        df.columns = df.columns.str.strip()
        for col in ["year", "mass (g)", "reclat", "reclong"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.rename(columns={"mass (g)": "mass_g"})
        df = df.dropna(subset=['year', 'mass_g', 'reclat', 'reclong'])
        df = df[(df['year'] >= 800) & (df['year'] <= 2025)]
        df = df[(df['reclat'] != 0) | (df['reclong'] != 0)]
        df = df[(df['reclat'].between(-90, 90)) & (df['reclong'].between(-180, 180))]
        df = df[df["mass_g"] > 0]
        df['year'] = df['year'].astype(int)
        df['log_mass'] = np.log10(df['mass_g'])
        return df
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

meteorites = load_data()

if meteorites.empty:
    MASS_LOG_MIN = -2.0
    MASS_LOG_MAX = 8.0
else:
    MASS_LOG_MIN = float(np.floor(meteorites["log_mass"].min() * 10) / 10)
    MASS_LOG_MAX = float(np.ceil(meteorites["log_mass"].max() * 10) / 10)

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css"),
        ui.tags.style("""
            body { background-color: #121212; color: #e0e0e0; margin: 0; padding: 0; }
            .container-fluid { padding: 0 !important; }
            
            .menu-widget {
                position: fixed;
                top: 25px;
                left: 25px;
                width: 340px;
                max-height: 85vh;
                background: #2a2a2a;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
                padding: 20px;
                z-index: 2000;
                box-shadow: 0 15px 50px rgba(0, 0, 0, 0.9);
                overflow-y: auto;
            }
            
            .action-button.close-btn {
                position: absolute; top: 15px; right: 15px;
                background: none !important; border: none !important;
                color: #888 !important; font-size: 20px;
            }
            
            .action-button.open-btn {
                position: fixed; top: 25px; left: 25px;
                width: 55px; height: 55px;
                background: #2a2a2a !important;
                border-radius: 0px !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                color: white !important; font-size: 28px;
                display: flex; align-items: center; justify-content: center;
                z-index: 1999;
            }
            
            .chart-card {
                background: #1f1f1f; border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px; margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            
            .irs-grid-text { color: #777 !important; }
            .irs-single, .irs-from, .irs-to { background: #0d6efd !important; border-color: #0a58ca !important; }
            .irs-bar { background: #0d6efd !important; border-top: 1px solid #0d6efd !important; border-bottom: 1px solid #0d6efd !important; }
            .irs-handle { border: 1px solid #0d6efd !important; background: #0d6efd !important; }
            
            label { font-weight: 600; color: #999 !important; text-transform: uppercase; font-size: 11px; letter-spacing: 1.5px; margin-bottom: 10px; }
            
            h3 { font-weight: 800; color: #fff; letter-spacing: -0.5px; margin-top: 0; }
            .impact-count { font-size: 14px; color: #00ff00 !important; font-family: monospace; font-weight: bold; }
            
            /* Toggle Switch Labels */
            .form-check-label { color: #bbb !important; font-size: 12px; font-weight: 500; }
        """)
    ),
    
    # Globe Section
    ui.div(
        output_widget("globe_plot", height="70vh", width="100%"),
        style="background-color: #121212; border-bottom: 1px solid #1a1a1a; overflow: hidden; padding-top: 40px;"
    ),
    
    # Content Section
    ui.div(
        ui.row(
            ui.column(8, 
                ui.div(
                    ui.h4("GLOBAL DISTRIBUTION HEATMAP", style="margin-bottom: 20px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("heatmap_2d", height="400px"),
                    class_="chart-card"
                ),
            ),
            ui.column(4, 
                ui.div(
                    ui.h4("IMPACTS PER YEAR", style="margin-bottom: 20px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("timeline_plot", height="400px"),
                    class_="chart-card"
                )
            ),
            style="padding: 30px 30px 0 30px;"
        ),
        ui.row(
            ui.column(6, 
                ui.div(
                    ui.h4("MASS DISTRIBUTION (LOG SCALE)", style="margin-bottom: 20px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("mass_hist", height="400px"),
                    class_="chart-card"
                ),
            ),
            ui.column(6, 
                ui.div(
                    ui.h4("TOP 10 METEORITE CLASSES", style="margin-bottom: 20px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("class_bar", height="400px"),
                    class_="chart-card"
                )
            ),
            style="padding: 0 30px 30px 30px;"
        ),
        style="position: relative; z-index: 10; background-color: #121212;"
    ),
    
    ui.output_ui("menu_container"),
)

def server(input, output, session):
    show_menu = reactive.Value(True)
    
    # Defaults
    cur_years = reactive.Value([1950, 2024])
    cur_mass_log = reactive.Value([MASS_LOG_MIN, MASS_LOG_MAX])
    cur_limit = reactive.Value(1000)
    cur_fall_filter = reactive.Value(["Fell", "Found"])
    
    # Trace Toggles
    show_impacts = reactive.Value(True)
    show_heatmap = reactive.Value(False)

    @reactive.effect
    @reactive.event(input.toggle_menu)
    def _():
        try:
            cur_years.set(input.year_range())
            cur_mass_log.set(input.mass_range_log())
            cur_limit.set(input.limit())
            cur_fall_filter.set(input.fall_filter())
            show_impacts.set(input.show_impacts())
            show_heatmap.set(input.show_heatmap())
        except:
            pass
        show_menu.set(not show_menu())

    @reactive.calc
    def filtered_data():
        if meteorites.empty:
            return pd.DataFrame()
        try:
            years = input.year_range()
            mass_log = input.mass_range_log()
            limit = input.limit()
            fall_types = input.fall_filter()
        except:
            years = cur_years()
            mass_log = cur_mass_log()
            limit = cur_limit()
            fall_types = cur_fall_filter()
        
        mask = (df['year'] >= years[0]) & (df['year'] <= years[1]) & \
               (df['log_mass'] >= mass_log[0]) & (df['log_mass'] <= mass_log[1]) & \
               (df['fall'].isin(fall_types)) if not (df := meteorites).empty else []
        
        df_filtered = df[mask].copy()
        if len(df_filtered) > limit:
            df_filtered = df_filtered.sample(limit, random_state=42)
        return df_filtered

    @output
    @render.ui
    def menu_container():
        if show_menu():
            return ui.div(
                ui.input_action_button(
                    "toggle_menu",
                    ui.tags.i(class_="bi bi-x-lg"),
                    class_="close-btn"
                ),
                ui.h3("ORBITAL DATA"),
                ui.div(ui.output_text("count_summary"), class_="impact-count"),
                ui.hr(style="border-color: #333; margin: 15px 0;"),
                ui.input_switch("show_impacts", "Show Impacts", value=show_impacts()),
                ui.input_switch("show_heatmap", "Show 3D Heatmap", value=show_heatmap()),
                ui.hr(style="border-color: #333; margin: 15px 0;"),
                ui.input_checkbox_group(
                    "fall_filter", "FALL TYPE",
                    {"Fell": "Fallen", "Found": "Found"},
                    selected=cur_fall_filter(),
                    inline=True
                ),
                ui.input_slider("year_range", "YEARS", 
                                min=int(meteorites['year'].min()), 
                                max=int(meteorites['year'].max()), 
                                value=cur_years(), 
                                sep=""),
                ui.input_slider("mass_range_log", "MASS (g/kg/t)", 
                                min=MASS_LOG_MIN, max=MASS_LOG_MAX, value=cur_mass_log(), step=0.1),
                ui.div(ui.output_text("mass_range_label"), style="font-size: 12px; color: #bbb; margin-top: 6px;"),
                ui.input_numeric("limit", "MAX POINTS", value=cur_limit(), min=1, max=45000),
                class_="menu-widget"
            )
        else:
            return ui.input_action_button(
                "toggle_menu",
                ui.tags.i(class_="bi bi-list"),
                class_="open-btn"
            )

    @render.text
    def count_summary():
        df = filtered_data()
        return f"{len(df):,} DETECTED IMPACTS"

    @render.text
    def mass_range_label():
        try:
            mass_log = input.mass_range_log()
        except:
            mass_log = cur_mass_log()
        low_g = 10 ** mass_log[0]
        high_g = 10 ** mass_log[1]
        return f"Selected mass: {format_mass(low_g)} to {format_mass(high_g)}"

    @render_widget
    def globe_plot():
        df = filtered_data()
        fig = go.Figure()

        fig.update_geos(
            resolution=110,
            projection_type="orthographic",
            showland=True, landcolor="#252525",
            showocean=True, oceancolor="#191919",
            showcountries=True, countrycolor="#333333",
            showlakes=True, lakecolor="#0d0d0d",
            showrivers=True, rivercolor="#0d0d0d",
            # Not working dont know why
            #showsubunits=True, subunitcolor="#333333",
            bgcolor="rgba(0,0,0,0)",
            showcoastlines=True, coastlinecolor="#444444",
            showframe=False,
            projection_scale=1.0, 
            center=dict(lat=0, lon=0),
            projection_rotation=dict(lon=0, lat=0, roll=0),
        )

        # Toggle Heatmap Layer (using hex binning simulation on Scattergeo)
        # Using a slightly reactive approach to read the UI state
        try:
            s_heatmap = input.show_heatmap()
        except:
            s_heatmap = show_heatmap()

        if s_heatmap and not df.empty:
            # Simple binning for "heatmap" effect on globe
            # Rounding lat/lon to create grid cells
            df_bin = df.copy()
            df_bin['lat_bin'] = df_bin['reclat'].round(0)
            df_bin['lon_bin'] = df_bin['reclong'].round(0)
            
            density = df_bin.groupby(['lat_bin', 'lon_bin']).size().reset_index(name='count')
            
            fig.add_trace(go.Scattergeo(
                lon = density['lon_bin'],
                lat = density['lat_bin'],
                mode = 'markers',
                hoverinfo = 'skip',
                marker = dict(
                    size = 10,
                    opacity = 0.6,
                    color = density['count'],
                    colorscale = 'Hot',
                    showscale = False,
                    # Blurry effect using symbol and line
                    line = dict(width=0)
                )
            ))

        # Toggle Individual Impact Dots
        try:
            s_impacts = input.show_impacts()
        except:
            s_impacts = show_impacts()

        if s_impacts and not df.empty:
            try:
                mass_log = input.mass_range_log()
            except:
                mass_log = cur_mass_log()
            tickvals, ticktext = decade_ticks(mass_log[0], mass_log[1])

            hover_texts = []
            for _, row in df.iterrows():
                fall_type = "Fallen" if row['fall'] == 'Fell' else ("Found" if row['fall'] == 'Found' else "")
                year_label = f"Year {fall_type}" if fall_type else "Year"
                text = (f"<b>{row['name']}</b><br>"
                        f"Class: {row['recclass']}<br>"
                        f"Mass: {format_mass(row['mass_g'])}<br>"
                        f"{year_label}: {row['year']}<br>"
                        f"Coord: {row['reclat']:.2f}, {row['reclong']:.2f}")
                hover_texts.append(text)

            fig.add_trace(go.Scattergeo(
                lon = df['reclong'],
                lat = df['reclat'],
                text = hover_texts,
                hoverinfo = 'text',
                mode = 'markers',
                marker = dict(
                    size = 5 + (df['log_mass'] * 1.5),
                    opacity = 0.8,
                    color = df['log_mass'],
                    cmin = mass_log[0],
                    cmax = mass_log[1],
                    colorscale = 'RdYlGn',
                    reversescale = True, 
                    showscale = True,
                    colorbar = dict(
                        title = "MASS (g/kg/t)",
                        titleside = "right",
                        thickness = 15,
                        len = 0.8,
                        x = 0.95,
                        y = 0.5,
                        tickvals = tickvals,
                        ticktext = ticktext,
                        tickfont = dict(color="#888", size=10),
                        titlefont = dict(color="#888", size=10)
                    ),
                    line = dict(width=0.5, color='rgba(255,255,255,0.2)')
                )
            ))

        fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            scene=dict(dragmode="orbit"),
            geo=dict(domain=dict(x=[0, 1], y=[0, 1])),
            height=600 # Size of Globe canvas
        )

        return fig

    @render_widget
    def heatmap_2d():
        df = filtered_data()
        if df.empty: return go.Figure()
        fig = go.Figure(go.Densitymapbox(
            lat=df['reclat'], lon=df['reclong'], z=df['log_mass'],
            radius=15
        ))
        fig.update_layout(
            mapbox=dict(style="carto-darkmatter", center=dict(lat=20, lon=0), zoom=1.2),
            margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
        )
        return fig

    @render_widget
    def timeline_plot():
        df = filtered_data()
        if df.empty: return go.Figure()
        yearly_counts = df.groupby('year').size().reset_index(name='count')
        fig = px.bar(yearly_counts, x='year', y='count', color='count', color_continuous_scale='RdYlGn_r')
        fig.update_layout(
            margin={"r":10,"t":10,"l":10,"b":10},
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False, coloraxis_showscale=False,
            xaxis=dict(title="YEAR", showgrid=False, tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
            yaxis=dict(title="FREQUENCY", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9))
        )
        return fig

    @render_widget
    def mass_hist():
        df = filtered_data()
        if df.empty: return go.Figure()
        fig = px.histogram(df, x="log_mass", nbins=50, color_discrete_sequence=['#555'])
        tickvals, ticktext = decade_ticks(df["log_mass"].min(), df["log_mass"].max())
        fig.update_layout(
            margin={"r":10,"t":10,"l":10,"b":10},
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(
                title="MASS (g/kg/t)",
                tickvals=tickvals,
                ticktext=ticktext,
                showgrid=False,
                tickfont=dict(color="#666"),
                titlefont=dict(color="#888", size=9)
            ),
            yaxis=dict(title="COUNT", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9))
        )
        return fig

    @render_widget
    def class_bar():
        df = filtered_data()
        if df.empty: return go.Figure()
        # Top 10 classes
        top_classes = df['recclass'].value_counts().nlargest(10).reset_index(name='count')
        top_classes.columns = ['class', 'count']
        fig = px.bar(top_classes, x='class', y='count', color='count', color_continuous_scale='RdYlGn_r')
        fig.update_layout(
            margin={"r":10,"t":10,"l":10,"b":10},
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False, coloraxis_showscale=False,
            xaxis=dict(title="METEORITE CLASS", showgrid=False, tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
            yaxis=dict(title="COUNT", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9))
        )
        return fig

app = App(app_ui, server)
