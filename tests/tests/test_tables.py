import unittest
from myapp import app, db, User, Place, Review, City, State

class MigrationTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_initial_migration(self):
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        retrieved_user = User.query.first()
        self.assertEqual(retrieved_user.email, 'test@example.com')

if __name__ == '__main__':
    unittest.main()
