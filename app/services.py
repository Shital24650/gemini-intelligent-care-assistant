import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Rule Engine
def detect_anomaly(data):
    if data.activity.lower() == "no_movement":
        if data.duration >= 180:
            return "HIGH_ALERT"
        elif data.duration >= 120:
            return "MEDIUM_ALERT"
    return "NORMAL"
def fallback_response(prompt):
    prompt = prompt.lower()

    if "no movement" in prompt or "no_movement" in prompt:
        return "Patient inactive for extended duration. Caregiver should check immediately."

    elif "fall" in prompt:
        return "Possible fall detected. Immediate assistance required."

    else:
        return "Activity appears normal. No immediate concern."



import re

import json

def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    headers = {"Content-Type": "application/json"}

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        res = requests.post(url, headers=headers, json=body)
        data = res.json()

        if "candidates" in data:
            text = data["candidates"][0]["content"]["parts"][0]["text"]

            try:
                return json.loads(text)  # ✅ Convert to dict
            except:
                return {"raw": text}  # fallback

        return {"raw": fallback_response(prompt)}

    except Exception as e:
        return {"raw": f"AI error: {str(e)}"}
def extract(text, key):
    import re
    pattern = rf"{key}:(.*?)(\n[A-Z][a-zA-Z ]+:|$)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""
