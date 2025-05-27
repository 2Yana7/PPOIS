import tkinter as tk
from tkinter import ttk
from .dialog_base import DialogBase
from typing import Callable, Dict, Any

class SearchDialog(DialogBase):
    def __init__(self, parent, on_search: Callable[[Dict[str, Any]], None]):
        super().__init__(parent, title="Поиск записи")
        
        self.on_search = on_search
        
        # Create main container that will expand
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Configure main frame grid
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Create search criteria frame
        criteria_frame = ttk.LabelFrame(main_frame, text="Критерии поиска")
        criteria_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        # Configure criteria frame grid
        criteria_frame.columnconfigure(1, weight=1)
        criteria_frame.columnconfigure(3, weight=1)
        
        # Create form fields in grid layout
        # Patient Name
        ttk.Label(criteria_frame, text="Имя пациента:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.patient_name = ttk.Entry(criteria_frame)
        self.patient_name.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Address
        ttk.Label(criteria_frame, text="Адрес:").grid(row=0, column=2, sticky=tk.W, padx=(150, 5), pady=2)
        self.address = ttk.Entry(criteria_frame)
        self.address.grid(row=0, column=3, sticky=tk.EW, padx=5, pady=2)
        
        # Birth Date
        ttk.Label(criteria_frame, text="Дата рождения:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.birth_date = self.create_date_entry(criteria_frame)
        self.birth_date.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Use birth date checkbox
        self.use_birth_date = tk.BooleanVar()
        ttk.Checkbutton(criteria_frame, text="учитывать дату рождения", variable=self.use_birth_date).grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)
        
        # Doctor Name
        ttk.Label(criteria_frame, text="Имя доктора:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.doctor_name = ttk.Entry(criteria_frame)
        self.doctor_name.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Appointment Date
        ttk.Label(criteria_frame, text="Дата приёма:").grid(row=2, column=2, sticky=tk.W, padx=(110, 5), pady=2)
        self.appointment_date = self.create_date_entry(criteria_frame)
        self.appointment_date.grid(row=2, column=3, sticky=tk.W, padx=5, pady=2)
        
        # Use appointment date checkbox
        self.use_appointment_date = tk.BooleanVar()
        ttk.Checkbutton(criteria_frame, text="учитывать дату приёма", variable=self.use_appointment_date).grid(row=2, column=4, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(criteria_frame)
        button_frame.grid(row=3, column=0, columnspan=5, pady=10)
        
        ttk.Button(button_frame, text="Поиск", command=self._on_search).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Очистить", command=self._clear_form).pack(side=tk.LEFT, padx=5)
        
        # Create results frame
        results_frame = ttk.LabelFrame(main_frame, text="Результаты поиска")
        results_frame.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)
        
        # Configure results frame grid
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Create treeview
        self.tree = ttk.Treeview(
            results_frame,
            columns=("patient_name", "address", "birth_date", "appointment_date", "doctor_name", "conclusion"),
            show="headings"
        )
        
        # Configure columns
        self.tree.heading("patient_name", text="Имя пациента")
        self.tree.heading("address", text="Адрес")
        self.tree.heading("birth_date", text="Дата рождения")
        self.tree.heading("appointment_date", text="Дата приёма")
        self.tree.heading("doctor_name", text="Имя доктора")
        self.tree.heading("conclusion", text="Заключение")
        
        # Configure column widths
        self.tree.column("patient_name", width=100)
        self.tree.column("address", width=150)
        self.tree.column("birth_date", width=80)
        self.tree.column("appointment_date", width=100)
        self.tree.column("doctor_name", width=100)
        self.tree.column("conclusion", width=200)
        
        # Add scrollbars
        vsb = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(results_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Grid treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        vsb.grid(row=0, column=1, sticky=tk.NS)
        hsb.grid(row=1, column=0, sticky=tk.EW)
        
        # Pagination frame
        pagination_frame = ttk.Frame(results_frame)
        pagination_frame.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=5)
        
        ttk.Button(pagination_frame, text="<<").pack(side=tk.LEFT, padx=2)
        ttk.Button(pagination_frame, text="<").pack(side=tk.LEFT, padx=2)
        ttk.Label(pagination_frame, text="Страница 1 из 1").pack(side=tk.LEFT, padx=10)
        ttk.Button(pagination_frame, text=">").pack(side=tk.LEFT, padx=2)
        ttk.Button(pagination_frame, text=">>").pack(side=tk.LEFT, padx=2)
        
        # Close button
        ttk.Button(main_frame, text="Закрыть", command=self.destroy).grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        
    def _clear_form(self):
        """Clear all form fields"""
        self.patient_name.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.doctor_name.delete(0, tk.END)
        # Reset date fields to current date
        today = self.birth_date.get_date()
        self.birth_date.set_date(today)
        self.appointment_date.set_date(today)
        self.use_birth_date.set(False)
        self.use_appointment_date.set(False)
        
    def _on_search(self):
        """Handle search button click"""
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Get search criteria
        criteria = {}
        
        if self.patient_name.get():
            criteria['patient_name'] = self.patient_name.get()
        if self.address.get():
            criteria['address'] = self.address.get()
        if self.doctor_name.get():
            criteria['doctor_name'] = self.doctor_name.get()
            
        # Only add dates if checkboxes are selected
        if self.use_birth_date.get():
            criteria['birth_date'] = self.birth_date.get_date().strftime('%Y-%m-%d')
        if self.use_appointment_date.get():
            criteria['appointment_date'] = self.appointment_date.get_date().strftime('%Y-%m-%d')
            
        # Perform search
        results = self.on_search(criteria)
        
        # Display results
        for record in results:
            self.tree.insert("", tk.END, values=(
                record.patient_name,
                record.address,
                record.birth_date,
                record.appointment_date,
                record.doctor_name,
                record.conclusion
            )) 