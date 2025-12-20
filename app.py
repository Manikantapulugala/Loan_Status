import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open("C:\\Users\\saikr\\Documents\\Loan_status_ml_project_deployment\\loan_status.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Loan Approval Prediction")

age = st.number_input("Enter Your Age", 18, 150)

education = st.selectbox("Education", ['Master', 'High School', 'Bachelor', 'Associate', 'Doctorate'])

home_ownership_status = st.pills("Home Ownership Status", ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])

income = st.number_input("Annual Income", 0)

Credit_score = st.number_input("Credit Score", 0)

credit_history_length = st.number_input("Credit History Length", 0)

loan_amount = st.number_input("Loan Amount", 0)

loan_purpose = st.selectbox("Loan Purpose", ['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'])

intrest_rate = st.slider("Interest Rate (%)", 0.00, 25.00, value=0.00, step= 0.01, format="%.2f")

loan_percent_income = st.slider("Loan Percent Income", 0.0, 0.99, value=0.0, step=0.01, format="%.2f")

past_loan_defaults = st.pills("Past Loan Defaults", ['No', 'Yes'])

if st.button("Loan Status"):
    input_df = pd.DataFrame([{'Age' : age,
                              'Education' : education,
                              'Home_Ownership_Status' : home_ownership_status,
                              'Income' : income,
                              'Credit_Score' : Credit_score,
                              'Credit_History_Length' : credit_history_length,
                              'Loan_Amount' : loan_amount,
                              'Loan_Purpose' : loan_purpose,
                              'Interest_Rate' : intrest_rate,
                              'Loan_Percent_Income' : loan_percent_income,
                              'Past_Loan_Defaults' : past_loan_defaults}])
    

    result = model.predict(input_df)[0]
    if result == 0:
        st.error("Rejected")
    else:
        st.success("Approved")