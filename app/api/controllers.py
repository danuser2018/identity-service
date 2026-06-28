from app.services.identity_service import IdentityService
from app.models.identity import Identity, NameResponse, EmailResponse, HealthResponse

class IdentityController:
    def __init__(self, service: IdentityService):
        self.service = service

    def get_identity(self) -> Identity:
        """
        Get complete identity response model.
        """
        return self.service.get_identity()

    def get_name(self) -> NameResponse:
        """
        Get name response model.
        """
        return NameResponse(name=self.service.get_name())

    def get_email(self) -> EmailResponse:
        """
        Get email response model.
        """
        return EmailResponse(email=self.service.get_email())

    def get_health(self) -> HealthResponse:
        """
        Get health check response model.
        """
        return HealthResponse(status="UP")
