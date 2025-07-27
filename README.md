# FastAPI Blog Project

A simple blog application built with FastAPI, SQLAlchemy, and Jinja2 templates. Users can register, view, and update their profiles, and create blog entries.

## Features

- User registration and management
- Blog post creation and display
- SQLite database integration
- Password hashing with bcrypt
- Responsive UI with custom CSS
- Templating with Jinja2

## Project Structure
```
fastapi-blog/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── static/
│   │   └── style.css
│   └── routers/
│       ├── users.py
│       └── posts.py
├── requirements.txt
└── README.md
```

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
