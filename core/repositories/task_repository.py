from core.entities import Task
class TaskRepository:
    def __init__(self):
        self._tasks : list[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def list(self) -> list[Task]:
        return self._tasks