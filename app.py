# app.py

import streamlit as st
import pandas as pd
from utils.report_generator import generate_html_report
from utils.leetcode_fetcher import fetch_leetcode_data

st.set_page_config(page_title="Student Report Analyzer", layout="wide")

st.title("📊 Student Report Analyzer")

uploaded_file = st.file_uploader("Upload the Excel file", type=["xlsx"])
student_name = st.text_input("Enter Student Name")

if uploaded_file and student_name:
    try:
        df = pd.read_excel(uploaded_file)

        # Extract LeetCode username if present
        leetcode_username = df.iloc[0].get("LeetCode Username", None)

        # Generate HTML Report
        html_report, precision_score, recall_score, f1_score = generate_html_report(df, student_name)

        # Fetch LeetCode stats if username is provided
        leetcode_info = ""
        if leetcode_username:
            try:
                stats = fetch_leetcode_data(leetcode_username)
                leetcode_info += f"💡 LeetCode Stats for `{leetcode_username}`\n"
                leetcode_info += f"- Total Problems Solved: {stats['totalSolved']}\n"
                leetcode_info += f"- Easy: {stats['easySolved']}, Medium: {stats['mediumSolved']}, Hard: {stats['hardSolved']}\n"
                leetcode_info += f"- Ranking: {stats['ranking']}"
                st.markdown(leetcode_info)
            except:
                st.warning("Could not fetch LeetCode stats.")

        st.markdown("---")
        st.markdown("### 🧾 Generated Report")
        st.components.v1.html(html_report, height=700, scrolling=True)

        st.markdown("### 🧮 Evaluation Metrics")
        st.write(f"- **Precision**: {precision_score}")
        st.write(f"- **Recall**: {recall_score}")
        st.write(f"- **F1 Score**: {f1_score}")

    except Exception as e:
        st.error(f"❌ Error processing the uploaded file. Make sure it's in the correct format.\n\nDetails: {str(e)}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
