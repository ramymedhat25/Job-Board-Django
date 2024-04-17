# Job-Board-Django

This is a simple job board application built with Django. It allows users to post job listings and view existing listings.

## Features

- Users can create an account and log in
- Users can post job listings, including a job title, description, and contact information
- Users can view a list of all job listings
- Users can search for job listings by keyword or location

## Tech Stack

- Python 3.8
- Django 3.2
- PostgreSQL

## Setup

To set up the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/Job-Board-Django.git`
2. Create a virtual environment: `python3 -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (on Linux/macOS) or `venv\Scripts\activate` (on Windows)
4. Install the requirements: `pip install -r requirements.txt`
5. Create a `.env` file in the project root directory and add the following variables:
   - `SECRET_KEY`: your Django secret key
   - `DATABASE_URL`: your PostgreSQL database URL
6. Apply the migrations: `python manage.py migrate`
7. Run the development server: `python manage.py runserver`

## Contributing

We welcome contributions to this project! To contribute, follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b my-branch-name`
3. Make your changes and commit them: `git commit -m 'Add my feature'`
4. Push your changes to your forked repository: `git push origin my-branch-name`
5. Create a pull request

## License

This project is licensed under the MIT License.
