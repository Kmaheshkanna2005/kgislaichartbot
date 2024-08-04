from flask import Flask, render_template, request, jsonify
from chatbot_model import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
