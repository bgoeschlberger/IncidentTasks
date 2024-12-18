from typing import List, Optional
from .user import User, UserRole


class Application:
    _instance = None

    def __init__(self):
        if not Application._instance:
            self.current_user: Optional[User] = None
            Application._instance = self

    @staticmethod
    def getInstance():
        if not Application._instance:
            Application()
        return Application._instance

    def login(self, username: str, password: str):
        if username == "agent":
            role = UserRole.RESPONSE_AGENT
        elif username == "manager":
            role = UserRole.RESPONSE_MANAGER
        elif username == "admin":
            role = UserRole.ADMIN
        else:
            role = UserRole.REGISTERED
        self.current_user = User(username, role)

    def getCurrentUser(self) -> Optional[User]:
        return self.current_user
