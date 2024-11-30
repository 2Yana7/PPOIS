#include "task.h"

task::task(const string& description, employee* assigned_employee)
    : description(description), status("In Progress"), assigned_employee(assigned_employee) {}

string task::get_description() const { return description; }
string task::get_status() const { return status; }

void task::mark_complete() {
    status = "Completed";
}

employee* task::get_assigned_employee() const {
    return assigned_employee;
}
