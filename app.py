from flask import Flask, render_template, request
import os


app = Flask(__name__, template_folder=os.getcwd())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    nota1 = float(request.form["nota1"])
    nota2 = float(request.form["nota2"])
    nota3 = float(request.form["nota3"])

    media = (nota1 + nota2 + nota3) / 3

    return render_template("index.html", media=media)

if __name__ == "__main__":
    app.run(debug=True)
