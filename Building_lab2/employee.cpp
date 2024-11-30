#include "employee.h"

employee::employee(const string& name, int id, const string& role)
: name(name), id(id), role(role) {}

string employee::get_name() const { return name; }
int employee::get_id() const { return id; }
string employee::get_role() const { return role; }
