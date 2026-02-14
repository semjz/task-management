from enums import TaskStatus
from core.entities import User
class Task:
    def __init__(
            self,
            owner:User,
            title: str,
            description:str,
            status:TaskStatus=TaskStatus.PENDING
    ) -> None:
        self.owner = owner
        self.title = title
        self.description = description
        self.status = status
