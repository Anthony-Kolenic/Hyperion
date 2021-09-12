from abc import ABC, abstractmethod

class BaseCmd(ABC):
    
    @abstractmethod
    def execute(self):
        pass
