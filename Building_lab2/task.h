#ifndef task_h
#define task_h

#include <string>
#include "employee.h"
using namespace std;

class task {
public:
    task(const string& description, employee* assigned_employee);

    string get_description() const;
    string get_status() const;
    void mark_complete();

    employee* get_assigned_employee() const;

private:
    string description;
    string status;
    employee* assigned_employee;  // указатель на сотрудника, ответственного за задачу
};

#endif
