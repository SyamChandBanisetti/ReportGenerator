def generate_html_report(results, student_name):
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f9f9f9;
            }}
            h1 {{
                color: #333;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #eee;
            }}
            .score {{
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>Formula Evaluation Report for {student_name}</h1>
        <table>
            <tr><th>Metric</th><th>Correct</th><th>Score</th></tr>
            <tr><td>Accuracy</td><td>{results['Accuracy']['correct']}</td><td>{results['Accuracy']['score']}</td></tr>
            <tr><td>Precision</td><td>{results['Precision']['correct']}</td><td>{results['Precision']['score']}</td></tr>
            <tr><td>Recall</td><td>{results['Recall']['correct']}</td><td>{results['Recall']['score']}</td></tr>
            <tr><td>F1-Score</td><td>{results['F1']['correct']}</td><td>{results['F1']['score']}</td></tr>
            <tr><td colspan="2" class="score">Total Score</td><td class="score">{results['Total']}</td></tr>
        </table>
    </body>
    </html>
    """
    return html
