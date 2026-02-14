from core.entities import Task, User
from enums import TaskStatus

class TaskService:
    def __init__(self, repo):
        self.repo = repo

    def create_task(
        self,
        owner: User,
        title: str,
        description: str,
        status: TaskStatus = TaskStatus.PENDING,
    ) -> Task:
        task = Task(owner=owner, title=title, description=description, status=status)
        self.repo.add(task)
        return task