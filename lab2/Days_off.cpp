#include "Days_off.h"

Days_off::Days_off(int days_count) : days_count(days_count) {}
Days_off::Days_off():days_count(0) {}

int Days_off::get_days_count() const {
    return days_count;
}

void Days_off::add_day_off() {
    days_count++;
}
