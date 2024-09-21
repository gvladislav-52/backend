from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../frontend'))

data_file_path = os.path.join(os.path.dirname(__file__), '../frontend/data.txt')

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    # Append the text to the file
    with open(data_file_path, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    return redirect(url_for('index'))

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    # Read from the file and return the contents
    if os.path.exists(data_file_path):
        with open(data_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = ""
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)
