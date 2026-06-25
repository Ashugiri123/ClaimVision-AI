<p align="center">
  <img src="README_assets/logo.png" width="220">
</p>

<h1 align="center">🛡️ ClaimVision AI</h1>

<p align="center">
AI Powered Insurance Claim Verification using Google Gemini Vision
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google">

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit">

<img src="https://img.shields.io/badge/Computer-Vision-blue?style=for-the-badge">

<img src="https://img.shields.io/badge/AI-Powered-success?style=for-the-badge">

<img src="https://img.shields.io/badge/Hackathon-Orchestrate-orange?style=for-the-badge">

</p>

---

# 📖 Overview

ClaimVision AI is an intelligent insurance claim verification system that leverages **Google Gemini 2.5 Flash Vision** to analyze damage images, understand customer claim descriptions, validate submitted evidence, assess customer claim history, and generate an AI-assisted insurance decision.

Instead of relying solely on manual inspection, ClaimVision AI automates the first level of claim verification, reducing processing time while helping identify suspicious or fraudulent claims.

---

# 🎥 Project Demo

<p align="center">

<a href="https://youtu.be/bg8ddYtOxtI">

<img src="https://img.youtube.com/vi/bg8ddYtOxtI/maxresdefault.jpg" width="900">

</a>

</p>

<p align="center">
Click the image above to watch the complete demonstration.
</p>

---

# ✨ Features

- 🚗 Supports Car, Laptop and Package insurance claims
- 🤖 Google Gemini Vision powered damage analysis
- 💬 Customer conversation understanding
- 🛡 Fraud risk assessment
- 📂 Customer history verification
- 📑 Evidence validation
- 📊 AI confidence score
- 📍 Damaged part identification
- 📄 Automatic PDF report generation
- 📥 JSON export
- 💻 Modern Streamlit dashboard

---

# 🖥 User Interface

## Landing Page

<p align="center">
<img src="README_assets/landing.png" width="1000">
</p>

A clean dashboard where users upload claim images, select claim type, provide customer conversation, and initiate AI analysis.

---

## Upload & Image Preview

<p align="center">
<img src="README_assets/upload.png" width="1000">
</p>

Users can instantly preview uploaded images before starting claim verification.

---

## AI Processing

<p align="center">
<img src="README_assets/processing.png" width="1000">
</p>

The system displays real-time progress while Gemini analyzes the uploaded image and the decision engine evaluates the claim.

---

## Final Decision

<p align="center">
<img src="README_assets/decision.png" width="1000">
</p>

ClaimVision AI automatically determines whether the claim should be:

- ✅ Approved
- ❌ Rejected
- 🟡 Sent for Manual Review

---

## Analysis Summary

<p align="center">
<img src="README_assets/summary.png" width="1000">
</p>

Provides

- Image validation
- Damage detection
- Severity assessment
- Issue type
- AI confidence

---

## Risk Assessment

<p align="center">
<img src="README_assets/risk.png" width="1000">
</p>

Evaluates customer history, evidence completeness, fraud suspicion, damaged part, AI explanation, and recommendation.

---

## Generated PDF Report

<p align="center">
<img src="README_assets/pdf_report.png" width="650">
</p>

Generates a professional insurance claim report including:

- Customer information
- Uploaded evidence
- AI decision
- Damage analysis
- Confidence
- Final recommendation

---

# ⚙ AI Workflow

```text
Customer
      │
      ▼
Upload Damage Image
      │
      ▼
Gemini Vision Analysis
      │
      ▼
Damage Detection
      │
      ▼
Conversation Analysis
      │
      ▼
Evidence Validation
      │
      ▼
Customer History Analysis
      │
      ▼
Decision Engine
      │
      ▼
Approve / Reject / Manual Review
      │
      ▼
Generate PDF Report
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | User Interface |
| Google Gemini 2.5 Flash | Vision AI |
| Pandas | Dataset Processing |
| Pillow | Image Handling |
| ReportLab | PDF Generation |
| dotenv | API Configuration |
| CSV | Local Data Storage |

---

# 📂 Project Structure

```text
ClaimVision-AI

├── code
│   ├── image_analyzer.py
│   ├── decision_engine.py
│   ├── history_checker.py
│   ├── evidence_checker.py
│   ├── streamlit_app.py
│   └── reports
│
├── dataset
│
├── README_assets
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

```bash
git clone https://github.com/Ashugiri123/ClaimVision-AI.git

cd ClaimVision-AI

python -m venv .venv

source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create

```
.env
```

Add

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
streamlit run code/streamlit_app.py
```

---

# 📈 Example Output

```
Claim Status : Approved

Severity : High

Issue : Broken Part

Fraud Risk : Low

Confidence : 97%

Damaged Part : Front Bumper
```

---

# 🔮 Future Improvements

- Multi-image damage mapping
- Repair cost estimation
- OCR document verification
- VIN verification
- Insurance API integration
- Cloud deployment
- Mobile application
- Video claim analysis

---

# 👨‍💻 Developer

**Ashutosh Giri**

Computer Science Engineering Student

Google Student Ambassador

---

# 📜 License

This project was developed for the **Orchestrate Hackathon**.

---

<h3 align="center">

⭐ If you found this project useful, please consider giving it a Star ⭐

</h3>