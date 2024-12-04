# test_datamanager.py
import unittest
from yourapp import app, db
from yourapp.models import User
from yourapp.datamanager import DataManager

class DataManagerTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()
        self.data_manager = DataManager()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_save_user_to_database(self):
        app.config['USE_DATABASE'] = True
        user = User(id='1', email='test@example.com', password='password')
        self.data_manager.save_user(user)
        loaded_users = self.data_manager.load_users()
        self.assertEqual(len(loaded_users), 1)
        self.assertEqual(loaded_users[0].email, 'test@example.com')

    def test_save_user_to_file(self):
        app.config['USE_DATABASE'] = False
        user = User(id='2', email='fileuser@example.com', password='password')
        self.data_manager.save_user(user)
        loaded_users = self.data_manager.load_users()
        self.assertEqual(len(loaded_users), 1)
        self.assertEqual(loaded_users[0].email, 'fileuser@example.com')

if __name__ == '__main__':
    unittest.main()
