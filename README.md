# F1 Data Science Portfolio

A growing collection of data analysis and simulation projects built on real F1 telemetry and timing data via [FastF1](https://docs.fastf1.dev/) — developed to build transferable data engineering skills for motorsport applications, combining a mechanical engineering background with Python-based data analysis.

---

## Project 1 — Qualifying Telemetry Analysis (Monza 2024)

A data analysis project exploring F1 telemetry data using the FastF1 Python library.
Focus: ERS deployment patterns, speed traces and driver comparison across top teams at Monza 2024 Qualifying.

**Notebook:** `monza_2024_qualifying_telemetry_analysis.ipynb`

### Analysis

- **Gap to Pole Position** – Qualifying gap for all 20 drivers with official team colors
- **Speed Trace** – Lap distance vs. speed comparison: Norris vs. Leclerc
- **Telemetry Comparison** – Speed, throttle and brake traces: Norris vs. Leclerc
- **ERS Deployment** – Engine RPM comparison across McLaren, Ferrari and Mercedes
- **ERS Boost Zones** – Speed & RPM overlay per driver to identify deployment zones

---

## Project 2 — Tyre Degradation Model & Monte Carlo Race Strategy Simulator (Monza 2024 Race)

A two-part project built on Charles Leclerc's Monza 2024 race data: first an isolated, physically validated model of tyre degradation and fuel-burn effects, then a Monte Carlo simulator that uses those parameters to compare pit strategies under realistic uncertainty.

**Notebook:** `tyre_degradation_model.ipynb`

### Part 1 & 2 — Degradation & Parameter Estimation

- Compound-specific degradation isolated from fuel-burn and compound baseline using a multi-driver regression model, after identifying and resolving severe multicollinearity in a single-driver model
- Noise, pit-stop time loss and safety car effects (lap time factor, net pit loss) all derived from real `PitInTime`/`PitOutTime` and `TrackStatus` data across multiple Monza races (2018–2024)
- Outlier laps are only removed with independent, documented justification (e.g. a confirmed pit lap) — never because a lap looks statistically unusual

### Part 3 — Monte Carlo Simulator

- Lap-by-lap race simulation combining fuel-burn, compound-specific degradation, empirical noise and safety car effects
- 1-stop vs. 2-stop strategy comparison across 1,000 simulated races per strategy, with a sensitivity analysis across three safety car probability scenarios
- A systematic pit-lap sweep used to test for an optimal stop timing — and to diagnose a genuine limitation of the linear degradation model (see notebook conclusion)

### Key finding

A 1-stop strategy (Medium 20 laps / Hard 33 laps) outperforms a comparable 2-stop strategy by ~18 seconds on average, a result that holds robustly across all tested safety car scenarios — but is explicitly tied to Leclerc's own, unusually low measured Hard-tyre degradation in this race, not a general Monza/compound property.

---

## Tech Stack

- Python 3.14
- [FastF1](https://docs.fastf1.dev/) 3.8.3
- pandas, numpy, matplotlib, scikit-learn

## Setup

```bash
git clone https://github.com/benni-kjc/f1-telemetry-analysis.git
cd f1-telemetry-analysis
python -m venv venv
source venv/bin/activate
pip install fastf1 pandas numpy matplotlib scikit-learn notebook ipykernel
```

Open either notebook in VS Code and run all cells.

## About

Built as part of a personal portfolio to develop data engineering skills
for motorsport applications — combining a mechanical engineering background
with Python-based data analysis.