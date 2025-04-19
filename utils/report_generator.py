import pdfkit

def generate_html_report(student_name, email, answers, scores, tasks, kaggle_subs, leetcode_subs):
    """
    Generate an HTML report string for the student.
    """
    html = f"""
    <h2>Student Report: {student_name}</h2>
    <p><strong>Email:</strong> {email}</p>

    <h3>🧾 Submission Summary</h3>
    <ul>
        <li><strong>Kaggle Submissions:</strong> {kaggle_subs}</li>
        <li><strong>LeetCode Submissions:</strong> {leetcode_subs}</li>
    </ul>

    <h3>🧠 Text Answers & Scores</h3>
    <ul>
        <li><strong>Precision:</strong> {answers['Precision']} (Score: {scores['Precision']}/5)</li>
        <li><strong>Recall:</strong> {answers['Recall']} (Score: {scores['Recall']}/5)</li>
        <li><strong>F1 Score:</strong> {answers['F1 Score']} (Score: {scores['F1 Score']}/5)</li>
    </ul>

    <h3>✅ Task Completion</h3>
    <ul>
    {''.join([f'<li>{\"✅\" if done else \"❌\"} {task}</li>' for task, done in tasks.items()])}
    </ul>
    """
    return html


def export_to_pdf(html_content):
    """
    Convert HTML content to PDF using pdfkit.
    """
    # Convert HTML to PDF using pdfkit (You may need to install wkhtmltopdf on your system)
    pdf = pdfkit.from_string(html_content, False)  # False to return bytes instead of saving
    return pdf
