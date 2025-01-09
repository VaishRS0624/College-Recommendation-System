from flask import Flask, render_template, request, jsonify,redirect,url_for
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'password',
    'database': 'collegedatabase',
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


def execute_query(query, params=None):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # Skip any additional result sets
        while cursor.nextset():
            pass

        connection.commit()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error executing query:", e)
        connection.rollback()
        return None
    finally:
        cursor.close()
        connection.close()

@app.route('/')
def index():
    return render_template('adminLogin.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('password')

        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to check user credentials (replace with your actual query)
        query = 'SELECT * FROM user WHERE username = %s AND password = %s'
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        connection.close()
        print(username)

        print(result)
        if result:
            if request.args.get('redirect'):
                # If 'redirect' is provided, send a JSON response with redirect attribute
                return jsonify(
                    {'success': True, 'message': 'Login successful', 'redirect': request.args.get('redirect')})
            else:
                # If 'redirect' is not provided, perform a server-side redirect
                return redirect(url_for('admin_dashboard'))
            # return jsonify({'success': True, 'message': 'Login successful', 'redirect': '/userDashboard.html'})
            # return redirect(url_for('user_dashboard'))
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password'})

    # If the method is not POST, return Method Not Allowed
    return jsonify({'success': False, 'message': 'Method Not Allowed'}), 405

# Route for Admin Dashboard page
@app.route('/adminDashboard.html')
def admin_dashboard():

    return render_template('adminDashboard.html')

# Route for Colleges page under Admin Dashboard
@app.route('/colleges.html')
def admin_colleges():

    return render_template('colleges.html')

# Existing routes...

# Route to handle adding colleges (adjust the route as needed)
@app.route('/addColleges', methods=['POST'])
def add_colleges():
    global cursor, connection
    try:
        # Access data from the POST request
        data = request.form
        print(data)
        institute_code = data.get('instituteCode')
        # print(institute_code)
        institute_name = data.get('instituteName')
        institute_status = data.get('instituteStatus')
        total_intake = data.get('totalIntake')
        # Try inserting data into the 'colleges' table
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Request received")
        # Rest of the code...
        print("Data inserted successfully")
        insert_query = """
        INSERT INTO collegelist (Institute_Code, Institute_Name, Status, total_intake)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(insert_query, (institute_code, institute_name, institute_status, total_intake))
        print(insert_query)
        # Commit the changes to the database
        result=cursor.fetchall()
        print(result)
        connection.commit()

        # Assuming some success response
        response_data = {'success': True, 'message': 'College added successfully'}

    except Exception as e:
        print(f"Error: {e}")
        response_data = {'success': False, 'message': 'An error occurred'}

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

    return jsonify(response_data)
# Route for Courses page under Admin Dashboard
@app.route('/courses.html')
def admin_courses():
    return render_template('courses.html')

@app.route('/addCourses', methods=['POST'])
def add_courses():
    global cursor, connection
    try:
        # Access data from the POST request
        data = request.form
        print(data)
        choice_code = data.get('instituteCode')
        # print(institute_code)
        course_name = data.get('instituteName')
        Exam = data.get('instituteStatus')
        CutOff = data.get('totalIntake')
        # Try inserting data into the 'colleges' table
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Request received HERE")
        # Rest of the code...
        print("Data inserted successfully")
        insert_query = """
        INSERT INTO coursenames (choicecode,coursename)
        VALUES (%s, %s)
        """

        cursor.execute(insert_query, (choice_code,course_name))
        print(insert_query)
        # Commit the changes to the database
        result=cursor.fetchall()
        print(result)
        connection.commit()

        # Assuming some success response
        response_data = {'success': True, 'message': 'Course added successfully'}

    except Exception as e:
        print(f"Error: {e}")
        response_data = {'success': False, 'message': 'An error occurred'}

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()

    return jsonify(response_data)
# Route for Courses page under Admin Dashboard
@app.route('/aboutUs.html')
def admin_about_us():
    return render_template('aboutUs.html')

# Route for Contact Us page under Admin Dashboard
@app.route('/contactUs.html')
def admin_contact_us():
    return render_template('contactUs.html')

if __name__ == '__main__':
    app.run(debug=True)
