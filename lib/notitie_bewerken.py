import sqlite3

class Note():
    def __init__(self):
        self.conn = sqlite3.connect("databases/testgpt.db")
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
    
    def read_notes(self):
        results = self.cursor.execute("SELECT * FROM notes").fetchall()
        return results
    
    #date_created?
    def add_note(self, teacher_id, is_public, title, note, note_source, category_id):
        self.cursor.execute("INSERT into notes(teacher_id, is_public, title, note, note_source, category_id) VALUES(?,?,?,?,?,?)",(teacher_id, is_public, title, note, note_source, category_id))
        self.cursor.connection.commit()
