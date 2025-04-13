from fastapi import FastAPI
from src.application.use_cases.control_robot_use_case import ControlRobotUseCase
from src.domain.models.robot_model import Robot

app = FastAPI()

@app.post("/control-robot/")
def control_robot(robot_id: int, command: str):
    use_case = ControlRobotUseCase(robot_service)
    return use_case.execute(robot_id, command)

