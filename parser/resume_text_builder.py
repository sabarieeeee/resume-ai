def resume_to_text(generated_resume):
    text = ""

    text += "Skills\n"
    text += generated_resume.get("Skills", "") + "\n\n"

    text += "Education\n"
    text += generated_resume.get("Education", "") + "\n\n"

    text += "Projects\n"
    for p in generated_resume.get("Projects", []):
        text += p + "\n"
    text += "\n"

    text += "Experience\n"
    for e in generated_resume.get("Experience", []):
        text += e + "\n"

    return text
