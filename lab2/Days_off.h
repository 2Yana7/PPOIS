#ifndef Days_off_h
#define Days_off_h

#include <string>
using namespace std;

class Days_off {
public:
    Days_off();
    Days_off(int days_count);

    int get_days_count() const;
    void add_day_off();

private:
    int days_count;
};

#endif
