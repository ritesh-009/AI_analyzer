from flask import Flask, render_template, request
import fitz
from utils.analyzer import analyze_resume

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        f=request.files["resume"]
        path="uploads/"+f.filename
        f.save(path)
        text=""
        doc=fitz.open(path)
        for p in doc:
            text+=p.get_text()
        result=analyze_resume(text)
        return render_template("result.html",result=result)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
