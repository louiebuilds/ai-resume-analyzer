import json
import os

from parser import load_text_file, extract_email, extract_phone
from skill_extractor import extract_skills, DEFAULT_SKILLS
from scorer import calculate_match_score, find_missing_skills
from recommendations import generate_recommendations


def save_output(result, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)


def main():
    resume_path = "data/sample_resume.txt"
    job_description_path = "data/sample_job_description.txt"
    output_path = "outputs/analysis_result.json"

    resume_text = load_text_file(resume_path)
    job_text = load_text_file(job_description_path)

    email = extract_email(resume_text)
    phone = extract_phone(resume_text)

    resume_skills = extract_skills(resume_text, DEFAULT_SKILLS)
    job_skills = extract_skills(job_text, DEFAULT_SKILLS)

    match_score, matched_skills = calculate_match_score(resume_skills, job_skills)
    missing_skills = find_missing_skills(resume_skills, job_skills)
    recommendations = generate_recommendations(missing_skills, match_score)

    result = {
        "candidate_email": email,
        "candidate_phone": phone,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score,
        "recommendations": recommendations
    }

    save_output(result, output_path)

    print("Resume Analysis Complete")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
