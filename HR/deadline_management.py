from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import and_, or_, desc
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost:3306/hr portal"
db = SQLAlchemy(app)
CORS(app)

class Role(db.Model):
    role_name = db.Column(db.String(20), primary_key=True)
    role_desc = db.Column(db.Text, nullable=False)
    department = db.Column(db.String(20), nullable=False)
    skills = db.relationship('RoleSkill', backref='role', lazy=True)


class RoleSkill(db.Model):
    role_name = db.Column(db.String(20), db.ForeignKey(
        'role.role_name'), primary_key=True)
    skill_name = db.Column(db.String(50), primary_key=True)


class Open_position(db.Model):
    Position_ID = db.Column(db.String(20), primary_key=True)
    Role_Name = db.Column(db.String(20), db.ForeignKey('role.role_name'))
    Starting_Date = db.Column(db.Date, nullable=True)
    Ending_Date = db.Column(db.Date, nullable=True)

# works
# testing
# check if data input is too little or blank
# check for if ending date has passed
# check if role name does not exist
# check if ending date is earlier than starting date

#check for minimum character
# def field_check(field):
#     min_length = 2
#     if field == "":
#         return "Missing fields"
#     elif len(str(field)) < min_length:
#         return "Need to input at least " + str(min_length) + " letters"
#     return None

def date_check(starting_date, ending_date, role_name):
    today = datetime.now().date()

    # Check for empty starting_date
    if not starting_date:
        return "Starting date is empty"
    
    # Check for empty ending_date
    if not ending_date:
        return "Ending date is empty"

    # Parse dates since they are not empty
    starting_date_parsed = datetime.strptime(starting_date, '%Y-%m-%d').date()
    ending_date_parsed = datetime.strptime(ending_date, '%Y-%m-%d').date()

    # Check if starting date has passed
    if starting_date_parsed < today:
        return "Starting date has passed"

    # Check if ending_date has passed today's date
    if ending_date_parsed < today:
        return "Ending date has passed"

    # Check if ending_date is earlier than starting_date
    if ending_date_parsed < starting_date_parsed:
        return "Ending date is earlier than starting date"

    # Check if there are any existing positions with overlapping dates for the same role name
    existing_positions = Open_position.query.filter(
        Open_position.Role_Name == role_name,
        or_(
            and_(Open_position.Starting_Date <= starting_date_parsed,
                 Open_position.Ending_Date >= starting_date_parsed),
            and_(Open_position.Starting_Date <= ending_date_parsed,
                 Open_position.Ending_Date >= ending_date_parsed),
            and_(Open_position.Starting_Date >= starting_date_parsed,
                 Open_position.Ending_Date <= ending_date_parsed)
        )
    ).all()

    if existing_positions:
        return "Dates overlap with existing positions for the same role name"

    return None


def generate_position_id():
    last_position = Open_position.query.order_by(desc(Open_position.Position_ID)).first()
    if last_position:
        # Assuming Position_ID is numeric and can be converted directly to int.
        # You might need to adjust this if the Position_ID format is different.
        last_id = int(last_position.Position_ID)
        new_id = last_id + 1
    else:
        new_id = 1  # This is the first position ID if there are no positions in the DB
    return str(new_id)

def role_exists(role_name):
    return Role.query.filter_by(role_name=role_name).first() is not None

@app.route('/HR/add_open_position', methods=['POST'])
def add_open_position():
    if request.is_json:
        try:
            data = request.get_json()
            role_name = data.get('role_name')
            department = data.get('department')  # This is not used in Open_position
            skills = data.get('skills')          # This is not used in Open_position
            role_desc = data.get('role_desc')    # This is not used in Open_position

            # Validate role_name exists
            if not role_exists(role_name):
                return jsonify({
                    'message': 'Role name does not exist',
                    'data': {"role_name": role_name}
                }), 400

            # Generate a new position ID
            position_id = generate_position_id()

            # Create and add the new open position without starting and ending dates
            new_open_position = Open_position(
                Position_ID=position_id,
                Role_Name=role_name,
                Starting_Date = None,
                Ending_Date = None,
                
            )
            db.session.add(new_open_position)
            db.session.commit()

            return jsonify({
                'message': 'Open position added successfully',
                'data': {
                    'Position_ID': position_id,
                    'Role_Name': role_name,
                    "Starting_Date": "Null",
                    "Ending_Date": "Null"
                }
            }), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({
                "code": 500,
                "message": "Internal error: " + str(e)
            }), 500

    else:
        return jsonify({
            "code": 400,
            "message": "Please use a valid JSON request"
        }), 400





# @app.route('/HR/open_position', methods=['POST'])
# def create_position():
#     if request.is_json:
#         try:
#             data = request.get_json()
#             Role_Name = data.get('Role_Name')
#             Starting_Date = data.get('Starting_Date')
#             Ending_Date = data.get('Ending_Date')

#             # Check if either Starting_Date or Ending_Date is provided but not both
#             if (Starting_Date is None and Ending_Date is not None) or (Starting_Date is not None and Ending_Date is None):
#                 return jsonify({
#                     'message': 'Both starting date and ending date are required if one is provided',
#                     'data': {}
#                 }), 400

#             # At this point, either both dates are provided or both are None
#             starting_date_parsed = None
#             ending_date_parsed = None

#             if Starting_Date and Ending_Date:
#                 starting_date_parsed = datetime.strptime(Starting_Date, '%Y-%m-%d').date()
#                 ending_date_parsed = datetime.strptime(Ending_Date, '%Y-%m-%d').date()

#             if not (Role.query.filter_by(role_name=Role_Name).first()):
#                 return jsonify({
#                     'message': 'Role Name does not exist',
#                     'data': {"role_name": Role_Name}
#                 }), 400

#             Position_ID = generate_position_id()

#             position = Open_position(Position_ID=Position_ID, Role_Name=Role_Name,
#                                      Starting_Date=starting_date_parsed,
#                                      Ending_Date=ending_date_parsed)
#             db.session.add(position)
#             db.session.commit()

#             return jsonify({
#                 'message': 'New Position created successfully',
#                 'data': {'Position_ID': Position_ID}
#             }), 201

#         except Exception as e:
#             print(str(e))
#             return jsonify({
#                 "code": 500,
#                 "message": "Internal error: " + str(e)
#             }), 500

#     return jsonify({
#         "code": 400,
#         "message": "Please use a valid JSON request"
#     }), 400











# # Works Starts
# @app.route('/HR/open_position', methods=['POST'])
# def create_position():
#     if request.is_json:
#         # send data to relevant columnn
#         try:
#             data = request.get_json()
#             Position_ID = data.get('Position_ID')
#             Role_Name = data.get('Role_Name')
#             Starting_Date = data.get('Starting_Date')
#             Ending_Date = data.get('Ending_Date')

#             # Check if position id is unique
#             if Open_position.query.filter_by(Position_ID=Position_ID).first():
#                 return jsonify({
#                     'message': 'Position ID already exists',
#                     'data': {"role_name": Position_ID}
#                 }), 400

#             # Check if role name is unique
#             if not (Role.query.filter_by(role_name=Role_Name).first()):
#                 return jsonify({
#                     'message': 'Role Name does not exist',
#                     'data': {"role_name": Role_Name}
#                 }), 400

#             fields_error = {}

#             # position_id_error = field_check(Position_ID)
#             # if position_id_error:
#             #     fields_error['position_id'] = position_id_error

#             # role_error = field_check(Role_Name)
#             # if role_error:
#             #     fields_error['role_name'] = role_error

#             date_error = date_check(Starting_Date, Ending_Date, Role_Name)
#             if date_error:
#                 fields_error['date_error'] = date_error

#             # Check if any field is missing
#             if fields_error:
#                 return jsonify({
#                     'message': 'Required fields are missing or invalid',
#                     'data': fields_error
#                 }), 400

#             # Create the position listing
#             position = Open_position(Position_ID=Position_ID, Role_Name=Role_Name,
#                                      Starting_Date=Starting_Date, Ending_Date=Ending_Date)
#             db.session.add(position)

#             db.session.commit()

#             return jsonify({
#                 'message': 'New Position created successfully'
#             }), 201

#         except Exception as e:
#             print(str(e))

#             return jsonify({
#                 "code": 500,
#                 "message": "internal error: " + str(e)
#             }), 500

#     # if reached here, not a JSON request.
#     return jsonify({
#         "code": 400,
#         "message": "Please use a valid json request"
#     }), 400

# #End








# @app.route('/HR/role_admin', methods=['PUT'])
# def update_role():
#     if request.is_json:
#         try:
#             data = request.get_json()
#             title = data.get('role_name')
#             description = data.get('description')
#             department_name = data.get('department')
#             skills = data.get('skills')

#             role = Role.query.filter_by(role_name=title).first()

#             if not role:
#                 return jsonify({'message': 'Role not found'}), 404

#             # field validation if it exists
#             fields_error = {}

#             if 'description' in data:
#                 description_error = field_check(description)
#                 if description_error:
#                     fields_error['description'] = description_error

#             if 'department' in data:
#                 department_error = field_check(department_name)
#                 if department_error:
#                     fields_error['department'] = department_error

#             if 'skills' in data:
#                 if isinstance(skills, list):
#                     skills_error = field_check(skills)
#                     if skills_error:
#                         fields_error['skills'] = skills_error
#                 else:
#                     fields_error['skills'] = "Skills should be a list"

#             # Check if any field is missing
#             if fields_error:
#                 return jsonify({
#                     'message': 'Required fields are missing or invalid',
#                     'data': fields_error
#                 }), 400

#             # Update the role data with the new values
#             if 'description' in data:
#                 role.role_desc = description

#             if 'department' in data:
#                 role.department = department_name

#             if 'skills' in data:
#                 # Filter out skills that are already associated with the role
#                 new_skills = [skill for skill in skills if skill not in [
#                     s.skill_name for s in role.skills]]

#                 # Add new skills
#                 for skill in new_skills:
#                     role_skill = RoleSkill(role_name=title, skill_name=skill)
#                     db.session.add(role_skill)

#             # Commit the changes to the database
#             db.session.commit()

#             # get skills for json response
#             skills = [skill.skill_name for skill in role.skills]

#             return jsonify({
#                 'message': 'Role updated successfully',
#                 'data': {
#                     'role_name': role.role_name,
#                     'role_desc': role.role_desc,
#                     'department': role.department,
#                     'skills': skills
#                 }}), 200

#         except Exception as e:
#             print(str(e))

#             return jsonify({
#                 "code": 500,
#                 "message": "internal error: " + str(e)
#             }), 500

#     # if reached here, not a JSON request.
#     return jsonify({
#         "code": 400,
#         "message": "Please use a valid json request"
#     }), 400


if __name__ == '__main__':
    app.run(port=5015, debug=True)
