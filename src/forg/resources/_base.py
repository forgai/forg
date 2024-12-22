from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Resource(ABC):
    @classmethod
    @abstractmethod
    def api_source(cls) -> str:
        ...
