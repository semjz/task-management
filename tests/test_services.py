import unittest

from core.repositories import TaskRepository, UserRepository
from core.services import TaskService, UserService
from enums import TaskStatus

class ServiceTests(unittest.TestCase):
    def test_create_user(self):
        repo = UserRepository()
        service = UserService(repo)

        user = service.create_user("Ada", "Lovelace", "ada@example.com")

        self.assertEqual(user.first_name, "Ada")
        self.assertEqual(len(repo.list()), 1)

    def test_create_task(self):
        user_repo = UserRepository()
        user_service = UserService(user_repo)
        owner = user_service.create_user("Grace", "Hopper", "grace@example.com")

        task_repo = TaskRepository()
        task_service = TaskService(task_repo)

        task = task_service.create_task(owner, "Ship feature", "Prepare v1 release", TaskStatus.IN_PROGRESS)

        self.assertEqual(task.owner.email, "grace@example.com")
        self.assertEqual(task.status, TaskStatus.IN_PROGRESS)
        self.assertEqual(len(task_repo.list()), 1)

if __name__ == "__main__":
    unittest.main()