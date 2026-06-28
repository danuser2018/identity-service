from fastapi import APIRouter
from app.services import EnvIdentityRepository, IdentityService
from app.api.controllers import IdentityController
from app.models.identity import Identity, NameResponse, EmailResponse, HealthResponse

router = APIRouter()

# Dependency injection setup for the MVP environment
repository = EnvIdentityRepository()
service = IdentityService(repository=repository)
controller = IdentityController(service=service)

@router.get("/identity", response_model=Identity)
def get_identity() -> Identity:
    """
    Endpoint to retrieve the full user identity.
    """
    return controller.get_identity()

@router.get("/identity/name", response_model=NameResponse)
def get_name() -> NameResponse:
    """
    Endpoint to retrieve the user's name.
    """
    return controller.get_name()

@router.get("/identity/email", response_model=EmailResponse)
def get_email() -> EmailResponse:
    """
    Endpoint to retrieve the user's email.
    """
    return controller.get_email()

@router.get("/health", response_model=HealthResponse)
def get_health() -> HealthResponse:
    """
    Endpoint to check the service health status.
    """
    return controller.get_health()
