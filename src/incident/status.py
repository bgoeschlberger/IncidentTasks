from enum import Enum

class IncidentStatus(Enum):
    OPEN = "Open"
    RESOLVED = "Resolved"

class TaskStatus(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    REQUIRES_CLARIFICATION = "Requires Clarification"
    RESOLVED = "Resolved"
