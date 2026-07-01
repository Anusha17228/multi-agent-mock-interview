import json
import os

SESSION_FILE = "data/sessions.json"

def save_session(data):
    sessions = []

    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as file:
            sessions = json.load(file)

    sessions.append(data)

    with open(SESSION_FILE, "w") as file:
        json.dump(sessions, file, indent=4)
