#include "Construction_time.h"

Construction_time::Construction_time(const string& start_date, const string& end_date)
    : start_date(start_date), end_date(end_date) {}
    Construction_time::Construction_time(){}


string Construction_time::get_start_date() const {
    return start_date;
}

string Construction_time::get_end_date() const {
    return end_date;
}
