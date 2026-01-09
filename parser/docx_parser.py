import docx

def extract_text_from_docx(file_path):
    try:
        document = docx.Document(file_path)
        text = []
        for para in document.paragraphs:
            text.append(para.text)
        return "\n".join(text)
    except:
        return ""
