import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime

# =============================================================
# Page Configuration
# =============================================================
st.set_page_config(
    page_title="EduPredict",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================
# Styling
# =============================================================
st.markdown("""
<style>
    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .result-card {
        padding: 1.2rem 1.4rem;
        border-radius: 12px;
        margin: 0.8rem 0;
        border: 1px solid rgba(128,128,128,0.25);
    }

    .small-note {
        color: #888;
        font-size: 0.85rem;
    }

    div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================
# Model loading
# =============================================================
MODEL_PATH = Path(__file__).parent / "models" / "edupredict_model.joblib"


@st.cache_resource
def load_model(path: Path):
    if not path.exists():
        return None
    return joblib.load(path)


model = load_model(MODEL_PATH)

# =============================================================
# Session state defaults
# =============================================================
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None
if "last_run_at" not in st.session_state:
    st.session_state.last_run_at = None

# =============================================================
# Sidebar
# =============================================================
with st.sidebar:
    st.markdown("## 🎓 EduPredict")
    st.caption("Student Outcome Prediction Assistant")
    st.divider()

    st.markdown("**Model status**")
    if model is None:
        st.error("Model not loaded")
    else:
        st.success("Model loaded and ready")

    st.divider()
    st.markdown("**How it works**")
    st.markdown(
        "1. Fill in student details across the tabs\n"
        "2. Click **Predict Student Outcome**\n"
        "3. Review the predicted outcome, confidence, "
        "and recommended actions"
    )

    st.divider()
    st.markdown("**About**")
    st.markdown(
        "<span class='small-note'>EduPredict classifies a student's likely "
        "outcome — Dropout, Enrolled, or Graduate — from admission, "
        "academic, and socio-economic data. It is a decision-support tool "
        "and should be used alongside academic/advisory judgement, not as "
        "a standalone decision.</span>",
        unsafe_allow_html=True
    )

# =============================================================
# Header
# =============================================================
st.title("🎓 EduPredict")
st.subheader("Student Dropout & Academic Performance Prediction")
st.caption(
    "Decision-support tool: predictions are estimates and should be used "
    "with academic/advisory review, not as final decisions."
)
st.divider()

if model is None:
    st.error(
        f"❌ Model file not found at `{MODEL_PATH}`. "
        "Please make sure `edupredict_model.joblib` is placed inside the "
        "`models/` folder next to this script."
    )
    st.stop()

# =============================================================
# Input form (wrapped in st.form so the app only reruns on submit,
# not on every single widget interaction)
# =============================================================
st.header("📝 Student Information")

tab_admission, tab_academic, tab_personal, tab_economic = st.tabs(
    ["🏫 Admission", "📚 Academic Performance", "💰 Personal & Financial", "🌍 Economic Indicators"]
)

with st.form("student_form", clear_on_submit=False):

    # ---------------- Admission ----------------
    with tab_admission:
        col1, col2, col3 = st.columns(3)
        with col1:
            marital_status = st.number_input("Marital Status", min_value=1, max_value=6, value=1)
            course = st.number_input("Course", min_value=33, max_value=9991, value=9238)
            previous_qualification_grade = st.number_input(
                "Previous Qualification Grade", min_value=0.0, max_value=200.0, value=125.0
            )
        with col2:
            application_mode = st.number_input("Application Mode", min_value=1, max_value=57, value=17)
            daytime_attendance = st.selectbox(
                "Daytime / Evening Attendance",
                options=[1, 0],
                format_func=lambda x: "Daytime" if x == 1 else "Evening"
            )
            nationality = st.number_input("Nationality", min_value=1, max_value=109, value=1)
        with col3:
            application_order = st.number_input("Application Order", min_value=0, max_value=9, value=1)
            previous_qualification = st.number_input("Previous Qualification", min_value=1, max_value=43, value=1)
            admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=130.0)

    # ---------------- Academic Performance ----------------
    with tab_academic:
        st.subheader("First Semester")
        col1, col2, col3 = st.columns(3)
        with col1:
            sem1_credited = st.number_input("1st Sem - Credited", min_value=0, max_value=30, value=0)
            sem1_approved = st.number_input("1st Sem - Approved", min_value=0, max_value=30, value=5)
        with col2:
            sem1_enrolled = st.number_input("1st Sem - Enrolled", min_value=0, max_value=30, value=6)
            sem1_grade = st.number_input("1st Sem - Grade", min_value=0.0, max_value=20.0, value=13.5, step=0.1)
        with col3:
            sem1_evaluations = st.number_input("1st Sem - Evaluations", min_value=0, max_value=30, value=6)
            sem1_without_eval = st.number_input("1st Sem - Without Evaluations", min_value=0, max_value=30, value=0)

        st.subheader("Second Semester")
        col1, col2, col3 = st.columns(3)
        with col1:
            sem2_credited = st.number_input("2nd Sem - Credited", min_value=0, max_value=30, value=0)
            sem2_approved = st.number_input("2nd Sem - Approved", min_value=0, max_value=30, value=5)
        with col2:
            sem2_enrolled = st.number_input("2nd Sem - Enrolled", min_value=0, max_value=30, value=6)
            sem2_grade = st.number_input("2nd Sem - Grade", min_value=0.0, max_value=20.0, value=13.0, step=0.1)
        with col3:
            sem2_evaluations = st.number_input("2nd Sem - Evaluations", min_value=0, max_value=30, value=6)
            sem2_without_eval = st.number_input("2nd Sem - Without Evaluations", min_value=0, max_value=30, value=0)

    # ---------------- Personal & Financial ----------------
    with tab_personal:
        col1, col2, col3 = st.columns(3)
        with col1:
            mother_qualification = st.number_input("Mother's Qualification", min_value=1, max_value=44, value=13)
            father_occupation = st.number_input("Father's Occupation", min_value=0, max_value=195, value=8)
            displaced = st.selectbox("Displaced", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
            scholarship_holder = st.selectbox(
                "Scholarship Holder", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"
            )
        with col2:
            father_qualification = st.number_input("Father's Qualification", min_value=1, max_value=44, value=10)
            age_at_enrollment = st.number_input("Age at Enrollment", min_value=17, max_value=70, value=19)
            educational_special_needs = st.selectbox(
                "Educational Special Needs", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"
            )
            international = st.selectbox(
                "International Student", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"
            )
        with col3:
            mother_occupation = st.number_input("Mother's Occupation", min_value=0, max_value=194, value=6)
            gender = st.selectbox(
                "Gender", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female"
            )
            debtor = st.selectbox("Debtor", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
            tuition_fees = st.selectbox(
                "Tuition Fees Up to Date", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No"
            )

    # ---------------- Economic Indicators ----------------
    with tab_economic:
        col1, col2, col3 = st.columns(3)
        with col1:
            unemployment_rate = st.number_input(
                "Unemployment Rate (%)", min_value=0.0, max_value=30.0, value=10.8, step=0.1
            )
        with col2:
            inflation_rate = st.number_input(
                "Inflation Rate (%)", min_value=-10.0, max_value=30.0, value=1.4, step=0.1
            )
        with col3:
            gdp = st.number_input("GDP", min_value=-10.0, max_value=30.0, value=1.74, step=0.01)

    st.divider()
    submit_col, reset_col = st.columns([1, 1])
    with submit_col:
        predict_clicked = st.form_submit_button(
            "🔮 Predict Student Outcome", type="primary", use_container_width=True
        )
    with reset_col:
        reset_clicked = st.form_submit_button(
            "🔄 Reset Prediction", use_container_width=True
        )

if reset_clicked:
    st.session_state.prediction_result = None
    st.session_state.last_run_at = None
    st.rerun()

# =============================================================
# Validation + Prediction
# =============================================================
if predict_clicked:

    validation_errors = []

    def check_not_exceeding(label: str, value: int, enrolled: int, sem_label: str):
        if value > enrolled:
            validation_errors.append(f"{sem_label}: {label} cannot exceed Enrolled units.")

    check_not_exceeding("Approved units", sem1_approved, sem1_enrolled, "1st semester")
    check_not_exceeding("Approved units", sem2_approved, sem2_enrolled, "2nd semester")
    check_not_exceeding("Evaluations", sem1_evaluations, sem1_enrolled, "1st semester")
    check_not_exceeding("Evaluations", sem2_evaluations, sem2_enrolled, "2nd semester")
    check_not_exceeding("Without-evaluation units", sem1_without_eval, sem1_enrolled, "1st semester")
    check_not_exceeding("Without-evaluation units", sem2_without_eval, sem2_enrolled, "2nd semester")
    check_not_exceeding("Credited units", sem1_credited, sem1_enrolled, "1st semester")
    check_not_exceeding("Credited units", sem2_credited, sem2_enrolled, "2nd semester")

    if validation_errors:
        for error in validation_errors:
            st.error(f"⚠️ {error}")
        st.stop()

    student_data = {
        "Marital status": marital_status,
        "Application mode": application_mode,
        "Application order": application_order,
        "Course": course,
        "Daytime/evening attendance": daytime_attendance,
        "Previous qualification": previous_qualification,
        "Previous qualification (grade)": previous_qualification_grade,
        "Nacionality": nationality,
        "Mother's qualification": mother_qualification,
        "Father's qualification": father_qualification,
        "Mother's occupation": mother_occupation,
        "Father's occupation": father_occupation,
        "Admission grade": admission_grade,

        "Displaced": displaced,
        "Educational special needs": educational_special_needs,
        "Debtor": debtor,
        "Tuition fees up to date": tuition_fees,
        "Gender": gender,
        "Scholarship holder": scholarship_holder,
        "Age at enrollment": age_at_enrollment,
        "International": international,

        "Curricular units 1st sem (credited)": sem1_credited,
        "Curricular units 1st sem (enrolled)": sem1_enrolled,
        "Curricular units 1st sem (evaluations)": sem1_evaluations,
        "Curricular units 1st sem (approved)": sem1_approved,
        "Curricular units 1st sem (grade)": sem1_grade,
        "Curricular units 1st sem (without evaluations)": sem1_without_eval,

        "Curricular units 2nd sem (credited)": sem2_credited,
        "Curricular units 2nd sem (enrolled)": sem2_enrolled,
        "Curricular units 2nd sem (evaluations)": sem2_evaluations,
        "Curricular units 2nd sem (approved)": sem2_approved,
        "Curricular units 2nd sem (grade)": sem2_grade,
        "Curricular units 2nd sem (without evaluations)": sem2_without_eval,

        "Unemployment rate": unemployment_rate,
        "Inflation rate": inflation_rate,
        "GDP": gdp
    }

    input_df = pd.DataFrame([student_data])

    try:
        with st.spinner("Running prediction..."):
            prediction = model.predict(input_df)[0]
            probabilities = model.predict_proba(input_df)[0]
            probability_dict = dict(zip(model.classes_, probabilities))

        st.session_state.prediction_result = {
            "prediction": prediction,
            "probability_dict": probability_dict,
            "student_data": student_data,
        }
        st.session_state.last_run_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        st.session_state.prediction_result = None
        st.error(f"⚠️ Prediction failed: {e}")

# =============================================================
# Results
# =============================================================
st.divider()
st.header("🤖 Prediction Result")

result = st.session_state.prediction_result

if result is not None:
    prediction = result["prediction"]
    probability_dict = result["probability_dict"]

    if st.session_state.last_run_at:
        st.caption(f"Last predicted at {st.session_state.last_run_at}")

    status_map = {
        "Dropout": ("🔴 HIGH RISK", "error",
                    "The model predicts Dropout. Consider timely academic support and review."),
        "Enrolled": ("🟡 MODERATE STATUS", "warning",
                     "The model predicts Enrolled. Continued academic monitoring is recommended."),
        "Graduate": ("🟢 POSITIVE OUTCOME", "success",
                     "The model predicts Graduate."),
    }
    label, level, message = status_map.get(
        prediction, ("ℹ️ RESULT", "info", "Prediction complete.")
    )

    result_col, metric_col = st.columns([2, 1])

    with result_col:
        getattr(st, level)(f"{label} — {message}")

    with metric_col:
        confidence = max(probability_dict.values()) * 100
        st.metric(label="Prediction Confidence", value=f"{confidence:.2f}%")

    st.caption(
        "This is the model-estimated probability of the predicted class; "
        "it is not a guarantee of the student's actual outcome."
    )

    st.subheader("📊 Prediction Probabilities")

    probability_df = pd.DataFrame({
        "Outcome": list(probability_dict.keys()),
        "Probability": [p * 100 for p in probability_dict.values()]
    })

    st.bar_chart(probability_df.set_index("Outcome"), y="Probability")
    st.caption("Probability values represent the model's estimated class probabilities.")

    # ---------------- Recommendation ----------------
    st.subheader("💡 Recommended Actions")

    recommendations = {
        "Dropout": (
            "warning", "⚠️ Immediate attention is recommended.",
            [
                "📚 Academic counselling",
                "📈 Regular performance monitoring",
                "🕐 Attendance and course-engagement monitoring",
                "💰 Assessment of possible financial difficulties",
                "👨‍🏫 Additional academic support",
            ]
        ),
        "Enrolled": (
            "info", "📚 Continued monitoring is recommended.",
            [
                "📈 Monitor academic progress",
                "🕐 Encourage consistent attendance",
                "📚 Support improvement in semester performance",
                "👨‍🏫 Provide guidance where difficulties appear",
            ]
        ),
        "Graduate": (
            "success", "🎓 Student shows a positive predicted outcome.",
            [
                "📚 Maintain current academic performance",
                "🕐 Continue regular attendance",
                "✅ Keep academic requirements up to date",
                "🎯 Encourage continued academic engagement",
            ]
        ),
    }

    level, note, bullets = recommendations.get(
        prediction, ("info", "No specific recommendation available.", [])
    )
    getattr(st, level)(note)
    if bullets:
        st.markdown("\n".join(f"- {b}" for b in bullets))

    # ---------------- Downloadable report ----------------
    report_lines = [
        "EduPredict — Prediction Report",
        f"Generated: {st.session_state.last_run_at}",
        f"Predicted Outcome: {prediction}",
        f"Confidence: {confidence:.2f}%",
        "",
        "Class Probabilities:",
    ] + [f"  - {k}: {v * 100:.2f}%" for k, v in probability_dict.items()]

    st.download_button(
        label="⬇️ Download Report (.txt)",
        data="\n".join(report_lines),
        file_name=f"edupredict_report_{st.session_state.last_run_at.replace(':', '-').replace(' ', '_')}.txt",
        mime="text/plain",
    )

else:
    st.info("Fill in the details above and click **Predict Student Outcome** to see results.")

# =============================================================
# Footer
# =============================================================
st.divider()
st.caption(
    "EduPredict • Machine Learning Student Outcome Prediction • "
    "For educational decision-support purposes"
)
