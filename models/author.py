from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        
        self._name = name

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
            conn.commit()
            self._id = cursor.lastrowid

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"AUTHOR: {self._name} || ID: {self._id} "
