from sqlalchemy.orm import Session
from src.domain.models.robot_model import Robot
from src.domain.repositories.robot_repository import RobotRepository

class PostgresRepository(RobotRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_robot(self, robot_id: int) -> Robot:
        return self.session.query(Robot).filter_by(id=robot_id).first()

