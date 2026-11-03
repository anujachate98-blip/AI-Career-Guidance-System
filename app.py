from flask import Flask, render_template, request

app = Flask(__name__)

CAREERS = {
    "Software Developer": {
        "interests": ["coding", "problem solving", "technology"],
        "skills": ["python", "java", "c", "cpp", "javascript", "html", "css"],
        "description": "Build websites, desktop applications, and software products.",
        "skills_to_learn": ["Python or Java", "Data Structures", "Git and GitHub", "SQL", "Basic web development"],
        "roadmap": ["Choose one programming language", "Practice basic programs and problem solving", "Build two small projects", "Learn Git and SQL", "Create a portfolio and prepare for interviews"]
    },
    "Data Analyst": {
        "interests": ["data", "maths", "analysis", "problem solving"],
        "skills": ["excel", "python", "sql", "statistics", "power bi"],
        "description": "Use data to find patterns and help organisations make decisions.",
        "skills_to_learn": ["Advanced Excel", "SQL", "Python basics", "Statistics", "Power BI or Tableau"],
        "roadmap": ["Learn Excel", "Practice SQL queries", "Learn basic statistics", "Create dashboards", "Complete a data analysis project"]
    },
    "Web Developer": {
        "interests": ["design", "coding", "websites", "creativity"],
        "skills": ["html", "css", "javascript", "python", "php"],
        "description": "Create and maintain websites and web applications.",
        "skills_to_learn": ["HTML", "CSS", "JavaScript", "Responsive design", "Flask or another backend framework"],
        "roadmap": ["Learn HTML structure", "Style pages using CSS", "Add interactions with JavaScript", "Build a multi-page website", "Deploy your website"]
    },
    "UI/UX Designer": {
        "interests": ["design", "creativity", "art", "user experience"],
        "skills": ["figma", "design", "creativity", "communication"],
        "description": "Design simple, attractive, and user-friendly digital experiences.",
        "skills_to_learn": ["Design principles", "Figma", "Wireframing", "Prototyping", "User research"],
        "roadmap": ["Study common app and website designs", "Learn Figma basics", "Create wireframes", "Design a prototype", "Build a small portfolio"]
    },
    "Cybersecurity Analyst": {
        "interests": ["security", "networking", "technology", "problem solving"],
        "skills": ["networking", "linux", "python", "security"],
        "description": "Help protect computer systems, networks, and information from threats.",
        "skills_to_learn": ["Computer networks", "Linux basics", "Security fundamentals", "Python basics", "Ethical and legal security practices"],
        "roadmap": ["Learn networking basics", "Practice Linux commands", "Study security fundamentals", "Use legal practice labs", "Document your learning projects"]
    },
    "AI / Machine Learning Engineer": {
        "interests": ["ai", "machine learning", "maths", "data", "technology"],
        "skills": ["python", "maths", "statistics", "machine learning"],
        "description": "Develop systems that learn patterns from data and make predictions.",
        "skills_to_learn": ["Python", "Statistics", "NumPy and pandas", "Machine learning basics", "Model evaluation"],
        "roadmap": ["Strengthen Python", "Learn basic statistics", "Practice with pandas", "Train simple ML models", "Build and explain a small ML project"]
    },
    "IT Support Specialist": {
        "interests": ["helping people", "technology", "troubleshooting"],
        "skills": ["communication", "networking", "windows", "troubleshooting"],
        "description": "Help users solve computer, software, and network problems.",
        "skills_to_learn": ["Computer hardware basics", "Windows and Linux basics", "Networking", "Troubleshooting", "Communication"],
        "roadmap": ["Understand computer components", "Learn operating system basics", "Practice common troubleshooting", "Study networking basics", "Prepare support scenarios"]
    }
}

def recommend_careers(interests, skills):
    ranked = []
    for name, info in CAREERS.items():
        interest_hits = sum(1 for item in interests if item in info["interests"])
        skill_hits = sum(1 for item in skills if item in info["skills"])
        # Interests have slightly more weight; scores are guidance, not scientific predictions.
        raw = interest_hits * 2 + skill_hits
        ranked.append((raw, name, info))
    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    top = ranked[:3]
    max_score = max((item[0] for item in ranked), default=1)
    results = []
    for score, name, info in top:
        match = round((score / max(max_score, 1)) * 100)
        results.append({"name": name, "match": match, **info})
    return results

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    name = request.form.get("name", "").strip() or "Student"
    education = request.form.get("education", "").strip()
    interests = [x.strip().lower() for x in request.form.getlist("interests")]
    skills = [x.strip().lower() for x in request.form.getlist("skills")]
    if not interests and not skills:
        return render_template("index.html", error="Please select at least one interest or skill.", name=name, education=education)
    results = recommend_careers(interests, skills)
    return render_template("results.html", name=name, education=education, results=results)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
