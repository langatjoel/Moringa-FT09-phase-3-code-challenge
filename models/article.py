from database.connection import get_db_connection

class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)',
                (title, author.id, magazine.id)
            )
            conn.commit()
            self._id = cursor.lastrowid

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def __repr__(self):
        return f"ARTICLE: {self._title}"
