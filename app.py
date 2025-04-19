import streamlit as st
import pandas as pd
import base64
from utils.analyzer import score_answer
from utils.report_generator import generate_html_report, export_to_pdf
from utils.leetcode_fetcher import fetch_leetcode_stats
import re

st.set_page_config(page_title="Student Submission Analyzer", layout="wide")
st.title("📊 Student Submission Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload the Excel File", type=["xlsx"])

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    # Display data overview
    with st.expander("📄 View Raw Data"):
        st.dataframe(df)

    # Show student selector
    students = df[["First Name", "Last Name"]].fillna("").apply(lambda x: f"{x['First Name']} {x['Last Name']}", axis=1).tolist()
    selected_student = st.selectbox("Select a student to view details", students)

    # Extract student data
    student_row = df.loc[students.index(selected_student)]

    # Display details
    st.subheader(f"🧑 Profile: {selected_student}")
    email = student_row['Email Address']
    st.markdown(f"**Email:** {email}")

    # Display Submission Links
    st.markdown("### 📎 Submissions")
    kaggle_link = student_row.iloc[-3]
    leetcode_link = student_row.iloc[-2]
    github_id = student_row.iloc[-1]

    st.markdown(f"- [Confusion Matrix Image]({student_row.iloc[5]})")
    st.markdown(f"- [Kaggle Profile]({kaggle_link})")
    st.markdown(f"- [LeetCode]({leetcode_link})")
    if pd.notna(github_id):
        st.markdown(f"- [GitHub](https://github.com/{github_id})")

    # Show NLP answers and score them
    st.markdown("### 🧠 Text Answers and Auto Scores")
    precision_ans = student_row['In english, describe what is Precision. (do not just describe how to calculate, describe what it means in simple english)']
    recall_ans = student_row['In english, describe what is Recall. (do not just describe how to calculate, describe what it means in simple english)']
    f1_ans = student_row['In english, describe what is F1 score, and when do you need it?']

    precision_score = score_answer(precision_ans, "Precision")
    recall_score = score_answer(recall_ans, "Recall")
    f1_score = score_answer(f1_ans, "F1 Score")

    st.markdown(f"**Precision:** {precision_ans} \n\n 🏅 Score: {precision_score}/5")
    st.markdown(f"**Recall:** {recall_ans} \n\n 🏅 Score: {recall_score}/5")
    st.markdown(f"**F1 Score:** {f1_ans} \n\n 🏅 Score: {f1_score}/5")

    # Task status
    st.markdown("### ✅ Task Completion")
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
        emoji = "✅" if done else "❌"
        task_status[task] = done
        st.markdown(f"- {emoji} {task}")

    # Count Kaggle/LeetCode submissions based on task mentions
    kaggle_submissions = sum([
        task_status["I have successfully uploaded another classification problem in Kaggle notebook to my folder."],
        task_status["I have successfully uploaded another regression problem in Kaggle notebook to my folder."]
    ])

    # Fetch LeetCode submissions if the username is present
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

    # Export to PDF
    st.markdown("### 🧾 Download Report")
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
    html_report = generate_html_report(selected_student, email, answers, scores, task_status, kaggle_submissions, leetcode_submissions)
    pdf_bytes = export_to_pdf(html_report)
    st.download_button("📄 Download Report as PDF", data=pdf_bytes, file_name=f"{selected_student.replace(' ', '_')}_report.pdf")

else:
    st.info("Please upload an Excel file to begin.")
