from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_key_here"

# Sample quiz questions and answers
questions = [
    {"question": " find: 8+888+8+88+8 ","answer":"1000"},
    {"question": "2x+5=11","answer":"3"},
    {"question": "find the derivative f(x)=2x^2", "answer": "4x"},
    {"question": "Find the perimeter of a rectangle with length 6cm and width 4cm.","answer":"20cm"},
    {"question": "Mean of 2,4,6,8,10","answer":"6"}
]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0
        for question in questions:
            user_answer = request.form.get(question["question"])
            if user_answer == question["answer"]:
                score += 1
        session["score"] = score
        return redirect(url_for("results"))
    return render_template("quiz.html", questions=questions)


@app.route("/results")
def results():
    score = session.get("score", 0)
    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)

