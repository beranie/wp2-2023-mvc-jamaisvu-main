import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route("/notitie/<notitie_id>")
def index(notitie_id):

    database = sqlite3.connect("databases/testgpt.db")
    cursor = database.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT n.*, c.omschrijving FROM notes n LEFT JOIN categories c on n.category_id = c.category_id WHERE note_id = " + notitie_id)
    note = cursor.fetchone()

    return render_template("lezen.html", page_title="Notitie lezen" + notitie_id, note=note)


if __name__ == "__main__":
    app.run(debug=True)