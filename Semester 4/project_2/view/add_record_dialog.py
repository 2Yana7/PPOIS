import tkinter as tk
from tkinter import ttk
from .dialog_base import DialogBase
from typing import Callable, Dict, Any
from tkcalendar import DateEntry

class AddRecordDialog(DialogBase):
    def __init__(self, parent, on_submit: Callable[[Dict[str, Any]], None]):
        super().__init__(parent, title="Добавьте нового пациента")
        
        self.on_submit = on_submit
        
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        main_frame.columnconfigure(1, weight=1)
        for i in range(7):
            main_frame.rowconfigure(i, weight=0)
        main_frame.rowconfigure(5, weight=1)
        

        ttk.Label(main_frame, text="Имя пациента:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.patient_name = ttk.Entry(main_frame)
        self.patient_name.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Адрес:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.address = ttk.Entry(main_frame)
        self.address.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Дата рождения:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.birth_date = self.create_date_entry(main_frame)
        self.birth_date.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Дата приёма:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
        self.appointment_date = self.create_date_entry(main_frame)
        self.appointment_date.grid(row=3, column=1, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Имя доктора:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=2)
        self.doctor_name = ttk.Entry(main_frame)
        self.doctor_name.grid(row=4, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(main_frame, text="Заключение:").grid(row=5, column=0, sticky=tk.NW, padx=5, pady=2)
        self.conclusion = tk.Text(main_frame, width=40)
        self.conclusion.grid(row=5, column=1, sticky=tk.NSEW, padx=5, pady=2)
        
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.conclusion.yview)
        scrollbar.grid(row=5, column=2, sticky=tk.NS)
        self.conclusion.config(yscrollcommand=scrollbar.set)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, sticky=tk.E, padx=5, pady=5)
        
        ttk.Button(button_frame, text="Отмена", command=self.destroy).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Подтвердить", command=self._on_submit).pack(side=tk.LEFT)
        
    def _on_submit(self):
        # Validate required fields
        if not self.patient_name.get().strip():
            self.show_error("Ошибка", "Имя пациента не может быть пустым")
            self.patient_name.focus()
            return
            
        if not self.address.get().strip():
            self.show_error("Ошибка", "Адрес не может быть пустым")
            self.address.focus()
            return
            
        if not self.doctor_name.get().strip():
            self.show_error("Ошибка", "Имя доктора не может быть пустым")
            self.doctor_name.focus()
            return
            
        if not self.conclusion.get("1.0", tk.END).strip():
            self.show_error("Ошибка", "Заключение не может быть пустым")
            self.conclusion.focus()
            return
        
        data = {
            'patient_name': self.patient_name.get().strip(),
            'address': self.address.get().strip(),
            'birth_date': self.birth_date.get_date().strftime('%Y-%m-%d'),
            'appointment_date': self.appointment_date.get_date().strftime('%Y-%m-%d'),
            'doctor_name': self.doctor_name.get().strip(),
            'conclusion': self.conclusion.get("1.0", tk.END).strip()
        }
        
        self.on_submit(data)
        self.destroy() 