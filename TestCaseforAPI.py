import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = 'http://localhost:27017'

    def test_faculty_api(self):
        # Add a faculty
        faculty_data = {
            "faculty_id": "F101",
            "faculty_name": "John Doe",
            "department": "Computer Science and Engineering",
            "position": "Professor",
            "email": "john.doe@example.com"
        }
        response = requests.post(f'{self.base_url}/faculty', json=faculty_data)
        self.assertEqual(response.status_code, 201)

        # Retrieve all faculty
        response = requests.get(f'{self.base_url}/faculty')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

        # Update the added faculty
        updated_data = {
            "faculty_id": "F101",
            "faculty_name": "John Doe",
            "department": "Computer Science and Engineering",
            "position": "Professor",
            "email": "john.doe@example.com"
        }
        response = requests.put(f'{self.base_url}/faculty/F101', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Delete the added/updated faculty
        response = requests.delete(f'{self.base_url}/faculty/F101')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
