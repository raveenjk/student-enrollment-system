
from models.user import User

class Lecture(User):
    def __init__(self, lecture_id: int, name: str, email: str, password: str, profile: str):
        super().__init__(lecture_id, name, email, password, role="Lecture")
        self.profile = profile

    def add_lecture_material(self, material):
        pass

    def grade_student(self, student, grade):
        pass

    def manage_course(self, course):
        pass
