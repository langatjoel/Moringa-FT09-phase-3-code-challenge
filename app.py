from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Count the initial number of records in each table
    cursor.execute('SELECT COUNT(*) FROM magazines')
    initial_magazine_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM authors')
    initial_author_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM articles')
    initial_article_count = cursor.fetchone()[0]

    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implementation.
    '''

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid  # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for newly inserted records
    cursor.execute('SELECT * FROM magazines WHERE id > ?', (initial_magazine_count,))
    new_magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors WHERE id > ?', (initial_author_count,))
    new_authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles WHERE id > ?', (initial_article_count,))
    new_articles = cursor.fetchall()

    conn.close()

    # Display only the newly inputted records
    print("\nMagazines:")
    for magazine in new_magazines:
        print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    for author in new_authors:
        print(Author(author["id"], author["name"]))

    print("\nArticles:")
    for article in new_articles:
        print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))


if __name__ == "__main__":
    main()
