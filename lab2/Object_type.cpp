#include "object_type.h"

object_type::object_type(const string& type_name) : type_name(type_name) {}

void object_type::set_type_name(const string& type_name) {
    this->type_name = type_name;
}

string object_type::get_type_name() const {
    return type_name;
}
