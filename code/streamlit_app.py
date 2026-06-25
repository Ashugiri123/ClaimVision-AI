import json
import time
from pathlib import Path

import streamlit as st

from image_analyzer import ImageAnalyzer
from history_checker import HistoryChecker
from evidence_checker import EvidenceChecker
from decision_engine import DecisionEngine
from reports.pdf_generator import PDFGenerator


def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"

    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )



st.set_page_config(
    page_title="ClaimVision AI",
    page_icon="🛡️",
    layout="wide"
)

load_css()

st.markdown("""
<div style="
background: linear-gradient(90deg,#2563EB,#1E3A8A);
padding:35px;
border-radius:20px;
text-align:center;
margin-bottom:30px;
box-shadow:0px 10px 25px rgba(0,0,0,.35);
">

<h1 style="color:white;font-size:52px;margin-bottom:10px;">
🛡️ ClaimVision AI
</h1>

<h3 style="color:white;">
AI Powered Insurance Claim Verification
</h3>

<p style="color:#E2E8F0;font-size:18px;">
Gemini AI • Computer Vision • Real-Time Damage Assessment
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([1,1])

with col1:

    uploaded_file = st.file_uploader(
        "Upload Damage Image",
        type=["jpg","jpeg","png"]
    )

    claim_object = st.selectbox(
        "Claim Object",
        ["Car","Laptop","Package"]
    )

    conversation = st.text_area(
        "Customer Conversation",
        height=180,
        placeholder="Paste customer conversation here..."
    )

    user_id = st.selectbox(
        "Customer ID",
        [
            "user_001",
            "user_002",
            "user_003",
            "user_004",
            "user_005",
            "user_006",
            "user_007",
            "user_008",
            "user_009",
            "user_010"
        ]
    )

    analyze = st.button(
        "Analyze Claim",
        use_container_width=True
    )

with col2:

    st.subheader("Image Preview")

    if uploaded_file:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

    else:

        st.info("Upload an image to preview it.")

st.markdown("---")

if analyze:

    if uploaded_file is None:
        st.error("Please upload an image.")
        st.stop()

    if conversation.strip() == "":
        st.error("Please enter the customer conversation.")
        st.stop()

    analyzer = ImageAnalyzer()
    history_checker = HistoryChecker()
    evidence_checker = EvidenceChecker()
    decision_engine = DecisionEngine()
    pdf_generator = PDFGenerator()

    with st.spinner("Analyzing image..."):

        progress = st.progress(0)

        try:

            progress.progress(15, text="Uploading image...")

            progress.progress(35, text="Running Gemini Vision...")

            gemini = analyzer.analyze_uploaded_image(
                uploaded_file,
                conversation,
                claim_object.lower()
            )

            progress.progress(70, text="Evaluating claim...")

            history = history_checker.get_user_history(user_id)
            evidence = evidence_checker.check_evidence(
                claim_object.lower(),
                uploaded_images=1
            )
            decision = decision_engine.decide(
                gemini,
                history,
                evidence
            )

            progress.progress(100, text="Completed ✅")

            
            time.sleep(0.5)

            progress.empty()

        except Exception as e:

            st.error(str(e))
            st.stop()


    st.success("Analysis Complete ✅")

    st.markdown("---")

    st.subheader("📋 Final Claim Decision")

    status = decision["claim_status"]

    if status == "supported":

        st.markdown("""
        <div style="
        background:#16A34A;
        padding:25px;
        border-radius:18px;
        text-align:center;
        font-size:34px;
        font-weight:bold;
        color:white;">
        ✅ CLAIM APPROVED
        </div>
        """, unsafe_allow_html=True)

    elif status == "contradicted":

        st.markdown("""
        <div style="
        background:#DC2626;
        padding:25px;
        border-radius:18px;
        text-align:center;
        font-size:34px;
        font-weight:bold;
        color:white;">
        ❌ CLAIM REJECTED
        </div>
        """, unsafe_allow_html=True)

    elif status == "manual_review":

        st.markdown("""
        <div style="
        background:#F59E0B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        font-size:34px;
        font-weight:bold;
        color:white;">
        🟡 MANUAL REVIEW REQUIRED
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        background:#64748B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        font-size:34px;
        font-weight:bold;
        color:white;">
        ⚠️ NOT ENOUGH INFORMATION
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("⚙️ AI Processing Pipeline")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.success("📷 Image")
    c2.success("🤖 Gemini")
    c3.success("🔍 Detection")
    c4.success("🛡 Risk")
    c5.success("📄 Report")

    st.markdown("---")

    st.subheader("📊 Analysis Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Valid Image",
            "✅ YES" if gemini["valid_image"] else "❌ NO"
        )

    with col2:
        st.metric(
            "Damage Found",
            "✅ YES" if gemini["visible_damage"] else "❌ NO"
        )

    with col3:
        st.metric(
            "Severity",
            decision["severity"].upper()
        )

    with col4:
        st.metric(
            "Issue Type",
            decision["issue_type"].replace("_", " ").title()
        )

    st.markdown("---")

    st.subheader("🎯 AI Confidence")

    if not gemini["valid_image"]:
        confidence = 40

    elif decision["severity"] == "high":
        confidence = 97

    elif decision["severity"] == "medium":
        confidence = 90

    elif decision["severity"] == "low":
        confidence = 82

    else:
        confidence = 70

    st.progress(confidence)

    st.write(f"Confidence Score: **{confidence}%**")

    st.markdown("---")

    st.subheader("📑 Evidence Assessment")

    if evidence["evidence_complete"]:
        st.success("✅ Evidence requirements satisfied")
    else:
        st.error(evidence["missing_evidence"])

    st.write("### Evidence Rules")

    for rule in evidence["requirements"]:
        st.write(f"• {rule}")

    st.markdown("---")


    st.subheader("🚩 Risk Assessment")

    if decision["risk_flags"] == "none":
        st.success("✅ Low Risk Customer")
    else:
        st.warning(f"⚠️ {decision['risk_flags']}")

    st.markdown("---")

    st.subheader("🤖 AI Recommendation")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Recommendation",
            gemini["recommended_action"]
        )

    with col2:
        st.metric(
            "Fraud Suspicion",
            gemini["fraud_suspicion"].upper()
        )

    with col3:
        st.metric(
            "AI Confidence",
            f"{gemini['confidence']}%"
        )

    st.markdown("---")

    st.subheader("📍 Damaged Part")

    part = decision["object_part"]

    if part == "":
        part = "Not Applicable"

    st.info(f"📍 {part}")

    st.subheader("📝 AI Explanation")

    st.success(decision["claim_status_justification"])

    st.markdown("---")


    developer_mode = st.checkbox("🛠 Developer Mode")

    if developer_mode:

        with st.expander("🤖 Gemini Response"):
            st.json(gemini)

        with st.expander("📋 Final Decision"):
            st.json(decision)


    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "⬇ Download JSON",
            json.dumps(decision, indent=4),
            file_name="analysis.json",
            mime="application/json"
        )

    with col2:

        pdf = pdf_generator.generate(
            decision,
            uploaded_file,
            user_id,
            claim_object
        )

        st.download_button(
            "📄 Download PDF Report",
            pdf,
            file_name="ClaimVision_Report.pdf",
            mime="application/pdf"
        )

    st.markdown("---")

    st.caption(
        "ClaimVision AI • Powered by Google Gemini 2.5 Flash • Built for the Orchestrate Hackathon"
    )