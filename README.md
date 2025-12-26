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

CSS

Bootstrap

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

SNAPSHOTS:

<img width="1859" height="451" alt="Screenshot 2025-12-26 161407" src="https://github.com/user-attachments/assets/074d80f3-3370-489c-a00b-9c45da120917" />

<img width="1184" height="649" alt="Screenshot 2025-12-26 161433" src="https://github.com/user-attachments/assets/e3a065f2-69b4-42c9-8cea-05939d76b7f1" />

<img width="828" height="459" alt="Screenshot 2025-12-26 161452" src="https://github.com/user-attachments/assets/b6a26e04-c93b-4909-8ed2-a9a7a41f4e44" />
