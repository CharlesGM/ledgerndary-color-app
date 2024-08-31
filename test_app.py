import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Test default color
        response = self.app.get('/')
        self.assertIn(b'background-color: white;', response.data)

        # Test environment variable color
        with self.app.application.app_context():
            self.app.application.config['PAGE_COLOUR'] = 'blue'
        response = self.app.get('/')
        self.assertIn(b'background-color: blue;', response.data)

if __name__ == '__main__':
    unittest.main()
