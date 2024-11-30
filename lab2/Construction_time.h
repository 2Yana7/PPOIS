#ifndef Construction_time_h
#define Construction_time_h

#include <string>
using namespace std;

class Construction_time {
public:
    Construction_time(const string& start_date, const string& end_date);
    Construction_time();
    string get_start_date() const;
    string get_end_date() const;

private:
    string start_date;
    string end_date;
};

#endif
