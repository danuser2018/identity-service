from abc import ABC, abstractmethod
from app.config import settings
from app.models.identity import Identity

class IdentityRepository(ABC):
    @abstractmethod
    def get_identity(self) -> Identity:
        """
        Retrieve the current user identity data.
        """
        pass

class EnvIdentityRepository(IdentityRepository):
    def get_identity(self) -> Identity:
        """
        Retrieve identity data from configuration settings loaded from environment.
        """
        return Identity(
            name=settings.USER_NAME,
            email=settings.USER_EMAIL
        )
