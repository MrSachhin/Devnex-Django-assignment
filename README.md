Steps to Run the Project

Prerequisites

    Install Python (>= 3.8).

    Install and configure PostgreSQL or use SQLite (default).

    Install Redis for Celery task queue.

    Install virtualenv:

    pip install virtualenv

    Setup Instructions

Clone the repository:

    git clone https://github.com/your-repo/library-management.git
    cd library-management

Create and activate a virtual environment:

    virtualenv venv
    source venv/bin/activate   # For Linux/Mac
    venv\Scripts\activate    # For Windows

Install project dependencies:

    pip install -r requirements.txt

Configure database settings in settings.py:
Update the DATABASES configuration if using PostgreSQL. Example:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

Run database migrations:

    python manage.py migrate

    Start the Django development server:

    python manage.py runserver

Set up and start Redis:
    Refer to the Redis documentation for installation instructions. After installation, start Redis:

    redis-server

Start Celery workers:
    Open a new terminal, activate the virtual environment, and run:

    celery -A library_management worker --loglevel=info

    Start Celery beat (optional, for periodic tasks):

    celery -A library_management beat --loglevel=info

Approach

    Design Overview

    Models:

    Author: Represents authors with fields for id, name, and bio.

    Book: Represents books with fields for id, title, author, isbn, and available_copies.

    BorrowRecord: Tracks borrowing with fields for id, book, borrowed_by, borrow_date, and return_date.

API Endpoints:

    CRUD operations for authors and books.

    Borrowing and returning books.

    Generating and retrieving reports.

Background Tasks:

    Celery is used for generating library activity reports asynchronously. The report is stored as a JSON file in the reports/ directory.

Key Features

    Clean separation of concerns using Django’s MVC architecture.

    DRF for efficient API development.

    Celery for handling time-intensive tasks like report generation.

    Redis as the task broker for Celery.

API Documentation

    Authors

    List Authors

    GET /authors/

Response:

    [
    {
        "id": 1,
        "name": "Author Name",
        "bio": "Biography"
    }
    ]

Create Author

POST /authors/

Request Body:

    {
    "name": "Author Name",
    "bio": "Biography"
    }

Books

List Books

    GET /books/

    Create Book

    POST /books/

    Borrow Records

    Borrow Book

    POST /borrow/

Request Body:

    {
    "book_id": 1,
    "borrowed_by": "User Name"
    }

Return Book

    PUT /borrow/<id>/return/

    Reports

    Generate Report

    POST /reports/

    Retrieve Latest Report

    GET /reports/
