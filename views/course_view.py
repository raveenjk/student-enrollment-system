
class CourseView:
    @staticmethod
    def display_course(course):
        print(f"Course ID: {course.course_id}, Name: {course.course_name}")
        for material in course.course_materials:
            print(f"- {material.types}: {material.content}")
