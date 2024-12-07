
class User:
    def __init__(self, user_id: int, name: str, email: str, password: str, role: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def login(self, password: str) -> bool:
        return self.password == password

    def get_role(self) -> str:
        return self.role
