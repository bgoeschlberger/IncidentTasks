import unittest
from application.application import Application
from application.user import User
from application.role import UserRole
from incident.incident import Incident


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = Application.getInstance()

    def test_login(self):
        self.app.login("test_user", "password")
        self.assertEqual(self.app.getCurrentUser().getName(), "test_user")
        self.assertEqual(self.app.getCurrentUser().getRole(), UserRole.REGISTERED)

if __name__ == '__main__':
    unittest.main()
