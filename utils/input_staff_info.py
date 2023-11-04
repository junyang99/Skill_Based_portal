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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/HR Portal'
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

    def __init__(self, Position_ID, Staff_ID, Application_Date, Cover_Letter, Application_Status):
        # self.Application_ID = Application_ID
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

class Role(db.Model):
    __tablename__ = 'Role'

    Role_Name = db.Column(db.String(20), nullable=False, primary_key=True)
    Role_Desc = db.Column(db.String(100), nullable=False)
    Department = db.Column(db.String(100), nullable=False)

    def __init__(self, Role_Name, Role_Desc, Department):
        self.Role_Name = Role_Name
        self.Role_Desc = Role_Desc
        self.Department = Department

    def json(self):
        return {
            'Role_Name': self.Role_Name,
            'Role_Desc': self.Role_Desc,
            'Department' : self.Department
        }
    
class Open_Position(db.Model):
    __tablename__ = 'Open_Position'

    Position_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Role_Name = db.Column(db.String(20), nullable=False)
    Starting_Date = db.Column(db.Date, nullable=False)
    Ending_Date = db.Column(db.Date, nullable=False)

    def __init__(self, Position_ID, Role_Name, Starting_Date, Ending_Date):
        self.Position_ID = Position_ID
        self.Role_Name = Role_Name
        self.Starting_Date = Starting_Date
        self.Ending_Date = Ending_Date

    def json(self):
        return {
            'Position_ID': self.Position_ID,
            'Role_Name': self.Role_Name,
            'Starting_Date': self.Starting_Date,
            'Ending_Date': self.Ending_Date
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

@app.route('/create_application', methods=['POST'])
def create_application():
    if request.method == 'POST':
        data = request.get_json()

        # Extract data from the request
        position_id = data.get('Position_ID')
        staff_id = data.get('Staff_ID')
        application_date = data.get('Application_Date')
        cover_letter = data.get('Cover_Letter')
        application_status = data.get('Application_Status')

        # Create a new Application instance
        new_application = Application(
            Position_ID=position_id,
            Staff_ID=staff_id,
            Application_Date=application_date,
            Cover_Letter=cover_letter,
            Application_Status=application_status
        )

        # Add the new application to the database
        db.session.add(new_application)
        db.session.commit()

        return jsonify({'message': 'Application created successfully'})
    

@app.route('/Staff/applications/<int:Staff_ID>', methods=['GET'])
def get_staff_applications(Staff_ID):
    try:
        # Retrieve applications for the specified Staff_ID
        applications = Application.query.filter_by(Staff_ID=Staff_ID).all()

        if applications:
            # Create a list to store the combined data
            combined_data = []

            for app in applications:
                # Get the position associated with the application
                position = Open_Position.query.get(app.Position_ID)

                # Get the role associated with the position
                role = Role.query.get(position.Role_Name)

                # Construct a JSON object with role_name, dept, application_date, and status
                combined_data.append({
                    'role_name': role.Role_Name,
                    'dept': role.Department,
                    'application_date': app.Application_Date,
                    'application_status': app.Application_Status,  # Include Application_Status 0: pending, 1: accepted, 2: rejected
                })

            return jsonify({
                'code': 200,
                'data': combined_data
            })
        else:
            return jsonify({
                'code': 404,
                'message': 'No applications found for the specified Staff ID.'
            }), 404
    except Exception as e:
        # Handle exceptions, log errors, and return an appropriate response
        return jsonify({
            'code': 500,
            'message': 'Internal Server Error: ' + str(e)
        }), 500

    
@app.route('/Staff/<int:Staff_ID>/roles', methods=['GET'])
def get_staff_roles(Staff_ID):
    try:
        # Retrieve roles for the specified Staff_ID from the Role table
        roles = Role.query.filter_by(Staff_ID=Staff_ID).all()

        if roles:
            # Convert the role objects to JSON format
            roles_json = [role.json() for role in roles]

            return jsonify({
                'code': 200,
                'data': roles_json
            })
        else:
            return jsonify({
                'code': 404,
                'message': 'No roles found for the specified Staff ID.'
            }), 404
    except Exception as e:
        # Handle exceptions, log errors, and return an appropriate response
        return jsonify({
            'code': 500,
            'message': 'Internal Server Error: ' + str(e)
        }), 500


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
    app.run(port=5016, debug=True)


