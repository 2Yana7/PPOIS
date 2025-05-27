import tkinter as tk
from tkinter import ttk, messagebox
from .dialog_base import DialogBase
from typing import Callable, Dict, Any

class DeleteDialog(DialogBase):
    def __init__(self, parent, on_delete: Callable[[Dict[str, Any]], None]):
        super().__init__(parent, title="Удаление записи")
        
        self.on_delete = on_delete
        
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        main_frame.columnconfigure(0, weight=1)
        
        criteria_frame = ttk.LabelFrame(main_frame, text="Критерия для удаления:")
        criteria_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        criteria_frame.columnconfigure(1, weight=1)
        

        ttk.Label(criteria_frame, text="Имя пациента:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.patient_name = ttk.Entry(criteria_frame)
        self.patient_name.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(criteria_frame, text="Адрес:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.address = ttk.Entry(criteria_frame)
        self.address.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(criteria_frame, text="Дата рождения:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.birth_date = self.create_date_entry(criteria_frame)
        self.birth_date.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        self.use_birth_date = tk.BooleanVar()
        ttk.Checkbutton(criteria_frame, text="Учитывать дату рождения", variable=self.use_birth_date).grid(row=2, column=2, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(criteria_frame, text="Имя доктора:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.doctor_name = ttk.Entry(criteria_frame)
        self.doctor_name.grid(row=3, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(criteria_frame, text="Дата приёма:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.appointment_date = self.create_date_entry(criteria_frame)
        self.appointment_date.grid(row=4, column=1, sticky=tk.W, padx=5, pady=2)
        
        self.use_appointment_date = tk.BooleanVar()
        ttk.Checkbutton(criteria_frame, text="Учитывать дату приёма", variable=self.use_appointment_date).grid(row=4, column=2, sticky=tk.W, padx=5, pady=2)
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        
        self.style = ttk.Style()
        self.style.configure("Danger.TButton", foreground="red")
        
        ttk.Button(button_frame, text="Отмена", command=self.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(
            button_frame, 
            text="Удалить запись",
            command=self._on_delete,
            style="Danger.TButton"
        ).pack(side=tk.LEFT)
        
    def _on_delete(self):
        criteria = {}
        
        if self.patient_name.get():
            criteria['patient_name'] = self.patient_name.get()
        if self.address.get():
            criteria['address'] = self.address.get()
        if self.doctor_name.get():
            criteria['doctor_name'] = self.doctor_name.get()
            
        if self.use_birth_date.get():
            criteria['birth_date'] = self.birth_date.get_date().strftime('%Y-%m-%d')
        if self.use_appointment_date.get():
            criteria['appointment_date'] = self.appointment_date.get_date().strftime('%Y-%m-%d')
            
        if not criteria:
            messagebox.showerror("Ошибка", "Должен совпадать хотя бы 1 критерий", parent=self)
            return
            
        if not messagebox.askyesno("Уточнение", "Вы уверены, что хотите удалить все записи подходящие под критерий?", parent=self):
            return
            
        deleted_count = self.on_delete(criteria)
        
        messagebox.showinfo("Успешно", f"Удалено {deleted_count} запись(и)", parent=self)
        self.destroy() 