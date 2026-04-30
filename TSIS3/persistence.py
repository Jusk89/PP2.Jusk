import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"


def load_json(filename, default):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return default


def save_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def save_score(name, score, distance):
    leaderboard = load_json(LEADERBOARD_FILE, [])

    leaderboard.append({
        "name": name,
        "score": score,
        "distance": int(distance)
    })

    leaderboard.sort(key=lambda item: item["score"], reverse=True)
    leaderboard = leaderboard[:10]

    save_json(LEADERBOARD_FILE, leaderboard)