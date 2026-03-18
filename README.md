# 🛡️ Autonomous Data Quality Management System

A Python + Flask based web application that automatically validates incoming data, quarantines invalid records, and maintains a detailed audit log — all within the database layer.

## Features
* Real-time database health monitoring
* Auto-validation of email format and phone number
* Invalid records automatically moved to quarantine
* Detailed audit trail with cleanup logs
* Separate user and admin interfaces
* Admin login protection

## Tech Stack
* Python
* Flask
* MySQL
* HTML / CSS / JavaScript

## Project Structure
```
DataQualityProject/
│
├── backend/
│   └── app.py              # Flask server & REST API
├── frontend/
│   ├── index.html          # User submission page
│   ├── admin.html          # Admin dashboard
│   ├── admin-login.html    # Admin login page
│   └── style.css           # Styling
└── README.md
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/sandhiya05-20/-DataQualityProject.git
cd -DataQualityProject
```

2. Install Python dependencies
```bash
pip install flask mysql-connector-python
```

3. Set up MySQL database
```bash
mysql -u root -p
```
```sql
CREATE DATABASE DataQualityDB;
USE DataQualityDB;
```
Then run all DDL and DML commands from Chapter 2 of the report.

4. Configure your MySQL password
Open `backend/app.py` and update line 8:
```python
password="your_mysql_password_here",
```

## Run the Project
```bash
cd backend
python app.py
```

## Open in Browser
* User Page → http://127.0.0.1:5000
* Admin Page → http://127.0.0.1:5000/admin-login

## Admin Login
* Contact the system administrator for login credentials.


## Requirements
* Python 3.10 / 3.11 recommended
* MySQL 8.0
* Any modern browser

## How It Works
1. User submits a record on the user page
2. Backend validates email format and phone number automatically
3. Valid records are saved to the database with status VALID
4. Invalid records are moved to quarantine automatically
5. Every action is logged in the cleanup log
6. Admin monitors all records and health metrics from the dashboard

## Possible Improvements
* Add duplicate email detection
* Add more validation rules
* Add email notification for quarantined records
* Add data export feature
* Add user authentication system
