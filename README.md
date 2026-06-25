# 🛡️ ClaimVision AI

> An AI-powered multimodal insurance claim verification system that analyzes customer conversations and submitted damage images to automatically determine claim validity.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![AI](https://img.shields.io/badge/AI-Multimodal-success)
![Status](https://img.shields.io/badge/Status-Active-green)

---

# 📌 Overview

ClaimVision AI is an intelligent insurance claim verification system designed to automate the first stage of claim inspection.

Instead of manually reviewing customer conversations and uploaded evidence images, the system combines computer vision, natural language understanding, and rule-based decision making to evaluate whether a claim is supported by sufficient visual evidence.

The project was developed for the HackerRank Orchestrate Hackathon and demonstrates how Large Vision Language Models can be integrated into real-world insurance workflows.

---

# 🚀 Features

- 📷 AI-powered image damage analysis
- 💬 Customer conversation parsing
- 🚗 Supports Cars, Laptops and Packages
- 📑 Automatic evidence verification
- ⚠️ User history based risk analysis
- 🤖 Rule-based decision engine
- 📊 Automatic CSV report generation
- 🧩 Modular architecture
- 🔒 Environment variable based API security

---

# ❗ Problem Statement

Insurance companies receive thousands of claims every day.

Manual verification is:

- Time consuming
- Expensive
- Error prone
- Difficult to scale

ClaimVision AI automates the initial verification process by analyzing:

- Customer conversations
- Uploaded damage images
- User claim history
- Evidence requirements

The system determines:

- Whether submitted evidence is sufficient
- Damage type
- Damaged object part
- Damage severity
- Whether the claim is supported or contradicted

---

# 🏗️ System Architecture

```
                Customer Claim
                       │
                       ▼
             Claim Conversation
                       │
                       ▼
               Claim Parser
                       │
                       ▼
            Gemini Vision Analyzer
                       │
                       ▼
            Evidence Verification
                       │
                       ▼
           User History Analysis
                       │
                       ▼
             Decision Engine
                       │
                       ▼
                output.csv
```

---

# 📂 Project Structure

```
ClaimVision-AI/
│
├── code/
│   ├── main.py
│   ├── claim_parser.py
│   ├── image_analyzer.py
│   ├── decision_engine.py
│   ├── history_checker.py
│   ├── evidence_checker.py
│   ├── data_loader.py
│   ├── output_writer.py
│   ├── prompts.py
│   └── config.py
│
├── dataset/
│
├── docs/
│
├── screenshots/
│
├── tests/
│
├── requirements.txt
│
├── .env
│
└── README.md
```

---

# ⚙️ Technologies Used

- Python
- Google Gemini 2.5 Flash
- Google GenAI SDK
- Pandas
- Pillow
- python-dotenv
- Prompt Engineering

---

# 🔄 Workflow

1. Read insurance claims from CSV.
2. Parse customer conversation.
3. Analyze uploaded damage images using Gemini Vision.
4. Validate submitted evidence.
5. Analyze previous user claim history.
6. Apply rule-based decision logic.
7. Generate structured insurance decision.
8. Export results to `output.csv`.

---

# 📄 Output

For every submitted claim, the system predicts:

- Evidence Standard
- Evidence Reason
- Risk Flags
- Issue Type
- Damaged Object Part
- Claim Status
- Justification
- Supporting Image IDs
- Image Validity
- Damage Severity

---

# 🛠 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ClaimVision-AI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
python code/main.py
```

---

# 📈 Future Improvements

- Local AI inference using Ollama
- Support multiple Vision Models
- Confidence score for predictions
- Multi-image reasoning
- Fraud detection module
- Streamlit web interface
- Docker support
- Cloud deployment

---

# 📸 Screenshots

Screenshots will be added after deployment.

---

# 👨‍💻 Author

**Ashutosh Giri**

Computer Science Engineering Student

Interested in Artificial Intelligence, Machine Learning, Java and Python.

---

# 📜 License

This project is licensed under the MIT License.