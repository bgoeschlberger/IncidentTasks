from typing import Optional

from application.application import Application
from .status import TaskStatus
from application.user import User, UserRole


class Task:
    def __init__(self, description: str):
        self.description = description
        self.status = TaskStatus.OPEN
        self.assigned_user: Optional[User] = None

    def assignUser(self, user: User):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            self.assigned_user = user
        else:
            raise PermissionError("Only incident managers can assign tasks")

    def updateDescription(self, newDesc: str):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            self.description = newDesc

    def startWorking(self):
        if self.assigned_user and self.assigned_user.getName() == Application.getInstance().getCurrentUser().getName():
            if self.status in {TaskStatus.OPEN, TaskStatus.REQUIRES_CLARIFICATION}:
                self.status = TaskStatus.IN_PROGRESS
            else:
                raise Exception("Task cannot be started unless it is OPEN or REQUIRES_CLARIFICATION")
        else:
            raise PermissionError("Only the assigned user can start working on the task")

    def finishTask(self):
        if self.assigned_user and Application.getInstance().getCurrentUser().getRole() == self.assigned_user.getRole():
            if self.status == TaskStatus.IN_PROGRESS:
                self.status = TaskStatus.RESOLVED
            else:
                raise Exception("Task cannot be finished unless it is IN_PROGRESS")
        else:
            raise PermissionError("Only the assigned user can finish the task")

    def setToRequiresClarification(self):
        if self.assigned_user and Application.getInstance().getCurrentUser().getRole() == self.assigned_user.getRole():
            if self.status in {TaskStatus.OPEN, TaskStatus.IN_PROGRESS}:
                self.status = TaskStatus.REQUIRES_CLARIFICATION
            else:
                raise Exception("Task cannot be set to REQUIRES_CLARIFICATION unless it is OPEN or IN_PROGRESS")
        else:
            raise PermissionError("Only the assigned user can set the task to REQUIRES_CLARIFICATION")

    def updateStatus(self, new_status: TaskStatus):
        if Application.getInstance().getCurrentUser().getRole() == UserRole.RESPONSE_MANAGER:
            self.status = new_status
        else:
            raise PermissionError("Only incident response managers can update the task status to any state")
