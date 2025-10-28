# Shekaf Store
A simple e-commerce website for selling posters, built with Flask, SQLite, SQLAlchemy, and HTML/CSS. This project is a work-in-progress and currently does not have a fully functional payment system.

---

## Features

- User authentication:
  - Sign up
  - Log in / Log out
- Browse available posters on the homepage
- View detailed poster pages
- Flash messages for notifications
- SQLite database stores posters and user accounts

---

## Tech Stack

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Werkzeug
- **Frontend:** HTML, CSS, Jinja2 templates
- **Database:** SQLite

---

## Installation

1. Clone this repository:
``` bash
git clone https://github.com/yourusername/poster-store.git
cd poster-store
```
2. Create and activate a virtual environment (optional but recommended):
``` bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3. Install dependencies:
``` bash
pip install -r requirements.txt
```
4.Run the app:
``` bash
python main.py
```
Open your browser at `http://127.0.0.1:5000/`

---

## Project Structure
``` graphql
poster-store/
│
├─ main.py              # Flask application
├─ forms.py             # WTForms for login and registration
├─ templates/           # HTML templates
│   ├─ index.html
│   ├─ header.html
│   ├─ login.html
│   ├─ signup.html
│   ├─ poster_page.html
│   └─ payment.html
├─ static/              # CSS and image files
├─ store.db             # SQLite database (created automatically)
└─ README.md
```

---

## Usage

- Browse posters on the homepage.
- Sign up or log in to access account-specific features.
- The “Add” button and payment page are placeholders and not fully functional yet.

## Future Improvements

- Implement full payment functionality.
- Add cart management (add/remove items, quantity control).
- Improve UI/UX design.
- Add search and filter options for posters.
- Deploy the website online.
