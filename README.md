# BlogSpace - FastAPI Blog Application

![BlogSpace Screenshot](https://i.imgur.com/your-screenshot-url.png)

A modern blog platform where users can share their stories and connect with readers worldwide.

## 🛠️ Technologies Used

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=flat&logo=render&logoColor=white)

- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Frontend**: HTML5, CSS3, Jinja2 Templates  
- **Authentication**: JWT, Bcrypt
- **Deployment**: Render

## ✨ Features

- User registration and login
- Create and manage blog posts
- View all blogs with responsive design
- User profile management
- Secure authentication with JWT
- Mobile-friendly interface

## 🚀 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Access the app:**
   - Website: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
fastapi-blog/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── templates/
│   ├── static/
│   └── routers/
├── requirements.txt
└── README.md
```

## 🌐 Live Demo

[View Live Application](https://your-app.render.com)

## 📧 Contact

For questions or feedback, feel free to reach out!
