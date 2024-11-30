#include "days_off.h"

days_off::days_off(int days_count) : days_count(days_count) {}
days_off::days_off():days_count(0) {}

int days_off::get_days_count() const {
    return days_count;
}

void days_off::add_day_off() {
    days_count++;
}
