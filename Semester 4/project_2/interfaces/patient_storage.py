from typing import Protocol, List, Any
#работа с записями
class IPatientStorage(Protocol):
    def add_record(self, record: Any) -> None:
        pass
    
    def get_records(self) -> List[Any]:
        pass
    
    def get_record_count(self) -> int:
        pass
    
    def delete_records(self, **conditions) -> int:
        pass
    
    def search_records(self, **conditions) -> List[Any]:
        pass
    
    def save_to_file(self, filename: str) -> None:
        pass
    
    def load_from_file(self, filename: str) -> None:
        pass