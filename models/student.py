
from models.user import User

class Student(User):
    def __init__(self, student_id: int, name: str, email: str, password: str, profile: str):
        super().__init__(student_id, name, email, password, role="Student")
        self.profile = profile

    def enroll_course(self, course):
        pass

    def unenroll_course(self, course):
        pass

    def submit_assignment(self, assignment):
        pass
