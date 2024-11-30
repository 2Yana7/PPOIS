#include "shift.h"

shift::shift(const string& start_time, const string& end_time)
    : start_time(start_time), end_time(end_time) {}

string shift::get_start_time() const {
    return start_time;
}

string shift::get_end_time() const {
    return end_time;
}
