from pdfminer.high_level import extract_text
import docx

def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        return extract_text(file)
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        return file.read().decode("utf-8")
