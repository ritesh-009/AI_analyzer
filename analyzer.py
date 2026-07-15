SKILLS=["python","java","html","css","javascript","sql","flask","django","react","git","docker","aws"]
def analyze_resume(text):
    t=text.lower()
    found=[s.title() for s in SKILLS if s in t]
    score=min(100,40+len(found)*5)
    missing=[s.title() for s in SKILLS if s.title() not in found][:5]
    return {
      "score":score,
      "skills":found,
      "missing":missing,
      "suggestions":[
        "Add measurable achievements.",
        "Include certifications.",
        "Improve professional summary."
      ]
    }
