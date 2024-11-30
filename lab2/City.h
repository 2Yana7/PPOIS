#ifndef City_h
#define City_h

#include <string>
using namespace std;

class City {
public:
    City(const string& name = "CITY");

    void set_name(const string& name);
    string get_name() const;

private:
    string name;
};

#endif
