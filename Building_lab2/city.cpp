#include "city.h"

city::city(const string& name) : name(name) {}

void city::set_name(const string& name) {
   this->name = name;}

string city::get_name() const {
    return name;
}
