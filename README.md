# BlogSpace

A simple blog application built with FastAPI, SQLAlchemy, and Jinja2 templates. Users can register, view and update their profiles, and create blog entries.

---

## Live Demo

Check out the running app here: [BlogSpace Live](https://blog-fastapi-uop4.onrender.com/user/home)

---

## Homepage Preview

![BlogSpace Homepage](app/static/blogspace_homepage.png)

---

## Features

- User registration and management  
- Blog post creation and display  
- SQLite database integration  
- Password hashing with bcrypt  
- Responsive UI with custom CSS  
- Templating with Jinja2  

---

## Project Structure

fastapi-blog/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── register.html
│ │ └── profile.html
│ ├── static/
│ │ ├── style.css
│ │ └── blogspace_homepage.png
│ └── routers/
│ ├── users.py
│ └── posts.py
├── requirements.txt
└── README.md

text

---

## Setup

1. **Clone the repository:**
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog

text

2. **Install dependencies:**
pip install -r requirements.txt

text

3. **Run the app locally:**
uvicorn app.main:app --reload

text

4. **Access the app:**  
Open `http://localhost:8000` in your browser.

---

## Contributing

Pull requests, issue reports, and feature suggestions are welcome! Feel free to fork and extend the project.

---

## License

MIT License



