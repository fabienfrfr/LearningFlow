from src.domain.services.robot_service import RobotService

class ControlRobotUseCase:
    def __init__(self, robot_service: RobotService):
        self.robot_service = robot_service

    def execute(self, robot_id: int, command: str) -> Robot:
        return self.robot_service.control_robot(robot_id, command)

