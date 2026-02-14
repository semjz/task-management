from core.entities import Task
class TaskService:
    def __init__(self, repo):
        self.repo = repo

    def create_user(self, first_name, last_name, email):
        task = Task(first_name, last_name, email)
        self.repo.add(task)
        return task