# Meteorite Impacts 3D Globe Explorer

An interactive 3D globe visualization of global meteorite impacts using **Shiny for Python** and **Plotly**. Explore thousands of historical meteorite landings, filtering by year and mass.

## Features

- **Interactive 3D Globe**: Rotate, zoom, and hover over impact sites.
- **Glowing Visuals**: Impacts are colored from **Green (Small)** to **Red (Large)** by mass.
- **Dynamic Filters**:
  - Filter by **Year Range** (860 AD - Present).
  - Filter by **Mass** (logarithmic scale for better granularity).
  - Control the **Max Displayed Points** to balance performance and detail.
- **Glassmorphism UI**: A sleek, semi-transparent floating menu that can be collapsed for a full-screen experience.
- **State Preservation**: The menu remembers your filter settings even when closed and reopened.

## Prerequisites

This project uses [**uv**](https://github.com/astral-sh/uv) for fast and reliable Python package management.

## Getting Started

### 1. Initialize the Environment
If you haven't already, initialize the virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
```

### 2. Install Dependencies
Install the required packages:

```bash
uv pip install shiny shinywidgets plotly pandas numpy
```

### 3. Run the Application
Start the Shiny server:

```bash
uv run shiny run app.py
```

Open the URL provided in the terminal (usually `http://127.0.0.1:8000`) in your web browser.

## Data Source
The dataset `Meteorite_Landings.csv` contains information on over 45,000 meteorite landings, including their names, mass, year of impact, and geographic coordinates.
