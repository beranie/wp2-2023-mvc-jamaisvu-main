import sqlite3
from notitie_bewerken import Note
from flask import Flask, render_template,request,jsonify, redirect

app = Flask(__name__)




@app.route("/notitie_bewerken")
def notitie_bewerken():
    note_file = notitie_bewerken()
    all_notes = note_file.read_notes()
    return render_template("notitie_bewerken.html",all_notes=all_notes)

@app.route("/notitie_opslaan")
def add_test():
    if request.method == "POST":
        note_file = Note()
        checkbox_value = request.form.get("checkbox")
        is_public = 0

        if checkbox_value == "checked":
            is_public = 1

        note_file.add_note(request.form.get("teacher_id"), is_public, request.form.get("title"), request.form.get("note"), request.form.get("not_source"), request.form.get("category_id"))
        return redirect("/index")
    else:
        return render_template("notitie_bewerken.html")
    


if __name__ == '__main__':
    app.run(debug=True)

