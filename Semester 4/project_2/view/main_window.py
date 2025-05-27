import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from interfaces.view import IView
from typing import List, Any, Callable

class MainWindow(IView):
    def __init__(self, root, title="Система управления записью пациентов"):
        self.root = root
        self.root.title(title)
        

        self.root.geometry("1200x600")  # Set initial size
        self.root.minsize(800, 400)     # Set minimum size
        
        self.style = ttk.Style()
        self.style.configure("Toolbar.TButton", padding=5)
        self.style.configure("Action.TButton", padding=5, background="#007bff")
        
        self.records_per_page = 10
        self.current_page = 1
        self.records_per_page_var = tk.StringVar(value="10")
        
        self._create_menu()
        
        # отступы
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self._create_toolbar()
        
        self._create_treeview()
        
        self._create_pagination()
        
    def _create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu, underline=0)
        
        file_menu.add_command(label="Открыть...", command=lambda: None, underline=0, accelerator="Ctrl+O")
        file_menu.add_command(label="Сохранить...", command=lambda: None, underline=0, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit, underline=1, accelerator="Alt+F4")
        
        self.file_menu = file_menu
        
    def _create_toolbar(self):

        toolbar = ttk.Frame(self.main_frame, relief="raised", borderwidth=1)
        toolbar.pack(fill=tk.X, padx=5, pady=(0, 10))
        
        self.open_button = ttk.Button(toolbar, text="Открыть файл", width=15,
                                    style="Toolbar.TButton")
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.save_button = ttk.Button(toolbar, text="Сохранить файл", width=15,
                                    style="Toolbar.TButton")
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        self.add_button = ttk.Button(toolbar, text="Добавить запись", width=15,
                                   style="Action.TButton")
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        

        self.search_button = ttk.Button(toolbar, text="Поиск", width=15,
                                      style="Toolbar.TButton")
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.delete_button = ttk.Button(toolbar, text="Удалить", width=15,
                                      style="Toolbar.TButton")
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.delete_selected_button = ttk.Button(toolbar, text="Удалить выделенное", width=19,
                                               style="Toolbar.TButton")
        self.delete_selected_button.pack(side=tk.LEFT, padx=5, pady=5)
        
    def _create_treeview(self):
        #список
        tree_frame = ttk.Frame(self.main_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tree = ttk.Treeview(tree_frame, columns=(
            "patient_name", "address", "birth_date",
            "appointment_date", "doctor_name", "conclusion"
        ), show="headings")
        
        self.tree.heading("patient_name", text="Имя пациента")
        self.tree.heading("address", text="Адрес")
        self.tree.heading("birth_date", text="Дата рождения")
        self.tree.heading("appointment_date", text="Дата приёма")
        self.tree.heading("doctor_name", text="Имя доктора")
        self.tree.heading("conclusion", text="Заключение")
        
        # Configure column widths
        self.tree.column("patient_name", width=150)
        self.tree.column("address", width=200)
        self.tree.column("birth_date", width=100)
        self.tree.column("appointment_date", width=100)
        self.tree.column("doctor_name", width=150)
        self.tree.column("conclusion", width=300)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def _create_pagination(self):
        pagination_frame = ttk.Frame(self.main_frame)
        pagination_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.first_page_btn = ttk.Button(pagination_frame, text="<<")
        self.first_page_btn.pack(side=tk.LEFT, padx=2)
        
        self.prev_page_btn = ttk.Button(pagination_frame, text="<")
        self.prev_page_btn.pack(side=tk.LEFT, padx=2)
        
        # Page info
        self.page_info = ttk.Label(pagination_frame, text="Страница 1 из 1")
        self.page_info.pack(side=tk.LEFT, padx=10)
        
        self.next_page_btn = ttk.Button(pagination_frame, text=">")
        self.next_page_btn.pack(side=tk.LEFT, padx=2)
        
        self.last_page_btn = ttk.Button(pagination_frame, text=">>")
        self.last_page_btn.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(pagination_frame, text="Записей на странице:").pack(side=tk.LEFT, padx=10)
        self.records_per_page_combo = ttk.Combobox(
            pagination_frame,
            textvariable=self.records_per_page_var,
            values=["5", "10", "20", "50", "100"],
            width=5,
            state="readonly"
        )
        self.records_per_page_combo.pack(side=tk.LEFT)
        
        self.records_per_page_combo.set("10")
        
        self._records_per_page_callback = None
        
    def set_add_record_command(self, command: Callable):
        self.add_button.config(command=command)
        
    def set_search_command(self, command: Callable):
        self.search_button.config(command=command)
        
    def set_delete_command(self, command: Callable):
        self.delete_button.config(command=command)
        
    def set_delete_selected_command(self, command: Callable):
        self.delete_selected_button.config(command=command)
        
    def set_open_command(self, command: Callable):
        self.open_button.config(command=command)
        self.file_menu.entryconfigure("Открыть...", command=command)
        
    def set_save_command(self, command: Callable):
        self.save_button.config(command=command)
        self.file_menu.entryconfigure("Сохранить...", command=command)
        
    def set_pagination_commands(self, first_page: Callable, prev_page: Callable,
                              next_page: Callable, last_page: Callable,
                              change_records: Callable):
        self.first_page_btn.config(command=first_page)
        self.prev_page_btn.config(command=prev_page)
        self.next_page_btn.config(command=next_page)
        self.last_page_btn.config(command=last_page)
        
    def update_pagination(self, current_page: int, total_pages: int,
                         total_records: int, records_per_page: int):
        self.page_info.config(
            text=f" {current_page} страница из {total_pages} (Всего записей: {total_records})"
        )
        
        if records_per_page != self.records_per_page:
            self.records_per_page = records_per_page
            self.records_per_page_var.set(str(records_per_page))
            
    def get_selected_item(self):
        selection = self.tree.selection()
        if selection:
            return selection[0]
        return None
        
    def display_records(self, records: List[Any], start_index: int = 0, count: int = None):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if count is None:
            count = len(records)
            
        end_index = min(start_index + count, len(records))
        page_records = records[start_index:end_index]
        
        for i, record in enumerate(page_records):
            item_id = self.tree.insert("", tk.END, values=(
                record.patient_name,
                record.address,
                record.birth_date,
                record.appointment_date,
                record.doctor_name,
                record.conclusion
            ))
            self.tree.item(item_id, tags=(str(start_index + i),))
            
    def show_message(self, title: str, message: str):
        messagebox.showinfo(title, message)
        
    def show_error(self, title: str, message: str):
        messagebox.showerror(title, message)
        
    def confirm_action(self, title: str, message: str) -> bool:
        return messagebox.askyesno(title, message)
        
    def ask_open_filename(self) -> str:
        return filedialog.askopenfilename(
            title="Открытье файла с записями",
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
        )
        
    def ask_save_filename(self) -> str:
        return filedialog.asksaveasfilename(
            title="Сохранение записей",
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
            defaultextension=".xml"
        )
        
    def set_records_per_page_callback(self, callback: Callable[[str], None]):
        self._records_per_page_callback = callback
        self.records_per_page_combo.bind('<<ComboboxSelected>>', self._on_records_per_page_change)
        
    def _on_records_per_page_change(self, event):
        if self._records_per_page_callback:
            new_value = self.records_per_page_var.get()
            self._records_per_page_callback(new_value) 