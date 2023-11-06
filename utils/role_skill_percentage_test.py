import unittest
from flask_testing import TestCase
from role_skill_percentage import app  # Import your Flask app from role_skill_percentage.py
import json

class RoleSkillPercentageTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_compare_skills(self):
        staff_id = 140001  # Replace with a valid staff ID
        role_name = "Account Manager"  # Replace with a valid role name

        response = self.client.get(f'/compare_skills?staff_id={staff_id}&role_name={role_name}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)  # Assuming you return 200 for successful requests
        self.assertIn('data', data)
        self.assertIn('percentage_match', data['data'])
        percentage_match = data['data']['percentage_match']

        # Check if the calculated percentage match matches the expected value
        expected_percentage_match = 30.76923076923077
        self.assertAlmostEqual(percentage_match, expected_percentage_match, places=4)

        self.assertEqual(data['message'], 'Skills comparison successful')

    def test_compare_skills_invalid_staff_id(self):
        staff_id = 999  # Replace with an invalid staff ID
        role_name = "Account Manager"  # Replace with a valid role name

        response = self.client.get(f'/compare_skills?staff_id={staff_id}&role_name={role_name}')
        data = json.loads(response.data)

        self.assertEqual(data['code'], 500)  # Assuming you return 500 for internal server errors
        self.assertIn('message', data)

    def test_compare_skills_invalid_role_name(self):
        staff_id = 140001  # Replace with a valid staff ID
        role_name = "invalid_role"  # Replace with an invalid role name

        response = self.client.get(f'/compare_skills?staff_id={staff_id}&role_name={role_name}')
        data = json.loads(response.data)

        self.assertEqual(data['code'], 500)  # Assuming you return 500 for internal server errors
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
