import fastf1
import os

cache_dir = "f1_cache"
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache(cache_dir)

print("Cache eingerichtet unter:", cache_dir)
