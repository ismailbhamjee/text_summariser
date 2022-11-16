from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    text=  request.form['text']
    text1=  request.form['text1']


    return 'You entered: {}'.format(request.form['text'])