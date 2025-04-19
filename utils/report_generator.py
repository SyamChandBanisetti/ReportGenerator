# report_generator.py
import weasyprint

def generate_html_report(student_name, email, answers, scores, task_status, kaggle_submissions, leetcode_submissions):
    """
    Generates an HTML report based on student information, answers, scores, task status, and submissions.
    """
    html_content = f"""
    <html>
        <head><title>Student Report for {student_name}</title></head>
        <body>
            <h1>Report for {student_name}</h1>
            <p>Email: {email}</p>
            <h2>Answers</h2>
            <ul>
    """
    
    for question, answer in answers.items():
        html_content += f"<li><b>{question}:</b> {answer}</li>"
    
    html_content += """
            </ul>
            <h2>Scores</h2>
            <ul>
    """
    
    for question, score in scores.items():
        html_content += f"<li><b>{question}:</b> {score}/5</li>"
    
    html_content += """
            </ul>
            <h2>Task Status</h2>
            <ul>
    """
    
    for task, status in task_status.items():
        status_str = "Completed" if status else "Not Completed"
        html_content += f"<li><b>{task}:</b> {status_str}</li>"
    
    html_content += f"""
            </ul>
            <h2>Kaggle Submissions</h2>
            <p>{kaggle_submissions} Kaggle submissions uploaded.</p>
            <h2>Leetcode Submissions</h2>
            <p>{leetcode_submissions} Leetcode problems solved.</p>
        </body>
    </html>
    """
    return html_content

def export_to_pdf(html_content):
    """
    Converts HTML content to a PDF and returns the PDF as bytes.
    Uses WeasyPrint for the conversion.
    """
    pdf = weasyprint.HTML(string=html_content).write_pdf()
    return pdf
