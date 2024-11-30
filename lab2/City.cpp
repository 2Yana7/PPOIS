#include "City.h"

City::City(const string& name) : name(name) {}

void City::set_name(const string& name) {
   this->name = name;}

string City::get_name() const {
    return name;
}
