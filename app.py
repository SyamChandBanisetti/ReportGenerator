# app.py

import streamlit as st
import pandas as pd
from utils.report_generator import generate_html_report
from utils.leetcode_fetcher import fetch_leetcode_data

st.set_page_config(page_title="Student Report Analyzer", layout="wide")

st.title("📊 Student Submission Analyzer")

uploaded_file = st.file_uploader("Upload Student Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        if "Name" not in df.columns:
            st.error("The uploaded file must contain a 'Name' column.")
        else:
            student_names = df["Name"].dropna().unique().tolist()
            selected_student = st.selectbox("Select a student to generate report", student_names)

            if st.button("Generate Report"):
                student_data = df[df["Name"] == selected_student]

                if student_data.empty:
                    st.warning("No data found for the selected student.")
                else:
                    # Extract LeetCode username (if available)
                    leetcode_username = student_data.iloc[0].get("Leetcode", "")
                    leetcode_stats = None
                    if pd.notna(leetcode_username) and leetcode_username.strip():
                        try:
                            leetcode_stats = fetch_leetcode_data(leetcode_username.strip())
                        except Exception as e:
                            st.warning(f"Could not fetch LeetCode data: {e}")

                    # Generate HTML report
                    html_report = generate_html_report(student_data, leetcode_stats)

                    # Display report in browser
                    st.components.v1.html(html_report, height=600, scrolling=True)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
