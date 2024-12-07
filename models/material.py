
class Material:
    def __init__(self, material_id: int, types: str, content: str):
        self.material_id = material_id
        self.types = types
        self.content = content

    def view_material(self):
        return self.content
