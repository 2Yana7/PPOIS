#ifndef Shift_h
#define Shift_h

#include <string>
using namespace std;

class Shift {
public:
    Shift(const string& start_time, const string& end_time);

    string get_start_time() const;
    string get_end_time() const;

private:
    string start_time;
    string end_time;
};

#endif
