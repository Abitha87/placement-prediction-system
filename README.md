# Student Placement Prediction System

## Project Overview

The Student Placement Prediction System is a Machine Learning-based web application that predicts whether a student is likely to be placed based on academic performance, technical skills, and employability factors.

The system analyzes multiple student attributes such as CGPA, coding skills, aptitude score, communication skills, internships, certifications, and projects to provide a placement prediction along with the probability of success.

---

## Features

* Predicts student placement status (Placed / Not Placed)
* Displays placement probability percentage
* Interactive web interface built using Streamlit
* Provides personalized improvement suggestions
* User-friendly and responsive design
* Real-time prediction results

---

## Dataset Information

The project uses the Indian Student Placement Dataset 2025, which contains information about students including:

* Gender
* Age
* Degree
* Branch
* CGPA
* Backlogs
* Internships
* Certifications
* Coding Skills
* Communication Skills
* Aptitude Score
* Projects
* Placement Status

Dataset Size:

* 12,000 records
* 16 attributes

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## Machine Learning Model

The placement prediction model was developed using the Random Forest Classifier algorithm.

### Model Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Model Deployment

---

## Input Parameters

The system accepts the following inputs:

* Gender
* Age
* CGPA
* Backlogs
* Internships
* Certifications
* Coding Skills
* Communication Skills
* Aptitude Score
* Projects Completed

---

## Output

The application provides:

* Placement Prediction
* Placement Probability (%)
* Career Improvement Suggestions

---

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```
## Live Demo
https://placement-prediction-system-abithashanmugam08.streamlit.app/
---

## Project Structure

```text
placement-prediction-system/
│
├── app.py
├── train_model.py
├── placement_model.pkl
├── requirements.txt
├── Indian_Student_Placement_Dataset_2025.csv
└── README.md
```

---

## Future Enhancements

* Salary Package Prediction
* Company Type Prediction
* Resume Analysis
* Student Performance Dashboard
* Advanced Data Visualizations
* AI-Based Career Guidance

---

## Developed By

Abitha S

B.Tech – Artificial Intelligence and Data Science

Machine Learning and Data Science Enthusiast
