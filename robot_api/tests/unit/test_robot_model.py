import pytest
from src.domain.models.robot_model import Robot

def test_robot_initialization():
    robot = Robot(id=1, name="TestRobot", status="active")
    assert robot.id == 1
    assert robot.name == "TestRobot"
    assert robot.status == "active"

