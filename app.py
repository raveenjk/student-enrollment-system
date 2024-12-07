
from models.admin import Admin
from models.student import Student
from models.course import Course
from models.material import Material
from controllers.user_controller import UserController
from views.course_view import CourseView

def main():
    # Controllers
    user_controller = UserController()

    # Adding users
    admin = Admin(admin_id=1, name="Admin1", email="admin@example.com", password="admin123")
    student = Student(student_id=2, name="Student1", email="student@example.com", password="student123", profile="CS")
    user_controller.add_user(admin)
    user_controller.add_user(student)

    # Display users
    user_controller.display_user(1)
    user_controller.display_user(2)

    # Create a course
    course = Course(course_id=101, course_name="Computer Science")
    material = Material(material_id=1, types="PDF", content="Introduction to CS")
    course.add_material(material)

    # Display course details
    CourseView.display_course(course)

if __name__ == "__main__":
    main()
