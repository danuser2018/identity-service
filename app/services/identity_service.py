from app.models.identity import Identity
from .repository import IdentityRepository

class IdentityService:
    def __init__(self, repository: IdentityRepository):
        self.repository = repository

    def get_identity(self) -> Identity:
        """
        Get the complete user identity.
        """
        return self.repository.get_identity()

    def get_name(self) -> str:
        """
        Get the username from identity.
        """
        return self.repository.get_identity().name

    def get_email(self) -> str:
        """
        Get the user email from identity.
        """
        return self.repository.get_identity().email
