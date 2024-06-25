# test_database.py
import os
import unittest
from yourapp import app, db
from yourapp.models import User
from dotenv import load_dotenv

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        load_dotenv()  # Ensure environment variables are loaded

        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_sqlite_connection(self):
        os.environ['DATABASE_URL'] = 'sqlite:///test.db'
        os.environ['DATABASE_TYPE'] = 'sqlite'
        with app.app_context():
            user = User(id='1', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()
            fetched_user = User.query.first()
            self.assertEqual(fetched_user.email, 'test@example.com')

    def test_postgresql_connection(self):
        os.environ['DATABASE_URL'] = 'postgresql://username:password@localhost/testdb'
        os.environ['DATABASE_TYPE'] = 'postgresql'
        with app.app_context():
            user = User(id='1', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()
            fetched_user = User.query.first()
            self.assertEqual(fetched_user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main()
