from flask import Flask, render_template, request, jsonify,redirect,url_for
import mysql.connector
from aimodel import *

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

@app.route('/')
def index():
    return render_template('userLogin.html')

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

        print(username)

        print(result)
        cursor.close()
        connection.close()
        if result:
            if request.args.get('redirect'):
                # If 'redirect' is provided, send a JSON response with redirect attribute
                return jsonify(
                    {'success': True, 'message': 'Login successful', 'redirect': request.args.get('redirect')})
            else:
                # If 'redirect' is not provided, perform a server-side redirect
                return redirect(url_for('user_dashboard'))
            # return jsonify({'success': True, 'message': 'Login successful', 'redirect': '/userDashboard.html'})
            # return redirect(url_for('user_dashboard'))
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password'})

    # If the method is not POST, return Method Not Allowed
    return jsonify({'success': False, 'message': 'Method Not Allowed'}), 405
@app.route('/signup')
def sign():
    return render_template('userSignUp.html')


@app.route('/signup1', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('password')
        # print(username)
        connection = get_db_connection()
        cursor = connection.cursor()

        # Check if the username already exists in the database
        check_query = 'SELECT * FROM user WHERE username = %s'
        cursor.execute(check_query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            connection.close()
            return jsonify({'success': False, 'message': 'Username already exists. Choose a different username.'})

        # If the username is not already taken, insert the new user into the database
        insert_query = 'INSERT INTO user (username, password,PERMISSION) VALUES (%s, %s,%s)'
        cursor.execute(insert_query, (username, password,0))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'success': True, 'message': 'User registered successfully'})

    # If the method is not POST, return Method Not Allowed
    return jsonify({'success': False, 'message': 'Method Not Allowed'}), 405
@app.route('/userDashboard')
def user_dashboard():
    return render_template('userDashboard.html')

def fetch_recommendations(combination, criteria, department):
    # Your database query logic here
    # Replace the following lines with your actual database query
    result = [
        {"college_name": "College 1", "ranking": 1},
        {"college_name": "College 2", "ranking": 2},
        # Add more data as needed
    ]
    return result

@app.route('/backend_endpoint', methods=['POST'])
def backend_endpoint():
    try:
        # Get data from the request
        data = request.get_json()

        # Extract parameters
        combination = data.get('combination')
        criteria = data.get('criteria')
        department = data.get('department')

        # Fetch recommendations from the database
        recommendations = fetch_recommendations(combination, criteria, department)

        # Return the recommendations as JSON
        return jsonify({'success': True, 'recommendations': recommendations})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'success': False, 'message': 'Error processing the request'})


@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/clgPredictor.html')
def college_predictor():
    return render_template('clgPredictor.html')
@app.route('/predictcolleges',methods=['POST'])
def predictcolleges():
    global cursor, connection
    try:
        # Access data from the POST request
        data = request.form
        print(data)
        rank = data.get('instituteCode')
        # print(institute_code)
        score = data.get('instituteName')
        institute_status = data.get('instituteStatus')
        total_intake = data.get('totalIntake')
        # Try inserting data into the 'colleges' table
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Request received")
        # Rest of the code...
        print("Data inserted successfully")
        a=aimodel()
        listodchoices=a.trainmodel([int(rank),int(score)])
        insert_query = """
            insert into choices(choicecodesss) values(%s)
            """
        insert_query1 = """
                    truncate choices
                    """
        cursor.execute(insert_query1)
        connection.commit()
        for i in listodchoices:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute(insert_query, [(i)])
            connection.commit()
            cursor.close()
            connection.close()
        insert_query2 = """
                            call collegedatabase.unite_all(%s);

                            """
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(insert_query, [str(listodchoices[0])])
        connection.commit()
        cursor.close()
        connection.close()
        # print(insert_query)
        viewquery=""" select * from final1"""
        cursor.execute(viewquery)
        # Commit the changes to the database
        result = cursor.fetchall()
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


# Route for About page
@app.route('/aboutUs.html')
def about_us():
    return render_template('aboutUs.html')

# Route for Contact page
@app.route('/contactUs.html')
def contact_us():
    return render_template('contactUs.html')

if __name__ == '__main__':
    app.run(debug=True)
