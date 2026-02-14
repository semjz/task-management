from core.entities import User
class UserRepository:
    def __init__(self):
        self._users : list[User] = []

    def add(self, user: User) -> None:
        self._users.append(user)

    def list(self) -> list[User]:
        return self._users