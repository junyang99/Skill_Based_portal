from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import re
import mysql.connector
from flask_cors import CORS

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'hr portal'
}

# Create a connection to the database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn.close()

# Execute a SELECT statement to retrieve data from the 'email' column
cursor.execute("SELECT Staff_ID FROM staff")

# Fetch all rows of data from the executed query
staff_ids = cursor.fetchall()
# print(staff_ids)

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'  # Change this to a secret key for session management

def validate_name(name):
    if not re.match(r'^[A-Za-z\'\s-]+$', name):
        return False
    return True

def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return False
    return True



@app.route('/Role-Application', methods=['GET'])
def roleApplication():
    sample_data = [
        {
            'id': 1,
            'title': 'Account Manager',
            'department': 'Sales',
            'staffID': '000123',
            'staffName': 'Account Manager',
            'staffEmail': 'alice@gmail.com',
            'staffCountry': 'Singapore',
            'staffDepartment': 'Marketing',
            'staffRole': 'Content Strategist',
            'staffSkills': ['Audit Frameworks', 'Budgeting', 'Business Acumen']
        }
    ]
    return jsonify(sample_data)

@app.route('/api/send-cover-letter', methods=['POST', 'GET'])
def receive_cover_letter():
    # return ("received")
    data = request.get_json()
    cover_letter = data.get('coverLetter')
    # Process the received cover letter as needed
    cursor.execute('''
            INSERT INTO application
            (Application_ID, Position_ID, Staff_ID, Application_Date, Cover_Letter, Application_Status)
            VALUES (1, 1, %s, NOW(), %s, 1)
        ''', ("1", cover_letter))
    conn.commit()

    return jsonify({'message': 'Cover Letter received and processed successfully'})

# @app.route('/')
# def index():
#     # Prepopulate sample data
#     sample_data = {
#         'staff_id': '210044',
#         'staff_fname': 'Chandara',
#         'staff_lname': 'Tith',
#         'department': 'IT',
#         'email': 'Phuc.Luong@allinone.com.sg',
#     }
    
#     return render_template('index.html', sample_data=sample_data)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    staff_id = request.form.get('staff_id')
    staff_fname = request.form.get('staff_fname')
    staff_lname = request.form.get('staff_lname')
    department = request.form.get('department')
    email = request.form.get('email')
    cover_letter = request.form.get('cover_letter')
    
    if not all([staff_id, staff_fname, staff_lname, department, email, cover_letter]):
        flash("Please fill in all required fields.")
        return redirect(url_for('index'))
    
    if not validate_name(staff_fname):
        flash("Invalid First Name. Please enter a valid name.")
        return redirect(url_for('index'))
    
    if not validate_name(staff_lname):
        flash("Invalid Last Name. Please enter a valid name.")
        return redirect(url_for('index'))
    
    if not validate_email(email):
        flash("Invalid email address. Please enter a valid email.")
        return redirect(url_for('index'))
    
    # Insert data into the application table, including the cover letter field
    try:
        cursor.execute('''
            INSERT INTO application
            (Application_ID, Position_ID, Staff_ID, Application_Date, Cover_Letter, Application_Status)
            VALUES (1, 1, %s, NOW(), %s, 1)
        ''', (staff_id, cover_letter))
        conn.commit()

        flash("Thank you! Your application has been submitted.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash(f"Error: {err}")
        flash("An error occurred while submitting your application.")

    return redirect(url_for('view_staff', staff_id=staff_id))

@app.route('/view_staff/<staff_id>')
def view_staff(staff_id):
    # Create a new connection and cursor for this route
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash(f"Error: {err}")
        flash("An error occurred while connecting to the database.")
        return redirect(url_for('index'))
    
    # Retrieve staff information from the database based on staff_id
    try:
        cursor.execute('''
            SELECT s.Staff_ID, s.Staff_FName, s.Staff_LName, s.Dept, s.Email, a.Cover_Letter
            FROM staff s
            LEFT JOIN `hr portal`.application a ON s.Staff_ID = a.Staff_ID
            WHERE s.Staff_ID = %s
        ''', (staff_id,))
        staff_info = cursor.fetchone()

        if staff_info:
            return render_template('view_staff.html', staff_id=staff_info[0], staff_fname=staff_info[1], staff_lname=staff_info[2], department=staff_info[3], email=staff_info[4], cover_letter=staff_info[5])
        else:
            flash("Staff not found")
            return redirect(url_for('index'))
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        flash(f"Error: {err}")
        flash("An error occurred while fetching staff information.")
        return redirect(url_for('index'))
    finally:
        # Close the cursor and the connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)


