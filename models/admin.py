
from models.user import User

class Admin(User):
    def __init__(self, admin_id: int, name: str, email: str, password: str):
        super().__init__(admin_id, name, email, password, role="Admin")

    def manage_student(self):
        pass

    def manage_lecture(self):
        pass

    def add_course(self, course):
        pass

    def assign_password(self, user, password):
        user.password = password
