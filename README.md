# College-Recommendation-System
## Project Overview
The College Recommendation System is a web-based application built with Flask as the backend framework and MySQL for database management. It offers features tailored for both administrators and users, enabling administrators to manage colleges and courses while allowing users to search for colleges and predict potential options based on their ranks and scores.

## Features
### For Administrators
- Login System: Secure login for administrators to access the admin dashboard.
- College Management: Add and manage college details, including institute codes, names, statuses, and total intake.
- Course Management: Add and manage courses offered by colleges.
### For Users
- User Registration and Login: Users can register and log in to access their personalized dashboard.
- College Search: Search for colleges using various criteria.
- College Predictor: Predict potential colleges based on user-provided ranks and scores.

## Project Structure
### flaskapp.py: Main Flask application for user interactions.
### flaskadmin.py: Flask application for administrative tasks.
### templates/: Contains HTML templates for the user interface.
### static/: Stores static assets like CSS and JavaScript files.
### database.sql: SQL script to create the database schema.

## Database Configuration
1. Ensure MySQL is installed and running.
2. Update the database configuration in flaskapp.py and flaskadmin.py with your MySQL credentials.

## Running the Application
### Clone the Repository
```bash
git clone https://github.com/your_username/college-recommendation-system.git
```
### Navigate to the Project Directory
```bash
cd college-recommendation-system
```
### Install Required Dependencies
```bash
pip install -r requirements.txt
```
### Run the Application
- For normal users:
```bash
python flaskapp.py
```
- For administrators:
```bash
python flaskadmin.py
```
### Access the Application
- For normal users: http://localhost:5000
- For administrators: http://localhost:5000/adminDashboard.html

