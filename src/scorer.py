def calculate_match_score(resume_skills, job_skills):
    if not job_skills:
        return 0

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = resume_set.intersection(job_set)
    score = (len(matched) / len(job_set)) * 100

    return round(score, 2), sorted(list(matched))


def find_missing_skills(resume_skills, job_skills):
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    missing = job_set - resume_set
    return sorted(list(missing))
