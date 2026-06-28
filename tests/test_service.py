import pytest
from app.models.identity import Identity
from app.services.repository import IdentityRepository
from app.services.identity_service import IdentityService

class MockIdentityRepository(IdentityRepository):
    def __init__(self, name: str = "Alice", email: str = "alice@example.com"):
        self.name = name
        self.email = email

    def get_identity(self) -> Identity:
        return Identity(
            name=self.name,
            email=self.email
        )

def test_identity_service_retrieval():
    mock_repo = MockIdentityRepository(name="Alice", email="alice@example.com")
    service = IdentityService(repository=mock_repo)

    # Test retrieving full identity
    identity = service.get_identity()
    assert identity.name == "Alice"
    assert identity.email == "alice@example.com"

    # Test individual name and email queries
    assert service.get_name() == "Alice"
    assert service.get_email() == "alice@example.com"
