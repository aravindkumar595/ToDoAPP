📝 Django To-Do List Application

This is a simple and modern To-Do List web application developed using the Django framework. The application allows users to manage daily tasks by adding, editing, deleting, and marking tasks as completed through a clean and responsive user interface.

The project uses Django ORM to interact with an SQLite database and follows Django’s MVT (Model-View-Template) architecture. The frontend is built with HTML, CSS, and Bootstrap, ensuring a user-friendly and responsive design.

This project is ideal for beginners learning Django and demonstrates practical implementation of CRUD operations, URL routing, form handling, and template rendering.


✨ Features

Add new tasks

Edit existing tasks

Delete tasks

Mark tasks as completed or undone

Responsive and modern UI

SQLite database for persistent storage


🛠️ Technologies Used

Python

Django

SQLite

HTML

Project Structure
DjangoTodoApp/
├── todo/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── templates/
│   ├── home.html
│   ├── edit.html
│
├── db.sqlite3
├── manage.py

⚙️ Installation & Setup

1.Clone the repository

git clone https://github.com/your-username/your-repository-name.git


2.Navigate to the project directory

cd DjangoTodoApp


3.Create and activate virtual environment

python -m venv env
env\Scripts\activate


4.Install Django

pip install django


5.Apply migrations

python manage.py migrate


6.Run the development server

python manage.py runserver


Open in browser

http://127.0.0.1:8000/




CSS

Bootstrap
