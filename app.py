import streamlit as st
import pandas as pd
from utils.report_generator import generate_html_report, export_to_pdf
from utils.analyzer import score_answer
from utils.leetcode_fetcher import fetch_leetcode_stats
import re

# Function to process the student's submission and generate report
def process_student_submission(file, student_name):
    df = pd.read_excel(file)
    student_row = df[df['First Name'] + ' ' + df['Last Name'] == student_name].iloc[0]
    
    # Fetch and score answers
    precision_ans = student_row['In english, describe what is Precision. (do not just describe how to calculate, describe what it means in simple english)']
    recall_ans = student_row['In english, describe what is Recall. (do not just describe how to calculate, describe what it means in simple english)']
    f1_ans = student_row['In english, describe what is F1 score, and when do you need it?']

    precision_score = score_answer(precision_ans, "Precision")
    recall_score = score_answer(recall_ans, "Recall")
    f1_score = score_answer(f1_ans, "F1 Score")

    # Task completion status
    task_cols = [
        "I have successfully uploaded the titanic notebook to my folder",
        "I have successfully uploaded the CA Housing Price notebook to my folder",
        "I have successfully uploaded another classification problem in Kaggle notebook to my folder.",
        "I have successfully uploaded another regression problem in Kaggle notebook to my folder."
    ]
    task_status = {}
    for task in task_cols:
        status = student_row[task]
        done = str(status).strip().lower() == "yes"
        task_status[task] = done

    # Kaggle and LeetCode submission counts
    kaggle_submissions = sum([
        task_status["I have successfully uploaded another classification problem in Kaggle notebook to my folder."],
        task_status["I have successfully uploaded another regression problem in Kaggle notebook to my folder."]
    ])

    leetcode_username = None
    try:
        leetcode_url = student_row.iloc[-2]  # or wherever the LeetCode profile is
        match = re.search(r"leetcode\.com/u/([^/]+)/?", leetcode_url)
        if match:
            leetcode_username = match.group(1)
    except:
        pass

    if leetcode_username:
        leetcode_submissions = fetch_leetcode_stats(leetcode_username)
    else:
        leetcode_submissions = 0

    # Generate HTML report
    answers = {
        "Precision": precision_ans,
        "Recall": recall_ans,
        "F1 Score": f1_ans
    }
    scores = {
        "Precision": precision_score,
        "Recall": recall_score,
        "F1 Score": f1_score
    }

    html_report = generate_html_report(student_name, student_row['Email Address'], answers, scores, task_status, kaggle_submissions, leetcode_submissions)
    pdf_bytes = export_to_pdf(html_report)

    return pdf_bytes, precision_score, recall_score, f1_score

# Streamlit UI
st.title("Student Submission Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload Excel file with student data", type="xlsx")

if uploaded_file:
    # Load the file to get student names
    df = pd.read_excel(uploaded_file)
    student_names = df['First Name'] + ' ' + df['Last Name']
    
    # Dropdown for selecting student
    student_name = st.selectbox("Select Student", student_names)
    
    # Button to generate report
    if st.button("Generate Report"):
        # Process the submission and generate report
        pdf_bytes, precision_score, recall_score, f1_score = process_student_submission(uploaded_file, student_name)

        # Show the scores
        st.subheader("Scores")
        st.write(f"Precision Score: {precision_score}/5")
        st.write(f"Recall Score: {recall_score}/5")
        st.write(f"F1 Score: {f1_score}/5")

        # Provide a link to download the PDF report
        st.download_button("Download PDF Report", pdf_bytes, file_name=f"{student_name}_report.pdf", mime="application/pdf")
