import streamlit as st
import requests
import json
import re

# -------------------------------
# CONFIG
# -------------------------------
API_URL = "https://gemini-intelligent-care-assistant.onrender.com/analyze"

st.set_page_config(
    page_title="AI Care Assistant",
    page_icon="🧠",
    layout="centered"
)

# -------------------------------
# SESSION STATE (HISTORY)
# -------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# HEADER
# -------------------------------
st.title("🧠 AI Care Assistant")
st.markdown("### Ethical IoT Monitoring + AI Insights")
st.markdown("---")

# -------------------------------
# INPUT FORM
# -------------------------------
st.subheader("📡 Patient Device Data")

device_id = st.text_input("Device ID", "101")

activity = st.selectbox(
    "Activity",
    ["no_movement", "walking", "sleeping", "running"]
)

duration = st.slider("Duration (minutes)", 0, 300, 120)

heart_rate = st.number_input("Heart Rate (optional)", 30, 200, 75)

location = st.selectbox(
    "Location",
    ["home", "outside", "hospital"]
)

# 🔥 NEW: ROLE-BASED INPUT
role = st.selectbox(
    "Select User Role",
    ["caregiver", "family"]
)

# -------------------------------
# ANALYZE BUTTON
# -------------------------------
analyze = st.button("🔍 Analyze Patient Status")

if analyze:

    payload = {
        "device_id": device_id,
        "activity": activity,
        "duration": duration,
        "heart_rate": heart_rate,
        "location": location,
        "role": role
    }

    with st.spinner("Analyzing patient data..."):

        try:
            res = requests.post(API_URL, json=payload)

            if res.status_code == 200:
                data = res.json()

                st.markdown("---")

                # -------------------------------
                # ALERT LEVEL
                # -------------------------------
                alert = data.get("alert_level")

                st.markdown("### 🚦 Alert Level")

                if alert == "HIGH_ALERT":
                    st.error("🚨 HIGH ALERT - Immediate Attention Required")
                elif alert == "MEDIUM_ALERT":
                    st.warning("⚠️ MEDIUM ALERT - Monitor Closely")
                else:
                    st.success("✅ NORMAL - No Immediate Risk")

                # -------------------------------
                # SAVE HISTORY
                # -------------------------------
                st.session_state.history.append({
                    "device_id": device_id,
                    "activity": activity,
                    "duration": duration,
                    "heart_rate": heart_rate,
                    "alert": alert
                })

                # -------------------------------
                # AI INSIGHT
                # -------------------------------
                st.markdown("### 🧠 AI Insight")

                insight = data.get("insight", "")

                # Try to parse JSON
                try:
                    insight = json.loads(insight)
                except:
                    pass

                # -------------------------------
                # CASE 1: JSON RESPONSE (BEST)
                # -------------------------------
                if isinstance(insight, dict):

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("📌 Summary")
                        st.info(insight.get("summary", "Not available"))

                        st.subheader("🔍 Possible Reason")
                        st.write(insight.get("possible_reason", "Not available"))

                        st.subheader("⚠️ Risk Explanation")
                        st.warning(insight.get("risk_explanation", "Not available"))

                    with col2:
                        st.subheader("👨‍⚕️ Caregiver Action")
                        st.error(insight.get("caregiver_action", "Not available"))

                        st.subheader("👪 Family Message")
                        st.success(insight.get("family_message", "Not available"))

                        st.subheader("📊 Confidence Level")

                        confidence = insight.get("confidence", "Unknown")

                        if confidence == "High":
                            st.success(f"Confidence: {confidence}")
                        elif confidence == "Medium":
                            st.warning(f"Confidence: {confidence}")
                        else:
                            st.error(f"Confidence: {confidence}")

                # -------------------------------
                # CASE 2: STRING RESPONSE (FALLBACK CLEAN PARSE)
                # -------------------------------
                else:

                    text = insight.replace("**", "")

                    def extract(title):
                        pattern = rf"{title}:(.*?)(?=\n[A-Z][a-zA-Z ]+:|$)"
                        match = re.search(pattern, text, re.DOTALL)
                        return match.group(1).strip() if match else "Not available"

                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("📌 Summary")
                        st.info(extract("Summary"))

                        st.subheader("🔍 Possible Reason")
                        st.write(extract("Possible Reason"))

                        st.subheader("⚠️ Risk Explanation")
                        st.warning(extract("Risk Level Explanation"))

                    with col2:
                        st.subheader("👨‍⚕️ Caregiver Action")
                        st.error(extract("Caregiver Action"))

                        st.subheader("👪 Family Message")
                        st.success(extract("Family Message"))

                        st.subheader("📊 Confidence Level")
                        st.metric("Confidence", extract("Confidence Level"))

                # -------------------------------
                # HUMAN VALIDATION (🔥 IMPORTANT)
                # -------------------------------
                st.markdown("### ✅ Human Validation")

                colA, colB = st.columns(2)

                with colA:
                    if st.button("✅ Approve Alert"):
                        st.success("Alert Approved by Caregiver")

                with colB:
                    if st.button("❌ Reject Alert"):
                        st.warning("Marked as False Alarm")

                st.markdown("---")

            else:
                st.error(f"❌ API Error: {res.status_code}")

        except Exception as e:
            st.error(f"❌ Connection Error: {e}")

# -------------------------------
# HISTORY SECTION
# -------------------------------
st.subheader("📊 Recent Activity History")

if st.session_state.history:
    for record in st.session_state.history[-5:]:
        st.write(record)
else:
    st.info("No history yet.")
