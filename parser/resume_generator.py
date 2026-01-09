def generate_resume_content(sections):
    resume = {}

    # -------------------------------
    # PERSONAL DETAILS (STRUCTURED)
    # -------------------------------
    name = ""
    email = ""
    phone = ""

    for item in sections.get("Personal Details", []):
        lower = item.lower()

        if "name" in lower:
            name = item.replace("Name:", "").strip()
        elif "email" in lower:
            email = item.replace("Email:", "").strip()
        elif "phone" in lower or "mobile" in lower:
            phone = item.replace("Phone:", "").strip()

    resume["Name"] = name if name else "Your Name"
    resume["Email"] = email if email else "your@email.com"
    resume["Phone"] = phone if phone else "XXXXXXXXXX"

    # -------------------------------
    # SKILLS (ATS KEYWORD DENSE)
    # -------------------------------
    skills = sections.get("Skills", [])
    resume["Skills"] = ", ".join(skills) if skills else "Python, Java, SQL"

    # -------------------------------
    # EDUCATION (STANDARD FORMAT)
    # -------------------------------
    education = sections.get("Education", [])
    if education:
        resume["Education"] = f"Bachelor of Technology in {education[0]}"
    else:
        resume["Education"] = "Bachelor of Technology in Computer Science"

    # -------------------------------
    # PROJECTS (ACTION-ORIENTED)
    # -------------------------------
    projects = sections.get("Projects", [])

    if projects:
        resume["Projects"] = [
            f"Developed a project focused on {projects[0].lower()}",
            "Applied problem-solving and development best practices"
        ]
    else:
        resume["Projects"] = [
            "Developed academic projects demonstrating technical proficiency",
            "Applied software development best practices"
        ]

    # -------------------------------
    # EXPERIENCE (FRESHER-SAFE)
    # -------------------------------
    experience = sections.get("Experience", [])

    resume["Experience"] = [
        "Seeking entry-level software engineering opportunities",
        "Strong foundation in programming and software development"
    ]

    return resume
