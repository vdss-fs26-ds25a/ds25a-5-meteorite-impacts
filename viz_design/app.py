import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from shiny import App, render, ui, reactive
from shinywidgets import output_widget, render_widget

# Load and clean data
def load_data():
    try:
        df = pd.read_csv("Meteorite_Landings.csv")
        df.columns = df.columns.str.strip()
        df = df.dropna(subset=['year', 'mass (g)', 'reclat', 'reclong'])
        df = df[(df['year'] >= 800) & (df['year'] <= 2025)]
        df = df[(df['reclat'] != 0) | (df['reclong'] != 0)]
        df = df[(df['reclat'].between(-90, 90)) & (df['reclong'].between(-180, 180))]
        df['year'] = df['year'].astype(int)
        df['log_mass'] = np.log10(df['mass (g)'].clip(lower=0.1))
        return df
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

meteorites = load_data()

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css"),
        ui.tags.style("""
            /* Page Background: Deep Pure Black */
            body { 
                background-color: #050505; 
                color: #e0e0e0; 
                margin: 0; 
                padding: 0; 
            }
            .container-fluid { padding: 0 !important; }
            
            /* Floating Menu Widget */
            .menu-widget {
                position: fixed;
                top: 25px;
                left: 25px;
                width: 340px;
                max-height: 85vh;
                background: #1a1a1a;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
                padding: 30px;
                z-index: 2000;
                box-shadow: 0 15px 50px rgba(0, 0, 0, 0.9);
                overflow-y: auto;
            }
            
            .action-button.close-btn {
                position: absolute;
                top: 15px;
                right: 15px;
                background: none !important;
                border: none !important;
                color: #888 !important;
                font-size: 20px;
                padding: 0;
                line-height: 1;
            }
            .action-button.close-btn:hover { color: #fff !important; }
            
            .action-button.open-btn {
                position: fixed;
                top: 25px;
                left: 25px;
                width: 55px;
                height: 55px;
                background: #1a1a1a !important;
                border-radius: 0px !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
                color: white !important;
                font-size: 28px;
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1999;
                box-shadow: 0 5px 20px rgba(0,0,0,0.5);
            }
            
            /* Chart Cards */
            .chart-card {
                background: #121212;
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 25px;
                margin-bottom: 40px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }
            
            .irs-grid-text { color: #777 !important; }
            .irs-single, .irs-bar, .irs-from, .irs-to { background: #555 !important; border-color: #666 !important; }
            label { font-weight: 600; color: #999 !important; text-transform: uppercase; font-size: 11px; letter-spacing: 1.5px; margin-bottom: 12px; }
            
            h3 { font-weight: 800; color: #fff; letter-spacing: -0.5px; }
            
            .impact-count { 
                font-size: 14px; 
                color: #00ff00 !important; 
                font-family: monospace; 
                font-weight: bold; 
            }
            
            /* Center the globe widget */
            .globe-container {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 180vh;
                background-color: #050505;
                border-bottom: 1px solid #1a1a1a;
                overflow: hidden;
            }
        """)
    ),
    
    # Globe Section
    ui.div(
        output_widget("globe_plot", height="180vh", width="100%"),
        class_="globe-container"
    ),
    
    # Content Section
    ui.div(
        ui.row(
            ui.column(8, 
                ui.div(
                    ui.h4("GLOBAL DISTRIBUTION HEATMAP", style="margin-bottom: 25px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("heatmap_2d", height="550px"),
                    class_="chart-card"
                ),
            ),
            ui.column(4, 
                ui.div(
                    ui.h4("IMPACTS OVER TIME", style="margin-bottom: 25px; color: #666; font-size: 12px; font-weight: 900;"),
                    output_widget("timeline_plot", height="550px"),
                    class_="chart-card"
                )
            ),
            style="padding: 40px;"
        ),
        style="position: relative; z-index: 10; background-color: #050505;"
    ),
    
    ui.output_ui("menu_container"),
)

def server(input, output, session):
    show_menu = reactive.Value(True)
    
    # Defaults
    cur_years = reactive.Value([1950, 2024])
    cur_mass_log = reactive.Value([1.5, 8.0])
    cur_limit = reactive.Value(1000)

    @reactive.effect
    @reactive.event(input.toggle_menu)
    def _():
        try:
            cur_years.set(input.year_range())
            cur_mass_log.set(input.mass_range_log())
            cur_limit.set(input.limit())
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
        except:
            years = cur_years()
            mass_log = cur_mass_log()
            limit = cur_limit()
        
        mask = (df['year'] >= years[0]) & (df['year'] <= years[1]) & \
               (df['log_mass'] >= mass_log[0]) & (df['log_mass'] <= mass_log[1]) if not (df := meteorites).empty else []
        
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
                ui.hr(style="border-color: #333; margin: 25px 0;"),
                ui.input_slider("year_range", "YEARS", 
                                min=int(meteorites['year'].min()), 
                                max=int(meteorites['year'].max()), 
                                value=cur_years(), 
                                sep=""),
                ui.input_slider("mass_range_log", "MASS (LOG G)", 
                                min=0, max=8, value=cur_mass_log(), step=0.1),
                ui.input_numeric("limit", "MAX POINTS", value=cur_limit(), min=1, max=45000),
                ui.hr(style="border-color: #333"),
                ui.markdown("""<small style="color:#555">SCROLL DOWN FOR ANALYSIS</small>"""),
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

    @render_widget
    def globe_plot():
        df = filtered_data()
        fig = go.Figure()

        fig.update_geos(
            projection_type="orthographic",
            showland=True, landcolor="#252525",
            showocean=True, oceancolor="#0d0d0d",
            showcountries=True, countrycolor="#333333",
            bgcolor="rgba(0,0,0,0)",
            showcoastlines=True, coastlinecolor="#444444",
            showframe=False,
            projection_scale=1.0, 
            center=dict(lat=0, lon=0),
            projection_rotation=dict(lon=0, lat=0, roll=0),
        )

        if not df.empty:
            fig.add_trace(go.Scattergeo(
                lon = df['reclong'],
                lat = df['reclat'],
                text = [f"<b>{name}</b><br>Mass: {mass:,.0f}g<br>Year: {year}" for name, mass, year in zip(df['name'], df['mass (g)'], df['year'])],
                hoverinfo = 'text',
                mode = 'markers',
                marker = dict(
                    size = 5 + (df['log_mass'] * 1.5),
                    opacity = 0.8,
                    color = df['log_mass'],
                    colorscale = 'RdYlGn',
                    reversescale = True, 
                    showscale = False,
                    line = dict(width=0.5, color='rgba(255,255,255,0.2)')
                )
            ))

        fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            scene=dict(dragmode="orbit"),
            geo=dict(domain=dict(x=[0, 1], y=[0.1, 0.9])) # Nudge the domain to help centering if needed
        )

        return fig

    @render_widget
    def heatmap_2d():
        df = filtered_data()
        fig = px.density_mapbox(
            df, 
            lat='reclat', 
            lon='reclong', 
            z='log_mass',
            radius=15,
            center=dict(lat=20, lon=0),
            zoom=1.2,
            mapbox_style="carto-darkmatter",
            color_continuous_scale='RdYlGn_r'
        )
        fig.update_layout(
            margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
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
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            coloraxis_showscale=False,
            xaxis=dict(title="YEAR", showgrid=False, tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9)),
            yaxis=dict(title="FREQUENCY", showgrid=True, gridcolor="#222", tickfont=dict(color="#666"), titlefont=dict(color="#888", size=9))
        )
        return fig

app = App(app_ui, server)
