import unittest
import json
from app import create_app, db, models


class LeadsTestCase(unittest.TestCase):
    """Test case for the auth blueprint."""

    def create_user(self):
        user = models.User(self.user_data['email'], self.user_data['password'])
        user.save()

    def setUp(self):
        """Set up test variables."""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client

        self.user_data = {
            'email': 'test@example.com',
            'password': 'password'
        }

        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()
            self.create_user()

    def login_user(self, email="test@example.com", password="password"):
        """This helper method helps log in a test user."""
        user_data = {
            'email': email,
            'password': password
        }
        return self.client().post('/auth', data=json.dumps(user_data), content_type='application/json')

    def test_user_login(self):
        res = self.login_user()
        self.assertEqual(res.status_code, 201)
        result = json.loads(res.data)
        self.assertEqual(result['message'], "You logged in successfully.")
        self.assertTrue(result['token'])

    def test_bad_password(self):

        bad_user_data = {
            'email': 'test@example.com',
            'password': 'bad_password'
        }

        res = self.client().post('/auth', data=json.dumps(bad_user_data), content_type='application/json')
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(json_data['message'], "Invalid email or password, Please try again")

    def test_not_registered_login(self):
        not_registered_user = {'email': 'email@not_registered.com', 'password': 'not_registered'}

        res = self.client().post('/auth', data=json.dumps(not_registered_user),
                                 content_type='application/json')

        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(
            json_data['message'], "Invalid email or password, Please try again")


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()