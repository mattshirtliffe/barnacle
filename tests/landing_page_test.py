import unittest
from app import create_app, db


class LandingPageTestCase(unittest.TestCase):
    """Test case for the landing blueprint."""

    def setUp(self):
        """Set up test variables."""
        self.app = create_app(config_name="testing")
        # initialize the test client
        self.client = self.app.test_client

        self.lead_data = {
            'email': 'test@example.com',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'phone': 'phone',
        }

        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()

    def test_landing_page(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_title(self):
        res = self.client().get('/')
        self.assertIn('<title>Landing Page - Start Bootstrap Theme</title>', res.data.decode())

    def test_lead_form(self):
        res = self.client().post('/', data=dict(
            first_name=self.lead_data['first_name'],
            last_name=self.lead_data['last_name'],
            email=self.lead_data['email'],
            phone=self.lead_data['phone']
        ))
        self.assertEqual(res.status_code, 302)

    def test_missing_field_lead_form(self):
        res = self.client().post('/', data=dict(
            first_name=self.lead_data['first_name'],
            last_name=self.lead_data['last_name'],
            phone=self.lead_data['phone']
        ),follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('This field is required.', res.data.decode())


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()