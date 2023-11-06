import unittest
from flask_testing import TestCase
from input_staff_info import app  
import json

class CreateApplication(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_create_application(self):
        test_data = {
            "Position_ID": 30001,
            "Staff_ID": 160065,
            "Application_Date": "2023-11-04",
            "Cover_Letter": "This is the cover letter text.",
            "Application_Status": 0
        }

        response = self.client.post('/create_application', json=test_data)
        data = json.loads(response.data)

        # self.assertEqual(response.status_code, 200)  #  Assuming you return 200 for successful requests
        self.assertEqual(data['message'], 'Application created successfully')

if __name__ == '__main__':
    unittest.main()
