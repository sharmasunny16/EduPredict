# 🎓 EduPredict — Student Dropout & Academic Performance Prediction

EduPredict is a Machine Learning-based web application that predicts a student's academic outcome as **Dropout, Enrolled, or Graduate** based on admission information, academic performance, personal/financial factors, and economic indicators.

The project is built using **Python, Scikit-learn, Pandas, Joblib, and Streamlit** and is deployed as a live web application using Streamlit Community Cloud.

---

## 🚀 Live Demo

🌐 **EduPredict Web App:**  
https://edupredict-szzu2ykxsdgtqxgpqbyl94.streamlit.app/

---

## 📌 Project Overview

Student dropout is an important challenge for educational institutions. Early identification of students who may be at risk can help institutions provide timely academic and financial support.

EduPredict uses Machine Learning to analyze student-related features and predict one of three possible outcomes:

- 🔴 **Dropout**
- 🟡 **Enrolled**
- 🟢 **Graduate**

The system is designed as a **decision-support tool**, not as a replacement for professional academic decision-making.

---

## 🎯 Objectives

- Predict student academic outcomes using Machine Learning.
- Identify students who may be at risk of dropping out.
- Analyze the impact of academic and student-related factors.
- Provide prediction probabilities for each outcome.
- Provide recommended actions based on the predicted outcome.
- Develop an easy-to-use web interface for prediction.
- Deploy the ML application online.

---

## 📊 Dataset

The project uses the **Predict Students' Dropout and Academic Success** dataset from the UCI Machine Learning Repository.

### Dataset Information

- **Instances:** 4,424
- **Input Features:** 36
- **Target Classes:** 3
- **Missing Values:** None

### Target Classes

| Target | Description |
|---|---|
| Dropout | Student discontinued studies |
| Enrolled | Student is currently enrolled |
| Graduate | Student successfully graduated |

### Dataset Source

UCI Machine Learning Repository:

https://uci.ics.uci.edu/dataset/697/predict%2Bstudents%2Bdropout%2Band%2Bacademic%2Bsuccess

---

## 🧠 Machine Learning Models

Multiple classification algorithms were trained and evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting
5. Balanced Logistic Regression

### Model Comparison

| Model | Test Accuracy | Macro F1 |
|---|---:|---:|
| Logistic Regression | **76.84%** | **0.70** |
| Decision Tree | ~72.43% | ~0.66 |
| Random Forest | 76.50% | 0.66 |
| Gradient Boosting | 75.59% | 0.67 |
| Balanced Logistic Regression | 72.54% | 0.69 |

### 🏆 Final Model

**Logistic Regression**

Test Accuracy:

**76.84%**

The final model was selected based on overall performance and class-wise evaluation.

---

## ⚙️ Machine Learning Pipeline

The project follows the following workflow:

```text
Student Dataset
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Train/Test Split
       ↓
Feature Preprocessing
       ↓
One-Hot Encoding
       ↓
Feature Scaling
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Final Logistic Regression Model
       ↓
Model Serialization
       ↓
Streamlit Application
       ↓
Online Deployment
🔧 Data Preprocessing

Different types of features are processed separately.

Categorical Features

Categorical variables are converted using:

OneHotEncoder(handle_unknown="ignore")
Numerical Features

Numerical variables are standardized using:

StandardScaler()
Binary Features

Binary features are passed through without transformation.

The complete preprocessing and model are combined into a Scikit-learn Pipeline.

📈 Model Evaluation

The final Logistic Regression model achieved:

Accuracy: 76.84%
Classification Report
Class	Precision	Recall	F1-Score
Dropout	0.79	0.75	0.77
Enrolled	0.55	0.40	0.46
Graduate	0.81	0.91	0.86
Macro Avg	0.72	0.69	0.70

The model performs particularly well for the Graduate and Dropout classes, while the Enrolled class is more challenging to classify.

🖥️ Application Features

EduPredict provides a user-friendly Streamlit interface with four major input sections:

1. 🎓 Admission Information
Marital Status
Application Mode
Application Order
Course
Daytime/Evening Attendance
Previous Qualification
Previous Qualification Grade
Admission Grade
2. 📚 Academic Performance
First Semester Academic Information
Second Semester Academic Information
Credits
Enrolled Units
Evaluations
Approved Units
Grades
Units Without Evaluation
3. 👤 Personal & Financial Information
Nationality
Gender
Debtor Status
Tuition Fees Status
Scholarship Holder
Educational Special Needs
International Student
Parent-related information
4. 🌍 Economic Indicators
Unemployment Rate
Inflation Rate
GDP
🔮 Prediction Output

After entering student information, the application provides:

Predicted Student Outcome
Prediction Confidence
Probability for each class
Outcome status
Recommended actions
Downloadable prediction report

Example:

Predicted Outcome: Graduate

Confidence: 89.78%

Dropout:   5.89%
Enrolled:  4.33%
Graduate: 89.78%
🛠️ Technology Stack
Technology	Purpose
Python	Programming Language
Pandas	Data Processing
NumPy	Numerical Operations
Scikit-learn	Machine Learning
Joblib	Model Serialization
Streamlit	Web Application
Git	Version Control
GitHub	Source Code Repository
Streamlit Community Cloud	Deployment
📁 Project Structure
EduPredict/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── data.csv
│
├── models/
│   └── edupredict_model.joblib
│
├── notebooks/
│   └── EDA and Model Training
│
├── src/
│   └── Project Source Files
│
├── images/
│   └── Project Screenshots
│
└── .venv/
    └── Python Virtual Environment

.venv/ should not be uploaded to GitHub and is normally included in .gitignore.

💻 Installation & Setup
1. Clone the Repository
git clone https://github.com/sharmasunny16/EduPredict.git
2. Navigate to the Project
cd EduPredict
3. Create Virtual Environment
python -m venv .venv
4. Activate Virtual Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
streamlit run app.py

The application will open in your browser.

📦 Requirements

Main dependencies:

streamlit==1.63.0
pandas
scikit-learn
joblib
🌐 Deployment

The application is deployed using Streamlit Community Cloud.

Deployment configuration:

Repository: sharmasunny16/EduPredict
Branch: main
Main File: app.py

Live application:

https://edupredict-szzu2ykxsdgtqxgpqbyl94.streamlit.app/

🔍 Important Features
Explainable Input Design

The original dataset contains numerical codes for several categorical variables. EduPredict converts these codes into human-readable options in the UI while preserving the original numerical values required by the trained model.

Probability-Based Prediction

Instead of displaying only the predicted class, the application also shows the probability distribution:

Dropout   → Probability
Enrolled  → Probability
Graduate  → Probability

This provides more information than a simple class prediction.

⚠️ Limitations
The model is trained on a specific dataset and may not generalize perfectly to every institution.
The Enrolled class is comparatively harder to predict.
Predictions should not be treated as guaranteed outcomes.
Model predictions should support, not replace, institutional or professional decisions.
Dataset-based correlations should not be interpreted as causal relationships.
🔮 Future Enhancements

Possible future improvements include:

📊 Interactive analytics dashboard
📈 Student risk trend visualization
🚨 Early-warning system for high-risk students
📧 Automated alerts for academic staff
👥 Student-wise prediction history
🗄️ Database integration
🔐 User authentication
📱 Improved mobile interface
🤖 Advanced ML models
🔍 Explainable AI using SHAP
☁️ Scalable cloud deployment
👨‍💻 Author

Sunny Sharma

GitHub:
https://github.com/sharmasunny16

Project Repository:
https://github.com/sharmasunny16/EduPredict

📜 Disclaimer

EduPredict is an academic Machine Learning project developed for educational and decision-support purposes.

The predictions generated by the system should not be considered definitive judgments about a student's future academic performance.

⭐ If You Like This Project

If you find EduPredict useful or interesting, consider giving the repository a ⭐ on GitHub.