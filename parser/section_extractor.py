import re

def extract_sections(text):
    sections = {
        "Personal Details": [],
        "Skills": [],
        "Education": [],
        "Projects": [],
        "Experience": []
    }

    # -------------------------------
    # PERSONAL DETAILS (SAFE TOKEN EXTRACTION)
    # -------------------------------

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\b\d{10}\b"

    # Name must STOP before email/phone or line end
    name_patterns = [
        r"my name is\s+([a-zA-Z ]+?)(?=\s+(email|phone)|$)",
        r"name\s*[:\-=\s]\s*([a-zA-Z ]+?)(?=\s+(email|phone)|$)"
    ]

    # ---- Extract tokens ----
    email_match = re.search(email_pattern, text, re.IGNORECASE)
    phone_match = re.search(phone_pattern, text)
    name = None

    for pattern in name_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            name = match.group(1).strip().title()
            break

    if name:
        sections["Personal Details"].append(f"Name: {name}")

    if email_match:
        sections["Personal Details"].append(f"Email: {email_match.group()}")

    if phone_match:
        sections["Personal Details"].append(f"Phone: {phone_match.group()}")

    # -------------------------------
    # REMOVE PERSONAL DETAILS FROM TEXT
    # -------------------------------

    clean_text = text

    if email_match:
        clean_text = clean_text.replace(email_match.group(), "")

    if phone_match:
        clean_text = clean_text.replace(phone_match.group(), "")

    for pattern in name_patterns:
        clean_text = re.sub(pattern, "", clean_text, flags=re.IGNORECASE)

    lines = [line.strip() for line in clean_text.split("\n") if line.strip()]

    # -------------------------------
    # SKILLS
    # -------------------------------

    known_skills = [
        "python", "java", "sql", "c++", "javascript",
        "html", "css", "react", "flask", "django"
    ]

    for line in lines:
        line_lower = line.lower()
        for skill in known_skills:
            if skill in line_lower:
                sections["Skills"].append(skill.capitalize())

    # -------------------------------
    # EDUCATION
    # -------------------------------

    for line in lines:
        line_lower = line.lower()
        if "computer science" in line_lower:
            sections["Education"].append("Computer Science")
        elif "student" in line_lower:
            sections["Education"].append("Student")

    # -------------------------------
    # PROJECTS
    # -------------------------------

    for line in lines:
        line_lower = line.lower()
        if "web" in line_lower:
            sections["Projects"].append("Web Development")
        elif "project" in line_lower:
            sections["Projects"].append("Academic Project")

    # -------------------------------
    # EXPERIENCE
    # -------------------------------

    for line in lines:
        line_lower = line.lower()
        if "software engineer" in line_lower:
            sections["Experience"].append("Software Engineer (Entry-level)")
        elif "intern" in line_lower:
            sections["Experience"].append("Internship Experience")

    # -------------------------------
    # REMOVE DUPLICATES
    # -------------------------------

    for key in sections:
        sections[key] = list(set(sections[key]))

    return sections
