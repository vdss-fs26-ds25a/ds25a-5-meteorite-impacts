# Meteorite Impacts 3D Globe Explorer

## Prerequisites

This project uses [**uv**](https://github.com/astral-sh/uv) for fast and reliable Python package management.

## Getting Started

### Initialize the Environment
If you haven't already, initialize the virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate     # On Windows
```

### Install Dependencies
Make shure you are in the `/viz_design` Directory

Install the required packages:

```bash
uv sync
```

> If this dose not work try the following command

```bash
uv pip install shiny shinywidgets plotly pandas numpy
```

### Download and clean data
```bash
uv run python ../data/data.py   
```

### Run the Application
Start the Shiny server:

```bash
uv run shiny run app.py
```

Open the URL provided in the terminal (usually `http://127.0.0.1:8000`) in your web browser.

## Data Source
The dataset `Meteorite_Landings.csv` contains information on over 45,000 meteorite landings, including their names, mass, year of impact, and geographic coordinates.
