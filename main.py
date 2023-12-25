
# from flask import Flask, render_template, request, redirect
# from lib.note import *
# from lib.note2 import Note_simone

import sqlite3
from lib.notitie_bewerken import Note
from lib.note2 import Note_simone
from flask import Flask, render_template,request,jsonify, redirect

app = Flask(__name__)


@app.route('/')
def inloggen():
    return render_template("inlogscherm.html")

@app.route('/wrong_password')
def inlog_scherm_2():
    # image_path = '/static/images/example.jpg'
    return render_template('inlogscherm_2.html')

@app.route('/account_aanmaken')
def account_aanmaken():
    return render_template('account_aanmaken.html')

@app.route('/check_user', methods=['POST', 'GET'])
def check_user():
    # In check user, it needs to check user if he is allowed to get in. else re-input password
    username = request.form.get("username")
    wachtwoord = request.form.get("wachtwoord")
    print(f'username, {username} // password, {wachtwoord}')
    print()
    # if wachtwoord == "amdin_ww" and username == "amin_us":. voor nu heb ik alla
    if wachtwoord == "alla" and username == "alla":
        return redirect("/account_aanmaken")
    if username == wachtwoord:
        return redirect("/wrong_password")
    # HIER MOET gechecked gaan worden of de username + wachtwoord combinatie bestaat in de database.
    # hier na verdwijnt de wachtwoord en username. Maar dat is (zowiezo alla in dit geval) (tenzij het geen admin is
    # dan vervalt de username en wachtwoord niet))
    return redirect("/index")

@app.route('/index', methods=['POST', 'GET'])
def index():
    conn = sqlite3.connect('databases/testgpt.db')
    cur = conn.cursor()
    # conn.close()

    #excute a query
    # cur.execute("SELECT categorie, titel, met_vraag, bron, publiek_beschikbaar, naam_docent, aanmaakdatum, Tekst FROM notes")
    data = cur.fetchall()
    print(data)
    #conn.close()

    print("accessed index route")
    return render_template("index.html", data=data)

@app.route('/get-data')
def get_data():
    conn = sqlite3.connect('databases/testgpt.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes")
    rows = cursor.fetchall()
    conn.close()
    # Convert the data to a JSON-friendly format
    data = [{ "column2": row[1], "column3": row[2], "column4": row[3], "column5": row[4], "column6": row[5], "column7": row[6], "column8": row[7]} for row in rows]
    print(data)
    return jsonify(data)

@app.route('/notitie_aanmaken', methods=["GET", "POST"])
def notitie_aanmaken():
    if request.method == "POST":
        note = Note_simone()
        note.add_note()
        # note.add_category()
    return render_template("notitie_aanmaken.html")

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


"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# websites used for information =
# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_method
# https://stackoverflow.com/questions/32022568/get-value-of-a-form-input-by-id-python-flask

@app.route('/index', methods=['POST', 'GET'])
def hello():
    new_username = request.form.get("new_username")
    new_wachtwoord = request.form.get("new_wachtwoord")
    naam_docent = request.form.get("naam_docent")
    # Aanmaakdatum word gelezen als eerst jaar, dan maand en tot slot dag. Dit kan je echter niet aangeven bij html
    aanmaakdatum = request.form.get("aanmaakdatum")
    print(f'new username, {new_username} // new wachtwoord, {new_wachtwoord} // '
          f'naam docent, {naam_docent}// aanmaakdatum, {aanmaakdatum}')
    return render_template("index.html")


@app.route('/notitie-aanmaken')
def notitie_aanmaken():
    return render_template("notitie-aanmaken.html")

@app.route('/')
def inlog_scherm():
    # image_path = '/static/images/example.jpg'
    return render_template('inlogscherm.html')

@app.route('/wrong_password')
def inlog_scherm_2():
    # image_path = '/static/images/example.jpg'
    return render_template('inlogscherm_2.html')

@app.route('/account_aanmaken')
def account_aanmaken():
    return render_template('account_aanmaken.html')


@app.route('/check_user', methods=['POST', 'GET'])
def check_user():
    # In check user, it needs to check user if he is allowed to get in. else re-input password
    username = request.form.get("username")
    wachtwoord = request.form.get("wachtwoord")
    print(f'username, {username} // password, {wachtwoord}')
    print()
    if wachtwoord == "alla" and username == "alla":
        return redirect("/account_aanmaken")
    if username != wachtwoord:
        return redirect("/wrong_password")
    # HIER MOET gechecked gaan worden of de username + wachtwoord combinatie bestaat in de database.
    # hier na verdwijnt de wachtwoord en username. Maar dat is (zowiezo alla in dit geval) (tenzij het geen admin is
    # dan vervalt de username en wachtwoord niet))
    return redirect("/index")


if __name__ == '__main__':
    app.run(debug=True)



"""

if __name__ == '__main__':
    app.run(debug=True)

