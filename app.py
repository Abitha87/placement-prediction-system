import streamlit as st
import joblib
import numpy as np
st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="🎓",
    layout="centered"
)
# Load model
model = joblib.load("placement_model.pkl")

st.title("🎓 Student Placement Prediction System")
st.markdown("""
This AI-powered system predicts a student's placement chances
based on academic performance, coding skills, aptitude, internships,
and communication skills.
""")

st.write("Enter student details below:")

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.number_input("Age", 18, 35)

cgpa = st.number_input("CGPA", 0.0, 10.0)

backlogs = st.number_input("Backlogs", 0, 20)

internships = st.number_input("Internships", 0, 20)

certifications = st.number_input("Certifications", 0, 50)

coding_skills = st.slider("Coding Skills", 0, 100)

communication_skills = st.slider("Communication Skills", 0, 100)

aptitude_score = st.slider("Aptitude Score", 0, 100)

projects = st.number_input("Projects", 0, 50)

if st.button("Predict Placement"):

    # Convert Gender
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    # Temporary values for Degree and Branch
    degree = 0
    branch = 0

    data = np.array([[
        gender,
        age,
        degree,
        branch,
        cgpa,
        backlogs,
        internships,
        certifications,
        coding_skills,
        communication_skills,
        aptitude_score,
        projects
    ]])

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    placement_chance = probability[0][1] * 100

    st.write(f"Placement Probability: {placement_chance:.2f}%")

    st.progress(int(placement_chance))

    if prediction[0] == 1:
     st.success("🎉 Student is likely to be Placed")
    else:
     st.error("❌ Student is unlikely to be Placed")

    if coding_skills < 70:
     st.warning("Improve coding skills.")

    if aptitude_score < 70:
     st.warning("Practice aptitude regularly.")

    if communication_skills < 70:
     st.warning("Work on communication skills.")

    if internships == 0:
     st.warning("Consider doing an internship.")

    if projects < 2:
     st.warning("Build more projects.")