#include "salary.h"

salary::salary(double amount) : amount(amount) {}
salary::salary() {}

double salary::get_amount() const {
    return amount;
}

void salary::update_salary(double new_amount) {
    amount = new_amount;
}
