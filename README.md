
# Book List - A Flask Application

This is a simple Flask application that demonstrates rendering a list of books and individual book details.

## Features

* Displays a list of books with title, author, year, and description.
* Allows viewing details of a specific book by ID.
* Uses Flask for routing and templating.

### Running the application

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   ```

2. **Install dependencies**

   ```bash
   pip install Flask
   ```

3. **Run the application**

   ```bash
   python app.py
   ```

   This will start the development server and make the application accessible at `http://127.0.0.1:5000/`.

### Project Structure

The project consists of the following files:

* `app.py`: The main Flask application file containing routes and logic.
* `templates/book_list.html`: The template for displaying the list of books.
* `templates/book_detail.html`: The template for displaying details of a specific book.

### How it works

* The `app.py` script imports Flask and creates a Flask application instance.
* It defines a list of book dictionaries containing information about each book.
* The application defines two routes:
  * `/`: This route renders the `book_list.html` template, passing the book list and a title.
  * `/book/<int:book_id>/: This route retrieves a book by ID and renders the`book_detail.html` template if found, or returns a 404 error if not found.
* The templates use Jinja templating language to dynamically display the book information.

### Contributing

Feel free to fork the repository and submit pull requests with improvements or additional features.
