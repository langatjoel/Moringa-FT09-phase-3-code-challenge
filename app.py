from database.setup import create_tables
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

    # Validate and collect article title input
    while True:
        article_title = input("Enter article title (5-50 characters): ")
        if 5 <= len(article_title) <= 50:
            break
        else:
            print("Invalid title. Please enter a title between 5 and 50 characters.")

    # Create an author
    author = Author(author_name)

    # Create a magazine
    magazine = Magazine(magazine_name, magazine_category)

    # Create an article
    article = Article(author, magazine, article_title)

    # Display only the newly inputted records
    print("\nMagazines:")
    print(magazine)

    print("\nAuthors:")
    print(author)

    print("\nArticles:")
    print(article)

if __name__ == "__main__":
    main()
