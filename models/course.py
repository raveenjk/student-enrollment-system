
class Course:
    def __init__(self, course_id: int, course_name: str):
        self.course_id = course_id
        self.course_name = course_name
        self.course_materials = []

    def add_material(self, material):
        self.course_materials.append(material)

    def remove_material(self, material):
        self.course_materials.remove(material)

    def add_assignment(self, assignment):
        pass

    def add_pdf(self, pdf: str):
        pass

    def add_recording(self, link: str):
        pass
