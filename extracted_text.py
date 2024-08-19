import fitz  # PyMuPDF
import requests

import docx2txt


def extract_text_from_docx(docx_path):
    text = docx2txt.process(docx_path)
    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    doc.close()
    return text

def send_text_to_backend(text):
    url = "http://localhost:8080/receive-text"
    response = requests.post(url, json={"text": text})
    return response.json()

if __name__ == "__main__":
    pdf_path = "demo.pdf"
    doc_path="demo.docx"
    doc_text=extract_text_from_docx(doc_path)
    text = extract_text_from_pdf(pdf_path)
    result = send_text_to_backend(doc_text)
    print(result)  # Check the response from the server
