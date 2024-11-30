#include "Equipment.h"
#include <iostream>

Equipment::Equipment(const string& type, int id) : type(type), id(id) {}

void Equipment::operate() const {}
string Equipment::get_type() const { return type; }
int Equipment::get_id() const { return id; }
