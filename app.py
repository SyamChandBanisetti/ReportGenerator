import streamlit as st
import pandas as pd
from utils.analyzer import evaluate_confusion_formulas
from utils.report_generator import generate_html_report

st.set_page_config(page_title="Student Formula Report", layout="wide")

st.title("📊 Student Confusion Matrix Formula Analyzer")

uploaded_file = st.file_uploader("Upload student Excel file", type=["xlsx"])
student_name = st.text_input("Enter Student Name")

if uploaded_file and student_name:
    try:
        df = pd.read_excel(uploaded_file)

        results = evaluate_confusion_formulas(df)
        html_report = generate_html_report(results, student_name)

        st.success("✅ Report generated successfully!")
        st.components.v1.html(html_report, height=800, scrolling=True)

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
