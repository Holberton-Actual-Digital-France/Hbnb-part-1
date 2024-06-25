""" manage the data """
import json
from .models import User
from . import db, app

class DataManager:
    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            # Implement file-based save logic
            self.save_user_to_file(user)

    def save_user_to_file(self, user):
        with open('users.json', 'a') as f:
            f.write(json.dumps(user.__dict__) + '\n')

    def load_users(self):
        if app.config['USE_DATABASE']:
            return User.query.all()
        else:
            # Implement file-based load logic
            return self.load_users_from_file()

    def load_users_from_file(self):
        users = []
        try:
            with open('users.json', 'r') as f:
                for line in f:
                    data = json.loads(line)
                    users.append(User(**data))
        except FileNotFoundError:
            pass
        return users
