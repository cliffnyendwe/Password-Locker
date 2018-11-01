import unittest
from password import Password

class TestPassword(unittest.TestCase):
    """
    Test class that defines test cases for the password class behaviours.

    Args:
        unitest.TestCase: TestCase class that helps in creating test cases
        """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_password = Password("first_name","last_name","email","password")
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_password.first_name,"first_name",)
        self.assertEqual(self.new_password.last_name,"last_name",)
        self.assertEqual(self.new_password.email,"email",)
        self.assertEqual(self.new_password.password,"password",)

    def test_save_password(self):
        """
        test_save_password.save_password()
        self.assertEqual(len(Password.password_list),1)
        """

if __name__ == '__main__':
    unittest.main()