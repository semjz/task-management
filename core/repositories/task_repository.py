class TaskRepository:
    def __init__(self):
        self._tasks = []

    def add(self, user):
        self._tasks.append(user)

    def list(self):
        return self._tasks