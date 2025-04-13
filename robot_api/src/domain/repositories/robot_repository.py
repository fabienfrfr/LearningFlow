from abc import ABC, abstractmethod
from src.domain.models.robot_model import Robot

class RobotRepository(ABC):
    @abstractmethod
    def get_robot(self, robot_id: int) -> Robot:
        pass

