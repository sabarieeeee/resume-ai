def score_ats(sections):
    score = 0
    feedback = []

    # -------------------------------
    # 1. SECTION COMPLETENESS (40)
    # -------------------------------
    section_weights = {
        "Skills": 10,
        "Education": 10,
        "Projects": 10,
        "Experience": 10
    }

    for section, weight in section_weights.items():
        if sections.get(section):
            score += weight
        else:
            feedback.append(f"Add content to your {section} section.")

    # -------------------------------
    # 2. SKILL COVERAGE (30)
    # -------------------------------
    skills = sections.get("Skills", [])
    skill_count = len(set(skills))

    if skill_count >= 6:
        score += 30
    elif skill_count >= 4:
        score += 25
    elif skill_count >= 3:
        score += 20
    else:
        score += skill_count * 5
        feedback.append("Consider adding more relevant technical skills.")

    # -------------------------------
    # 3. CONTENT DEPTH (20)
    # -------------------------------
    content_score = 0

    projects = sections.get("Projects", [])
    experience = sections.get("Experience", [])

    if len(projects) >= 2:
        content_score += 10
    elif len(projects) == 1:
        content_score += 5
        feedback.append("Add more detailed project descriptions.")

    if len(experience) >= 2:
        content_score += 10
    elif len(experience) == 1:
        content_score += 5
        feedback.append("Expand experience section with responsibilities.")

    score += content_score

    # -------------------------------
    # 4. ACTION VERBS BONUS (10)
    # -------------------------------
    action_verbs = [
        "developed", "implemented", "designed",
        "built", "optimized", "created", "analyzed"
    ]

    verb_bonus = 0
    for sec in ["Projects", "Experience"]:
        for line in sections.get(sec, []):
            if any(v in line.lower() for v in action_verbs):
                verb_bonus = 10
                break

    if verb_bonus == 0:
        feedback.append("Use action verbs to strengthen impact.")

    score += verb_bonus

    # -------------------------------
    # FINAL CLAMP
    # -------------------------------
    score = max(0, min(100, score))

    return score, feedback
