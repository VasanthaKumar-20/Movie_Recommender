# 🎬 Movie Recommendation App

A **Movie Recommendation App** built using **Django REST Framework (DRF)** for the backend and **HTML** for the frontend. This application allows users to discover personalized movie recommendations based on their preferences.

---

## 🌟 Features

- **User Management**: 
  - User registration, login, and logout.
  - Profile management for storing user preferences.

- **Movie Recommendations**:
  - Recommends movies based on user ratings, genres, or popularity.
  - Provides personalized movie suggestions.

- **Search and Browse**:
  - Search for movies by title, genre, or release year.
  - Explore popular and trending movies.

- **Interactive UI**:
  - Simple and intuitive frontend built with HTML.
  - Fully responsive design for seamless use on various devices.

---

## 🚀 Tech Stack

- **Backend**:
  - Django REST Framework (DRF)
  - SQLite for database 

- **Frontend**:
  - HTML, CSS 
  
---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

---

## 📚 API Endpoints

| Endpoint                  | Method | Description                              |
|---------------------------|--------|------------------------------------------|
| `/api/movies/`            | GET    | Retrieve a list of movies               |
| `/api/recommendations/`   | POST   | Get movie recommendations for a user    |
| `/api/users/`             | POST   | Register a new user                     |
| `/api/users/login/`       | POST   | Login a user and retrieve an auth token |

---
