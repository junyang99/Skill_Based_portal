#Connected
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from invokes import invoke_http
from urllib.parse import quote
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/HR Portal'  # Adjust the database name here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

viewStaffSkillURL = "http://localhost:5012/Staff_Skill"
roleSkillPercentURL = "http://localhost:5014/compare_skills"

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
    Role_Name = db.Column(db.String(20),db.ForeignKey('Role.Role_Name'), nullable=False)
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

class Role_Skill(db.Model):
    __tablename__ = 'Role_Skill'

    Role_Name = db.Column(db.String(20),db.ForeignKey('Role.Role_Name'), nullable=False, primary_key=True)
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'), nullable=False, primary_key = True)


    def __init__(self, Role_Name, Skill_Name):
        self.Role_Name = Role_Name
        self.Skill_Name = Skill_Name


    def json(self):
        return {
            'Skill_Name': self.Role_Name,
            'Skill_Desc': self.Skill_Name
        }
    
# specific role listings
@app.route('/Role_Listing', methods=['GET'])
def get_role_listing():
    # position_id = request.get_json()['position_id'] # input format -- {"position_id": position_id, "staff_id": staff_id}
    # staff_id = request.get_json()['staff_id']

    position_id = request.args.get('position_id')
    staff_id = request.args.get('staff_id')

    if position_id and staff_id:
        # get row from Open_Position table
        # can get Role_Name (1) from here
        selected_role_listing = Open_Position.query.filter_by(Position_ID = position_id).first()

        today = datetime.now().date()

        if selected_role_listing.Ending_Date < today:
            return jsonify({
                'code': 400,
                'message': 'Ending date has passed.'
            }), 400

        # use Role_Name from Open_Position table to match with Role_Name in Role table
        # Role table -> Role_Desc (2), Department (3)
        selected_role_info = Role.query.filter_by(Role_Name = selected_role_listing.Role_Name).first()

        # use Role Name from Open_Position table to match with Role_Name in Role_Skill table
        # get required skills (4) for the selected role listing
        selected_skill_info = Role_Skill.query.filter_by(Role_Name = selected_role_listing.Role_Name).all()

        # get Staff's current skills (5) from Staff_Skill table 
        staffURL = viewStaffSkillURL + "/" + str(staff_id)
        staff_skill = invoke_http(staffURL, method='GET') # this function is using get_staff_skills to return skills of a specific staff

        # return Role-Skill Match (6) from role_skill_percentage.py
        role_skill_params = {'staff_id': staff_id, 'role_name': selected_role_listing.Role_Name}
        role_skill_match = requests.get(roleSkillPercentURL, params=role_skill_params).json()

        if selected_role_info and selected_skill_info and staff_skill["code"]==200 and role_skill_match["code"]==200:
            return jsonify({
                'code': 200,
                'data':
                    {
                        'Role_Name': selected_role_listing.Role_Name,
                        'Role_Desc': selected_role_info.Role_Desc,
                        'Department': selected_role_info.Department,
                        'Required Skills for Role': [roleSkill.json() for roleSkill in selected_skill_info],
                        'Staff Skills': staff_skill,
                        'Role-Skill Match': role_skill_match
                    }
            })
        
        return jsonify({
            'code': 400,
            'message': 'Missing information for selected role listing.'
        }), 400

    return jsonify({
        'code': 400,
        'message': 'No role listing selected or no staff ID found.'
    }), 400

if __name__ == '__main__':
    app.run(port=5013, debug=True)