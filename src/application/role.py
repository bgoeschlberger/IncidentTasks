from enum import Enum

class UserRole(Enum):
    UNREGISTERED = "Unregistered"
    REGISTERED = "Registered"
    RESPONSE_AGENT = "Response Agent"
    RESPONSE_MANAGER = "Response Manager"
    ADMIN = "Admin"
