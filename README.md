# gemini-intelligent-care-assistant

**AI-powered IoT care assistant using Gemini API for ethical, explainable, and role-based patient monitoring insights**

# 🧠 Gemini-Powered Intelligent Care Assistant

---

## 🌟 Overview

Modern IoT care systems generate continuous streams of low-level signals such as movement, duration, and vital signs. However, these signals lack immediate interpretability and can overwhelm caregivers.

This project introduces an **AI interpretation layer** that:

- Transforms raw IoT data into meaningful insights  
- Generates context-aware alerts  
- Ensures ethical AI usage (no diagnosis, human-in-loop)  
- Supports multiple user roles (caregiver, family, supervisor)  

---

## 🧩 Key Features

### 🧠 AI-Powered Insights (Gemini API)
- Converts patient data into structured JSON insights  
- Explains *why* an alert is triggered  
- Provides confidence levels for transparency  

---

### ⚠️ Intelligent Alert System
- Rule-based anomaly detection  
- Detects:
  - Prolonged inactivity  
  - Abnormal heart rate  
  - Location anomalies  

---

### 👥 Role-Based AI Responses
Different outputs for different users:

| Role        | Output Style |
|------------|-------------|
| Caregiver  | Detailed + actionable |
| Family     | Simple + reassuring |
| Supervisor | Concise + decision-focused |

---

### 🛑 Human-in-the-Loop (Ethical AI)
- Alerts require supervisor approval before escalation  
- AI assists decisions — does NOT replace humans  

---

### 🔍 Explainable AI
- Every alert includes:
  - Summary  
  - Reason  
  - Risk explanation  
  - Recommended action  
  - Confidence level  


---

## 🏗️ Architecture
<img width="1536" height="1024" alt="ArchitectureDiagram" src="https://github.com/user-attachments/assets/8bbf24b0-1e7a-4b13-b62d-935389b816f1" />

---

## ⚙️ Tech Stack

- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **AI Engine:** Gemini API (Google)  
- **Language:** Python  
- **Data Format:** Structured JSON  

---

## 📂 Project Structure

```
ai-care-assistant/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── services.py
│   ├── utils.py
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-care-assistant.git
cd ai-care-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Gemini API Key

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

### Start Backend (FastAPI)
```bash
uvicorn app.main:app --reload
```

API runs at:  
http://127.0.0.1:8000  

### Start Frontend (Streamlit)
```bash
streamlit run app.py
```

App runs at:  
http://localhost:8501  

---

## 🧪 Example Input
```json
{
  "device_id": "101",
  "activity": "no_movement",
  "duration": 120,
  "heart_rate": 75,
  "location": "home",
  "role": "caregiver"
}
```

---

## 📤 Example Output
```json
{
  "summary": "...",
  "possible_reason": "...",
  "risk_explanation": "...",
  "caregiver_action": "...",
  "family_message": "...",
  "confidence": "Medium"
}
```

---

## 🧭 Ethical AI Principles
- ❌ No medical diagnosis  
- ✅ Explainability-first outputs  
- ✅ Human approval required  
- ✅ Role-based access control  
- ✅ Confidence transparency  

---

## 🎯 Use Cases
- Elderly care monitoring  
- Remote patient observation  
- Assisted living environments  
- Family reassurance systems  

---

## 🌐 Live Demo

- Frontend: [https://gemini-intelligent-care-assistantfomvhhnvhymxsrcm3xaqob.streamlit.app/ ](https://gemini-intelligent-care-assistant-fomvhhnvhymxsrcm3xaqob.streamlit.app/)
- Backend API: https://gemini-intelligent-care-assistant.onrender.com/

---

## 🚀 Deployment Guide

### 🔹 Backend (Render / Railway)
- Push code to GitHub  
- Go to https://render.com  
- Create New Web Service  
- Connect GitHub repo  

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

Add Environment Variable:
```
GEMINI_API_KEY=your_key
```

---

### 🔹 Frontend (Streamlit Cloud)
- Go to https://streamlit.io/cloud  
- Connect GitHub repo  
- Select `app.py`  
- Deploy  

---

## 📊 Future Scope
- Time-series behavior tracking  
- Feedback loop for AI improvement  
- Voice-based interaction for elderly users  
- Supervisor dashboard with approval workflow  

---

## 🏁 Conclusion

This project demonstrates a real-world application of responsible AI, where:

- AI enhances decision-making  
- Humans remain in control  
- Insights are transparent and explainable  

---

## 👨‍💻 Author

**Shital Parab**
