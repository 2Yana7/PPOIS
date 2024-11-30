#ifndef city_h
#define city_h

#include <string>
using namespace std;

class city {
public:
    city(const string& name = "CITY");

    void set_name(const string& name);
    string get_name() const;

private:
    string name;
};

#endif
