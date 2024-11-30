#ifndef days_off_h
#define days_off_h

#include <string>
using namespace std;

class days_off {
public:
    days_off();
    days_off(int days_count);

    int get_days_count() const;
    void add_day_off();

private:
    int days_count;
};

#endif
