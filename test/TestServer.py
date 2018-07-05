import unittest
from server import app


class TestServer(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def test_getJuice(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
