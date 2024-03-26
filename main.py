from flask import Flask, render_template

app = Flask(__name__)

title = "Book List"
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "description": "A novel about the American Dream.",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "description": "A classic novel addressing racial injustice.",
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "description": "A dystopian novel about surveillance and totalitarianism.",
    },
    {
        "id": 4,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "description": "The story of Holden Caulfield, a cynical teenager who has been expelled from boarding school and reflects on his disillusionment with society.",
    },
    {
        "id": 5,
        "title": "The Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "year": 1885,
        "description": "Huckleberry Finn runs away from home and travels down the Mississippi River with Jim, a runaway slave, encountering satire and social commentary along the way.",
    },
]

# Route for the list of books
@app.route("/")
def book_list():
    return render_template("book_list.html", title=title, books=books)


@app.route("/book/<int:book_id>")
def book_detail(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return render_template("book_detail.html", book=book)
    else:
        return "Book not found", 404


if __name__ == "__main__":
    app.run(debug=True)
