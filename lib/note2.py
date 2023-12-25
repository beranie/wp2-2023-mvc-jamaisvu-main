from flask import request
import sqlite3

class Note_simone():
    def __init__(self):
        self.conn = sqlite3.connect("databases/testgpt.db")
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
    
    def add_note(self):
        titel = request.form.get("titel")
        bron = request.form.get("bron")
        categorie = request.form.get("categorie")
        publiek = request.form.get("publiek")
        tekst = request.form.get("tekst")
        publiek = request.form.get("publiek")
        # moet nog weg
        teacher_id = 100
        categorie = str(categorie)
        if publiek == "on":
            publiek = 1
        else:
            publiek = 0

        # int maken van categorie
        if categorie == "category2":
            categorie = 2
        if categorie == "category3":
            categorie = 3
        if categorie == "category4":
            categorie = 4
        query = """
            INSERT INTO notes (title, note_source, is_public, teacher_id, category_id, note)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (titel, bron, publiek, teacher_id, categorie, tekst)

        self.cursor.execute(query, values)

        # Commit the transaction to save changes to the database
        self.conn.commit()

    
    def add_category(self, omschrijving):
        omschrijving = request.form.get("categorie")
        query = """
            INSERT INTO notes (omschrijving)
            VALUES (?)
        """
        values = (omschrijving, )

        self.cursor.execute(query, values)

        # Commit the transaction to save changes to the database
        self.conn.commit()
        


