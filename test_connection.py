import fastf1
import os

os.makedirs("f1_cache", exist_ok=True)
fastf1.Cache.enable_cache("f1_cache")

session = fastf1.get_session(2024, "Monza", "Q")
session.load()

laps = session.laps
print(f"Runden geladen: {len(laps)}")
print(laps[["Driver", "LapTime", "Compound"]].head(10))
