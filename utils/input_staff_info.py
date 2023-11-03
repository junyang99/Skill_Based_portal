from flask import Flask, render_template, request, redirect, url_for, flash
import re
import mysql.connector

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from view_access_control import Access_Control
from datetime import datetime

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/HR Portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Access_Control(db.Model):
    __tablename__ = 'Access_Control'

    Access_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Access_Control_Name = db.Column(db.String(20), nullable=False)
    

    def __init__(self, Access_ID , Access_Control_Name):
        self.Access_ID= Access_ID
        self.Access_Control_Name = Access_Control_Name


    def json(self):
        return {
            'Access_ID': self.Access_ID,
            'Access_Control_Name': self.Access_Control_Name
        }
class Application(db.Model):
    __tablename__ = 'Application'

    Application_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Position_ID = db.Column(db.Integer, db.ForeignKey(
        'Open_Position.Position_ID'), nullable=False)
    Staff_ID = db.Column(db.Integer, db.ForeignKey(
        'Staff.Staff_ID'), nullable=False)
    Application_Date = db.Column(db.Date, nullable=False)
    Cover_Letter = db.Column(db.String(10000), nullable=False)
    Application_Status = db.Column(db.Integer, nullable=False)

    def __init__(self, Application_ID, Position_ID, Staff_ID, Application_Date, Cover_Letter, Application_Status):
        self.Application_ID = Application_ID
        self.Position_ID = Position_ID
        self.Staff_ID = Staff_ID
        self.Application_Date = Application_Date
        self.Cover_Letter = Cover_Letter
        self.Application_Status = Application_Status

    def json(self):
        return {
            'Application_ID': self.Application_ID,
            'Position_ID': self.Position_ID,
            'Staff_ID': self.Staff_ID,
            'Application_Date': self.Application_Date,
            'Cover_Letter': self.Cover_Letter,
            'Application_Status': self.Application_Status,
        }

class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Access_ID = db.Column(db.Integer, db.ForeignKey('Access_Control.Access_ID'), nullable=False)  # Foreign key reference
    access_control = db.relationship(Access_Control, backref='staff', lazy=True)

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Country, Email, Access_ID):
        self.Staff_ID = Staff_ID
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Country = Country
        self.Email = Email
        self.Access_ID = Access_ID

    def json(self):
        return {
            'Staff_ID': self.Staff_ID,
            'Staff_FName': self.Staff_FName,
            'Staff_LName': self.Staff_LName,
            'Dept': self.Dept,
            'Country': self.Country,
            'Email': self.Email,
            'Access_ID': self.Access_ID
        }
    
# get staff by staff id
@app.route('/Staff/<int:Staff_ID>', methods = ['POST', 'GET'])
def find_by_staff_id(Staff_ID):
    staff = Staff.query.filter_by(Staff_ID=Staff_ID).first()
    if staff:
        return jsonify({
            'code': 200,
            'data': staff.json()
        })
    return jsonify({
        'code': 404,
        'message': 'Staff not found.'
    }), 404


# get all staff
@app.route('/Staff', methods = ['POST', 'GET'])
def get_all():
    staff_list = Staff.query.all()
    if staff_list:
        return jsonify({
            'code': 200,
            'data': {
                'Staff': [staff.json() for staff in staff_list]
            }
        })
    return {
        'code': 400,
        'message': 'There are no available staff members'
    }

@app.route('/submit-application', methods=['POST', 'GET'])
def submit_application():
    if request.method == 'POST':
        try:
            # Get data from the request
            data = request.get_json()
            position_id = data.get('Position_Id')  # Replace with the actual field name for position ID
            staff_id = data.get('Staff_Id')  # Replace with the actual field name for staff ID
            cover_letter = data.get('Cover_Letter')  # Replace with the actual field name for cover letter
            application_status = 1  # Set the application status as needed

            # Create a new application object
            new_application = Application(Application_ID=1, Position_ID=1, Staff_ID=1, Application_Date= "2023-11-02",Cover_Letter="abc", Application_Status=1)

            # Add the new application to the database
            db.session.add(new_application)
            db.session.commit()

            return jsonify({'message': 'Application submitted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    

@app.route('/Staff/<int:Staff_ID>/applications', methods=['GET'])
def get_staff_applications(Staff_ID):
    # Retrieve applications for the specified Staff_ID
    applications = Application.query.filter_by(Staff_ID=Staff_ID).all()

    if applications:
        # Convert the application objects to JSON format
        applications_json = [app.json() for app in applications]

        return jsonify({
            'code': 200,
            'data': applications_json
        })
    else:
        return jsonify({
            'code': 404,
            'message': 'No applications found for the specified Staff ID.'
        }), 404


# @app.route('/submit', methods=['POST'])
# def submit():
#     staff_id = request.form.get('staff_id')
#     staff_fname = request.form.get('staff_fname')
#     staff_lname = request.form.get('staff_lname')
#     department = request.form.get('department')
#     email = request.form.get('email')
#     cover_letter = request.form.get('cover_letter')
    
    
#     # Insert data into the application table, including the cover letter field
#     try:
#         cursor.execute('''
#             INSERT INTO application
#             (Application_ID, Position_ID, Staff_ID, Application_Date, Cover_Letter, Application_Status)
#             VALUES (1, 1, %s, NOW(), %s, 1)
#         ''', (staff_id, cover_letter))
#         conn.commit()

#         flash("Thank you! Your application has been submitted.")
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         flash(f"Error: {err}")
#         flash("An error occurred while submitting your application.")

#     return redirect(url_for('view_staff', staff_id=staff_id))

# @app.route('/view_staff/<staff_id>')
# def view_staff(staff_id):
#     # Create a new connection and cursor for this route
#     try:
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         flash(f"Error: {err}")
#         flash("An error occurred while connecting to the database.")
#         return redirect(url_for('index'))
    
#     # Retrieve staff information from the database based on staff_id
#     try:
#         cursor.execute('''
#             SELECT s.Staff_ID, s.Staff_FName, s.Staff_LName, s.Dept, s.Email, a.Cover_Letter
#             FROM staff s
#             LEFT JOIN `hr portal`.application a ON s.Staff_ID = a.Staff_ID
#             WHERE s.Staff_ID = %s
#         ''', (staff_id,))
#         staff_info = cursor.fetchone()

#         if staff_info:
#             return render_template('view_staff.html', staff_id=staff_info[0], staff_fname=staff_info[1], staff_lname=staff_info[2], department=staff_info[3], email=staff_info[4], cover_letter=staff_info[5])
#         else:
#             flash("Staff not found")
#             return redirect(url_for('index'))
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         flash(f"Error: {err}")
#         flash("An error occurred while fetching staff information.")
#         return redirect(url_for('index'))
#     finally:
#         # Close the cursor and the connection
#         cursor.close()
#         conn.close()



if __name__ == "__main__":
    app.run(port=5008, debug=True)


