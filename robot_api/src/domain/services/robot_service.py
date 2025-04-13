from src.domain.models.robot_model import Robot
from src.domain.repositories.robot_repository import RobotRepository

class RobotService:
    def __init__(self, repository: RobotRepository):
        self.repository = repository

    def get_robot(self, robot_id: int) -> Robot:
        return self.repository.get_robot(robot_id)

    def control_robot(self, robot_id: int, command: str) -> Robot:
        robot = self.get_robot(robot_id)
        # Implement control logic here
        return robot

