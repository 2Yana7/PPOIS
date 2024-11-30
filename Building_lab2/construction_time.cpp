#include "construction_time.h"

construction_time::construction_time(const string& start_date, const string& end_date)
    : start_date(start_date), end_date(end_date) {}
    construction_time::construction_time(){}


string construction_time::get_start_date() const {
    return start_date;
}

string construction_time::get_end_date() const {
    return end_date;
}
