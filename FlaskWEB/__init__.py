from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def interfazMenu():
    return render_template("interfazMenu.html")

@app.route('/interfazAreaPersonal/')
def interfazAreaPersonal():
    return render_template("interfazAreaPersonal.html")

@app.route('/interfazProfesores/')
def interfazProfesores():
    return render_template("interfazProfesores.html")

@app.route('/interfazUniversidad/')
def interfazUniversidad():
    return render_template("interfazUniversidad.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)