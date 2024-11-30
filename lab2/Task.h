#ifndef Task_h
#define Task_h

#include <string>
#include "Employee.h"
using namespace std;

class Task {
public:
    Task(const string& description, Employee* assigned_employee);

    string get_description() const;
    string get_status() const;
    void mark_complete();

    Employee* get_assigned_employee() const;

private:
    string description;
    string status;
    Employee* assigned_employee;  // указатель на сотрудника, ответственного за задачу
};

#endif
