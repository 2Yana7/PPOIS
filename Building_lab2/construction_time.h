#ifndef construction_time_h
#define construction_time_h

#include <string>
using namespace std;

class construction_time {
public:
    construction_time(const string& start_date, const string& end_date);
    construction_time();
    string get_start_date() const;
    string get_end_date() const;

private:
    string start_date;
    string end_date;
};

#endif
