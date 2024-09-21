import streamlit as st

# Function to calculate  Score
def calculate_heart_score(history, ecg, age, risk_factors, troponin):
    return history + ecg + age + risk_factors + troponin

# Function to interpret the HEART score result
def interpret_heart_score(score):
    if score <= 3:
        return "Low risk (1.7% risk of major cardiac events)"
    elif 4 <= score <= 6:
        return "Moderate risk (16.6% risk of major cardiac events)"
    else:
        return "High risk (50.1% risk of major cardiac events)"

# Streamlit app layout
def main():
    st.title("Beta Version - Score Calculator")

    st.write("""
    ## HEART Score for Major Adverse Cardiac Events
    The HEART score is used to evaluate the risk of major adverse cardiac events (MACE) in patients with chest pain.
    The score consists of 5 elements: history, ECG, age, risk factors, and troponin levels.
    """)

    # Input for History
    st.subheader("History")
    history = st.radio(
        "Select the history score:",
        (0, 1, 2),
        format_func=lambda x: {0: "Slightly suspicious", 1: "Moderately suspicious", 2: "Highly suspicious"}[x]
    )

    # Input for ECG
    st.subheader("ECG")
    ecg = st.radio(
        "Select the ECG score:",
        (0, 1, 2),
        format_func=lambda x: {0: "Normal", 1: "Non-specific repolarization disturbance", 2: "Significant ST deviation"}[x]
    )

    # Input for Age
    st.subheader("Age")
    age = st.radio(
        "Select the age score:",
        (0, 1, 2),
        format_func=lambda x: {0: "<45 years", 1: "45-65 years", 2: ">65 years"}[x]
    )

    # Input for Risk Factors
    st.subheader("Risk Factors")
    risk_factors = st.radio(
        "Select the risk factors score:",
        (0, 1, 2),
        format_func=lambda x: {
            0: "No known risk factors",
            1: "1-2 risk factors (e.g., hypertension, smoking)",
            2: "≥3 risk factors or history of atherosclerosis"
        }[x]
    )

    # Input for Troponin
    st.subheader("Troponin")
    troponin = st.radio(
        "Select the troponin score:",
        (0, 1, 2),
        format_func=lambda x: {0: "≤ normal limit", 1: "1-3x normal limit", 2: ">3x normal limit"}[x]
    )

    # Button to calculate HEART score
    if st.button("Calculate HEART Score"):
        score = calculate_heart_score(history, ecg, age, risk_factors, troponin)
        st.write(f"### Your HEART Score is: {score}")
        st.write(f"### Risk Category: {interpret_heart_score(score)}")

# Run the app
if __name__ == '__main__':
    main()
