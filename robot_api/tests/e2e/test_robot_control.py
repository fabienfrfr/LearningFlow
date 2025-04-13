import pytest
from src.application.use_cases.control_robot_use_case import ControlRobotUseCase
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

@pytest.fixture
def use_case(service):
    return ControlRobotUseCase(service)

def test_control_robot(use_case):
    result = use_case.execute(1, "move forward")
    assert result is not None

