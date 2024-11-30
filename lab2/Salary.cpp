#include "Salary.h"

Salary::Salary(double amount) : amount(amount) {}
Salary::Salary() {}

double Salary::get_amount() const {
    return amount;
}

void Salary::update_Salary(double new_amount) {
    amount = new_amount;
}
