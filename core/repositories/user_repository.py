class UserRepository:
    def __init__(self):
        self._users = []

    def add(self, user):
        self._users.append(user)

    def list(self):
        return self._users