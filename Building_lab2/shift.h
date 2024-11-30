#ifndef shift_h
#define shift_h

#include <string>
using namespace std;

class shift {
public:
    shift(const string& start_time, const string& end_time);

    string get_start_time() const;
    string get_end_time() const;

private:
    string start_time;
    string end_time;
};

#endif
