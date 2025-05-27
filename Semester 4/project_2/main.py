import tkinter as tk
from controller.patient_controller import PatientController

def main():
    """Main entry point for the application"""
    root = tk.Tk()
    root.title("Patient Records Management System")
    
    # Create and initialize the controller
    controller = PatientController(root)
    
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
