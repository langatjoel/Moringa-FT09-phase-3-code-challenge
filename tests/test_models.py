import unittest
from models.author import Author
from models.magazine import Magazine
from models.article import Article

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Test Author creation with valid name
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

        # Test Author creation with empty name
        with self.assertRaises(ValueError):
            Author("")

    def test_magazine_creation(self):
        # Test Magazine creation with valid name and category
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

        # Test Magazine creation with invalid name (less than 2 characters)
        with self.assertRaises(ValueError):
            Magazine("T", "Technology")

        # Test Magazine creation with invalid category (empty string)
        with self.assertRaises(ValueError):
            Magazine("Tech Weekly", "")

    def test_article_creation(self):
        # Test Article creation with valid title
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author.name, "John Doe")
        self.assertEqual(article.magazine.name, "Tech Weekly")

        # Test Article creation with invalid title (less than 5 characters)
        with self.assertRaises(ValueError):
            Article(author, magazine, "Test")

    def test_author_id(self):
        # Test Author id retrieval
        author = Author("John Doe")
        self.assertIsInstance(author.id, int)

    def test_magazine_id(self):
        # Test Magazine id retrieval
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertIsInstance(magazine.id, int)

    def test_article_id(self):
        # Test Article id retrieval
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title")
        self.assertIsInstance(article.id, int)

    def test_author_name_immutable(self):
        # Test that Author name cannot be changed after instantiation
        author = Author("John Doe")
        with self.assertRaises(AttributeError):
            author.name = "Jane Doe"

    def test_magazine_name_immutable(self):
        # Test that Magazine name cannot be changed after instantiation
        magazine = Magazine("Tech Weekly", "Technology")
        with self.assertRaises(AttributeError):
            magazine.name = "New Magazine"

    def test_article_title_immutable(self):
        # Test that Article title cannot be changed after instantiation
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article(author, magazine, "Test Title")
        with self.assertRaises(AttributeError):
            article.title = "New Title"

if __name__ == '__main__':
    unittest.main()
