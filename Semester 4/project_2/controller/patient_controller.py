import tkinter as tk
from model.patient_model import PatientModel
from model.patient_record import PatientRecord
from view.main_window import MainWindow
from view.add_record_dialog import AddRecordDialog
from view.search_dialog import SearchDialog
from view.delete_dialog import DeleteDialog
from interfaces.observer import Observer
from interfaces.controller import IController

class PatientController(Observer, IController):

    
    def __init__(self, root):
        self.model: PatientModel = PatientModel()
        self.view: MainWindow = MainWindow(root)
        
        # связь контр и модели
        self.model.add_observer(self)
        
        # связь контр и вью
        self._setup_command_bindings()
        
        # Initialize pagination
        self.current_page = 1
        self.records_per_page = 10
        self.update_view()
    
    def _setup_command_bindings(self):
        self.view.set_add_record_command(self.show_add_dialog)
        self.view.set_search_command(self.show_search_dialog)
        self.view.set_delete_command(self.show_delete_dialog)
        self.view.set_delete_selected_command(self.delete_selected_record)
        self.view.set_open_command(self.load_file)
        self.view.set_save_command(self.save_file)
        

        self.view.set_pagination_commands(
            self.go_to_first_page,
            self.go_to_prev_page,
            self.go_to_next_page,
            self.go_to_last_page,
            self.change_records_per_page
        )
        
        # сигнал об изменении колво записей
        self.view.set_records_per_page_callback(self.change_records_per_page)
        
        # обновить интерфейс при изменении колва записей
        self.view.root.bind("<<RecordsPerPageChanged>>", lambda e: self.handle_records_per_page_changed(e))
        self.view.root.bind("<<RefreshRequest>>", lambda e: self.update_view())
        
    def update(self):
    #Вызывается моделью при её изменении
        self.update_view()
        
    def update_view(self):
        #принудительно обновляет интерфейс, включая пагинацию.
        total_records = self.model.get_record_count()
        total_pages = max(1, (total_records + self.records_per_page - 1) // self.records_per_page)
        
        # Ensure current page is valid
        if total_records == 0:
            self.current_page = 1
        elif self.current_page > total_pages:
            self.current_page = total_pages
            

        start_index = (self.current_page - 1) * self.records_per_page
        
        # обнова вью
        self.view.update_pagination(
            self.current_page,
            total_pages,
            total_records,
            self.records_per_page
        )
        self.view.display_records(
            self.model.get_records(),
            start_index,
            self.records_per_page
        )
        
    def go_to_first_page(self):
        if self.current_page != 1:
            self.current_page = 1
            self.update_view()
            
    def go_to_prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_view()
            
    def go_to_next_page(self):
        total_records = self.model.get_record_count()
        total_pages = max(1, (total_records + self.records_per_page - 1) // self.records_per_page)
        
        if self.current_page < total_pages:
            self.current_page += 1
            self.update_view()
            
    def go_to_last_page(self):
        total_records = self.model.get_record_count()
        total_pages = max(1, (total_records + self.records_per_page - 1) // self.records_per_page)
        
        if self.current_page != total_pages:
            self.current_page = total_pages
            self.update_view()
            
    def change_records_per_page(self, value: str):
       #изменение колва записей
        try:
            new_value = int(value)
            if new_value > 0 and new_value != self.records_per_page:
                current_first_record = (self.current_page - 1) * self.records_per_page
                self.records_per_page = new_value
                self.current_page = (current_first_record // new_value) + 1
                
                self.update_view()
        except ValueError:
            self.view.show_error("Error", "Invalid number of records per page")
    
    def handle_records_per_page_changed(self, event):
        #обработчик события изменения колва записей
        # Try to get data from event
        try:
            value = event.data
        except:
            value = self.view.records_per_page
        
        self.change_records_per_page(value)
    
    def delete_selected_record(self):
        #удаление выделенной строки
        selected_item = self.view.get_selected_item()
        
        if not selected_item:
            self.view.show_error("Ошибка", "Нет выбранной записи")
            return

        try:
            record_index = int(self.view.tree.item(selected_item, "tags")[0])
            
            if 0 <= record_index < len(self.model.get_records()):
                confirm = self.view.confirm_action(
                    "Подтверждение удаления",
                    f"Уверены, что хотите удалить эту запись?"
                )
                
                if confirm:

                    records = self.model.get_records()
                    record_to_delete = records[record_index]
                    
                    updated_records = [r for i, r in enumerate(records) if i != record_index]
                    self.model.records = updated_records
                    self.model.notify_observers()
                    self.view.show_message("Успешно", "Запись успешно удалена")
        
        except (IndexError, ValueError) as e:
            print(f"Ошибка удаления: {e}")
            self.view.show_error("Ошибка", "Неверный выбор записи")
            
    def show_add_dialog(self):
        #окно добавления
        AddRecordDialog(self.view.root, on_submit=self.add_record)
        
    def add_record(self, data):
        record = PatientRecord(
            patient_name=data['patient_name'],
            address=data['address'],
            birth_date=data['birth_date'],
            appointment_date=data['appointment_date'],
            doctor_name=data['doctor_name'],
            conclusion=data['conclusion']
        )
        self.model.add_record(record)
        self.view.show_message("Успешно", "Запись успешно добавлена")
        
    def show_search_dialog(self):
        SearchDialog(self.view.root, on_search=self.search_records)
        
    def search_records(self, criteria):
        return self.model.search_records(**criteria)
        
    def show_delete_dialog(self):
        DeleteDialog(self.view.root, on_delete=self.delete_records)
        
    def delete_records(self, criteria):
        return self.model.delete_records(**criteria)
        
    def load_file(self):
        """Load records from a file"""
        filename = self.view.ask_open_filename()
            
        if filename:
            try:
                self.model.load_from_file(filename)
                self.view.show_message("Успешно", "Файл успешно открыт")
            except Exception as e:
                self.view.show_error("Ошибка", f"Файл не открылся: {e}")
                
    def save_file(self):
        filename = self.view.ask_save_filename()
            
        if filename:
            try:
                self.model.save_to_file(filename)
                self.view.show_message("Успешно", "Файл успешно сохранен")
            except Exception as e:
                self.view.show_error("Ошибка", f"Файл не сохранен: {e}")