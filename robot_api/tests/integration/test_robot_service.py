import pytest
from src.domain.services.robot_service import RobotService
from src.infrastructure.persistence.postgres_repository import PostgresRepository
from sqlalchemy.orm import Session

@pytest.fixture
def session():
    return Session()  # Mock session

@pytest.fixture
def repository(session):
    return PostgresRepository(session)

@pytest.fixture
def service(repository):
    return RobotService(repository)

def test_get_robot(service):
    robot = service.get_robot(1)
    assert robot is not None

