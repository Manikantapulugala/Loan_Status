# 🏦 Loan Approval Prediction App

An AI-powered Loan Approval Prediction web application built using **Python**, **Machine Learning**, and **Streamlit**.  
This application predicts whether a loan application will be **Approved** or **Rejected** based on user financial and personal details.  
The model is trained using historical loan data and deployed with an interactive Streamlit interface.

Source Code: :contentReference[oaicite:0]{index=0}

---

# 🚀 Features

- ✅ Predict loan approval instantly
- ✅ User-friendly Streamlit interface
- ✅ Machine Learning-based prediction system
- ✅ Handles multiple user input parameters
- ✅ Interactive sliders and selection fields
- ✅ Real-time prediction results
- ✅ Clean and responsive UI
- ✅ Supports categorical and numerical inputs

---

# 🛠 Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Pickle
- Machine Learning Model

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── loan_status.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/loan-approval-prediction.git

cd loan-approval-prediction
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 Input Parameters

The application uses the following user inputs for prediction:

- Age
- Education
- Home Ownership Status
- Annual Income
- Credit Score
- Credit History Length
- Loan Amount
- Loan Purpose
- Interest Rate
- Loan Percent Income
- Past Loan Defaults

---

# 🤖 Machine Learning Workflow

```text
User Input
     ↓
Data Preprocessing
     ↓
ML Model Prediction
     ↓
Loan Approval Result
     ↓
Approved / Rejected
```

---

# 📸 Application Preview

## Home Page

> Add Screenshot Here

---

## Prediction Result

> Add Screenshot Here

---

# 📦 Model Prediction

The trained model predicts:

- ✅ Loan Approved
- ❌ Loan Rejected

based on the financial and credit details entered by the user.

---

# 🔥 Key Concepts Used

- Streamlit UI Components
- Machine Learning Prediction
- DataFrames using Pandas
- Pickle Model Loading
- User Input Handling
- Real-time Predictions

---

# 🎯 Future Improvements

- Add probability/confidence score
- Deploy using Streamlit Cloud
- Add authentication system
- Improve UI with custom themes
- Add graphical analytics dashboard
- Support multiple ML models
