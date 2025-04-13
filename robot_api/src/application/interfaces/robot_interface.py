from abc import ABC, abstractmethod

class RobotInterface(ABC):
    @abstractmethod
    def move(self, direction: str):
        pass

    @abstractmethod
    def stop(self):
        pass

