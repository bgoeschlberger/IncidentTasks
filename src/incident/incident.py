from typing import List

from application.application import Application
from application.role import UserRole
from .task import Task, TaskStatus
from .status import IncidentStatus


class Incident:
    def __init__(self, description: str):
        self.description = description
        self.status = IncidentStatus.OPEN
        self.tasks: List[Task] = []

    def addTask(self, task: Task):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            self.tasks.append(task)
        else:
            raise PermissionError("Only incident response managers can create tasks")

    def resolve(self):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            if any(task.status != TaskStatus.RESOLVED for task in self.tasks):
                raise Exception("Incident cannot be resolved because not all tasks are resolved")
            self.status = IncidentStatus.RESOLVED
        else:
            raise PermissionError("Only incident response managers can resolve incidents")

    def reopen(self):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            self.status = IncidentStatus.OPEN
        else:
            raise PermissionError("Only incident response managers can reopen incidents")

    def updateDescription(self, newDesc: str):
        self.description = newDesc
