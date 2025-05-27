import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class DialogBase(tk.Toplevel):
    def __init__(self, parent, title="Dialog"):
        super().__init__(parent)
        
        self.title(title)
        self.resizable(True, True)
        self.transient(parent)
        self.grab_set()
        
        self.minsize(400, 300)
        
        self.geometry("+%d+%d" % (
            parent.winfo_rootx() + 50,
            parent.winfo_rooty() + 50
        ))
        
    def create_date_entry(self, parent, **kwargs):
        return DateEntry(
            parent,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='yyyy-mm-dd',
            firstweekday='sunday',
            showweeknumbers=False,
            **kwargs
        )
        
    def create_form_field(self, container, label_text, entry_widget=None):
        frame = ttk.Frame(container)
        frame.pack(fill=tk.X, padx=5, pady=2)
        
        label = ttk.Label(frame, text=label_text, width=15)
        label.pack(side=tk.LEFT)
        
        if entry_widget is None:
            entry_widget = ttk.Entry(frame)
        entry_widget.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        return entry_widget

    def show_error(self, title: str, message: str):
        messagebox.showerror(title, message, parent=self)
        
    def show_message(self, title: str, message: str):
        messagebox.showinfo(title, message, parent=self)
        
    def show_confirm(self, title: str, message: str) -> bool:
        return messagebox.askyesno(title, message, parent=self)