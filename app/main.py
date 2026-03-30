from fastapi import FastAPI, HTTPException
from app.models import IoTData
from app.services import detect_anomaly, call_gemini
from app.utils import build_prompt
from dotenv import load_dotenv
import os

load_dotenv()
print("KEY LOADED:", os.getenv("GEMINI_API_KEY"))
app = FastAPI(
    title="AI Care Assistant",
    description="IoT + Gemini AI based Care Insight System",
    version="1.0"
)

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
def analyze(data: IoTData):

    # -------------------------------
    # STEP 1: Detect anomaly
    # -------------------------------
    status = detect_anomaly(data)

    # Normalize status
    if status == "ALERT":
        status = "MEDIUM_ALERT"

    # -------------------------------
    # STEP 2: Human-in-loop flag
    # -------------------------------
    needs_approval = True if status in ["MEDIUM_ALERT", "HIGH_ALERT"] else False

    # -------------------------------
    # STEP 3: Build prompt
    # -------------------------------
    prompt = build_prompt(data, status)

    # -------------------------------
    # STEP 4: Call Gemini
    # -------------------------------
    ai_output = call_gemini(prompt)

    # -------------------------------
    # STEP 5: Ensure JSON response
    # -------------------------------
    parsed_output = {}

    try:
        # If Gemini already returns JSON string
        if isinstance(ai_output, str):
            parsed_output = json.loads(ai_output)

        # If somehow dict (safe case)
        elif isinstance(ai_output, dict):
            parsed_output = ai_output

    except Exception:
        # Fallback structured output
        parsed_output = {
            "summary": "Patient inactive for extended duration.",
            "possible_reason": "Could be resting, sleeping, or inactive.",
            "risk_explanation": "Prolonged inactivity detected. Needs manual check.",
            "caregiver_action": "Contact patient or check physically.",
            "family_message": "Patient inactive for a long time. Please check once.",
            "confidence": "Medium"
        }

    # -------------------------------
    # STEP 6: Return response
    # -------------------------------
    return {
        "device_id": data.device_id,
        "alert_level": status,
        "needs_approval": needs_approval,
        "insight": parsed_output   # ✅ ALWAYS JSON now
    }
