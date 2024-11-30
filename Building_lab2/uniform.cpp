#include "uniform.h"

uniform::uniform(const string& type, int quantity) : type(type), quantity(quantity) {}

void uniform::set_type(const string& type) {
    this->type = type;
}

string uniform::get_type() const {
    return type;
}

void uniform::set_quantity(int quantity) {
    this->quantity = quantity;
}

int uniform::get_quantity() const {
    return quantity;
}
