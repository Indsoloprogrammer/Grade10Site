from flask import Flask, redirect, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/question_papers')
def qp():
    return render_template('qp.html')

@app.route('/books')
def books():
    return render_template('books.html')

if __name__ == '__main__':
    app.run(debug=True)
