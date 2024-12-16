import unittest
from unittest.mock import patch
from incident.incident import Incident
from incident.task import Task, TaskStatus
from incident.status import IncidentStatus
from application.user import User, UserRole
from application.application import Application


class TestIncident(unittest.TestCase):

    def setUp(self):
        self.incident = Incident("Sample Incident")

    @patch('application.application.Application.getCurrentUser')
    def test_add_task_to_incident_as_manager(self, mock_getCurrentUser):
        # Mock the getCurrentUser method
        mock_getCurrentUser.return_value = User("testuser", UserRole.RESPONSE_MANAGER)
        task = Task("Task 1")
        self.incident.addTask(task)
        self.assertEqual(len(self.incident.tasks), 1)

    @patch('application.application.Application.getCurrentUser')
    def test_add_task_to_incident_as_non_manager(self, mock_getCurrentUser):
        # Mock the getCurrentUser method
        mock_getCurrentUser.return_value = User("testuser", UserRole.REGISTERED)
        
        # Try to add a task as a non-manager
        task = Task("Task 1")
        with self.assertRaises(PermissionError):
            self.incident.addTask(task)

    @patch('application.application.Application.getCurrentUser')
    def test_resolve_incident_with_unresolved_tasks(self, mock_getCurrentUser):
        # Mock the getCurrentUser method
        mock_getCurrentUser.return_value = User("testuser", UserRole.RESPONSE_MANAGER)

        task1 = Task("Task 1")
        task2 = Task("Task 2")
        task1.status = TaskStatus.RESOLVED
        self.incident.addTask(task1)
        self.incident.addTask(task2)
        with self.assertRaises(Exception):
            self.incident.resolve()

    @patch('application.application.Application.getCurrentUser')
    def test_resolve_incident_with_all_tasks_resolved(self, mock_getCurrentUser):
        # Mock the getCurrentUser method
        mock_getCurrentUser.return_value = User("testuser", UserRole.RESPONSE_MANAGER)
        
        task1 = Task("Task 1")
        task2 = Task("Task 2")
        task1.status = TaskStatus.RESOLVED
        task2.status = TaskStatus.RESOLVED
        self.incident.addTask(task1)
        self.incident.addTask(task2)
        self.incident.resolve()
        self.assertEqual(self.incident.status, IncidentStatus.RESOLVED)

    @patch('application.application.Application.getCurrentUser')
    def test_reopen_resolved_incident(self, mock_getCurrentUser):
        # Mock the getCurrentUser method
        mock_getCurrentUser.return_value = User("testuser", UserRole.RESPONSE_MANAGER)

        task1 = Task("Task 1")
        task2 = Task("Task 2")
        task1.status = TaskStatus.RESOLVED
        task2.status = TaskStatus.RESOLVED
        self.incident.addTask(task1)
        self.incident.addTask(task2)
        self.incident.resolve()
        self.incident.reopen()
        self.assertEqual(self.incident.status, IncidentStatus.OPEN)


if __name__ == '__main__':
    unittest.main()
