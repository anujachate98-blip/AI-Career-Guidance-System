CAREERCOMPASS - AI-BASED CAREER GUIDANCE SYSTEM
Second Year B.E. Mini Project
Technology: Python, Flask, HTML, CSS

ABOUT
CareerCompass is a student career guidance website. A student selects interests
and existing skills. The Flask application compares these selections with
predefined career profiles and displays the top three career suggestions,
skills to learn, and a beginner roadmap.

NOTE
This starter mini-project uses a simple rule-based matching algorithm. It does
not call an external AI service or train a machine-learning model. In your
project report/demo, describe it accurately as a career recommendation system.
You can add a Gemini API integration later if your project guide requires a
real AI API.

HOW TO RUN (Windows)
1. Install Python 3.
2. Extract the ZIP file.
3. Open the extracted AI_Career_Guidance_System folder.
4. Click the folder address bar, type cmd, and press Enter.
5. Run:
      python -m venv venv
      venv\Scripts\activate
      pip install -r requirements.txt
      python app.py
6. Open this address in Chrome:
      http://127.0.0.1:5000

PROJECT MODULES
1. Home page and student details
2. Interest selection
3. Existing skill selection
4. Career matching and ranking
5. Career result cards
6. Skills-to-learn and learning roadmap

FOLDER STRUCTURE
AI_Career_Guidance_System/
  app.py
  requirements.txt
  README.txt
  templates/
    index.html
    results.html
  static/
    style.css

DEMO
Enter a name, choose education, select interests such as Coding and Technology,
select skills such as Python and HTML, then click Find my career matches.
Try different combinations to see different recommendations.
