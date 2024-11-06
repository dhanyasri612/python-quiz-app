import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load questions from JSON
with open('questions.json') as f:

    questions = json.load(f)

@app.route('/')
def home():
    questions_with_index = list(enumerate(questions))
    return render_template('quiz.html', questions=questions_with_index)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        selected_answer = request.form.get(f'question-{i}')
        if selected_answer == question['answer']:
            score += 1
    return render_template('quiz.html', questions=enumerate(questions), score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
