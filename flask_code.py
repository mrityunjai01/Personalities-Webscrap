from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_answers', methods = ["POST"])
def get_ans():
    personality_input = request.form.get("personality_input")
    print("hey"+personality_input)
    return render_template('index.html')
