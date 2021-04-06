from app import app, db
from flask import render_template


@app.route('/disciplinas/associar')
def associar():
    return render_template("professor_disciplina.html")