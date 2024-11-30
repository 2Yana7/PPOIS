#include "Task.h"

Task::Task(const string& description, Employee* assigned_employee)
    : description(description), status("In Progress"), assigned_employee(assigned_employee) {}

string Task::get_description() const { return description; }
string Task::get_status() const { return status; }

void Task::mark_complete() {
    status = "Completed";
}

Employee* Task::get_assigned_employee() const {
    return assigned_employee;
}
