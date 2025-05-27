from typing import List
from interfaces.observer import Observer

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
        
    def add_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
            
    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
            
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update() 