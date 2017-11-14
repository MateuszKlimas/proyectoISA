from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/Prueba/')
def prueba():
    return render_template("prueba.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)