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
    self.new_password = Password("first_name","last_name","password")
def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEgual(self.new_password.first_name,"",)
    self.assertEqual(self.new_password.last_name,"",)
    self.assertEqual(self.new_password.password,"",)

if __name__ == '__main__':
    unittest.main()