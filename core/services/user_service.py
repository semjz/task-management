from core.entities import User
class UserService:
    def __init__(self, repo):
        self.repo = repo

    def create_user(self, first_name, last_name, email):
        user = User(first_name, last_name, email)
        self.repo.add(user)
        return user