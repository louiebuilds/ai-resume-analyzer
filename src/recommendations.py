def generate_recommendations(missing_skills, score):
    recommendations = []

    if score >= 80:
        recommendations.append("Strong resume match for the target role.")
    elif score >= 60:
        recommendations.append("Moderate resume match. Add more relevant keywords and project details.")
    else:
        recommendations.append("Low resume match. Tailor the resume more closely to the job description.")

    if missing_skills:
        recommendations.append(
            "Consider adding these missing skills if you have experience with them: "
            + ", ".join(missing_skills)
        )

    recommendations.append("Use measurable achievements in your experience section.")
    recommendations.append("Tailor your summary to match the job description.")
    recommendations.append("Include relevant tools, platforms, and certifications.")

    return recommendations
