#Connected
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import ForeignKey

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/HR Portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

#Checked 
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
        
#Checked
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

#Checked
class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Access_ID = db.Column(db.Integer, db.ForeignKey('Access_Control.Access_ID'), nullable=False)  # Foreign key reference
    # access_control = db.relationship(Access_Control, backref='staff', lazy=True)

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

class Application(db.Model):
    __tablename__ = 'Application'

    Application_ID = db.Column(db.Integer, nullable=False, primary_key=True)
    Position_ID = db.Column(db.Integer, db.ForeignKey('Open_Position.Position_ID'), nullable=False)
    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'), nullable=False)
    Application_Date = db.Column(db.Date, nullable=False)
    Cover_Letter = db.Column(db.String, nullable=False)
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


@app.route('/Application')
def get_all():
    ApplicationList = Application.query.all()
    if ApplicationList:
        return jsonify({
            'code': 200,
            'data': {
                'Application': [Application.json() for Application in ApplicationList]
            }
        }
        )
    return {
        'code': 400,
        'message': 'There is no records of applicant'
    }
    
# @app.route('/application/<string:Application_ID>')
# def get_application(Application_ID):
#     application = application.query.filter_by(
#         Application_ID=Application_ID).first()
#     if application:
#         if application.quantity != 0:
#             return jsonify({
#                 'code': 200,
#                 'application': application.json()
#             }
#             )
#         else:
#             return jsonify({
#                 'code': 200,
#                 'message': 'application does not exist.',
#                 "application": application.json()
#             }
#             )
#     return jsonify(
#         {
#             'code': 404,
#             'message': 'application not found'
#         }), 404

if __name__ == '__main__':
    app.run(port=5004, debug=True)
