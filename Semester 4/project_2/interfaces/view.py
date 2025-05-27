from typing import Protocol, List, Any, Callable, Optional

class IView(Protocol):
    def display_records(self, records: List[Any], start_index: int = 0, count: Optional[int] = None) -> None:
        pass
    
    def show_message(self, title: str, message: str) -> None:
        pass
    
    def show_error(self, title: str, message: str) -> None:
        pass
    
    def confirm_action(self, title: str, message: str) -> bool:
        pass
    
    def ask_open_filename(self) -> str:
        pass
    
    def ask_save_filename(self) -> str:
            pass