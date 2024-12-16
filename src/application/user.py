from .role import UserRole


class User:
    def __init__(self, username: str, role: UserRole):
        self.username = username
        self.role = role

    def getName(self) -> str:
        return self.username

    def getRole(self) -> UserRole:
        return self.role
