def score_builder_resume(generated_resume):
    score = 0
    feedback = []

    # -------------------------------
    # 1. SECTION PRESENCE (30)
    # -------------------------------
    if generated_resume.get("Skills"):
        score += 10
    if generated_resume.get("Education"):
        score += 5
    if generated_resume.get("Projects"):
        score += 10
    if generated_resume.get("Experience"):
        score += 5

    # -------------------------------
    # 2. SKILLS DENSITY (25)
    # -------------------------------
    skills = generated_resume.get("Skills", "")
    skill_count = len([s for s in skills.split(",") if s.strip()])

    if skill_count >= 6:
        score += 25
    elif skill_count >= 4:
        score += 20
    else:
        score += skill_count * 5
        feedback.append("Add more technical skills.")

    # -------------------------------
    # 3. PROJECT DEPTH (20)
    # -------------------------------
    projects = generated_resume.get("Projects", [])

    if len(projects) >= 3:
        score += 20
    elif len(projects) == 2:
        score += 15
    elif len(projects) == 1:
        score += 8
        feedback.append("Add more project impact points.")

    # -------------------------------
    # 4. EXPERIENCE DEPTH (15)
    # -------------------------------
    experience = generated_resume.get("Experience", [])

    if len(experience) >= 3:
        score += 15
    elif len(experience) == 2:
        score += 10
    elif len(experience) == 1:
        score += 5
        feedback.append("Expand experience responsibilities.")

    # -------------------------------
    # 5. ACTION VERBS BONUS (10)
    # -------------------------------
    action_verbs = [
        "developed", "implemented", "designed",
        "built", "optimized", "created", "analyzed", "applied"
    ]

    verb_bonus = 0
    for section in ["Projects", "Experience"]:
        for line in generated_resume.get(section, []):
            if any(v in line.lower() for v in action_verbs):
                verb_bonus = 10
                break

    score += verb_bonus

    # -------------------------------
    # FINAL CLAMP
    # -------------------------------
    score = max(0, min(100, score))

    return score, feedback
