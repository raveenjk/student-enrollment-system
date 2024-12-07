
from models.admin import Admin
from models.student import Student
from models.lecture import Lecture
from views.user_view import UserView

class UserController:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user

    def display_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            UserView.display_user(user)
        else:
            print("User not found.")
