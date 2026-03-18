# 🛡️ Autonomous Data Quality Management System

A mini project for **21CSC205P Database Management Systems**  
**SRM Institute of Science and Technology**

## 👥 Team Members
- Archana V [RA2411030010324]
- Sandhiya S [RA2411030010339]

## 📌 Project Overview
An Autonomous Data Quality Management System that automatically validates incoming data, quarantines invalid records, and maintains a detailed audit log — all within the database layer.

## 🛠️ Tech Stack
- **Database:** MySQL 8.0
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript

## 📁 Project Structure
DataQualityProject/
├── backend/
│   └── app.py
├── frontend/
│   ├── index.html
│   ├── admin.html
│   ├── admin-login.html
│   └── style.css

## 🚀 How to Run
1. Install dependencies:
pip install flask mysql-connector-python
2. Set up MySQL database and run the DDL commands
3. Update password in app.py
4. Run the Flask server:
cd backend
python app.py
5. Open browser at http://127.0.0.1:5000

## 🔐 Admin Access
- URL: http://127.0.0.1:5000/admin-login
- Username: admin
- Password: admin123

## ✨ Features
- ✅ Auto-validation of email and phone number
- ✅ Quarantine system for invalid records
- ✅ Real-time health metrics dashboard
- ✅ Audit trail with cleanup logs
- ✅ Separate user and admin interfaces
