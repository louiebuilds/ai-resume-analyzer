def normalize_text(text):
    return text.lower()


def extract_skills(text, skill_list):
    text_lower = normalize_text(text)
    found_skills = []

    for skill in skill_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


DEFAULT_SKILLS = [
    "Python",
    "Machine Learning",
    "NLP",
    "Power Automate",
    "ServiceNow",
    "Workflow Automation",
    "Excel",
    "Data Analysis",
    "Process Optimization",
    "Incident Management",
    "Automation",
    "AI",
    "Reporting",
    "Dashboard",
    "Text Processing"
]
