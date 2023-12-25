import sqlite3

class Note():
    def __init__(self):
        self.conn = sqlite3.connect("databases/testgpt.db")
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
    
    def read_notes(self):
        results = self.cursor.execute("SELECT * FROM notes").fetchall()
        return results
    
    # def add_note(self, title, note_source, is_public, teacher_id, category_id, note):
    #     self.cursor.execute("INSERT into notes(title, note_source, is_public, teacher_id, category_id, note) VALUES (?,?,?,?,?,?)",(title,note_source, is_public, teacher_id, category_id, note))
    #     self.cursor.connection.commit()
