# Hospital Management System

A role-based Hospital Management System built using Flask that streamlines hospital operations by providing separate dashboards and functionalities for Admin, Doctor, and Patient users.

The system supports authentication, role-based access control, doctor discovery, appointment workflows, and a clean modern UI built with Tailwind CSS.

# Features

## Authentication & Authorization

* Secure user registration and login

* Role-based access (Admin / Doctor / Patient)

* Session management using Flask-Login

## Doctor

* Doctor dashboard

* View assigned patients

* Manage profile and availability

##* Patient

* Patient dashboard

* View and search doctors

* Book appointments

* View appointment history

## Admin

* Admin dashboard

* Manage doctors and patients

* Oversee system-level operations

## UI & UX

* Responsive UI using Tailwind CSS

* Clean navigation bar with dropdown menus

* Flash messages for feedback

* Background watermark branding

# Tech Stack

## Backend

* Python 3

* Flask

* Flask-SQLAlchemy

* Flask-Login

* Flask-WTF

* WTForms

* Email Validator

* python-dotenv

## Frontend

* HTML5

* Tailwind CSS

* Jinja2 Templates

* Database

* SQLite 

## Tools

* Virtual Environment (venv)

* Git & GitHub

* VS Code

## Project Structure

```

Project-main/
│
├── app.py                  # Main Flask application
├── setup_database.py       # Database initialization script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── instance/
│   └── hospital.db         # SQLite database (auto-created)
│
├── static/
│   ├── logo.png            # Application logo
│   └── css/                # Static styles (if any)
│
├── templates/
│   ├── base.html           # Base layout
│   ├── login.html
│   ├── register.html
│   ├── dashboards/
│   │   ├── admin.html
│   │   ├── doctor.html
│   │   └── patient.html
│   └── other_pages.html
│
└── venv/                   # Virtual environment (local)

```

## Setup & Installation

A. Clone the Repository
   
```
 git clone <repository-url>

```

```
cd Project-main

```

B. Create Virtual Environment

```
python -m venv venv

```

C. Activate Virtual Environment

1. Windows (PowerShell):
   
```
.\venv\Scripts\activate

```

Mac / Linux:

```
source venv/bin/activate

```

D. Install Dependencies
```
pip install -r requirements.txt

```

E. Setup Database

```
python setup_database.py

```

This will create the SQLite database and required tables.

F. Run the Application

```
python app.py

```

Open your browser and visit:

```
http://127.0.0.1:5000

```

G. Running After Restarting VS Code

Every time you restart VS Code:

```
cd "C:\Users\DELL\Desktop\Project-main new\Project-main"
.\venv\Scripts\activate
python app.py
```

H. Environment Variables

Create a .env file in the project root:

```
SECRET_KEY=your_secret_key

```
(Optional: add database URI for production)

# Default Roles

* Admin – Full access

* Doctor – Medical access

* Patient – Appointment & search access

Roles are assigned during registration or by admin.

# Future Enhancements

* Appointment reminders

* Medical record uploads

* REST API integration

* Deployment on cloud (Render / AWS / Railway)

* PostgreSQL support

* Email notifications

# Contributors

| Name                  | Role                           | Responsibilities                                                             |
| --------------------- | ------------------------------ | ---------------------------------------------------------------------------- |
| **Shivansh Jhallani** | Backend Developer              | Flask Routing, Database Management, API Integration, Logic & CRUD Operations |
| **Shriya Gupta**      | Frontend Developer             | Frontend Design, Admin Dashboard, Table UI, Styling, User Experience         |


# License

This project is for educational and learning purposes.
Feel free to fork, modify, and improve it.
