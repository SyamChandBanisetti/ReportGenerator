# Remove this line (pdfkit import)
# import pdfkit

from weasyprint import HTML  # Keep only WeasyPrint import

def export_to_pdf(html_content):
    """
    Convert HTML content to PDF using WeasyPrint.
    This function takes an HTML string and returns the PDF as bytes.

    Args:
    - html_content (str): The HTML content to be converted into a PDF.

    Returns:
    - pdf (bytes): The generated PDF in byte format.
    """
    try:
        # Convert HTML string to PDF using WeasyPrint
        pdf = HTML(string=html_content).write_pdf()
        return pdf
    except Exception as e:
        print(f"Error converting HTML to PDF: {e}")
        raise
