#include "Employee.h"

Employee::Employee(const string& name, int id, const string& role)
: name(name), id(id), role(role) {}

string Employee::get_name() const { return name; }
int Employee::get_id() const { return id; }
string Employee::get_role() const { return role; }
