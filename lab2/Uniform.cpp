#include "Uniform.h"

Uniform::Uniform(const string& type, int quantity) : type(type), quantity(quantity) {}

void Uniform::set_type(const string& type) {
    this->type = type;
}

string Uniform::get_type() const {
    return type;
}

void Uniform::set_quantity(int quantity) {
    this->quantity = quantity;
}

int Uniform::get_quantity() const {
    return quantity;
}
