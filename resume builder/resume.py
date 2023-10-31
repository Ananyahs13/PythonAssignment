def generate_resume(name, summary, technical_skills, project_details):
    resume = f"Name: {name}\n"
    resume += f"Summary: {summary}\n"
    resume += f"Technical Skills: {technical_skills}\n\n"

    resume += "Project Details:\n"
    for project in project_details:
        resume += f"Project Name: {project['name']}\n"
        resume += f"Description: {project['description']}\n"
        resume += f"Duration: {project['duration']}\n\n"

    return resume


if __name__ == "__main__":
    # Sample data
    name = "Ananya"
    summary = "Developer"
    technical_skills = "Python, JavaScript, SQL"
    project1 = {"name": "Project A", "description": "Web application development", "duration": "6 months"}
    project2 = {"name": "Project B", "description": "Database design", "duration": "4 months"}
    project_details = [project1, project2]

    # Generate the resume
    resume_text = generate_resume(name, summary, technical_skills, project_details)

    # Print the resume
    print(resume_text)
