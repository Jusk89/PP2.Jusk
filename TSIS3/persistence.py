import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return default


def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def save_score(leaderboard, name, score, distance):
    leaderboard.append({
        "name": name,
        "score": score,
        "distance": int(distance)
    })

    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    return leaderboard[:10]