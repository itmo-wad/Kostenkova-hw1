from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('profile.html')

@app.route('/profile')
def profile():
    return redirect('/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)