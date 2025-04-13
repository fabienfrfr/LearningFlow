import pytest
from src.application.use_cases.train_robot_model_use_case import TrainRobotModelUseCase

@pytest.fixture
def model_and_dataset():
    return "distilbert-base-uncased", "imdb"

def test_train_robot_model(model_and_dataset):
    model_name, dataset_name = model_and_dataset
    use_case = TrainRobotModelUseCase(model_name, dataset_name)
    log_history = use_case.execute()
    assert log_history is not None

