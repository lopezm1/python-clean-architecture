from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class EntityModel(ABC):

    @abstractmethod
    def from_dict(self, adict):
        pass

