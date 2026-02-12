import pandas as pd
import os
from datetime import datetime

LOG_FILE = "data/mood_history.csv"


def log_mood(emotion):
    """Logs anonymized data for tracking (Features 3 & 6)."""
    # Feature 6: Privacy - No employee names, only IDs or timestamps
    data = {"timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")], "mood": [emotion]}
    df = pd.DataFrame(data)

    if not os.path.exists("data"): os.makedirs("data")
    if not os.path.isfile(LOG_FILE):
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)


def get_team_analytics():
    """Aggregates data for morale insights (Feature 5)."""
    if not os.path.exists(LOG_FILE): return "No data available"
    df = pd.read_csv(LOG_FILE)
    return df['mood'].value_counts().to_dict()