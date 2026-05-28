# Meteorite Visualisation

This project is part of the geosciences domain and focuses on meteorite findings.
The goal is to present key information about meteorites and their discoveries
worldwide in a clear and accessible way, specifically designed for tablet use
in museums. The target audience is museum visitors aged 15 and above who want
to learn about meteorites for the first time.

## Website

### [Visualisation](https://vdss-fs26-ds25a.github.io/ds25a-5-meteorite-impacts/)

### [Documentation](https://vdss-fs26-ds25a.github.io/ds25a-5-meteorite-impacts/docs)

### [Presentation](https://vdss-fs26-ds25a.github.io/ds25a-5-meteorite-impacts/presentation)

See section `Quarto Setup and Usage` and `Python Shiny App Setup and Usage Local` for instructions on how to build and serve the documentation website and Shiny App Localy

## Project Organisation

Code and configurations used in the different project phases are stored in the correspoding subfolders. Documentation artefacts in the form of a Quarto project are provided in `docs`.

| Phase                            | Code folders | Documentation section | `docs`-File        |
| :------------------------------- | :----------- | :-------------------- | :----------------- |
| Project Understanding            | -            | Project Charta        | project_charta.qmd |
| Data Acquisition and Exploration | `eda`        | Data Report           | data_report.qmd    |
| Presentation                     | -            | Presentation          | Presentation.qmd   |

## Python Shiny App Setup and Usage

### Prerequisites

This project uses [**uv**](https://github.com/astral-sh/uv) for fast and reliable Python package management.

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

## Quarto Setup and Usage Local

Make shure you are in the `/docs` Directory

Make shure `quarto` is installed

To render the Quarto Documentation Localy run

```bash
quarto preview
```
