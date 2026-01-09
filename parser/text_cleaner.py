import re

def clean_profile_text(text):
    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Normalize newlines for readability
    text = text.replace(". ", ".\n")

    # Strip leading/trailing spaces
    return text.strip()
