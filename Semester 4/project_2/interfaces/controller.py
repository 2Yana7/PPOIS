from abc import ABC, abstractmethod

class IController(ABC):

    @abstractmethod
    def update(self):
        pass
        
    @abstractmethod
    def update_view(self):
        pass
        
    @abstractmethod
    def show_add_dialog(self):
        pass
        
    @abstractmethod
    def add_record(self, data):
        pass
        
    @abstractmethod
    def show_search_dialog(self):
        pass
        
    @abstractmethod
    def search_records(self, criteria):
        pass
        
    @abstractmethod
    def show_delete_dialog(self):
        pass
        
    @abstractmethod
    def delete_records(self, criteria):
        pass
        
    @abstractmethod
    def load_file(self):
        pass
        
    @abstractmethod
    def save_file(self):
        pass