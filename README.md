# F1 Telemetry Analysis – Monza 2024 Qualifying

A data analysis project exploring F1 telemetry data using the FastF1 Python library.  
Focus: ERS deployment patterns, speed traces and driver comparison across top teams at Monza 2024 Qualifying.

## Analysis

- **Gap to Pole Position** – Qualifying gap for all 20 drivers with official team colors
- **Speed Trace** – Lap distance vs. speed comparison: Norris vs. Leclerc
- **Telemetry Comparison** – Speed, throttle and brake traces: Norris vs. Leclerc
- **ERS Deployment** – Engine RPM comparison across McLaren, Ferrari and Mercedes
- **ERS Boost Zones** – Speed & RPM overlay per driver to identify deployment zones

## Tech Stack

- Python 3.14
- [FastF1](https://docs.fastf1.dev/) 3.8.3
- pandas, matplotlib, seaborn, plotly

## Setup

```bash
git clone https://github.com/benni-kjc/f1-telemetry-analysis.git
cd f1-telemetry-analysis
python -m venv venv
source venv/bin/activate
pip install fastf1 plotly seaborn notebook ipykernel
```

Open `projekt1_telemetrie.ipynb` in VS Code and run all cells.

## About

Built as part of a personal portfolio to develop data engineering skills  
for motorsport applications — combining a mechanical engineering background  
with Python-based data analysis.