#include "Shift.h"

Shift::Shift(const string& start_time, const string& end_time)
    : start_time(start_time), end_time(end_time) {}

string Shift::get_start_time() const {
    return start_time;
}

string Shift::get_end_time() const {
    return end_time;
}
