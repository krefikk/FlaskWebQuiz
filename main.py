from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'kodland'

@app.before_request
def before_request():
    if 'best_score' not in session:
        session['best_score'] = 0

correct_answers = {
    "question1": "q1a2",        # NumPy
    "question2": "q2a1",        # A single forward and backward pass of all training examples
    "question3": "q3a1",        # Data Manipulation and Analysis
    "question4": "tokenization" # Tokenization
}

@app.route('/', methods=["POST", "GET"])
def index():
    score = 0
    overview = [0, 0, 0, 0]
    if request.method == "POST":
        answer_question_1 = request.form.get("question1")
        answer_question_2 = request.form.get("question2")
        answer_question_3 = request.form.get("question3")
        answer_question_4 = request.form.get("question4").lower()

        if answer_question_1 == correct_answers["question1"]:
            score += 25
            overview[0] = 1
        if answer_question_2 == correct_answers["question2"]:
            score += 25
            overview[1] = 1
        if answer_question_3 == correct_answers["question3"]:
            score += 25
            overview[2] = 1
        if answer_question_4 == correct_answers["question4"]:
            score += 25
            overview[3] = 1

        if score > session['best_score']:
            session['best_score'] = score

    return render_template('index.html', score=score, overview=overview, best_score=session['best_score'])

if __name__ == '__main__':
    app.run(debug=True)