from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import and_, or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost:3306/hr portal"
db = SQLAlchemy(app)


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
    Starting_Date = db.Column(db.Date, nullable=False)
    Ending_Date = db.Column(db.Date, nullable=False)

# works
# testing
# check if data input is too little or blank
# check for if ending date has passed
# check if role name does not exist
# check if ending date is earlier than starting date


def field_check(field):
    min_length = 2
    if field == "":
        return "Missing fields"
    elif len(str(field)) < min_length:
        return "Need to input at least " + str(min_length) + " letters"
    return None

# function works as expected

# OLD
# def date_check(starting_date, ending_date):
#     today = datetime.now().date()
#     min_length = 10

#     # Parse starting_date and ending_date strings to datetime.date objects
#     starting_date = datetime.strptime(starting_date, '%Y-%m-%d').date()
#     ending_date = datetime.strptime(ending_date, '%Y-%m-%d').date()

#     if starting_date == "" or ending_date == "":
#         return "Missing fields"
#     elif len(str(starting_date)) < min_length or len(str(ending_date)) < min_length:
#         return "Need to input at least " + str(min_length) + " letters"

#     # Check if ending_date has passed today's date
#     if ending_date < today:
#         return "Ending date has passed"
#     # Check if ending_date is earlier than starting_date
#     elif ending_date < starting_date:
#         return "Ending date is earlier than starting date"
#     return None


def date_check(starting_date, ending_date, role_name):
    today = datetime.now().date()
    min_length = 10

    starting_date = datetime.strptime(starting_date, '%Y-%m-%d').date()
    ending_date = datetime.strptime(ending_date, '%Y-%m-%d').date()

    if starting_date == "" or ending_date == "":
        return "Missing fields"
    elif len(str(starting_date)) < min_length or len(str(ending_date)) < min_length:
        return "Need to input at least " + str(min_length) + " letters"

    # Check if starting date has passed
    if starting_date < today:
        return "Starting date has passed"

    # Check if ending_date has passed today's date
    if ending_date < today:
        return "Ending date has passed"
    # Check if ending_date is earlier than starting_date
    elif ending_date < starting_date:
        return "Ending date is earlier than starting date"

    # Check if there are any existing positions with overlapping dates for the same role name
    existing_positions = Open_position.query.filter(
        Open_position.Role_Name == role_name,
        or_(
            and_(Open_position.Starting_Date <= starting_date,
                 Open_position.Ending_Date >= starting_date),
            and_(Open_position.Starting_Date <= ending_date,
                 Open_position.Ending_Date >= ending_date),
            and_(Open_position.Starting_Date >= starting_date,
                 Open_position.Ending_Date <= ending_date)
        )
    ).all()

    if existing_positions:
        return "Dates overlap with existing positions for the same role name"

    return None


# Works
@app.route('/HR/open_position', methods=['POST'])
def create_position():
    if request.is_json:
        # send data to relevant columnn
        try:
            data = request.get_json()
            Position_ID = data.get('Position_ID')
            Role_Name = data.get('Role_Name')
            Starting_Date = data.get('Starting_Date')
            Ending_Date = data.get('Ending_Date')

            # Check if position id is unique
            if Open_position.query.filter_by(Position_ID=Position_ID).first():
                return jsonify({
                    'message': 'Position ID already exists',
                    'data': {"role_name": Position_ID}
                }), 400

            # Check if role name is unique
            if not (Role.query.filter_by(role_name=Role_Name).first()):
                return jsonify({
                    'message': 'Role Name does not exist',
                    'data': {"role_name": Role_Name}
                }), 400

            fields_error = {}

            position_id_error = field_check(Position_ID)
            if position_id_error:
                fields_error['position_id'] = position_id_error

            role_error = field_check(Role_Name)
            if role_error:
                fields_error['role_name'] = role_error

            date_error = date_check(Starting_Date, Ending_Date, Role_Name)
            if date_error:
                fields_error['date_error'] = date_error

            # Check if any field is missing
            if fields_error:
                return jsonify({
                    'message': 'Required fields are missing or invalid',
                    'data': fields_error
                }), 400

            # Create the position listing
            position = Open_position(Position_ID=Position_ID, Role_Name=Role_Name,
                                     Starting_Date=Starting_Date, Ending_Date=Ending_Date)
            db.session.add(position)

            db.session.commit()

            return jsonify({
                'message': 'New Position created successfully'
            }), 201

        except Exception as e:
            print(str(e))

            return jsonify({
                "code": 500,
                "message": "internal error: " + str(e)
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Please use a valid json request"
    }), 400


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
