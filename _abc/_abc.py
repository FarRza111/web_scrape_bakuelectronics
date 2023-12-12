import abc
from dataclasses import dataclass
from abc import ABC, abstractmethod


class MyABC(ABC):

    @abstractmethod
    def get_soup(self):
        pass

    @abstractmethod
    def process_soup(self):
        pass

    def scrape(self):
        pass

