#include "equipment.h"
#include <iostream>

equipment::equipment(const string& type, int id) : type(type), id(id) {}

void equipment::operate() const {}
string equipment::get_type() const { return type; }
int equipment::get_id() const { return id; }
